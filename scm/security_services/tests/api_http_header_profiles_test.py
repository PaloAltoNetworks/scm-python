import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.http_header_profiles import HttpHeaderProfiles
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
def http_header_profiles_api(client):
    return client.security_services.HttpHeaderProfilesApi(client.security_services.api_client)


@pytest.fixture
def clean_http_header_profile(http_header_profiles_api):
    """
    Setup/Teardown for a simple HTTP Header Profile.
    """
    profile_name = f"scm-http-{uuid.uuid4().hex[:6]}"

    payload = HttpHeaderProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    logger.info(f"\n[SETUP] Creating HTTP Header Profile: {profile_name}")
    created_profile = perform(
        http_header_profiles_api.create_http_header_profiles_with_http_info,
        response_type=HttpHeaderProfiles,
        http_header_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting HTTP Header Profile: {created_profile.id}")
    try:
        perform(
            http_header_profiles_api.delete_http_header_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup HTTP Header Profile: {e}")


def test_create_http_header_profile(http_header_profiles_api):
    """Test creation of an HTTP Header Profile."""
    profile_name = f"scm-http-create-{uuid.uuid4().hex[:6]}"

    payload = HttpHeaderProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        http_header_profiles_api.create_http_header_profiles_with_http_info,
        response_type=HttpHeaderProfiles,
        http_header_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name

    perform(
        http_header_profiles_api.delete_http_header_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_http_header_profile_by_id(http_header_profiles_api, clean_http_header_profile):
    """Test retrieving an HTTP Header Profile by ID."""
    fetched_obj = perform(
        http_header_profiles_api.get_http_header_profiles_by_id_with_http_info,
        id=clean_http_header_profile.id
    )

    assert fetched_obj.id == clean_http_header_profile.id
    assert fetched_obj.name == clean_http_header_profile.name


def test_update_http_header_profile(http_header_profiles_api, clean_http_header_profile):
    """Test updating an HTTP Header Profile."""
    update_payload = clean_http_header_profile
    update_payload.description = "Updated description"

    updated_obj = perform(
        http_header_profiles_api.update_http_header_profiles_by_id_with_http_info,
        id=clean_http_header_profile.id,
        http_header_profiles=update_payload
    )

    assert updated_obj.id == clean_http_header_profile.id
    assert updated_obj.description == "Updated description"


def test_list_http_header_profiles(http_header_profiles_api, clean_http_header_profile):
    """Test listing HTTP Header Profiles."""
    response = perform(
        http_header_profiles_api.list_http_header_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_http_header_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_http_header_profile.name} not found in list response"


def test_delete_http_header_profile_by_id(http_header_profiles_api):
    """Test deleting an HTTP Header Profile."""
    profile_name = f"scm-http-delete-{uuid.uuid4().hex[:6]}"

    payload = HttpHeaderProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        http_header_profiles_api.create_http_header_profiles_with_http_info,
        response_type=HttpHeaderProfiles,
        http_header_profiles=payload
    )

    perform(
        http_header_profiles_api.delete_http_header_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        http_header_profiles_api.get_http_header_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
