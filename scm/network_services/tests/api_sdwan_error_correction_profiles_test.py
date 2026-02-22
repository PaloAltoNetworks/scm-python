import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.sdwan_error_correction_profiles import SdwanErrorCorrectionProfiles
from scm.network_services.models.sdwan_error_correction_profiles_mode import SdwanErrorCorrectionProfilesMode
from scm.network_services.models.sdwan_error_correction_profiles_mode_forward_error_correction import SdwanErrorCorrectionProfilesModeForwardErrorCorrection
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
def sdwan_error_correction_profiles_api(client):
    return client.network_services.SDWANErrorCorrectionProfilesApi(client.network_services.api_client)


def _make_sdwan_ecp_payload(name, threshold=2, ratio="10% (20:2)", duration=1000):
    mode = SdwanErrorCorrectionProfilesMode(
        forward_error_correction=SdwanErrorCorrectionProfilesModeForwardErrorCorrection(
            ratio=ratio,
            recovery_duration=duration,
        ),
    )
    return SdwanErrorCorrectionProfiles(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        activation_threshold=threshold,
        mode=mode,
    )


@pytest.fixture
def clean_sdwan_error_correction_profile(sdwan_error_correction_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-ecp-{random_id}"

    payload = _make_sdwan_ecp_payload(object_name)

    logger.info(f"\n[SETUP] Creating SDWAN Error Correction Profile: {object_name}")
    created_obj = perform(
        sdwan_error_correction_profiles_api.create_sdwan_error_correction_profiles_with_http_info,
        response_type=SdwanErrorCorrectionProfiles,
        sdwan_error_correction_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting SDWAN Error Correction Profile ID: {created_obj.id}")
    try:
        sdwan_error_correction_profiles_api.delete_sdwan_error_correction_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_sdwan_error_correction_profile(sdwan_error_correction_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-ecp-create-{random_id}"

    payload = _make_sdwan_ecp_payload(object_name)

    created_obj = perform(
        sdwan_error_correction_profiles_api.create_sdwan_error_correction_profiles_with_http_info,
        response_type=SdwanErrorCorrectionProfiles,
        sdwan_error_correction_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    sdwan_error_correction_profiles_api.delete_sdwan_error_correction_profiles_by_id(id=created_obj.id)


def test_get_sdwan_error_correction_profile_by_id(sdwan_error_correction_profiles_api, clean_sdwan_error_correction_profile):
    fetched_obj = sdwan_error_correction_profiles_api.get_sdwan_error_correction_profiles_by_id(id=clean_sdwan_error_correction_profile.id)
    assert fetched_obj.id == clean_sdwan_error_correction_profile.id
    assert fetched_obj.name == clean_sdwan_error_correction_profile.name


def test_update_sdwan_error_correction_profile(sdwan_error_correction_profiles_api, clean_sdwan_error_correction_profile):
    # Update with different threshold and ratio
    # Note: valid ratio "20% (20:4)" per Go test
    update_payload = _make_sdwan_ecp_payload(
        clean_sdwan_error_correction_profile.name,
        threshold=3,
        ratio="20% (20:4)",
        duration=2000,
    )

    updated_obj = sdwan_error_correction_profiles_api.update_sdwan_error_correction_profiles_by_id(
        id=clean_sdwan_error_correction_profile.id,
        sdwan_error_correction_profiles=update_payload,
    )

    assert updated_obj.id == clean_sdwan_error_correction_profile.id
    assert updated_obj.activation_threshold == 3


def test_list_sdwan_error_correction_profiles(sdwan_error_correction_profiles_api, clean_sdwan_error_correction_profile):
    response = sdwan_error_correction_profiles_api.list_sdwan_error_correction_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None

    found = False
    if response.data:
        for item in response.data:
            if item.name == clean_sdwan_error_correction_profile.name:
                found = True
                break
    assert found is True


def test_fetch_sdwan_error_correction_profiles(sdwan_error_correction_profiles_api, clean_sdwan_error_correction_profile):
    fetched_obj = sdwan_error_correction_profiles_api.fetch_sdwan_error_correction_profiles(
        name=clean_sdwan_error_correction_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.name == clean_sdwan_error_correction_profile.name
    logger.info(f"\n[SUCCESS] fetch_sdwan_error_correction_profiles found object: {fetched_obj.name}")

    not_found = sdwan_error_correction_profiles_api.fetch_sdwan_error_correction_profiles(
        name="non-existent-sdwan-ecp-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_sdwan_error_correction_profiles correctly returned None for non-existent object")


def test_delete_sdwan_error_correction_profile_by_id(sdwan_error_correction_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-sdwan-ecp-del-{random_id}"

    payload = _make_sdwan_ecp_payload(object_name)

    created_obj = perform(
        sdwan_error_correction_profiles_api.create_sdwan_error_correction_profiles_with_http_info,
        response_type=SdwanErrorCorrectionProfiles,
        sdwan_error_correction_profiles=payload,
    )

    sdwan_error_correction_profiles_api.delete_sdwan_error_correction_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        sdwan_error_correction_profiles_api.get_sdwan_error_correction_profiles_by_id(id=created_obj.id)
        pytest.fail("SDWAN Error Correction Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
