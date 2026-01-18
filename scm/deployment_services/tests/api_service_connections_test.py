
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.service_connections import ServiceConnections

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
def service_connections_api(client):
    """
    Fixture to return the ServiceConnections API instance.
    """
    return client.deployment_services.ServiceConnectionsApi(client.deployment_services.api_client)

@pytest.fixture
def clean_service_connection(service_connections_api):
    """
    Fixture to create a temporary ServiceConnection for testing and automatically delete it after.
    """
    # 1. SETUP: Create ServiceConnection
    random_id = uuid.uuid4().hex[:6]
    connection_name = f"test-sc-{random_id}"

    payload = ServiceConnections(
        id="",
        name=connection_name,
        region="us-east-1",
        ipsec_tunnel="ipsec-tunnel-1",
        subnets=["10.0.0.0/24"],
        onboarding_type="classic"
    )

    logger.info(f"\n[SETUP] Creating ServiceConnection: {connection_name}")
    created_obj = service_connections_api.create_service_connections(service_connections=payload)
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete ServiceConnection
    logger.info(f"\n[TEARDOWN] Deleting ServiceConnection ID: {created_obj.id}")
    try:
        service_connections_api.delete_service_connections_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_service_connection(service_connections_api):
    """
    Test manual creation and deletion of a service connection object.
    Equivalent to Go: Test_deployment_services_ServiceConnectionsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    connection_name = f"test-sc-create-{random_suffix}"

    payload = ServiceConnections(
        id="",
        name=connection_name,
        region="us-west-2",
        ipsec_tunnel="ipsec-tunnel-test",
        subnets=["192.168.1.0/24", "192.168.2.0/24"],
        onboarding_type="classic",
        source_nat=True
    )

    # Create
    created_obj = service_connections_api.create_service_connections(service_connections=payload)

    # Verify
    assert created_obj.name == connection_name
    assert created_obj.id is not None
    assert created_obj.region == "us-west-2"
    assert created_obj.ipsec_tunnel == "ipsec-tunnel-test"
    assert set(created_obj.subnets) == set(["192.168.1.0/24", "192.168.2.0/24"])
    assert created_obj.source_nat == True

    # Cleanup
    service_connections_api.delete_service_connections_by_id(id=created_obj.id)


def test_get_service_connection_by_id(service_connections_api, clean_service_connection):
    """
    Test retrieving a service connection by ID.
    Equivalent to Go: Test_deployment_services_ServiceConnectionsAPIService_GetByID
    """
    # Retrieve
    fetched_obj = service_connections_api.get_service_connections_by_id(id=clean_service_connection.id)

    # Verify
    assert fetched_obj.id == clean_service_connection.id
    assert fetched_obj.name == clean_service_connection.name
    assert fetched_obj.region == clean_service_connection.region
    assert fetched_obj.ipsec_tunnel == clean_service_connection.ipsec_tunnel


def test_update_service_connection(service_connections_api, clean_service_connection):
    """
    Test updating an existing service connection.
    Equivalent to Go: Test_deployment_services_ServiceConnectionsAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_service_connection
    update_payload.subnets = ["10.1.0.0/24", "10.2.0.0/24", "10.3.0.0/24"]
    update_payload.region = "us-west-1"
    update_payload.source_nat = True

    # Perform Update
    updated_obj = service_connections_api.update_service_connections_by_id(
        id=clean_service_connection.id,
        service_connections=update_payload
    )

    # Verify
    assert updated_obj.id == clean_service_connection.id
    assert updated_obj.name == clean_service_connection.name
    assert set(updated_obj.subnets) == set(["10.1.0.0/24", "10.2.0.0/24", "10.3.0.0/24"])
    assert updated_obj.region == "us-west-1"
    assert updated_obj.source_nat == True


def test_list_service_connections(service_connections_api, clean_service_connection):
    """
    Test listing service connections.
    Equivalent to Go: Test_deployment_services_ServiceConnectionsAPIService_List
    """
    # List all service connections
    response = service_connections_api.list_service_connections(limit=10000)

    assert response is not None
    assert len(response.data) > 0

    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.name == clean_service_connection.name:
            found = True
            break

    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_delete_service_connection_by_id(service_connections_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_deployment_services_ServiceConnectionsAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    connection_name = f"test-sc-delete-{random_suffix}"

    payload = ServiceConnections(
        id="",
        name=connection_name,
        region="eu-west-1",
        ipsec_tunnel="ipsec-tunnel-delete",
        subnets=["172.16.0.0/24"],
        onboarding_type="classic"
    )
    created_obj = service_connections_api.create_service_connections(service_connections=payload)

    # Perform Delete
    service_connections_api.delete_service_connections_by_id(id=created_obj.id)

    # Verify Deletion (Expect 404 on Get)
    try:
        service_connections_api.get_service_connections_by_id(id=created_obj.id)
        pytest.fail("ServiceConnection should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
