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
TARGET_FOLDER = "All"
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
    update_payload = clean_anti_spyware_profile
    update_payload.name = f"{clean_anti_spyware_profile.name}-updated"

    updated_obj = perform(
        anti_spyware_profiles_api.update_anti_spyware_profiles_by_id_with_http_info,
        id=clean_anti_spyware_profile.id,
        anti_spyware_profiles=update_payload
    )

    assert updated_obj.id == clean_anti_spyware_profile.id
    assert updated_obj.name == update_payload.name


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


def test_delete_anti_spyware_profile_by_id(anti_spyware_profiles_api):
    """Test deleting an Anti-Spyware Profile."""
    profile_name = f"scm-antispyware-delete-{uuid.uuid4().hex[:6]}"

    payload = AntiSpywareProfiles(
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

    try:
        anti_spyware_profiles_api.get_anti_spyware_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
