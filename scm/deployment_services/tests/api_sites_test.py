
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.sites import Sites
from scm.deployment_services.models.sites_members_inner import SitesMembersInner
from scm.deployment_services.models.remote_networks import RemoteNetworks
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
RN_FOLDER = "Remote Networks"
SITES_LIST_FOLDER = "All"
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
def sites_api(client):
    """
    Fixture to return the Sites API instance.
    """
    return client.deployment_services.SitesApi(client.deployment_services.api_client)


def create_ike_crypto_profile(network_services_client, name, folder=RN_FOLDER):
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


def create_ike_gateway(network_services_client, name, crypto_profile_name, folder=RN_FOLDER):
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


def create_ipsec_tunnel(network_services_client, name, gateway_name, folder=RN_FOLDER):
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


def create_remote_network(deployment_services_client, name, tunnel_name):
    """Helper to create a Remote Network dependency for site members."""
    logger.info(f"Creating Remote Network: {name}")

    rn = RemoteNetworks(
        id="",
        name=name,
        folder=RN_FOLDER,
        spn_name="us-west-dakota",
        license_type="FWAAS-AGGREGATE",
        region="us-west-2",
        ipsec_tunnel=tunnel_name
    )

    created = perform(
        deployment_services_client.RemoteNetworksApi(deployment_services_client.api_client).create_remote_networks_with_http_info,
        response_type=RemoteNetworks,
        remote_networks=rn
    )

    logger.info(f"Created Remote Network '{name}' with ID: {created.id}")
    return created.id, created.name


def delete_remote_network(deployment_services_client, rn_id, name):
    """Helper to delete a Remote Network."""
    logger.info(f"Deleting Remote Network: {name} (ID: {rn_id})")
    try:
        deployment_services_client.RemoteNetworksApi(deployment_services_client.api_client).delete_remote_networks_by_id(id=rn_id)
        logger.info(f"Deleted Remote Network: {name}")
    except Exception as e:
        logger.error(f"Failed to delete Remote Network {name}: {e}")


@pytest.fixture
def remote_network_with_deps(network_services_client, deployment_services_client):
    """
    Fixture to create a Remote Network with all its IPsec tunnel dependencies.
    Creates: IKE Crypto Profile -> IKE Gateway -> IPsec Tunnel -> Remote Network
    Returns the remote network name.
    """
    suffix = uuid.uuid4().hex[:6]

    # Create IKE Crypto Profile
    crypto_name = f"test-crypto-s-{suffix}"
    crypto_id = create_ike_crypto_profile(network_services_client, crypto_name)

    # Create IKE Gateway
    gateway_name = f"test-gw-s-{suffix}"
    gateway_id = create_ike_gateway(network_services_client, gateway_name, crypto_name)

    # Create IPsec Tunnel
    tunnel_name = f"test-tunnel-s-{suffix}"
    tunnel_id, tunnel_name = create_ipsec_tunnel(network_services_client, tunnel_name, gateway_name)

    # Create Remote Network
    rn_name = f"test-rn-s-{suffix}"
    rn_id, rn_name = create_remote_network(deployment_services_client, rn_name, tunnel_name)

    yield rn_name

    # Cleanup in reverse order
    delete_remote_network(deployment_services_client, rn_id, rn_name)
    delete_ipsec_tunnel(network_services_client, tunnel_id, tunnel_name)
    delete_ike_gateway(network_services_client, gateway_id, gateway_name)
    delete_ike_crypto_profile(network_services_client, crypto_id, crypto_name)


@pytest.fixture
def clean_site(sites_api, remote_network_with_deps):
    """
    Fixture to create a temporary Site for testing and automatically delete it after.
    """
    random_id = uuid.uuid4().hex[:6]
    site_name = f"test-site-{random_id}"

    payload = Sites(
        name=site_name,
        city="San Jose",
        country="US",
        state="California",
        members=[
            SitesMembersInner(
                name=remote_network_with_deps,
                mode="active",
                remote_network=remote_network_with_deps
            )
        ]
    )

    logger.info(f"\n[SETUP] Creating Site: {site_name}")
    created_obj = perform(
        sites_api.create_sites_with_http_info,
        response_type=Sites,
        sites=payload
    )
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Site ID: {created_obj.id}")
    try:
        sites_api.delete_sites_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_site(sites_api, remote_network_with_deps):
    """
    Test manual creation and deletion of a site object.
    Equivalent to Go: Test_deployment_services_SitesAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    site_name = f"test-site-create-{random_suffix}"

    payload = Sites(
        name=site_name,
        city="San Jose",
        country="US",
        state="California",
        members=[
            SitesMembersInner(
                name=remote_network_with_deps,
                mode="active",
                remote_network=remote_network_with_deps
            )
        ]
    )

    # Create
    created_obj = perform(
        sites_api.create_sites_with_http_info,
        response_type=Sites,
        sites=payload
    )

    # Verify
    assert created_obj.name == site_name
    assert created_obj.id is not None

    # Cleanup
    sites_api.delete_sites_by_id(id=created_obj.id)


def test_get_site_by_id(sites_api, clean_site):
    """
    Test retrieving a site by its ID.
    Equivalent to Go: Test_deployment_services_SitesAPIService_GetByID
    """
    fetched_obj = perform(
        sites_api.get_sites_by_id_with_http_info,
        response_type=Sites,
        id=clean_site.id
    )

    # Verify
    assert fetched_obj.id == clean_site.id
    assert fetched_obj.name == clean_site.name


def test_update_site(sites_api, clean_site):
    """
    Test updating an existing site.
    Equivalent to Go: Test_deployment_services_SitesAPIService_Update
    """
    # Prepare Update Payload with modified address
    update_payload = Sites(
        name=clean_site.name,
        id=clean_site.id,
        address_line_1="123 Updated Street",
        city="San Jose",
        country="US",
        state="California",
        members=clean_site.members
    )

    # Perform Update
    updated_obj = perform(
        sites_api.update_sites_by_id_with_http_info,
        response_type=Sites,
        id=clean_site.id,
        sites=update_payload
    )

    # Verify
    assert updated_obj.id == clean_site.id
    assert updated_obj.name == clean_site.name
    assert updated_obj.address_line_1 == "123 Updated Street"


def test_list_sites(sites_api, clean_site):
    """
    Test listing sites.
    Equivalent to Go: Test_deployment_services_SitesAPIService_List
    """
    response = sites_api.list_sites(
        folder=SITES_LIST_FOLDER,
        limit=200,
        offset=0
    )

    # Verify
    assert response is not None
    assert response.total > 0
    logger.info(f"Successfully listed sites, total: {response.total}")


def test_fetch_sites(sites_api, clean_site):
    """
    Test fetching a single site by name using the fetch convenience method.
    Equivalent to Go: Test_deployment_services_SitesAPIService_FetchSites
    """
    # Fetch by exact name
    fetched_obj = sites_api.fetch_sites(
        name=clean_site.name,
        folder=SITES_LIST_FOLDER
    )

    # Verify
    assert fetched_obj is not None, f"Should have found site '{clean_site.name}'"
    assert fetched_obj.id == clean_site.id
    assert fetched_obj.name == clean_site.name
    logger.info(f"\n[SUCCESS] fetch_sites found object: {fetched_obj.name}")

    # Test fetching non-existent site (should return None)
    not_found = sites_api.fetch_sites(
        name="non-existent-site-xyz-12345",
        folder=SITES_LIST_FOLDER
    )
    assert not_found is None, "Should return None for non-existent site"
    logger.info(f"\n[SUCCESS] fetch_sites correctly returned None for non-existent site")


def test_delete_site_by_id(sites_api, remote_network_with_deps):
    """
    Test deleting a site.
    Equivalent to Go: Test_deployment_services_SitesAPIService_DeleteByID
    """
    random_suffix = uuid.uuid4().hex[:6]
    site_name = f"test-site-delete-{random_suffix}"

    payload = Sites(
        name=site_name,
        city="San Jose",
        country="US",
        state="California",
        members=[
            SitesMembersInner(
                name=remote_network_with_deps,
                mode="active",
                remote_network=remote_network_with_deps
            )
        ]
    )

    # Create
    created_obj = perform(
        sites_api.create_sites_with_http_info,
        response_type=Sites,
        sites=payload
    )

    # Delete
    sites_api.delete_sites_by_id(id=created_obj.id)

    # Verify deletion (expect ObjectNotPresentError)
    from scm.exceptions import ObjectNotPresentError

    try:
        sites_api.get_sites_by_id(id=created_obj.id)
        pytest.fail("Site should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
