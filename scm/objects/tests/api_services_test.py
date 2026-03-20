
import logging
import uuid
import pytest
from scm import Scm

from scm.objects.models import (
    Services,
    ServicesProtocol,
    ServicesProtocolTcp,
    ServicesProtocolTcpOverride,
    ServicesProtocolUdp,
    Tags
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Prisma Access"
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (To manage dependent Tag objects)
# -----------------------------------------------------------------------------
def create_test_tag(api, name):
    """Helper to create a single tag object for Service testing."""
    payload = Tags(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        description="Temp tag for Service test"
    )
    return api.create_tags(tags=payload)

def delete_test_tag(api, tag_id):
    """Helper to delete a single tag object."""
    try:
        api.delete_tags_by_id(id=tag_id)
    except Exception as e:
        # 404 is acceptable during cleanup
        if "404" not in str(e):
            logger.warning(f"Failed to cleanup tag {tag_id}: {e}")

# -----------------------------------------------------------------------------
# FIXTURES
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
def services_api(client):
    return client.objects.ServicesApi(client.objects.api_client)

@pytest.fixture(scope="module")
def tags_api(client):
    return client.objects.TagsApi(client.objects.api_client)

@pytest.fixture
def clean_service(services_api):
    """
    Fixture to create a temporary Service for testing and automatically delete it after.
    Creates a UDP service.
    """
    # 1. SETUP: Create Service
    random_id = uuid.uuid4().hex[:6]
    svc_name = f"test-svc-{random_id}"
    
    payload = Services(
        id="",
        name=svc_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        protocol=ServicesProtocol(
            udp=ServicesProtocolUdp(port="53, 55")
        )
    )
    
    logger.info(f"\n[SETUP] Creating Service: {svc_name}")
    created_obj = services_api.create_services(services=payload)
    assert created_obj.id is not None
    
    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Service
    logger.info(f"\n[TEARDOWN] Deleting Service ID: {created_obj.id}")
    try:
        services_api.delete_services_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def test_create_service(services_api, tags_api):
    """
    Test manual creation and deletion of a TCP service object with tags.
    Equivalent to Go: Test_objects_ServicesAPIService_CreateService
    """
    random_suffix = uuid.uuid4().hex[:6]
    svc_name = f"test-tcp-create-{random_suffix}"
    tag1_name = f"tag1-{random_suffix}"
    tag2_name = f"tag2-{random_suffix}"

    # 1. Create Dependencies (Tags)
    tag1 = create_test_tag(tags_api, tag1_name)
    tag2 = create_test_tag(tags_api, tag2_name)

    created_svc = None

    try:
        # 2. Create TCP Service
        payload = Services(
            id="",
            name=svc_name,
            folder=TARGET_FOLDER,
            description="Test TCP service for create API",
            protocol=ServicesProtocol(
                tcp=ServicesProtocolTcp(
                    port="1024-1026",
                    source_port="1024"
                )
            ),
            tag=[tag1.name, tag2.name]
        )

        created_svc = services_api.create_services(services=payload)

        # Verify
        assert created_svc.name == svc_name
        assert created_svc.id is not None
        assert created_svc.folder == TARGET_FOLDER or created_svc.folder == "Shared"
        assert created_svc.protocol.tcp is not None
        assert created_svc.protocol.tcp.port == "1024-1026"
        assert set(created_svc.tag) == set([tag1.name, tag2.name])

    finally:
        # 3. Cleanup Service
        if created_svc and created_svc.id:
            try:
                services_api.delete_services_by_id(id=created_svc.id)
            except Exception as e:
                logger.warning(f"Failed to delete service: {e}")

        # 4. Cleanup Tags
        delete_test_tag(tags_api, tag1.id)
        delete_test_tag(tags_api, tag2.id)


def test_get_service_by_id(services_api, clean_service):
    """
    Test retrieving a service by ID (UDP).
    Equivalent to Go: Test_objects_ServicesAPIService_GetByID
    """
    # Retrieve
    fetched_obj = services_api.get_services_by_id(id=clean_service.id)
    
    # Verify
    assert fetched_obj.id == clean_service.id
    assert fetched_obj.name == clean_service.name
    assert fetched_obj.protocol.udp is not None
    assert fetched_obj.protocol.udp.port == "53, 55"


def test_update_service(services_api, tags_api):
    """
    Test updating an existing service (TCP -> TCP with Override).
    Equivalent to Go: Test_objects_ServicesAPIService_Update
    """
    random_suffix = uuid.uuid4().hex[:6]
    svc_name = f"test-svc-update-{random_suffix}"
    
    # 1. Setup Service (TCP 3389)
    initial_payload = Services(
        id="",
        name=svc_name,
        folder=TARGET_FOLDER,
        protocol=ServicesProtocol(
            tcp=ServicesProtocolTcp(port="3389")
        )
    )
    created_svc = services_api.create_services(services=initial_payload)

    # 2. Setup New Tags
    tag1_name = f"corp-{random_suffix}"
    tag2_name = f"remote-{random_suffix}"
    tag1 = create_test_tag(tags_api, tag1_name)
    tag2 = create_test_tag(tags_api, tag2_name)

    try:
        # 3. Prepare Update Payload
        # Note: In Pydantic models, we modify properties directly
        update_payload = created_svc
        update_payload.description = "Updated RDP service"
        update_payload.tag = [tag1.name, tag2.name]
        
        # Add TCP Override (timeout)
        update_payload.protocol.tcp.override = ServicesProtocolTcpOverride(
            timeout=7200
        )

        # 4. Perform Update
        updated_obj = services_api.update_services_by_id(
            id=created_svc.id,
            services=update_payload
        )

        # 5. Verify
        assert updated_obj.description == "Updated RDP service"
        assert set(updated_obj.tag) == set([tag1.name, tag2.name])
        assert updated_obj.protocol.tcp.override is not None
        assert updated_obj.protocol.tcp.override.timeout == 7200
        assert updated_obj.id == created_svc.id

    finally:
        # Cleanup Service
        try:
            services_api.delete_services_by_id(id=created_svc.id)
        except Exception as e:
            logger.warning(f"Failed to delete service: {e}")
            
        # Cleanup Tags
        delete_test_tag(tags_api, tag1.id)
        delete_test_tag(tags_api, tag2.id)


def test_list_services(services_api, clean_service):
    """
    Test listing services.
    Equivalent to Go: Test_objects_ServicesAPIService_List
    """
    response = services_api.list_services(folder=TARGET_FOLDER, limit=10000)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.id == clean_service.id:
            found = True
            assert item.name == clean_service.name
            break
            
    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")




def test_fetch_services(services_api, clean_service):
    """
    Test fetching a single services by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = services_api.fetch_services(
        name=clean_service.name,
        folder=clean_service.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found services '{clean_service.name}'"
    assert fetched_obj.id == clean_service.id
    assert fetched_obj.name == clean_service.name
    assert fetched_obj.folder == clean_service.folder
    logger.info(f"\n[SUCCESS] fetch_services found object: {fetched_obj.name}")

    # Test fetching non-existent services (should return None)
    not_found = services_api.fetch_services(
        name="non-existent-services-xyz-12345",
        folder=clean_service.folder
    )
    assert not_found is None, "Should return None for non-existent services"
    logger.info(f"\n[SUCCESS] fetch_services correctly returned None for non-existent services")


def test_delete_service_by_id(services_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_ServicesAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    svc_name = f"test-svc-del-{random_suffix}"
    
    payload = Services(
        id="",
        name=svc_name,
        folder=TARGET_FOLDER,
        protocol=ServicesProtocol(
            tcp=ServicesProtocolTcp(port="9999")
        )
    )
    created_obj = services_api.create_services(services=payload)

    # Perform Delete
    services_api.delete_services_by_id(id=created_obj.id)

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    from scm.exceptions import ObjectNotPresentError
    # Decorator already converts NotFoundException to ObjectNotPresentError

    try:
        services_api.get_services_by_id(id=created_obj.id)
        pytest.fail("Service should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
