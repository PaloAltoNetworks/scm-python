
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    IkeCryptoProfiles,
    IkeCryptoProfilesLifetime
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "Shared"

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def ike_api(client):
    return client.network_services.IKECryptoProfilesApi(client.network_services.api_client)

@pytest.fixture
def clean_ike_profile(ike_api):
    """
    Fixture for standard CRUD tests.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ike-{random_id}"
    
    payload = IkeCryptoProfiles(
		id="",
        name=name,
        folder=TARGET_FOLDER,
        hash=["sha256"],
        dh_group=["group14"],
        encryption=["aes-256-cbc"],
        lifetime=IkeCryptoProfilesLifetime(hours=8)
    )
    
    logger.info(f"\n[SETUP] Creating IKE Crypto Profile: {name}")
    created_obj = ike_api.create_ike_crypto_profiles(ike_crypto_profiles=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting IKE Crypto Profile ID: {created_obj.id}")
    try:
        ike_api.delete_ike_crypto_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_ike_crypto_profile(ike_api):
    """
    Test creating an IKE Crypto Profile.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ike-create-{random_id}"
    
    payload = IkeCryptoProfiles(
		id="",
        name=name,
        folder=TARGET_FOLDER,
        hash=["sha256", "sha384"],
        dh_group=["group14"],
        encryption=["aes-256-cbc"],
        lifetime=IkeCryptoProfilesLifetime(hours=8)
    )

    try:
        created_obj = ike_api.create_ike_crypto_profiles(ike_crypto_profiles=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == name
    assert "sha384" in created_obj.hash

    # Cleanup
    ike_api.delete_ike_crypto_profiles_by_id(id=created_obj.id)


def test_get_ike_crypto_profile_by_id(ike_api, clean_ike_profile):
    """
    Test retrieving an IKE Crypto Profile by ID.
    """
    fetched_obj = ike_api.get_ike_crypto_profiles_by_id(id=clean_ike_profile.id)
    assert fetched_obj.id == clean_ike_profile.id
    assert fetched_obj.name == clean_ike_profile.name
    assert fetched_obj.encryption == ["aes-256-cbc"]


def test_update_ike_crypto_profile(ike_api, clean_ike_profile):
    """
    Test updating an IKE Crypto Profile.
    """
    update_payload = clean_ike_profile
    update_payload.hash = ["sha512"]
    update_payload.encryption = ["aes-256-gcm"]
    update_payload.lifetime = IkeCryptoProfilesLifetime(hours=24)
    
    updated_obj = ike_api.update_ike_crypto_profiles_by_id(
        id=clean_ike_profile.id,
        ike_crypto_profiles=update_payload
    )
    
    assert updated_obj.id == clean_ike_profile.id
    assert updated_obj.hash == ["sha512"]
    assert updated_obj.encryption == ["aes-256-gcm"]
    assert updated_obj.lifetime.hours == 24


def test_list_ike_crypto_profiles(ike_api, clean_ike_profile):
    """
    Test listing IKE Crypto Profiles.
    """
    response = ike_api.list_ike_crypto_profiles(folder=TARGET_FOLDER)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_ike_profile.id:
            found = True
            break
    assert found is True


def test_delete_ike_crypto_profile_by_id(ike_api):
    """
    Test deleting an IKE Crypto Profile.
    """
    random_id = uuid.uuid4().hex[:6]
    name = f"test-ike-del-{random_id}"
    
    payload = IkeCryptoProfiles(
		id="",
        name=name,
        folder=TARGET_FOLDER,
        hash=["sha1"],
        dh_group=["group5"],
        encryption=["3des"],
        lifetime=IkeCryptoProfilesLifetime(hours=1)
    )
    
    created_obj = ike_api.create_ike_crypto_profiles(ike_crypto_profiles=payload)
    
    ike_api.delete_ike_crypto_profiles_by_id(id=created_obj.id)
    
    try:
        ike_api.get_ike_crypto_profiles_by_id(id=created_obj.id)
        pytest.fail("Profile should be deleted")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
