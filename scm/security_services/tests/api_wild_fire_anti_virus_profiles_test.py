import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.wildfire_anti_virus_profiles import WildfireAntiVirusProfiles
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
def wild_fire_anti_virus_profiles_api(client):
    return client.security_services.WildFireAntiVirusProfilesApi(client.security_services.api_client)


@pytest.fixture
def clean_wild_fire_anti_virus_profile(wild_fire_anti_virus_profiles_api):
    """
    Setup/Teardown for a simple WildFire Anti-Virus Profile.
    """
    profile_name = f"scm-wfav-{uuid.uuid4().hex[:6]}"

    payload = WildfireAntiVirusProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name,
        description="Test WildFire anti-virus profile"
    )

    logger.info(f"\n[SETUP] Creating WildFire Anti-Virus Profile: {profile_name}")
    created_profile = perform(
        wild_fire_anti_virus_profiles_api.create_wild_fire_anti_virus_profiles_with_http_info,
        response_type=WildfireAntiVirusProfiles,
        wildfire_anti_virus_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting WildFire Anti-Virus Profile: {created_profile.id}")
    try:
        perform(
            wild_fire_anti_virus_profiles_api.delete_wild_fire_anti_virus_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup WildFire Anti-Virus Profile: {e}")


def test_create_wild_fire_anti_virus_profile(wild_fire_anti_virus_profiles_api):
    """Test creation of a WildFire Anti-Virus Profile."""
    profile_name = f"scm-wfav-create-{uuid.uuid4().hex[:6]}"

    payload = WildfireAntiVirusProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name,
        description="Test WildFire anti-virus profile for create API testing"
    )

    created_obj = perform(
        wild_fire_anti_virus_profiles_api.create_wild_fire_anti_virus_profiles_with_http_info,
        response_type=WildfireAntiVirusProfiles,
        wildfire_anti_virus_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert created_obj.description == "Test WildFire anti-virus profile for create API testing"

    perform(
        wild_fire_anti_virus_profiles_api.delete_wild_fire_anti_virus_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_wild_fire_anti_virus_profile_by_id(wild_fire_anti_virus_profiles_api, clean_wild_fire_anti_virus_profile):
    """Test retrieving a WildFire Anti-Virus Profile by ID."""
    fetched_obj = perform(
        wild_fire_anti_virus_profiles_api.get_wild_fire_anti_virus_profiles_by_id_with_http_info,
        id=clean_wild_fire_anti_virus_profile.id
    )

    assert fetched_obj.id == clean_wild_fire_anti_virus_profile.id
    assert fetched_obj.name == clean_wild_fire_anti_virus_profile.name


def test_update_wild_fire_anti_virus_profile(wild_fire_anti_virus_profiles_api, clean_wild_fire_anti_virus_profile):
    """Test updating a WildFire Anti-Virus Profile."""
    update_payload = clean_wild_fire_anti_virus_profile
    update_payload.description = "Updated test WildFire anti-virus profile description"

    updated_obj = perform(
        wild_fire_anti_virus_profiles_api.update_wild_fire_anti_virus_profiles_by_id_with_http_info,
        id=clean_wild_fire_anti_virus_profile.id,
        wildfire_anti_virus_profiles=update_payload
    )

    assert updated_obj.id == clean_wild_fire_anti_virus_profile.id
    assert updated_obj.description == "Updated test WildFire anti-virus profile description"


def test_list_wild_fire_anti_virus_profiles(wild_fire_anti_virus_profiles_api, clean_wild_fire_anti_virus_profile):
    """Test listing WildFire Anti-Virus Profiles."""
    response = perform(
        wild_fire_anti_virus_profiles_api.list_wild_fire_anti_virus_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_wild_fire_anti_virus_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_wild_fire_anti_virus_profile.name} not found in list response"


def test_fetch_wild_fire_anti_virus_profiles(wild_fire_anti_virus_profiles_api, clean_wild_fire_anti_virus_profile):
    """
    Test fetching a single WildFire Anti-Virus Profile by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = wild_fire_anti_virus_profiles_api.fetch_wild_fire_anti_virus_profiles(
        name=clean_wild_fire_anti_virus_profile.name,
        folder=clean_wild_fire_anti_virus_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found WildFire Anti-Virus Profile '{clean_wild_fire_anti_virus_profile.name}'"
    assert fetched_obj.id == clean_wild_fire_anti_virus_profile.id
    assert fetched_obj.name == clean_wild_fire_anti_virus_profile.name
    assert fetched_obj.folder == clean_wild_fire_anti_virus_profile.folder
    logger.info(f"\n[SUCCESS] fetch_wild_fire_anti_virus_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent profile (should return None)
    not_found = wild_fire_anti_virus_profiles_api.fetch_wild_fire_anti_virus_profiles(
        name="non-existent-wfav-profile-xyz-12345",
        folder=clean_wild_fire_anti_virus_profile.folder
    )
    assert not_found is None, "Should return None for non-existent WildFire Anti-Virus Profile"
    logger.info(f"\n[SUCCESS] fetch_wild_fire_anti_virus_profiles correctly returned None for non-existent profile")


def test_delete_wild_fire_anti_virus_profile_by_id(wild_fire_anti_virus_profiles_api):
    """Test deleting a WildFire Anti-Virus Profile."""
    profile_name = f"scm-wfav-delete-{uuid.uuid4().hex[:6]}"

    payload = WildfireAntiVirusProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name,
        description="Test WildFire anti-virus profile for delete API testing"
    )

    created_obj = perform(
        wild_fire_anti_virus_profiles_api.create_wild_fire_anti_virus_profiles_with_http_info,
        response_type=WildfireAntiVirusProfiles,
        wildfire_anti_virus_profiles=payload
    )

    perform(
        wild_fire_anti_virus_profiles_api.delete_wild_fire_anti_virus_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        wild_fire_anti_virus_profiles_api.get_wild_fire_anti_virus_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
