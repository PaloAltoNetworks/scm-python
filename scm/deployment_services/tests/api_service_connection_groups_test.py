
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.service_connection_groups import ServiceConnectionGroups
from scm.deployment_services.models.service_connections import ServiceConnections
from scm.network_services.models.ike_crypto_profiles import IkeCryptoProfiles
from scm.network_services.models.ike_gateways import IkeGateways
from scm.network_services.models.ike_gateways_authentication import IkeGatewaysAuthentication
from scm.network_services.models.ike_gateways_authentication_pre_shared_key import IkeGatewaysAuthenticationPreSharedKey
from scm.network_services.models.ike_gateways_peer_address import IkeGatewaysPeerAddress
from scm.network_services.models.ike_gateways_peer_id import IkeGatewaysPeerId
from scm.network_services.models.ike_gateways_local_id import IkeGatewaysLocalId
from scm.network_services.models.ike_gateways_protocol import IkeGatewaysProtocol
from scm.network_services.models.ike_gateways_protocol_ikev1 import IkeGatewaysProtocolIkev1
from scm.network_services.models.ike_gateways_protocol_ikev1_dpd import IkeGatewaysProtocolIkev1Dpd
from scm.network_services.models.ipsec_tunnels import IpsecTunnels
from scm.network_services.models.ipsec_tunnels_auto_key import IpsecTunnelsAutoKey
from scm.network_services.models.ipsec_tunnels_auto_key_ike_gateway_inner import IpsecTunnelsAutoKeyIkeGatewayInner
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Service Connections"
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
def network_services_client(client):
    """Return network services API client for creating dependencies."""
    return client.network_services


@pytest.fixture(scope="module")
def deployment_services_client(client):
    """Return deployment services API client."""
    return client.deployment_services


@pytest.fixture(scope="module")
def service_connection_groups_api(client):
    """
    Fixture to return the ServiceConnectionGroups API instance.
    """
    return client.deployment_services.ServiceConnectionGroupsApi(client.deployment_services.api_client)


def create_ike_crypto_profile(network_services_client, name, folder=TARGET_FOLDER):
    """Helper to create an IKE Crypto Profile dependency."""
    logger.info(f"Creating IKE Crypto Profile: {name}")

    profile = IkeCryptoProfiles(
        name=name,
        folder=folder,
        hash=["sha256"],
        dh_group=["group14"],
        encryption=["aes-256-cbc"]
    )

    created = perform(
        network_services_client.IKECryptoProfilesApi(network_services_client.api_client).create_ike_crypto_profiles_with_http_info,
        response_type=IkeCryptoProfiles,
        ike_crypto_profiles=profile
    )

    logger.info(f"Created IKE Crypto Profile '{name}' with ID: {created.id}")
    return created.id


def delete_ike_crypto_profile(network_services_client, profile_id, name):
    """Helper to delete an IKE Crypto Profile."""
    logger.info(f"Deleting IKE Crypto Profile: {name} (ID: {profile_id})")
    try:
        network_services_client.IKECryptoProfilesApi(network_services_client.api_client).delete_ike_crypto_profiles_by_id(id=profile_id)
        logger.info(f"Deleted IKE Crypto Profile: {name}")
    except Exception as e:
        logger.error(f"Failed to delete IKE Crypto Profile {name}: {e}")


def create_ike_gateway(network_services_client, name, crypto_profile_name, folder=TARGET_FOLDER):
    """Helper to create an IKE Gateway dependency."""
    logger.info(f"Creating IKE Gateway: {name}")

    gateway = IkeGateways(
        name=name,
        folder=folder,
        authentication=IkeGatewaysAuthentication(
            pre_shared_key=IkeGatewaysAuthenticationPreSharedKey(key="123456")
        ),
        peer_address=IkeGatewaysPeerAddress(ip="2.2.2.4"),
        peer_id=IkeGatewaysPeerId(type="ipaddr", id="10.3.3.4"),
        local_id=IkeGatewaysLocalId(type="ipaddr", id="10.3.4.4"),
        protocol=IkeGatewaysProtocol(
            ikev1=IkeGatewaysProtocolIkev1(
                ike_crypto_profile=crypto_profile_name,
                dpd=IkeGatewaysProtocolIkev1Dpd(enable=True)
            ),
            ikev2=IkeGatewaysProtocolIkev1(
                ike_crypto_profile=crypto_profile_name,
                dpd=IkeGatewaysProtocolIkev1Dpd(enable=True)
            )
        )
    )

    created = perform(
        network_services_client.IKEGatewaysApi(network_services_client.api_client).create_ike_gateways_with_http_info,
        response_type=IkeGateways,
        ike_gateways=gateway
    )

    logger.info(f"Created IKE Gateway '{name}' with ID: {created.id}")
    return created.id


def delete_ike_gateway(network_services_client, gateway_id, name):
    """Helper to delete an IKE Gateway."""
    logger.info(f"Deleting IKE Gateway: {name} (ID: {gateway_id})")
    try:
        network_services_client.IKEGatewaysApi(network_services_client.api_client).delete_ike_gateways_by_id(id=gateway_id)
        logger.info(f"Deleted IKE Gateway: {name}")
    except Exception as e:
        logger.error(f"Failed to delete IKE Gateway {name}: {e}")


def create_ipsec_tunnel(network_services_client, name, gateway_name, folder=TARGET_FOLDER):
    """Helper to create an IPsec Tunnel dependency."""
    logger.info(f"Creating IPsec Tunnel: {name}")

    tunnel = IpsecTunnels(
        name=name,
        folder=folder,
        anti_replay=True,
        copy_tos=False,
        enable_gre_encapsulation=False,
        auto_key=IpsecTunnelsAutoKey(
            ike_gateway=[IpsecTunnelsAutoKeyIkeGatewayInner(name=gateway_name)],
            ipsec_crypto_profile="PaloAlto-Networks-IPSec-Crypto"
        )
    )

    created = perform(
        network_services_client.IPsecTunnelsApi(network_services_client.api_client).create_i_psec_tunnels_with_http_info,
        response_type=IpsecTunnels,
        ipsec_tunnels=tunnel
    )

    logger.info(f"Created IPsec Tunnel '{name}' with ID: {created.id}")
    return created.id, created.name


def delete_ipsec_tunnel(network_services_client, tunnel_id, name):
    """Helper to delete an IPsec Tunnel."""
    logger.info(f"Deleting IPsec Tunnel: {name} (ID: {tunnel_id})")
    try:
        network_services_client.IPsecTunnelsApi(network_services_client.api_client).delete_i_psec_tunnels_by_id(id=tunnel_id)
        logger.info(f"Deleted IPsec Tunnel: {name}")
    except Exception as e:
        logger.error(f"Failed to delete IPsec Tunnel {name}: {e}")


def create_service_connection(deployment_services_client, name, tunnel_name):
    """Helper to create a Service Connection dependency."""
    logger.info(f"Creating Service Connection: {name}")

    sc = ServiceConnections(
        id="",
        name=name,
        ipsec_tunnel=tunnel_name,
        region="us-central1-a",
        onboarding_type="classic",
        subnets=["10.0.0.0/24"],
        source_nat=True
    )

    created = perform(
        deployment_services_client.ServiceConnectionsApi(deployment_services_client.api_client).create_service_connections_with_http_info,
        response_type=ServiceConnections,
        service_connections=sc
    )

    logger.info(f"Created Service Connection '{name}' with ID: {created.id}")
    return created.id, created.name


def delete_service_connection(deployment_services_client, sc_id, name):
    """Helper to delete a Service Connection."""
    logger.info(f"Deleting Service Connection: {name} (ID: {sc_id})")
    try:
        deployment_services_client.ServiceConnectionsApi(deployment_services_client.api_client).delete_service_connections_by_id(id=sc_id)
        logger.info(f"Deleted Service Connection: {name}")
    except Exception as e:
        logger.error(f"Failed to delete Service Connection {name}: {e}")


@pytest.fixture
def service_connection_with_deps(network_services_client, deployment_services_client):
    """
    Fixture to create a full Service Connection with all dependencies.
    Creates: IKE Crypto Profile → IKE Gateway → IPsec Tunnel → Service Connection
    Returns the SC name and cleanup function.
    """
    suffix = uuid.uuid4().hex[:6]

    # Create IKE Crypto Profile
    crypto_name = f"test-crypto-scg-{suffix}"
    crypto_id = create_ike_crypto_profile(network_services_client, crypto_name)

    # Create IKE Gateway
    gateway_name = f"test-gw-scg-{suffix}"
    gateway_id = create_ike_gateway(network_services_client, gateway_name, crypto_name)

    # Create IPsec Tunnel
    tunnel_name = f"test-tunnel-scg-{suffix}"
    tunnel_id, tunnel_name = create_ipsec_tunnel(network_services_client, tunnel_name, gateway_name)

    # Create Service Connection
    sc_name = f"test-sc-scg-{suffix}"
    sc_id, sc_name = create_service_connection(deployment_services_client, sc_name, tunnel_name)

    yield sc_name

    # Cleanup in reverse order
    delete_service_connection(deployment_services_client, sc_id, sc_name)
    delete_ipsec_tunnel(network_services_client, tunnel_id, tunnel_name)
    delete_ike_gateway(network_services_client, gateway_id, gateway_name)
    delete_ike_crypto_profile(network_services_client, crypto_id, crypto_name)


@pytest.fixture
def clean_service_connection_group(service_connection_groups_api, service_connection_with_deps):
    """
    Fixture to create a temporary ServiceConnectionGroup for testing and automatically delete it after.
    """
    random_id = uuid.uuid4().hex[:6]
    group_name = f"test-scg-{random_id}"

    payload = ServiceConnectionGroups(
        id="",
        name=group_name,
        target=[service_connection_with_deps],
        disable_snat=True
    )

    logger.info(f"\n[SETUP] Creating ServiceConnectionGroup: {group_name}")
    created_obj = perform(
        service_connection_groups_api.create_service_connection_groups_with_http_info,
        response_type=ServiceConnectionGroups,
        service_connection_groups=payload
    )
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting ServiceConnectionGroup ID: {created_obj.id}")
    try:
        service_connection_groups_api.delete_service_connection_groups_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_service_connection_group(service_connection_groups_api, service_connection_with_deps):
    """
    Test manual creation and deletion of a service connection group object.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    group_name = f"test-scg-create-{random_suffix}"

    payload = ServiceConnectionGroups(
        id="",
        name=group_name,
        target=[service_connection_with_deps],
        disable_snat=True
    )

    # Create
    created_obj = perform(
        service_connection_groups_api.create_service_connection_groups_with_http_info,
        response_type=ServiceConnectionGroups,
        service_connection_groups=payload
    )

    # Verify
    assert created_obj.name == group_name
    assert created_obj.id is not None
    assert service_connection_with_deps in created_obj.target

    # Cleanup
    service_connection_groups_api.delete_service_connection_groups_by_id(id=created_obj.id)


def test_get_service_connection_group_by_id(service_connection_groups_api, clean_service_connection_group):
    """
    Test retrieving a service connection group by its ID.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_GetByID
    """
    fetched_obj = perform(
        service_connection_groups_api.get_service_connection_groups_by_id_with_http_info,
        response_type=ServiceConnectionGroups,
        id=clean_service_connection_group.id
    )

    # Verify
    assert fetched_obj.id == clean_service_connection_group.id
    assert fetched_obj.name == clean_service_connection_group.name


def test_update_service_connection_group(service_connection_groups_api, clean_service_connection_group):
    """
    Test updating an existing service connection group.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_service_connection_group
    update_payload.disable_snat = False

    # Perform Update
    updated_obj = perform(
        service_connection_groups_api.update_service_connection_groups_by_id_with_http_info,
        response_type=ServiceConnectionGroups,
        id=clean_service_connection_group.id,
        service_connection_groups=update_payload
    )

    # Verify
    assert updated_obj.id == clean_service_connection_group.id
    assert updated_obj.name == clean_service_connection_group.name
    assert updated_obj.disable_snat is False


def test_list_service_connection_groups(service_connection_groups_api, clean_service_connection_group):
    """
    Test listing service connection groups.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_List
    """
    response = perform(
        service_connection_groups_api.list_service_connection_groups_with_http_info,
        folder=TARGET_FOLDER
    )

    # Verify
    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_service_connection_group.name:
            found = True
            break
    assert found is True, f"Created group {clean_service_connection_group.name} not found in list response"



def test_delete_service_connection_group_by_id(service_connection_groups_api, service_connection_with_deps):
    """
    Test deleting a service connection group.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_DeleteByID
    """
    random_suffix = uuid.uuid4().hex[:6]
    group_name = f"test-scg-delete-{random_suffix}"

    payload = ServiceConnectionGroups(
        id="",
        name=group_name,
        target=[service_connection_with_deps],
        disable_snat=True
    )

    # Create
    created_obj = perform(
        service_connection_groups_api.create_service_connection_groups_with_http_info,
        response_type=ServiceConnectionGroups,
        service_connection_groups=payload
    )

    # Delete
    service_connection_groups_api.delete_service_connection_groups_by_id(id=created_obj.id)

    # Verify deletion (expect ObjectNotPresentError)
    from scm.exceptions import ObjectNotPresentError
    # Decorator already converts NotFoundException to ObjectNotPresentError

    try:
        service_connection_groups_api.get_service_connection_groups_by_id(id=created_obj.id)
        pytest.fail("Group should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")


def test_fetch_service_connection_groups(service_connection_groups_api, clean_service_connection_group):
    """
    Test fetching a single service connection group by name using the fetch convenience method.
    Equivalent to Go: Test_deployment_services_ServiceConnectionGroupsAPIService_FetchServiceConnectionGroups
    """
    # Fetch by exact name
    fetched_obj = service_connection_groups_api.fetch_service_connection_groups(
        name=clean_service_connection_group.name,
        folder=TARGET_FOLDER
    )

    # Verify
    assert fetched_obj is not None, f"Should have found group '{clean_service_connection_group.name}'"
    assert fetched_obj.id == clean_service_connection_group.id
    assert fetched_obj.name == clean_service_connection_group.name
    logger.info(f"\n[SUCCESS] fetch_service_connection_groups found object: {fetched_obj.name}")

    # Test fetching non-existent group (should return None)
    not_found = service_connection_groups_api.fetch_service_connection_groups(
        name="non-existent-service-connection-group-xyz-12345",
        folder=TARGET_FOLDER
    )
    assert not_found is None, "Should return None for non-existent group"
    logger.info(f"\n[SUCCESS] fetch_service_connection_groups correctly returned None for non-existent group")
