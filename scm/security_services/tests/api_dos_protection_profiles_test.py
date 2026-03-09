import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.dos_protection_profiles import DosProtectionProfiles
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
def dos_protection_profiles_api(client):
    return client.security_services.DoSProtectionProfilesApi(client.security_services.api_client)


@pytest.fixture
def clean_dos_protection_profile(dos_protection_profiles_api):
    """
    Setup/Teardown for a simple DoS Protection Profile.
    """
    profile_name = f"scm-dos-{uuid.uuid4().hex[:6]}"

    payload = DosProtectionProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name,
        description="Test DoS protection profile",
        type="aggregate"
    )

    logger.info(f"\n[SETUP] Creating DoS Protection Profile: {profile_name}")
    created_profile = perform(
        dos_protection_profiles_api.create_do_s_protection_profiles_with_http_info,
        response_type=DosProtectionProfiles,
        dos_protection_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting DoS Protection Profile: {created_profile.id}")
    try:
        perform(
            dos_protection_profiles_api.delete_do_s_protection_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup DoS Protection Profile: {e}")


def test_create_dos_protection_profile(dos_protection_profiles_api):
    """Test creation of a DoS Protection Profile."""
    profile_name = f"scm-dos-create-{uuid.uuid4().hex[:6]}"

    payload = DosProtectionProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name,
        description="Test DoS protection profile for create API testing",
        type="aggregate"
    )

    created_obj = perform(
        dos_protection_profiles_api.create_do_s_protection_profiles_with_http_info,
        response_type=DosProtectionProfiles,
        dos_protection_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert created_obj.description == "Test DoS protection profile for create API testing"
    assert created_obj.type == "aggregate"

    perform(
        dos_protection_profiles_api.delete_do_s_protection_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_dos_protection_profile_by_id(dos_protection_profiles_api, clean_dos_protection_profile):
    """Test retrieving a DoS Protection Profile by ID."""
    fetched_obj = perform(
        dos_protection_profiles_api.get_do_s_protection_profiles_by_id_with_http_info,
        id=clean_dos_protection_profile.id
    )

    assert fetched_obj.id == clean_dos_protection_profile.id
    assert fetched_obj.name == clean_dos_protection_profile.name
    assert fetched_obj.type == "aggregate"


def test_update_dos_protection_profile(dos_protection_profiles_api, clean_dos_protection_profile):
    """Test updating a DoS Protection Profile."""
    update_payload = clean_dos_protection_profile
    update_payload.description = "Updated test DoS protection profile description"

    updated_obj = perform(
        dos_protection_profiles_api.update_do_s_protection_profiles_by_id_with_http_info,
        id=clean_dos_protection_profile.id,
        dos_protection_profiles=update_payload
    )

    assert updated_obj.id == clean_dos_protection_profile.id
    assert updated_obj.description == "Updated test DoS protection profile description"
    assert updated_obj.type == "aggregate"


def test_list_dos_protection_profiles(dos_protection_profiles_api, clean_dos_protection_profile):
    """Test listing DoS Protection Profiles."""
    response = perform(
        dos_protection_profiles_api.list_do_s_protection_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_dos_protection_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_dos_protection_profile.name} not found in list response"


def test_fetch_dos_protection_profiles(dos_protection_profiles_api, clean_dos_protection_profile):
    """
    Test fetching a single DoS Protection Profile by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = dos_protection_profiles_api.fetch_dos_protection_profiles(
        name=clean_dos_protection_profile.name,
        folder=clean_dos_protection_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found DoS Protection Profile '{clean_dos_protection_profile.name}'"
    assert fetched_obj.id == clean_dos_protection_profile.id
    assert fetched_obj.name == clean_dos_protection_profile.name
    assert fetched_obj.folder == clean_dos_protection_profile.folder
    logger.info(f"\n[SUCCESS] fetch_dos_protection_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent profile (should return None)
    not_found = dos_protection_profiles_api.fetch_dos_protection_profiles(
        name="non-existent-dos-profile-xyz-12345",
        folder=clean_dos_protection_profile.folder
    )
    assert not_found is None, "Should return None for non-existent DoS Protection Profile"
    logger.info(f"\n[SUCCESS] fetch_dos_protection_profiles correctly returned None for non-existent profile")


def test_delete_dos_protection_profile_by_id(dos_protection_profiles_api):
    """Test deleting a DoS Protection Profile."""
    profile_name = f"scm-dos-delete-{uuid.uuid4().hex[:6]}"

    payload = DosProtectionProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name,
        description="Test DoS protection profile for delete API testing",
        type="aggregate"
    )

    created_obj = perform(
        dos_protection_profiles_api.create_do_s_protection_profiles_with_http_info,
        response_type=DosProtectionProfiles,
        dos_protection_profiles=payload
    )

    perform(
        dos_protection_profiles_api.delete_do_s_protection_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        dos_protection_profiles_api.get_do_s_protection_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
