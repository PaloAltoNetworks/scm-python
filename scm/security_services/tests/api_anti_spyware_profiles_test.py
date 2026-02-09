import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.anti_spyware_profiles import AntiSpywareProfiles
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Prisma Access"
# -----------------------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def anti_spyware_profiles_api(client):
    return client.security_services.AntiSpywareProfilesApi(client.security_services.api_client)


@pytest.fixture
def clean_anti_spyware_profile(anti_spyware_profiles_api):
    """
    Setup/Teardown for a simple Anti-Spyware profile.
    """
    profile_name = f"scm-antispyware-{uuid.uuid4().hex[:6]}"

    payload = AntiSpywareProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    logger.info(f"\n[SETUP] Creating Anti-Spyware Profile: {profile_name}")
    created_profile = perform(
        anti_spyware_profiles_api.create_anti_spyware_profiles_with_http_info,
        response_type=AntiSpywareProfiles,
        anti_spyware_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting Anti-Spyware Profile: {created_profile.id}")
    try:
        perform(
            anti_spyware_profiles_api.delete_anti_spyware_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Anti-Spyware profile: {e}")


def test_create_anti_spyware_profile(anti_spyware_profiles_api):
    """Test creation of an Anti-Spyware Profile."""
    profile_name = f"scm-antispyware-create-{uuid.uuid4().hex[:6]}"

    payload = AntiSpywareProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        anti_spyware_profiles_api.create_anti_spyware_profiles_with_http_info,
        response_type=AntiSpywareProfiles,
        anti_spyware_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name

    perform(
        anti_spyware_profiles_api.delete_anti_spyware_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_anti_spyware_profile_by_id(anti_spyware_profiles_api, clean_anti_spyware_profile):
    """Test retrieving an Anti-Spyware Profile by ID."""
    fetched_obj = perform(
        anti_spyware_profiles_api.get_anti_spyware_profiles_by_id_with_http_info,
        id=clean_anti_spyware_profile.id
    )

    assert fetched_obj.id == clean_anti_spyware_profile.id
    assert fetched_obj.name == clean_anti_spyware_profile.name


def test_update_anti_spyware_profile(anti_spyware_profiles_api, clean_anti_spyware_profile):
    """Test updating an Anti-Spyware Profile."""
    # Create fresh payload with all required fields to avoid Pydantic serialization issues
    # Note: Name cannot be changed for anti-spyware profiles (same as decryption profiles)
    update_payload = AntiSpywareProfiles(
        id=clean_anti_spyware_profile.id,
        name=clean_anti_spyware_profile.name,  # Name cannot be changed for anti-spyware profiles
        folder=clean_anti_spyware_profile.folder,
        description="Updated test anti-spyware profile description"
    )

    updated_obj = perform(
        anti_spyware_profiles_api.update_anti_spyware_profiles_by_id_with_http_info,
        id=clean_anti_spyware_profile.id,
        anti_spyware_profiles=update_payload
    )

    assert updated_obj.id == clean_anti_spyware_profile.id
    assert updated_obj.name == clean_anti_spyware_profile.name
    assert updated_obj.description == "Updated test anti-spyware profile description"


def test_list_anti_spyware_profiles(anti_spyware_profiles_api, clean_anti_spyware_profile):
    """Test listing Anti-Spyware Profiles."""
    response = perform(
        anti_spyware_profiles_api.list_anti_spyware_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_anti_spyware_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_anti_spyware_profile.name} not found in list response"




def test_fetch_anti_spyware_profiles(anti_spyware_profiles_api, clean_anti_spyware_profile):
    """
    Test fetching a single anti_spyware_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = anti_spyware_profiles_api.fetch_anti_spyware_profiles(
        name=clean_anti_spyware_profile.name,
        folder=clean_anti_spyware_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found anti_spyware_profiles '{clean_anti_spyware_profile.name}'"
    assert fetched_obj.id == clean_anti_spyware_profile.id
    assert fetched_obj.name == clean_anti_spyware_profile.name
    assert fetched_obj.folder == clean_anti_spyware_profile.folder
    logger.info(f"\n[SUCCESS] fetch_anti_spyware_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent anti_spyware_profiles (should return None)
    not_found = anti_spyware_profiles_api.fetch_anti_spyware_profiles(
        name="non-existent-anti_spyware_profiles-xyz-12345",
        folder=clean_anti_spyware_profile.folder
    )
    assert not_found is None, "Should return None for non-existent anti_spyware_profiles"
    logger.info(f"\n[SUCCESS] fetch_anti_spyware_profiles correctly returned None for non-existent anti_spyware_profiles")


def test_delete_anti_spyware_profile_by_id(anti_spyware_profiles_api):
    """Test deleting an Anti-Spyware Profile."""
    profile_name = f"scm-antispyware-delete-{uuid.uuid4().hex[:6]}"

    payload = AntiSpywareProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        anti_spyware_profiles_api.create_anti_spyware_profiles_with_http_info,
        response_type=AntiSpywareProfiles,
        anti_spyware_profiles=payload
    )

    perform(
        anti_spyware_profiles_api.delete_anti_spyware_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        anti_spyware_profiles_api.get_anti_spyware_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
