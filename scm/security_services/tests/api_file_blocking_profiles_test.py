import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.file_blocking_profiles import FileBlockingProfiles
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
def file_blocking_profiles_api(client):
    return client.security_services.FileBlockingProfilesApi(client.security_services.api_client)


@pytest.fixture
def clean_file_blocking_profile(file_blocking_profiles_api):
    """
    Setup/Teardown for a simple File Blocking Profile.
    """
    profile_name = f"scm-fb-{uuid.uuid4().hex[:6]}"

    payload = FileBlockingProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    logger.info(f"\n[SETUP] Creating File Blocking Profile: {profile_name}")
    created_profile = perform(
        file_blocking_profiles_api.create_file_blocking_profiles_with_http_info,
        response_type=FileBlockingProfiles,
        file_blocking_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting File Blocking Profile: {created_profile.id}")
    try:
        perform(
            file_blocking_profiles_api.delete_file_blocking_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup File Blocking Profile: {e}")


def test_create_file_blocking_profile(file_blocking_profiles_api):
    """Test creation of a File Blocking Profile."""
    profile_name = f"scm-fb-create-{uuid.uuid4().hex[:6]}"

    payload = FileBlockingProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        file_blocking_profiles_api.create_file_blocking_profiles_with_http_info,
        response_type=FileBlockingProfiles,
        file_blocking_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name

    perform(
        file_blocking_profiles_api.delete_file_blocking_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_file_blocking_profile_by_id(file_blocking_profiles_api, clean_file_blocking_profile):
    """Test retrieving a File Blocking Profile by ID."""
    fetched_obj = perform(
        file_blocking_profiles_api.get_file_blocking_profiles_by_id_with_http_info,
        id=clean_file_blocking_profile.id
    )

    assert fetched_obj.id == clean_file_blocking_profile.id
    assert fetched_obj.name == clean_file_blocking_profile.name


def test_update_file_blocking_profile(file_blocking_profiles_api, clean_file_blocking_profile):
    """Test updating a File Blocking Profile."""
    update_payload = clean_file_blocking_profile
    update_payload.description = "Updated description"

    updated_obj = perform(
        file_blocking_profiles_api.update_file_blocking_profiles_by_id_with_http_info,
        id=clean_file_blocking_profile.id,
        file_blocking_profiles=update_payload
    )

    assert updated_obj.id == clean_file_blocking_profile.id
    assert updated_obj.description == "Updated description"


def test_list_file_blocking_profiles(file_blocking_profiles_api, clean_file_blocking_profile):
    """Test listing File Blocking Profiles."""
    response = perform(
        file_blocking_profiles_api.list_file_blocking_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_file_blocking_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_file_blocking_profile.name} not found in list response"




def test_fetch_file_blocking_profiles(file_blocking_profiles_api, clean_file_blocking_profile):
    """
    Test fetching a single file_blocking_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = file_blocking_profiles_api.fetch_file_blocking_profiles(
        name=clean_file_blocking_profile.name,
        folder=clean_file_blocking_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found file_blocking_profiles '{clean_file_blocking_profile.name}'"
    assert fetched_obj.id == clean_file_blocking_profile.id
    assert fetched_obj.name == clean_file_blocking_profile.name
    assert fetched_obj.folder == clean_file_blocking_profile.folder
    logger.info(f"\n[SUCCESS] fetch_file_blocking_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent file_blocking_profiles (should return None)
    not_found = file_blocking_profiles_api.fetch_file_blocking_profiles(
        name="non-existent-file_blocking_profiles-xyz-12345",
        folder=clean_file_blocking_profile.folder
    )
    assert not_found is None, "Should return None for non-existent file_blocking_profiles"
    logger.info(f"\n[SUCCESS] fetch_file_blocking_profiles correctly returned None for non-existent file_blocking_profiles")


def test_delete_file_blocking_profile_by_id(file_blocking_profiles_api):
    """Test deleting a File Blocking Profile."""
    profile_name = f"scm-fb-delete-{uuid.uuid4().hex[:6]}"

    payload = FileBlockingProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        file_blocking_profiles_api.create_file_blocking_profiles_with_http_info,
        response_type=FileBlockingProfiles,
        file_blocking_profiles=payload
    )

    perform(
        file_blocking_profiles_api.delete_file_blocking_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        file_blocking_profiles_api.get_file_blocking_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
