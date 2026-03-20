import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.decryption_profiles import DecryptionProfiles
from scm.security_services.models.decryption_profiles_ssl_inbound_proxy import DecryptionProfilesSslInboundProxy
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Shared"
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
        id="",
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
        id="",
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
    # Create fresh payload - name must stay the same, ssl_inbound_proxy required for updates
    update_payload = DecryptionProfiles(
        id=clean_decryption_profile.id,
        name=clean_decryption_profile.name,  # Name cannot be changed for decryption profiles
        folder=TARGET_FOLDER,
        ssl_inbound_proxy=DecryptionProfilesSslInboundProxy()  # Required for updates
    )

    updated_obj = perform(
        decryption_profiles_api.update_decryption_profiles_by_id_with_http_info,
        id=clean_decryption_profile.id,
        decryption_profiles=update_payload
    )

    assert updated_obj.id == clean_decryption_profile.id
    assert updated_obj.name == clean_decryption_profile.name


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




def test_fetch_decryption_profiles(decryption_profiles_api, clean_decryption_profile):
    """
    Test fetching a single decryption_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = decryption_profiles_api.fetch_decryption_profiles(
        name=clean_decryption_profile.name,
        folder=clean_decryption_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found decryption_profiles '{clean_decryption_profile.name}'"
    assert fetched_obj.id == clean_decryption_profile.id
    assert fetched_obj.name == clean_decryption_profile.name
    assert fetched_obj.folder == clean_decryption_profile.folder
    logger.info(f"\n[SUCCESS] fetch_decryption_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent decryption_profiles (should return None)
    not_found = decryption_profiles_api.fetch_decryption_profiles(
        name="non-existent-decryption_profiles-xyz-12345",
        folder=clean_decryption_profile.folder
    )
    assert not_found is None, "Should return None for non-existent decryption_profiles"
    logger.info(f"\n[SUCCESS] fetch_decryption_profiles correctly returned None for non-existent decryption_profiles")


def test_delete_decryption_profile_by_id(decryption_profiles_api):
    """Test deleting a Decryption Profile."""
    profile_name = f"scm-decryption-delete-{uuid.uuid4().hex[:6]}"

    payload = DecryptionProfiles(
        id="",
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

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        decryption_profiles_api.get_decryption_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
