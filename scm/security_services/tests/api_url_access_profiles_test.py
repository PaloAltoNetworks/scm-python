import logging
import uuid
import json
import pytest
from scm import Scm
from scm.security_services.models.url_access_profiles import UrlAccessProfiles
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
    """
    Fixture to initialize the SCM client once for the module.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def url_access_profiles_api(client):
    """
    Fixture to return the URL Access Profiles API instance.
    """
    return client.security_services.UrlAccessProfilesApi(client.security_services.api_client)

@pytest.fixture
def clean_url_access_profile(url_access_profiles_api):
    """
    Fixture to create a temporary URL Access Profile for testing and automatically delete it after.
    """
    profile_name = f"test-url-prof-{uuid.uuid4().hex[:6]}"

    payload = UrlAccessProfiles(
        name=profile_name,
        folder=TARGET_FOLDER
    )

    logger.info(f"\n[SETUP] Creating URL Access Profile: {profile_name}")
    created_obj = perform(
        url_access_profiles_api.create_url_access_profiles_with_http_info,
        response_type=UrlAccessProfiles,
        url_access_profiles=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting URL Access Profile ID: {created_obj.id}")
    try:
        perform(
            url_access_profiles_api.delete_url_access_profiles_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_url_access_profile(url_access_profiles_api):
    """
    Test manual creation and deletion of a URL Access Profile with logging.
    """
    profile_name = f"test-url-create-{uuid.uuid4().hex[:6]}"

    payload = UrlAccessProfiles(
        name=profile_name,
        folder=TARGET_FOLDER
    )

    # Create with logging
    created_obj = perform(
        url_access_profiles_api.create_url_access_profiles_with_http_info,
        response_type=UrlAccessProfiles,
        url_access_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert created_obj.folder == TARGET_FOLDER

    # Cleanup with logging
    perform(
        url_access_profiles_api.delete_url_access_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_url_access_profile_by_id(url_access_profiles_api, clean_url_access_profile):
    """
    Test retrieving a URL Access Profile by ID with logging.
    """
    fetched_obj = perform(
        url_access_profiles_api.get_url_access_profiles_by_id_with_http_info,
        id=clean_url_access_profile.id
    )

    assert fetched_obj.id == clean_url_access_profile.id
    assert fetched_obj.name == clean_url_access_profile.name


def test_update_url_access_profile(url_access_profiles_api, clean_url_access_profile):
    """
    Test updating a URL Access Profile with logging.
    """
    update_payload = clean_url_access_profile
    update_payload.description = "Updated description via Pytest"

    updated_obj = perform(
        url_access_profiles_api.update_url_access_profiles_by_id_with_http_info,
        id=clean_url_access_profile.id,
        url_access_profiles=update_payload
    )

    assert updated_obj.id == clean_url_access_profile.id
    assert updated_obj.description == "Updated description via Pytest"


def test_list_url_access_profiles(url_access_profiles_api, clean_url_access_profile):
    """
    Test listing URL Access Profiles with logging.
    """
    response = perform(
        url_access_profiles_api.list_url_access_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify the fixture object is in the list
    found = False
    for item in response.data:
        if item.id == clean_url_access_profile.id:
            found = True
            break
    assert found is True, f"Created profile {clean_url_access_profile.id} not found in list response"


def test_delete_url_access_profile_by_id(url_access_profiles_api):
    """
    Test deletion specifically with logging.
    """
    # Setup
    profile_name = f"test-url-del-{uuid.uuid4().hex[:6]}"

    payload = UrlAccessProfiles(
        name=profile_name,
        folder=TARGET_FOLDER
    )

    created_obj = perform(
        url_access_profiles_api.create_url_access_profiles_with_http_info,
        response_type=UrlAccessProfiles,
        url_access_profiles=payload
    )

    # Perform Delete with logging
    perform(
        url_access_profiles_api.delete_url_access_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    # Verify Deletion
    try:
        url_access_profiles_api.get_url_access_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
