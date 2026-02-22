import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.bgp_filtering_profiles import BgpFilteringProfiles
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "Prisma Access"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def bgp_filtering_profiles_api(client):
    return client.network_services.BGPFilteringProfilesApi(client.network_services.api_client)


@pytest.fixture
def clean_bgp_filtering_profile(bgp_filtering_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-filter-{random_id}"

    payload = BgpFilteringProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
    )

    logger.info(f"\n[SETUP] Creating BGP Filtering Profile: {object_name}")
    created_obj = perform(
        bgp_filtering_profiles_api.create_bgp_filtering_profiles_with_http_info,
        response_type=BgpFilteringProfiles,
        bgp_filtering_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting BGP Filtering Profile ID: {created_obj.id}")
    try:
        bgp_filtering_profiles_api.delete_bgp_filtering_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_bgp_filtering_profile(bgp_filtering_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-filter-create-{random_id}"

    payload = BgpFilteringProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
    )

    created_obj = perform(
        bgp_filtering_profiles_api.create_bgp_filtering_profiles_with_http_info,
        response_type=BgpFilteringProfiles,
        bgp_filtering_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    bgp_filtering_profiles_api.delete_bgp_filtering_profiles_by_id(id=created_obj.id)


def test_get_bgp_filtering_profile_by_id(bgp_filtering_profiles_api, clean_bgp_filtering_profile):
    fetched_obj = bgp_filtering_profiles_api.get_bgp_filtering_profiles_by_id(id=clean_bgp_filtering_profile.id)
    assert fetched_obj.id == clean_bgp_filtering_profile.id
    assert fetched_obj.name == clean_bgp_filtering_profile.name


def test_update_bgp_filtering_profile(bgp_filtering_profiles_api, clean_bgp_filtering_profile):
    update_payload = clean_bgp_filtering_profile
    update_payload.description = "Updated description"

    updated_obj = bgp_filtering_profiles_api.update_bgp_filtering_profiles_by_id(
        id=clean_bgp_filtering_profile.id,
        bgp_filtering_profiles=update_payload,
    )

    assert updated_obj.id == clean_bgp_filtering_profile.id
    assert updated_obj.name == clean_bgp_filtering_profile.name


def test_list_bgp_filtering_profiles(bgp_filtering_profiles_api, clean_bgp_filtering_profile):
    response = bgp_filtering_profiles_api.list_bgp_filtering_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert response.data is not None


def test_fetch_bgp_filtering_profiles(bgp_filtering_profiles_api, clean_bgp_filtering_profile):
    fetched_obj = bgp_filtering_profiles_api.fetch_bgp_filtering_profiles(
        name=clean_bgp_filtering_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_bgp_filtering_profile.id
    assert fetched_obj.name == clean_bgp_filtering_profile.name
    logger.info(f"\n[SUCCESS] fetch_bgp_filtering_profiles found object: {fetched_obj.name}")

    not_found = bgp_filtering_profiles_api.fetch_bgp_filtering_profiles(
        name="non-existent-bgp-filter-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_bgp_filtering_profiles correctly returned None for non-existent object")


def test_delete_bgp_filtering_profile_by_id(bgp_filtering_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-filter-del-{random_id}"

    payload = BgpFilteringProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
    )

    created_obj = perform(
        bgp_filtering_profiles_api.create_bgp_filtering_profiles_with_http_info,
        response_type=BgpFilteringProfiles,
        bgp_filtering_profiles=payload,
    )

    bgp_filtering_profiles_api.delete_bgp_filtering_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        bgp_filtering_profiles_api.get_bgp_filtering_profiles_by_id(id=created_obj.id)
        pytest.fail("BGP Filtering Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
