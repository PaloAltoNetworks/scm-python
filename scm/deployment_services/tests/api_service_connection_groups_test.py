
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.service_connection_groups import ServiceConnectionGroups

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
# -----------------------------------------------------------------------------

@pytest.fixture(scope="module")
def client():
    """
    Fixture to initialize the SCM client once for the module.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def service_connection_groups_api(client):
    """
    Fixture to return the ServiceConnectionGroups API instance.
    """
    return client.deployment_services.ServiceConnectionGroupsApi(client.deployment_services.api_client)

@pytest.fixture
def clean_service_connection_group(service_connection_groups_api):
    """
    Fixture to create a temporary ServiceConnectionGroup for testing and automatically delete it after.
    """
    # 1. SETUP: Create ServiceConnectionGroup
    random_id = uuid.uuid4().hex[:6]
    group_name = f"test-scg-{random_id}"

    payload = ServiceConnectionGroups(
        id="",
        name=group_name,
        target=[TARGET_FOLDER],
        disable_snat=False,
        pbf_only=False
    )

    logger.info(f"\n[SETUP] Creating ServiceConnectionGroup: {group_name}")
    created_obj = service_connection_groups_api.create_service_connection_groups(service_connection_groups=payload)
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete ServiceConnectionGroup
    logger.info(f"\n[TEARDOWN] Deleting ServiceConnectionGroup ID: {created_obj.id}")
    try:
        service_connection_groups_api.delete_service_connection_groups_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_service_connection_group(service_connection_groups_api):
    """
    Test manual creation and deletion of a service connection group object.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    group_name = f"test-scg-create-{random_suffix}"

    payload = ServiceConnectionGroups(
        id="",
        name=group_name,
        target=[TARGET_FOLDER],
        disable_snat=True,
        pbf_only=False
    )

    # Create
    created_obj = service_connection_groups_api.create_service_connection_groups(service_connection_groups=payload)

    # Verify
    assert created_obj.name == group_name
    assert created_obj.id is not None
    assert created_obj.disable_snat == True
    assert created_obj.pbf_only == False
    assert TARGET_FOLDER in created_obj.target

    # Cleanup
    service_connection_groups_api.delete_service_connection_groups_by_id(id=created_obj.id)


def test_get_service_connection_group_by_id(service_connection_groups_api, clean_service_connection_group):
    """
    Test retrieving a service connection group by ID.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_GetByID
    """
    # Retrieve
    fetched_obj = service_connection_groups_api.get_service_connection_groups_by_id(id=clean_service_connection_group.id)

    # Verify
    assert fetched_obj.id == clean_service_connection_group.id
    assert fetched_obj.name == clean_service_connection_group.name
    assert fetched_obj.target == clean_service_connection_group.target


def test_update_service_connection_group(service_connection_groups_api, clean_service_connection_group):
    """
    Test updating an existing service connection group.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_service_connection_group
    update_payload.disable_snat = True
    update_payload.pbf_only = True

    # Perform Update
    updated_obj = service_connection_groups_api.update_service_connection_groups_by_id(
        id=clean_service_connection_group.id,
        service_connection_groups=update_payload
    )

    # Verify
    assert updated_obj.id == clean_service_connection_group.id
    assert updated_obj.name == clean_service_connection_group.name
    assert updated_obj.disable_snat == True
    assert updated_obj.pbf_only == True


def test_list_service_connection_groups(service_connection_groups_api, clean_service_connection_group):
    """
    Test listing service connection groups.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_List
    """
    # List all service connection groups
    response = service_connection_groups_api.list_service_connection_groups(limit=10000)

    assert response is not None
    assert len(response.data) > 0

    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.name == clean_service_connection_group.name:
            found = True
            break

    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_delete_service_connection_group_by_id(service_connection_groups_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    group_name = f"test-scg-delete-{random_suffix}"

    payload = ServiceConnectionGroups(
        id="",
        name=group_name,
        target=[TARGET_FOLDER],
        disable_snat=False,
        pbf_only=False
    )
    created_obj = service_connection_groups_api.create_service_connection_groups(service_connection_groups=payload)

    # Perform Delete
    service_connection_groups_api.delete_service_connection_groups_by_id(id=created_obj.id)

    # Verify Deletion (Expect 404 on Get)
    try:
        service_connection_groups_api.get_service_connection_groups_by_id(id=created_obj.id)
        pytest.fail("ServiceConnectionGroup should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
