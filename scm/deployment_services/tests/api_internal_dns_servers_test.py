
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.internal_dns_servers import InternalDnsServers
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


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
def internal_dns_servers_api(client):
    """
    Fixture to return the InternalDNSServers API instance.
    """
    return client.deployment_services.InternalDNSServersApi(client.deployment_services.api_client)


@pytest.fixture
def clean_internal_dns_server(internal_dns_servers_api):
    """
    Fixture to create a temporary Internal DNS Server for testing and automatically delete it after.
    """
    random_id = uuid.uuid4().hex[:6]
    server_name = f"test-dns-srv-{random_id}"

    payload = InternalDnsServers(
        id="",
        name=server_name,
        domain_name=["example.com"],
        primary="8.8.8.8"
    )

    logger.info(f"\n[SETUP] Creating InternalDnsServer: {server_name}")
    created_obj = perform(
        internal_dns_servers_api.create_internal_dns_servers_with_http_info,
        response_type=InternalDnsServers,
        internal_dns_servers=payload
    )
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting InternalDnsServer ID: {created_obj.id}")
    try:
        internal_dns_servers_api.delete_internal_dns_servers_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_internal_dns_server(internal_dns_servers_api):
    """
    Test manual creation and deletion of an internal DNS server object.
    Equivalent to Go: Test_deployment_services_InternalDNSServersAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    server_name = f"test-dns-srv-create-{random_suffix}"

    payload = InternalDnsServers(
        id="",
        name=server_name,
        domain_name=["example.com"],
        primary="8.8.8.8"
    )

    # Create
    created_obj = perform(
        internal_dns_servers_api.create_internal_dns_servers_with_http_info,
        response_type=InternalDnsServers,
        internal_dns_servers=payload
    )

    # Verify
    assert created_obj.name == server_name
    assert created_obj.id is not None
    assert created_obj.primary == "8.8.8.8"
    assert "example.com" in created_obj.domain_name

    # Cleanup
    internal_dns_servers_api.delete_internal_dns_servers_by_id(id=created_obj.id)


def test_get_internal_dns_server_by_id(internal_dns_servers_api, clean_internal_dns_server):
    """
    Test retrieving an internal DNS server by its ID.
    Equivalent to Go: Test_deployment_services_InternalDNSServersAPIService_GetByID
    """
    fetched_obj = perform(
        internal_dns_servers_api.get_internal_dns_servers_by_id_with_http_info,
        response_type=InternalDnsServers,
        id=clean_internal_dns_server.id
    )

    # Verify
    assert fetched_obj.id == clean_internal_dns_server.id
    assert fetched_obj.name == clean_internal_dns_server.name


def test_update_internal_dns_server(internal_dns_servers_api, clean_internal_dns_server):
    """
    Test updating an existing internal DNS server.
    Equivalent to Go: Test_deployment_services_InternalDNSServersAPIService_Update
    """
    # Prepare Update Payload with modified fields
    update_payload = InternalDnsServers(
        id=clean_internal_dns_server.id,
        name=clean_internal_dns_server.name,
        domain_name=["example.com", "test.com"],
        primary="1.1.1.1",
        secondary="8.8.4.4"
    )

    # Perform Update
    updated_obj = perform(
        internal_dns_servers_api.update_internal_dns_servers_by_id_with_http_info,
        response_type=InternalDnsServers,
        id=clean_internal_dns_server.id,
        internal_dns_servers=update_payload
    )

    # Verify
    assert updated_obj.id == clean_internal_dns_server.id
    assert updated_obj.primary == "1.1.1.1"
    assert len(updated_obj.domain_name) == 2


def test_list_internal_dns_servers(internal_dns_servers_api, clean_internal_dns_server):
    """
    Test listing internal DNS servers.
    Equivalent to Go: Test_deployment_services_InternalDNSServersAPIService_List
    """
    response = internal_dns_servers_api.list_internal_dns_servers()

    # Verify
    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_internal_dns_server.id:
            found = True
            assert item.name == clean_internal_dns_server.name
            break
    assert found is True, f"Created DNS server {clean_internal_dns_server.name} not found in list response"


def test_fetch_internal_dns_servers(internal_dns_servers_api, clean_internal_dns_server):
    """
    Test fetching a single internal DNS server by name using the fetch convenience method.
    Equivalent to Go: Test_deployment_services_InternalDNSServersAPIService_FetchInternalDNSServers
    """
    # Fetch by exact name
    fetched_obj = internal_dns_servers_api.fetch_internal_dns_servers(
        name=clean_internal_dns_server.name,
    )

    # Verify
    assert fetched_obj is not None, f"Should have found internal_dns_servers '{clean_internal_dns_server.name}'"
    assert fetched_obj.id == clean_internal_dns_server.id
    assert fetched_obj.name == clean_internal_dns_server.name
    logger.info(f"\n[SUCCESS] fetch_internal_dns_servers found object: {fetched_obj.name}")

    # Test fetching non-existent internal_dns_servers (should return None)
    not_found = internal_dns_servers_api.fetch_internal_dns_servers(
        name="non-existent-internal-dns-xyz-12345",
    )
    assert not_found is None, "Should return None for non-existent internal_dns_servers"
    logger.info(f"\n[SUCCESS] fetch_internal_dns_servers correctly returned None for non-existent internal_dns_servers")


def test_delete_internal_dns_server_by_id(internal_dns_servers_api):
    """
    Test deleting an internal DNS server.
    Equivalent to Go: Test_deployment_services_InternalDNSServersAPIService_DeleteByID
    """
    random_suffix = uuid.uuid4().hex[:6]
    server_name = f"test-dns-srv-delete-{random_suffix}"

    payload = InternalDnsServers(
        id="",
        name=server_name,
        domain_name=["example.com"],
        primary="8.8.8.8"
    )

    # Create
    created_obj = perform(
        internal_dns_servers_api.create_internal_dns_servers_with_http_info,
        response_type=InternalDnsServers,
        internal_dns_servers=payload
    )

    # Delete
    internal_dns_servers_api.delete_internal_dns_servers_by_id(id=created_obj.id)

    # Verify deletion (expect ObjectNotPresentError)
    from scm.exceptions import ObjectNotPresentError

    try:
        internal_dns_servers_api.get_internal_dns_servers_by_id(id=created_obj.id)
        pytest.fail("DNS server should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
