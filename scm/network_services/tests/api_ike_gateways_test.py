
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    IkeCryptoProfiles,
    IkeCryptoProfilesLifetime,
    IkeGateways,
    IkeGatewaysAuthentication,
    IkeGatewaysAuthenticationPreSharedKey,
    IkeGatewaysPeerAddress,
    IkeGatewaysProtocol,
    IkeGatewaysProtocolIkev1,
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
def ike_gw_api(client):
    return client.network_services.IKEGatewaysApi(client.network_services.api_client)

@pytest.fixture(scope="module")
def ike_crypto_api(client):
    return client.network_services.IKECryptoProfilesApi(client.network_services.api_client)

@pytest.fixture
def crypto_profile(ike_crypto_api):
    """Fixture to create dependency IKE Crypto Profile."""
    random_id = uuid.uuid4().hex[:6]
    name = f"dep-crypto-{random_id}"
    payload = IkeCryptoProfiles(
		id="",
        name=name,
        folder=TARGET_FOLDER,
        hash=["sha256"],
        dh_group=["group14"],
        encryption=["aes-256-cbc"],
        lifetime=IkeCryptoProfilesLifetime(hours=8)
    )
    created = ike_crypto_api.create_ike_crypto_profiles(ike_crypto_profiles=payload)
    yield created
    try:
        ike_crypto_api.delete_ike_crypto_profiles_by_id(id=created.id)
    except:
        pass

@pytest.fixture
def clean_ike_gateway(ike_gw_api, crypto_profile):
    """
    Fixture for standard CRUD tests.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ike-gw-{random_id}"
    
    payload = IkeGateways(
        name=name,
        folder=TARGET_FOLDER,
        authentication=IkeGatewaysAuthentication(
            pre_shared_key=IkeGatewaysAuthenticationPreSharedKey(key="secret123")
        ),
        peer_address=IkeGatewaysPeerAddress(ip="1.1.1.1"),
        protocol=IkeGatewaysProtocol(
            ikev1=IkeGatewaysProtocolIkev1(
                ike_crypto_profile=crypto_profile.name
            ),
            version="ikev1"
        )
    )
    
    logger.info(f"\n[SETUP] Creating IKE Gateway: {name}")
    created_obj = ike_gw_api.create_ike_gateways(ike_gateways=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting IKE Gateway ID: {created_obj.id}")
    try:
        ike_gw_api.delete_ike_gateways_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_ike_gateway(ike_gw_api, crypto_profile):
    """
    Test creating an IKE Gateway.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ikegw-create-{random_id}"
    
    payload = IkeGateways(
        name=name,
        folder=TARGET_FOLDER,
        authentication=IkeGatewaysAuthentication(
            pre_shared_key=IkeGatewaysAuthenticationPreSharedKey(key="secret123")
        ),
        peer_address=IkeGatewaysPeerAddress(ip="8.8.8.8"),
        protocol=IkeGatewaysProtocol(
            ikev1=IkeGatewaysProtocolIkev1(
                ike_crypto_profile=crypto_profile.name
            ),
            version="ikev1"
        )
    )

    try:
        created_obj = ike_gw_api.create_ike_gateways(ike_gateways=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == name
    assert created_obj.peer_address.ip == "8.8.8.8"

    # Cleanup
    ike_gw_api.delete_ike_gateways_by_id(id=created_obj.id)


def test_get_ike_gateway_by_id(ike_gw_api, clean_ike_gateway):
    """
    Test retrieving an IKE Gateway by ID.
    """
    fetched_obj = ike_gw_api.get_ike_gateways_by_id(id=clean_ike_gateway.id)
    assert fetched_obj.id == clean_ike_gateway.id
    assert fetched_obj.name == clean_ike_gateway.name
    assert fetched_obj.peer_address.ip == "1.1.1.1"


def test_update_ike_gateway(ike_gw_api, clean_ike_gateway):
    """
    Test updating an IKE Gateway.
    """
    update_payload = clean_ike_gateway
    update_payload.peer_address.ip = "2.2.2.2"
    update_payload.authentication.pre_shared_key.key = "newsecret456"
    
    updated_obj = ike_gw_api.update_ike_gateways_by_id(
        id=clean_ike_gateway.id,
        ike_gateways=update_payload
    )
    
    assert updated_obj.id == clean_ike_gateway.id
    assert updated_obj.peer_address.ip == "2.2.2.2"


def test_list_ike_gateways(ike_gw_api, clean_ike_gateway):
    """
    Test listing IKE Gateways.
    """
    response = ike_gw_api.list_ike_gateways(folder=TARGET_FOLDER)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_ike_gateway.id:
            found = True
            break
    assert found is True




def test_fetch_ike_gateways(ike_gw_api, clean_ike_gateway):
    """
    Test fetching a single ike_gateways by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = ike_gw_api.fetch_ike_gateways(
        name=clean_ike_gateway.name,
        folder=clean_ike_gateway.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found ike_gateways '{clean_ike_gateway.name}'"
    assert fetched_obj.id == clean_ike_gateway.id
    assert fetched_obj.name == clean_ike_gateway.name
    assert fetched_obj.folder == clean_ike_gateway.folder
    logger.info(f"\n[SUCCESS] fetch_ike_gateways found object: {fetched_obj.name}")

    # Test fetching non-existent ike_gateways (should return None)
    not_found = ike_gw_api.fetch_ike_gateways(
        name="non-existent-ike_gateways-xyz-12345",
        folder=clean_ike_gateway.folder
    )
    assert not_found is None, "Should return None for non-existent ike_gateways"
    logger.info(f"\n[SUCCESS] fetch_ike_gateways correctly returned None for non-existent ike_gateways")


def test_delete_ike_gateway_by_id(ike_gw_api, crypto_profile):
    """
    Test deleting an IKE Gateway.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ikegw-del-{random_id}"
    
    payload = IkeGateways(
        name=name,
        folder=TARGET_FOLDER,
        authentication=IkeGatewaysAuthentication(
            pre_shared_key=IkeGatewaysAuthenticationPreSharedKey(key="secret123")
        ),
        peer_address=IkeGatewaysPeerAddress(ip="1.1.1.1"),
        protocol=IkeGatewaysProtocol(
            ikev1=IkeGatewaysProtocolIkev1(
                ike_crypto_profile=crypto_profile.name
            ),
            version="ikev1"
        )
    )
    
    created_obj = ike_gw_api.create_ike_gateways(ike_gateways=payload)
    
    ike_gw_api.delete_ike_gateways_by_id(id=created_obj.id)
    
    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        ike_gw_api.get_ike_gateways_by_id(id=created_obj.id)
        pytest.fail("Gateway should be deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
