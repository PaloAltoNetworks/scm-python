import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.sdwan_path_quality_profiles import SdwanPathQualityProfiles
from scm.network_services.models.sdwan_path_quality_profiles_metric import SdwanPathQualityProfilesMetric
from scm.network_services.models.sdwan_path_quality_profiles_metric_jitter import SdwanPathQualityProfilesMetricJitter
from scm.network_services.models.sdwan_path_quality_profiles_metric_latency import SdwanPathQualityProfilesMetricLatency
from scm.network_services.models.sdwan_path_quality_profiles_metric_pkt_loss import SdwanPathQualityProfilesMetricPktLoss
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
def sdwan_path_quality_profiles_api(client):
    return client.network_services.SDWANPathQualityProfilesApi(client.network_services.api_client)


def _make_sdwan_pqp_payload(name, jitter_threshold=100, latency_threshold=100, pkt_loss_threshold=1, sensitivity="medium"):
    metric = SdwanPathQualityProfilesMetric(
        jitter=SdwanPathQualityProfilesMetricJitter(
            sensitivity=sensitivity,
            threshold=jitter_threshold,
        ),
        latency=SdwanPathQualityProfilesMetricLatency(
            sensitivity=sensitivity,
            threshold=latency_threshold,
        ),
        pkt_loss=SdwanPathQualityProfilesMetricPktLoss(
            sensitivity=sensitivity,
            threshold=pkt_loss_threshold,
        ),
    )
    return SdwanPathQualityProfiles(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        metric=metric,
    )


@pytest.fixture
def clean_sdwan_path_quality_profile(sdwan_path_quality_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-pqp-{random_id}"

    payload = _make_sdwan_pqp_payload(object_name)

    logger.info(f"\n[SETUP] Creating SDWAN Path Quality Profile: {object_name}")
    created_obj = perform(
        sdwan_path_quality_profiles_api.create_sdwan_path_quality_profiles_with_http_info,
        response_type=SdwanPathQualityProfiles,
        sdwan_path_quality_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting SDWAN Path Quality Profile ID: {created_obj.id}")
    try:
        sdwan_path_quality_profiles_api.delete_sdwan_path_quality_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_sdwan_path_quality_profile(sdwan_path_quality_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-pqp-create-{random_id}"

    payload = _make_sdwan_pqp_payload(object_name)

    created_obj = perform(
        sdwan_path_quality_profiles_api.create_sdwan_path_quality_profiles_with_http_info,
        response_type=SdwanPathQualityProfiles,
        sdwan_path_quality_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    sdwan_path_quality_profiles_api.delete_sdwan_path_quality_profiles_by_id(id=created_obj.id)


def test_get_sdwan_path_quality_profile_by_id(sdwan_path_quality_profiles_api, clean_sdwan_path_quality_profile):
    fetched_obj = sdwan_path_quality_profiles_api.get_sdwan_path_quality_profiles_by_id(id=clean_sdwan_path_quality_profile.id)
    assert fetched_obj.id == clean_sdwan_path_quality_profile.id
    assert fetched_obj.name == clean_sdwan_path_quality_profile.name


def test_update_sdwan_path_quality_profile(sdwan_path_quality_profiles_api, clean_sdwan_path_quality_profile):
    update_payload = _make_sdwan_pqp_payload(
        clean_sdwan_path_quality_profile.name,
        jitter_threshold=150,
        latency_threshold=150,
        pkt_loss_threshold=2,
        sensitivity="high",
    )

    updated_obj = sdwan_path_quality_profiles_api.update_sdwan_path_quality_profiles_by_id(
        id=clean_sdwan_path_quality_profile.id,
        sdwan_path_quality_profiles=update_payload,
    )

    assert updated_obj.id == clean_sdwan_path_quality_profile.id
    assert updated_obj.metric.jitter.threshold == 150
    assert updated_obj.metric.latency.threshold == 150


def test_list_sdwan_path_quality_profiles(sdwan_path_quality_profiles_api, clean_sdwan_path_quality_profile):
    response = sdwan_path_quality_profiles_api.list_sdwan_path_quality_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None

    found = False
    if response.data:
        for item in response.data:
            if item.name == clean_sdwan_path_quality_profile.name:
                found = True
                break
    assert found is True


def test_fetch_sdwan_path_quality_profiles(sdwan_path_quality_profiles_api, clean_sdwan_path_quality_profile):
    fetched_obj = sdwan_path_quality_profiles_api.fetch_sdwan_path_quality_profiles(
        name=clean_sdwan_path_quality_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.name == clean_sdwan_path_quality_profile.name
    logger.info(f"\n[SUCCESS] fetch_sdwan_path_quality_profiles found object: {fetched_obj.name}")

    not_found = sdwan_path_quality_profiles_api.fetch_sdwan_path_quality_profiles(
        name="non-existent-sdwan-pqp-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_sdwan_path_quality_profiles correctly returned None for non-existent object")


def test_delete_sdwan_path_quality_profile_by_id(sdwan_path_quality_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-pqp-del-{random_id}"

    payload = _make_sdwan_pqp_payload(object_name)

    created_obj = perform(
        sdwan_path_quality_profiles_api.create_sdwan_path_quality_profiles_with_http_info,
        response_type=SdwanPathQualityProfiles,
        sdwan_path_quality_profiles=payload,
    )

    sdwan_path_quality_profiles_api.delete_sdwan_path_quality_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        sdwan_path_quality_profiles_api.get_sdwan_path_quality_profiles_by_id(id=created_obj.id)
        pytest.fail("SDWAN Path Quality Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
