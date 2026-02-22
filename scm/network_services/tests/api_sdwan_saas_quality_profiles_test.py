import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.sdwan_saas_quality_profiles import SdwanSaasQualityProfiles
from scm.network_services.models.sdwan_saas_quality_profiles_monitor_mode import SdwanSaasQualityProfilesMonitorMode
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "All"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def sdwan_saas_quality_profiles_api(client):
    return client.network_services.SDWANSaaSQualityProfilesApi(client.network_services.api_client)


def _make_sdwan_sqp_payload(name):
    monitor_mode = SdwanSaasQualityProfilesMonitorMode(
        adaptive={},
    )
    return SdwanSaasQualityProfiles(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        monitor_mode=monitor_mode,
    )


@pytest.fixture
def clean_sdwan_saas_quality_profile(sdwan_saas_quality_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-sqp-{random_id}"

    payload = _make_sdwan_sqp_payload(object_name)

    logger.info(f"\n[SETUP] Creating SDWAN SaaS Quality Profile: {object_name}")
    created_obj = perform(
        sdwan_saas_quality_profiles_api.create_sdwan_saa_s_quality_profiles_with_http_info,
        response_type=SdwanSaasQualityProfiles,
        sdwan_saas_quality_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting SDWAN SaaS Quality Profile ID: {created_obj.id}")
    try:
        sdwan_saas_quality_profiles_api.delete_sdwan_saa_s_quality_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_sdwan_saas_quality_profile(sdwan_saas_quality_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-sqp-create-{random_id}"

    payload = _make_sdwan_sqp_payload(object_name)

    created_obj = perform(
        sdwan_saas_quality_profiles_api.create_sdwan_saa_s_quality_profiles_with_http_info,
        response_type=SdwanSaasQualityProfiles,
        sdwan_saas_quality_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    sdwan_saas_quality_profiles_api.delete_sdwan_saa_s_quality_profiles_by_id(id=created_obj.id)


def test_get_sdwan_saas_quality_profile_by_id(sdwan_saas_quality_profiles_api, clean_sdwan_saas_quality_profile):
    fetched_obj = sdwan_saas_quality_profiles_api.get_sdwan_saa_s_quality_profiles_by_id(id=clean_sdwan_saas_quality_profile.id)
    assert fetched_obj.id == clean_sdwan_saas_quality_profile.id
    assert fetched_obj.name == clean_sdwan_saas_quality_profile.name


def test_update_sdwan_saas_quality_profile(sdwan_saas_quality_profiles_api, clean_sdwan_saas_quality_profile):
    update_payload = _make_sdwan_sqp_payload(clean_sdwan_saas_quality_profile.name)

    updated_obj = sdwan_saas_quality_profiles_api.update_sdwan_saa_s_quality_profiles_by_id(
        id=clean_sdwan_saas_quality_profile.id,
        sdwan_saas_quality_profiles=update_payload,
    )

    assert updated_obj.id == clean_sdwan_saas_quality_profile.id
    assert updated_obj.name == clean_sdwan_saas_quality_profile.name


def test_list_sdwan_saas_quality_profiles(sdwan_saas_quality_profiles_api, clean_sdwan_saas_quality_profile):
    response = sdwan_saas_quality_profiles_api.list_sdwan_saa_s_quality_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None

    found = False
    if response.data:
        for item in response.data:
            if item.name == clean_sdwan_saas_quality_profile.name:
                found = True
                break
    assert found is True


def test_fetch_sdwan_saas_quality_profiles(sdwan_saas_quality_profiles_api, clean_sdwan_saas_quality_profile):
    fetched_obj = sdwan_saas_quality_profiles_api.fetch_sdwan_saa_s_quality_profiles(
        name=clean_sdwan_saas_quality_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.name == clean_sdwan_saas_quality_profile.name
    logger.info(f"\n[SUCCESS] fetch_sdwan_saas_quality_profiles found object: {fetched_obj.name}")

    not_found = sdwan_saas_quality_profiles_api.fetch_sdwan_saa_s_quality_profiles(
        name="non-existent-sdwan-sqp-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_sdwan_saas_quality_profiles correctly returned None for non-existent object")


def test_delete_sdwan_saas_quality_profile_by_id(sdwan_saas_quality_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-sqp-del-{random_id}"

    payload = _make_sdwan_sqp_payload(object_name)

    created_obj = perform(
        sdwan_saas_quality_profiles_api.create_sdwan_saa_s_quality_profiles_with_http_info,
        response_type=SdwanSaasQualityProfiles,
        sdwan_saas_quality_profiles=payload,
    )

    sdwan_saas_quality_profiles_api.delete_sdwan_saa_s_quality_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        sdwan_saas_quality_profiles_api.get_sdwan_saa_s_quality_profiles_by_id(id=created_obj.id)
        pytest.fail("SDWAN SaaS Quality Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
