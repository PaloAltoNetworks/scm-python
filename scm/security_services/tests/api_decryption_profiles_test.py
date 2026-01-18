import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.decryption_profiles import DecryptionProfiles
from scm.test_helpers import perform

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
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def decryption_profiles_api(client):
    return client.security_services.DecryptionProfilesApi(client.security_services.api_client)


@pytest.fixture
def clean_decryption_profile(decryption_profiles_api):
    """
    Setup/Teardown for a simple Decryption profile.
    """
    profile_name = f"scm-decryption-{uuid.uuid4().hex[:6]}"

    payload = DecryptionProfiles(
        folder=TARGET_FOLDER,
        name=profile_name
    )

    logger.info(f"\n[SETUP] Creating Decryption Profile: {profile_name}")
    created_profile = perform(
        decryption_profiles_api.create_decryption_profiles_with_http_info,
        response_type=DecryptionProfiles,
        decryption_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting Decryption Profile: {created_profile.id}")
    try:
        perform(
            decryption_profiles_api.delete_decryption_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Decryption profile: {e}")


def test_create_decryption_profile(decryption_profiles_api):
    """Test creation of a Decryption Profile."""
    profile_name = f"scm-decryption-create-{uuid.uuid4().hex[:6]}"

    payload = DecryptionProfiles(
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        decryption_profiles_api.create_decryption_profiles_with_http_info,
        response_type=DecryptionProfiles,
        decryption_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name

    perform(
        decryption_profiles_api.delete_decryption_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_decryption_profile_by_id(decryption_profiles_api, clean_decryption_profile):
    """Test retrieving a Decryption Profile by ID."""
    fetched_obj = perform(
        decryption_profiles_api.get_decryption_profiles_by_id_with_http_info,
        id=clean_decryption_profile.id
    )

    assert fetched_obj.id == clean_decryption_profile.id
    assert fetched_obj.name == clean_decryption_profile.name


def test_update_decryption_profile(decryption_profiles_api, clean_decryption_profile):
    """Test updating a Decryption Profile."""
    update_payload = clean_decryption_profile
    update_payload.name = f"{clean_decryption_profile.name}-updated"

    updated_obj = perform(
        decryption_profiles_api.update_decryption_profiles_by_id_with_http_info,
        id=clean_decryption_profile.id,
        decryption_profiles=update_payload
    )

    assert updated_obj.id == clean_decryption_profile.id
    assert updated_obj.name == update_payload.name


def test_list_decryption_profiles(decryption_profiles_api, clean_decryption_profile):
    """Test listing Decryption Profiles."""
    response = perform(
        decryption_profiles_api.list_decryption_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_decryption_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_decryption_profile.name} not found in list response"


def test_delete_decryption_profile_by_id(decryption_profiles_api):
    """Test deleting a Decryption Profile."""
    profile_name = f"scm-decryption-delete-{uuid.uuid4().hex[:6]}"

    payload = DecryptionProfiles(
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        decryption_profiles_api.create_decryption_profiles_with_http_info,
        response_type=DecryptionProfiles,
        decryption_profiles=payload
    )

    perform(
        decryption_profiles_api.delete_decryption_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        decryption_profiles_api.get_decryption_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
