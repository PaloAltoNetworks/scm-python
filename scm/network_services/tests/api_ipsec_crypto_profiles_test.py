
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    IpsecCryptoProfiles,
    IpsecCryptoProfilesEsp,
    IpsecCryptoProfilesLifetime
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
def ipsec_api(client):
    return client.network_services.IPsecCryptoProfilesApi(client.network_services.api_client)

@pytest.fixture
def clean_ipsec_profile(ipsec_api):
    """
    Fixture for standard CRUD tests.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ipsec-{random_id}"
    
    payload = IpsecCryptoProfiles(
        name=name,
        folder=TARGET_FOLDER,
        dh_group="group14",
        esp=IpsecCryptoProfilesEsp(
            authentication=["sha256"],
            encryption=["aes-256-gcm"]
        ),
        lifetime=IpsecCryptoProfilesLifetime(hours=8)
    )
    
    logger.info(f"\n[SETUP] Creating IPsec Crypto Profile: {name}")
    created_obj = ipsec_api.create_i_psec_crypto_profiles(ipsec_crypto_profiles=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting IPsec Crypto Profile ID: {created_obj.id}")
    try:
        ipsec_api.delete_i_psec_crypto_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_ipsec_crypto_profile(ipsec_api):
    """
    Test creating an IPsec Crypto Profile.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ipsec-create-{random_id}"
    
    payload = IpsecCryptoProfiles(
        name=name,
        folder=TARGET_FOLDER,
        dh_group="group14",
        esp=IpsecCryptoProfilesEsp(
            authentication=["sha256"],
            encryption=["aes-256-gcm"]
        ),
        lifetime=IpsecCryptoProfilesLifetime(hours=8)
    )

    try:
        created_obj = ipsec_api.create_i_psec_crypto_profiles(ipsec_crypto_profiles=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == name
    assert created_obj.dh_group == "group14"
    assert created_obj.esp.encryption == ["aes-256-gcm"]

    # Cleanup
    ipsec_api.delete_i_psec_crypto_profiles_by_id(id=created_obj.id)


def test_get_ipsec_crypto_profile_by_id(ipsec_api, clean_ipsec_profile):
    """
    Test retrieving an IPsec Crypto Profile by ID.
    """
    fetched_obj = ipsec_api.get_i_psec_crypto_profiles_by_id(id=clean_ipsec_profile.id)
    assert fetched_obj.id == clean_ipsec_profile.id
    assert fetched_obj.name == clean_ipsec_profile.name
    assert fetched_obj.dh_group == "group14"


def test_update_ipsec_crypto_profile(ipsec_api, clean_ipsec_profile):
    """
    Test updating an IPsec Crypto Profile.
    """
    update_payload = clean_ipsec_profile
    update_payload.dh_group = "group5"
    update_payload.esp.authentication = ["sha384"]
    
    updated_obj = ipsec_api.update_i_psec_crypto_profiles_by_id(
        id=clean_ipsec_profile.id,
        ipsec_crypto_profiles=update_payload
    )
    
    assert updated_obj.id == clean_ipsec_profile.id
    assert updated_obj.dh_group == "group5"
    assert updated_obj.esp.authentication == ["sha384"]


def test_list_ipsec_crypto_profiles(ipsec_api, clean_ipsec_profile):
    """
    Test listing IPsec Crypto Profiles.
    """
    response = ipsec_api.list_i_psec_crypto_profiles(folder=TARGET_FOLDER)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_ipsec_profile.id:
            found = True
            break
    assert found is True



def test_delete_ipsec_crypto_profile_by_id(ipsec_api):
    """
    Test deleting an IPsec Crypto Profile.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ipsec-del-{random_id}"
    
    payload = IpsecCryptoProfiles(
        name=name,
        folder=TARGET_FOLDER,
        dh_group="group14",
        esp=IpsecCryptoProfilesEsp(
            authentication=["sha256"],
            encryption=["aes-256-cbc"]
        ),
        lifetime=IpsecCryptoProfilesLifetime(hours=1)
    )
    
    created_obj = ipsec_api.create_i_psec_crypto_profiles(ipsec_crypto_profiles=payload)
    
    ipsec_api.delete_i_psec_crypto_profiles_by_id(id=created_obj.id)
    
    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        ipsec_api.get_i_psec_crypto_profiles_by_id(id=created_obj.id)
        pytest.fail("Profile should be deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
