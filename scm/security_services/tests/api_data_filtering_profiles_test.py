
import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.data_filtering_profiles import DataFilteringProfiles
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "ngfw-shared"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def data_filtering_profiles_api(client):
    return client.security_services.DataFilteringApi(client.security_services.api_client)


@pytest.fixture
def clean_data_filtering_profile(data_filtering_profiles_api):
    """
    Fixture to create a temporary data filtering profile for testing and automatically delete it after.
    """
    object_name = f"test-df-{uuid.uuid4().hex[:6]}"

    payload = DataFilteringProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        data_capture=False
    )

    logger.info(f"\n[SETUP] Creating Data Filtering Profile: {object_name}")
    created_obj = perform(
        data_filtering_profiles_api.create_data_filtering_profiles_with_http_info,
        response_type=DataFilteringProfiles,
        data_filtering_profiles=payload
    )

    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Data Filtering Profile ID: {created_obj.id}")
    try:
        perform(
            data_filtering_profiles_api.delete_data_filtering_profiles_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_data_filtering_profile(data_filtering_profiles_api):
    """
    Test manual creation and deletion of a data filtering profile.
    """
    object_name = f"test-df-create-{uuid.uuid4().hex[:6]}"
    payload = DataFilteringProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test data filtering profile for create API testing",
        data_capture=False
    )

    created_obj = perform(
        data_filtering_profiles_api.create_data_filtering_profiles_with_http_info,
        response_type=DataFilteringProfiles,
        data_filtering_profiles=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER

    perform(
        data_filtering_profiles_api.delete_data_filtering_profiles_by_id,
        id=created_obj.id
    )


def test_get_data_filtering_profile_by_id(data_filtering_profiles_api, clean_data_filtering_profile):
    """
    Test retrieving a data filtering profile by ID.
    """
    fetched_obj = perform(
        data_filtering_profiles_api.get_data_filtering_profiles_by_id,
        response_type=DataFilteringProfiles,
        id=clean_data_filtering_profile.id
    )

    assert fetched_obj.id == clean_data_filtering_profile.id
    assert fetched_obj.name == clean_data_filtering_profile.name
    assert fetched_obj.folder == clean_data_filtering_profile.folder


def test_update_data_filtering_profile(data_filtering_profiles_api, clean_data_filtering_profile):
    """
    Test updating a data filtering profile.
    """
    update_payload = clean_data_filtering_profile
    update_payload.description = "Updated Description via Pytest"

    updated_obj = perform(
        data_filtering_profiles_api.update_data_filtering_profiles_by_id,
        response_type=DataFilteringProfiles,
        id=clean_data_filtering_profile.id,
        data_filtering_profiles=update_payload
    )

    assert updated_obj.description == "Updated Description via Pytest"
    assert updated_obj.id == clean_data_filtering_profile.id


def test_list_data_filtering_profiles(data_filtering_profiles_api, clean_data_filtering_profile):
    """
    Test listing data filtering profiles with folder filter.
    """
    response = perform(
        data_filtering_profiles_api.list_data_filtering_profiles,
        folder=clean_data_filtering_profile.folder
    )

    assert response is not None
    assert len(response.data) > 0
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_fetch_data_filtering_profiles(data_filtering_profiles_api, clean_data_filtering_profile):
    """
    Test fetching a single data filtering profile by name using the fetch convenience method.
    """
    fetched_obj = data_filtering_profiles_api.fetch_data_filtering(
        name=clean_data_filtering_profile.name,
        folder=clean_data_filtering_profile.folder
    )

    assert fetched_obj is not None, f"Should have found data filtering profile '{clean_data_filtering_profile.name}'"
    assert fetched_obj.id == clean_data_filtering_profile.id
    assert fetched_obj.name == clean_data_filtering_profile.name
    assert fetched_obj.folder == clean_data_filtering_profile.folder
    logger.info(f"\n[SUCCESS] fetch_data_filtering found object: {fetched_obj.name}")

    not_found = data_filtering_profiles_api.fetch_data_filtering(
        name="non-existent-data-filtering-profile-xyz-12345",
        folder=clean_data_filtering_profile.folder
    )
    assert not_found is None, "Should return None for non-existent data filtering profile"
    logger.info(f"\n[SUCCESS] fetch_data_filtering correctly returned None for non-existent object")


def test_delete_data_filtering_profile_by_id(data_filtering_profiles_api):
    """
    Test deletion specifically.
    """
    from scm.exceptions import ObjectNotPresentError

    object_name = f"test-df-del-{uuid.uuid4().hex[:6]}"
    payload = DataFilteringProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test data filtering profile for delete API testing",
        data_capture=False
    )

    created_obj = perform(
        data_filtering_profiles_api.create_data_filtering_profiles_with_http_info,
        response_type=DataFilteringProfiles,
        data_filtering_profiles=payload
    )

    perform(
        data_filtering_profiles_api.delete_data_filtering_profiles_by_id,
        id=created_obj.id
    )

    try:
        data_filtering_profiles_api.get_data_filtering_profiles_by_id(id=created_obj.id)
        pytest.fail("Data Filtering Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
