
import logging
import uuid
import pytest
from scm import Scm

# FIX: Import all model classes from the main package 'scm.objects.models'
from scm.objects.models import (
    Services,
    ServicesProtocol,
    ServicesProtocolTcp,
    ServicesProtocolUdp,
    ServiceGroups
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Shared"
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (To manage dependent Service objects)
# -----------------------------------------------------------------------------
def create_test_service(api, name, protocol_type="tcp", port="80"):
    """Helper to create a single service object for group membership."""
    if protocol_type == "tcp":
        protocol = ServicesProtocol(
            tcp=ServicesProtocolTcp(port=port)
        )
    else:
        protocol = ServicesProtocol(
            udp=ServicesProtocolUdp(port=port)
        )

    payload = Services(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        protocol=protocol,
        description="Temp service for ServiceGroup test"
    )
    return api.create_services(services=payload)

def delete_test_service(api, service_id):
    """Helper to delete a single service object."""
    try:
        api.delete_services_by_id(id=service_id)
    except Exception as e:
        # 404 is acceptable during cleanup
        if "404" not in str(e):
            logger.warning(f"Failed to cleanup service {service_id}: {e}")

def cleanup_group_by_name(api, name):
    """
    Robust cleanup: Tries to find and delete a group by name.
    Useful if the Create operation returned None or failed partially.
    """
    try:
        response = api.list_service_groups(folder=TARGET_FOLDER)
        for group in response.data:
            if group.name == name:
                logger.info(f"Cleanup: Found orphan group '{name}' (ID: {group.id}). Deleting...")
                api.delete_service_groups_by_id(id=group.id)
                return
    except Exception as e:
        logger.warning(f"Fallback cleanup failed for {name}: {e}")

# -----------------------------------------------------------------------------
# FIXTURES
# -----------------------------------------------------------------------------

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def services_api(client):
    return client.objects.ServicesApi(client.objects.api_client)

@pytest.fixture(scope="module")
def service_groups_api(client):
    return client.objects.ServiceGroupsApi(client.objects.api_client)

@pytest.fixture
def clean_service_group(services_api, service_groups_api):
    """
    Fixture to create a temporary Service Group AND its dependent Service.
    Strictly follows Go logic: Delete Group first, then Services.
    """
    # 1. SETUP: Create Dependency (Service)
    random_id = uuid.uuid4().hex[:6]
    svc1 = create_test_service(services_api, f"grp-dep-{random_id}", "tcp", "8080")
    group_name = f"test-sg-{random_id}"

    created_group = None

    try:
        # 2. SETUP: Create Service Group
        payload = ServiceGroups(
            id="",
            name=group_name,
            folder=TARGET_FOLDER,
            members=[svc1.name],
        )
        
        logger.info(f"\n[SETUP] Creating Service Group: {group_name}")
        created_group = service_groups_api.create_service_groups(service_groups=payload)
        
        # SDK Safety Check
        if created_group is None:
            logger.warning("SDK returned None for creation. Fetching object by name.")
            response = service_groups_api.list_service_groups(folder=TARGET_FOLDER)
            for entry in response.data:
                if entry.name == group_name:
                    created_group = entry
                    break

        yield created_group

    finally:
        # 3. TEARDOWN: Delete Group FIRST
        if created_group and created_group.id:
            logger.info(f"\n[TEARDOWN] Deleting Service Group ID: {created_group.id}")
            try:
                service_groups_api.delete_service_groups_by_id(id=created_group.id)
            except Exception as e:
                logger.warning(f"Group teardown failed: {e}")
        else:
            cleanup_group_by_name(service_groups_api, group_name)

        # 4. TEARDOWN: Delete Dependency SECOND
        if svc1 and svc1.id:
            logger.info(f"[TEARDOWN] Deleting Service ID: {svc1.id}")
            delete_test_service(services_api, svc1.id)


# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def test_create_service_group(services_api, service_groups_api):
    """
    Test manual creation and deletion of a service group.
    Equivalent to Go: Test_objects_ServiceGroupsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    
    # 1. Create dependencies
    svc1 = create_test_service(services_api, f"test-svc-1-{random_suffix}", "tcp", "80")
    svc2 = create_test_service(services_api, f"test-svc-2-{random_suffix}", "udp", "53")
    group_name = f"test-sg-create-{random_suffix}"
    
    created_group = None

    try:
        # 2. Create Group
        payload = ServiceGroups(
            id="",
            name=group_name,
            folder=TARGET_FOLDER,
            members=[svc1.name, svc2.name],
        )
        
        created_group = service_groups_api.create_service_groups(service_groups=payload)
        
        # SDK Safety Check
        if created_group is None:
            response = service_groups_api.list_service_groups(folder=TARGET_FOLDER)
            for entry in response.data:
                if entry.name == group_name:
                    created_group = entry
                    break

        # Verify
        assert created_group is not None
        assert created_group.name == group_name
        assert created_group.id is not None
        assert set(created_group.members) == set([svc1.name, svc2.name])

    finally:
        # 3. CLEANUP: Delete Group FIRST
        if created_group and created_group.id:
            try:
                service_groups_api.delete_service_groups_by_id(id=created_group.id)
            except Exception as e:
                logger.warning(f"Delete group failed: {e}")
        else:
            cleanup_group_by_name(service_groups_api, group_name)

        # 4. CLEANUP: Delete Services SECOND
        if svc1: delete_test_service(services_api, svc1.id)
        if svc2: delete_test_service(services_api, svc2.id)


def test_get_service_group_by_id(service_groups_api, clean_service_group):
    """
    Test retrieving a service group by ID.
    Equivalent to Go: Test_objects_ServiceGroupsAPIService_GetByID
    """
    if not clean_service_group:
        pytest.fail("Fixture failed to create Service Group")

    fetched_obj = service_groups_api.get_service_groups_by_id(id=clean_service_group.id)
    
    assert fetched_obj.id == clean_service_group.id
    assert fetched_obj.name == clean_service_group.name
    assert set(fetched_obj.members) == set(clean_service_group.members)


def test_update_service_group(services_api, service_groups_api, clean_service_group):
    """
    Test updating an existing service group.
    Equivalent to Go: Test_objects_ServiceGroupsAPIService_Update
    """
    if not clean_service_group:
        pytest.fail("Fixture failed to create Service Group")

    # 1. Create NEW service
    random_suffix = uuid.uuid4().hex[:6]
    new_svc = create_test_service(services_api, f"upd-svc-{random_suffix}", "tcp", "443")

    try:
        # 2. Update Group (Add new service)
        current_members = clean_service_group.members
        new_members = current_members + [new_svc.name]

        update_payload = clean_service_group
        update_payload.members = new_members
        
        updated_obj = service_groups_api.update_service_groups_by_id(
            id=clean_service_group.id, 
            service_groups=update_payload
        )
        
        assert set(updated_obj.members) == set(new_members)
    
    finally:
        # 3. Revert Update (Remove new service from group so it can be deleted)
        try:
            revert_members = [m for m in clean_service_group.members if m != new_svc.name]
            clean_service_group.members = revert_members
            service_groups_api.update_service_groups_by_id(
                id=clean_service_group.id,
                service_groups=clean_service_group
            )
        except Exception as e:
            logger.warning(f"Failed to revert update: {e}")

        # 4. Delete New Service
        delete_test_service(services_api, new_svc.id)


def test_list_service_groups(service_groups_api, clean_service_group):
    """
    Test listing service groups.
    Equivalent to Go: Test_objects_ServiceGroupsAPIService_List
    """
    if not clean_service_group:
        pytest.fail("Fixture failed to create Service Group")

    response = service_groups_api.list_service_groups(folder=TARGET_FOLDER)
    
    found = False
    for item in response.data:
        if item.id == clean_service_group.id:
            found = True
            break
    assert found is True


def test_delete_service_group_by_id(services_api, service_groups_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_ServiceGroupsAPIService_DeleteByID
    """
    random_suffix = uuid.uuid4().hex[:6]

    # 1. Create Dependencies
    svc1 = create_test_service(services_api, f"del-svc-1-{random_suffix}", "tcp", "22")
    group_name = f"test-sg-del-{random_suffix}"
    
    created_group = None

    try:
        # 2. Create Group
        payload = ServiceGroups(
            id="",
            name=group_name,
            folder=TARGET_FOLDER,
            members=[svc1.name],
        )
        created_group = service_groups_api.create_service_groups(service_groups=payload)
        
        if created_group is None:
            response = service_groups_api.list_service_groups(folder=TARGET_FOLDER)
            for entry in response.data:
                if entry.name == group_name:
                    created_group = entry
                    break

        assert created_group is not None

        # 3. Perform Delete
        service_groups_api.delete_service_groups_by_id(id=created_group.id)

        # 4. Verify 404
        try:
            service_groups_api.get_service_groups_by_id(id=created_group.id)
            pytest.fail("Group should be deleted")
        except Exception as e:
            assert "404" in str(e) or "Not Found" in str(e)

    finally:
        # 5. Cleanup Group (If delete failed)
        if created_group and created_group.id:
            try:
                service_groups_api.delete_service_groups_by_id(id=created_group.id)
            except Exception:
                pass
        else:
            cleanup_group_by_name(service_groups_api, group_name)

        # 6. Delete Service (Safe now that Group is gone)
        if svc1: delete_test_service(services_api, svc1.id)
