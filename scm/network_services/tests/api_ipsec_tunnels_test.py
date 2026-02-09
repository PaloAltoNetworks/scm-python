
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    IpsecTunnels,
    IpsecTunnelsAutoKey,
    IpsecTunnelsAutoKeyIkeGatewayInner,
    IkeGateways,
    IkeGatewaysAuthentication,
    IkeGatewaysAuthenticationPreSharedKey,
    IkeGatewaysPeerAddress,
    IkeGatewaysProtocol,
    IkeGatewaysProtocolIkev1,
    IkeCryptoProfiles,
    IkeCryptoProfilesLifetime
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "Remote Networks"

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def tunnel_api(client):
    return client.network_services.IPsecTunnelsApi(client.network_services.api_client)

@pytest.fixture(scope="module")
def ike_gw_api(client):
    return client.network_services.IKEGatewaysApi(client.network_services.api_client)

@pytest.fixture(scope="module")
def ike_crypto_api(client):
    return client.network_services.IKECryptoProfilesApi(client.network_services.api_client)

@pytest.fixture
def dependency_ike_gateway(ike_gw_api, ike_crypto_api):
    """
    Creates necessary dependencies: Crypto Profile -> IKE Gateway
    """
    # 1. Create Crypto Profile
    random_id = uuid.uuid4().hex[:6]
    crypto_name = f"dep-crypto-{random_id}"
    crypto_payload = IkeCryptoProfiles(
        name=crypto_name,
        folder=TARGET_FOLDER,
        hash=["sha256"],
        dh_group=["group14"],
        encryption=["aes-256-cbc"],
        lifetime=IkeCryptoProfilesLifetime(hours=8)
    )
    crypto_obj = ike_crypto_api.create_ike_crypto_profiles(ike_crypto_profiles=crypto_payload)

    # 2. Create IKE Gateway
    gw_name = f"dep-gw-{random_id}"
    gw_payload = IkeGateways(
        name=gw_name,
        folder=TARGET_FOLDER,
        authentication=IkeGatewaysAuthentication(
            pre_shared_key=IkeGatewaysAuthenticationPreSharedKey(key="secret123")
        ),
        peer_address=IkeGatewaysPeerAddress(ip="1.1.1.1"),
        protocol=IkeGatewaysProtocol(
            ikev1=IkeGatewaysProtocolIkev1(ike_crypto_profile=crypto_name),
            version="ikev1"
        )
    )
    gw_obj = ike_gw_api.create_ike_gateways(ike_gateways=gw_payload)

    yield gw_obj

    # Cleanup
    try:
        ike_gw_api.delete_ike_gateways_by_id(id=gw_obj.id)
    except: pass
    try:
        ike_crypto_api.delete_ike_crypto_profiles_by_id(id=crypto_obj.id)
    except: pass


@pytest.fixture
def clean_tunnel(tunnel_api, dependency_ike_gateway):
    """
    Fixture for standard CRUD tests.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-tunnel-{random_id}"
    
    payload = IpsecTunnels(
        name=name,
        folder=TARGET_FOLDER,
        anti_replay=True,
        copy_tos=False,
        auto_key=IpsecTunnelsAutoKey(
            ike_gateway=[IpsecTunnelsAutoKeyIkeGatewayInner(name=dependency_ike_gateway.name)],
            ipsec_crypto_profile="PaloAlto-Networks-IPSec-Crypto" # Default profile usually available
        )
    )
    
    logger.info(f"\n[SETUP] Creating IPsec Tunnel: {name}")
    created_obj = tunnel_api.create_i_psec_tunnels(ipsec_tunnels=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting IPsec Tunnel ID: {created_obj.id}")
    try:
        tunnel_api.delete_i_psec_tunnels_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_ipsec_tunnel(tunnel_api, dependency_ike_gateway):
    """
    Test creating an IPsec Tunnel.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-tunnel-create-{random_id}"
    
    payload = IpsecTunnels(
        name=name,
        folder=TARGET_FOLDER,
        anti_replay=True,
        copy_tos=False,
        auto_key=IpsecTunnelsAutoKey(
            ike_gateway=[IpsecTunnelsAutoKeyIkeGatewayInner(name=dependency_ike_gateway.name)],
            ipsec_crypto_profile="PaloAlto-Networks-IPSec-Crypto"
        )
    )

    try:
        created_obj = tunnel_api.create_i_psec_tunnels(ipsec_tunnels=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == name
    assert created_obj.anti_replay is True

    # Cleanup
    tunnel_api.delete_i_psec_tunnels_by_id(id=created_obj.id)


def test_get_ipsec_tunnel_by_id(tunnel_api, clean_tunnel):
    """
    Test retrieving an IPsec Tunnel by ID.
    """
    fetched_obj = tunnel_api.get_i_psec_tunnels_by_id(id=clean_tunnel.id)
    assert fetched_obj.id == clean_tunnel.id
    assert fetched_obj.name == clean_tunnel.name


def test_update_ipsec_tunnel(tunnel_api, clean_tunnel):
    """
    Test updating an IPsec Tunnel.
    """
    update_payload = clean_tunnel
    update_payload.copy_tos = True
    update_payload.anti_replay = False
    
    updated_obj = tunnel_api.update_i_psec_tunnels_by_id(
        id=clean_tunnel.id,
        ipsec_tunnels=update_payload
    )
    
    assert updated_obj.id == clean_tunnel.id
    assert updated_obj.copy_tos is True
    assert updated_obj.anti_replay is False


def test_list_ipsec_tunnels(tunnel_api, clean_tunnel):
    """
    Test listing IPsec Tunnels.
    """
    response = tunnel_api.list_i_psec_tunnels(folder=TARGET_FOLDER)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_tunnel.id:
            found = True
            break
    assert found is True



def test_delete_ipsec_tunnel_by_id(tunnel_api, dependency_ike_gateway):
    """
    Test deleting an IPsec Tunnel.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-tunnel-del-{random_id}"
    
    payload = IpsecTunnels(
        name=name,
        folder=TARGET_FOLDER,
        anti_replay=True,
        auto_key=IpsecTunnelsAutoKey(
            ike_gateway=[IpsecTunnelsAutoKeyIkeGatewayInner(name=dependency_ike_gateway.name)],
            ipsec_crypto_profile="PaloAlto-Networks-IPSec-Crypto"
        )
    )
    created_obj = tunnel_api.create_i_psec_tunnels(ipsec_tunnels=payload)
    
    tunnel_api.delete_i_psec_tunnels_by_id(id=created_obj.id)
    
    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        tunnel_api.get_i_psec_tunnels_by_id(id=created_obj.id)
        pytest.fail("Tunnel should be deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
