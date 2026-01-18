
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.remote_networks import RemoteNetworks

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
def remote_networks_api(client):
    """
    Fixture to return the RemoteNetworks API instance.
    """
    return client.deployment_services.RemoteNetworksApi(client.deployment_services.api_client)

@pytest.fixture
def clean_remote_network(remote_networks_api):
    """
    Fixture to create a temporary RemoteNetwork for testing and automatically delete it after.
    """
    # 1. SETUP: Create RemoteNetwork
    random_id = uuid.uuid4().hex[:6]
    network_name = f"test-rn-{random_id}"

    payload = RemoteNetworks(
        id="",
        name=network_name,
        folder=TARGET_FOLDER,
        region="us-east-1",
        license_type="FWAAS-AGGREGATE",
        subnets=["10.0.0.0/24"],
        ipsec_tunnel="ipsec-tunnel-1",
        spn_name="test-spn"
    )

    logger.info(f"\n[SETUP] Creating RemoteNetwork: {network_name}")
    created_obj = remote_networks_api.create_remote_networks(remote_networks=payload)
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete RemoteNetwork
    logger.info(f"\n[TEARDOWN] Deleting RemoteNetwork ID: {created_obj.id}")
    try:
        remote_networks_api.delete_remote_networks_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_remote_network(remote_networks_api):
    """
    Test manual creation and deletion of a remote network object.
    Equivalent to Go: Test_deployment_services_RemoteNetworksAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    network_name = f"test-rn-create-{random_suffix}"

    payload = RemoteNetworks(
        id="",
        name=network_name,
        folder=TARGET_FOLDER,
        region="us-west-2",
        license_type="FWAAS-AGGREGATE",
        subnets=["192.168.1.0/24", "192.168.2.0/24"],
        ipsec_tunnel="ipsec-tunnel-test",
        spn_name="test-spn-create"
    )

    # Create
    created_obj = remote_networks_api.create_remote_networks(remote_networks=payload)

    # Verify
    assert created_obj.name == network_name
    assert created_obj.id is not None
    assert created_obj.region == "us-west-2"
    assert created_obj.license_type == "FWAAS-AGGREGATE"
    assert set(created_obj.subnets) == set(["192.168.1.0/24", "192.168.2.0/24"])
    assert created_obj.folder == TARGET_FOLDER

    # Cleanup
    remote_networks_api.delete_remote_networks_by_id(id=created_obj.id)


def test_get_remote_network_by_id(remote_networks_api, clean_remote_network):
    """
    Test retrieving a remote network by ID.
    Equivalent to Go: Test_deployment_services_RemoteNetworksAPIService_GetByID
    """
    # Retrieve
    fetched_obj = remote_networks_api.get_remote_networks_by_id(id=clean_remote_network.id)

    # Verify
    assert fetched_obj.id == clean_remote_network.id
    assert fetched_obj.name == clean_remote_network.name
    assert fetched_obj.region == clean_remote_network.region
    assert fetched_obj.license_type == clean_remote_network.license_type


def test_update_remote_network(remote_networks_api, clean_remote_network):
    """
    Test updating an existing remote network.
    Equivalent to Go: Test_deployment_services_RemoteNetworksAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_remote_network
    update_payload.subnets = ["10.1.0.0/24", "10.2.0.0/24", "10.3.0.0/24"]
    update_payload.region = "us-west-1"

    # Perform Update
    updated_obj = remote_networks_api.update_remote_networks_by_id(
        id=clean_remote_network.id,
        remote_networks=update_payload
    )

    # Verify
    assert updated_obj.id == clean_remote_network.id
    assert updated_obj.name == clean_remote_network.name
    assert set(updated_obj.subnets) == set(["10.1.0.0/24", "10.2.0.0/24", "10.3.0.0/24"])
    assert updated_obj.region == "us-west-1"


def test_list_remote_networks(remote_networks_api, clean_remote_network):
    """
    Test listing remote networks with folder filter.
    Equivalent to Go: Test_deployment_services_RemoteNetworksAPIService_List
    """
    # List with filter
    response = remote_networks_api.list_remote_networks(folder=TARGET_FOLDER, limit=10000)

    assert response is not None
    assert len(response.data) > 0

    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.name == clean_remote_network.name:
            found = True
            break

    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_delete_remote_network_by_id(remote_networks_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_deployment_services_RemoteNetworksAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    network_name = f"test-rn-delete-{random_suffix}"

    payload = RemoteNetworks(
        id="",
        name=network_name,
        folder=TARGET_FOLDER,
        region="eu-west-1",
        license_type="FWAAS-AGGREGATE",
        subnets=["172.16.0.0/24"],
        ipsec_tunnel="ipsec-tunnel-delete",
        spn_name="test-spn-delete"
    )
    created_obj = remote_networks_api.create_remote_networks(remote_networks=payload)

    # Perform Delete
    remote_networks_api.delete_remote_networks_by_id(id=created_obj.id)

    # Verify Deletion (Expect 404 on Get)
    try:
        remote_networks_api.get_remote_networks_by_id(id=created_obj.id)
        pytest.fail("RemoteNetwork should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
