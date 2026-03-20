import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.zone_protection_profiles import ZoneProtectionProfiles
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
def zone_protection_profiles_api(client):
    return client.network_services.ZoneProtectionProfilesApi(client.network_services.api_client)


@pytest.fixture
def clean_zone_protection_profile(zone_protection_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-zpp-{random_id}"

    payload = ZoneProtectionProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test zone protection profile",
        discard_icmp_embedded_error=True,
        icmp_frag_discard=True,
    )

    logger.info(f"\n[SETUP] Creating Zone Protection Profile: {object_name}")
    created_obj = perform(
        zone_protection_profiles_api.create_zone_protection_profiles_with_http_info,
        response_type=ZoneProtectionProfiles,
        zone_protection_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Zone Protection Profile ID: {created_obj.id}")
    try:
        zone_protection_profiles_api.delete_zone_protection_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_zone_protection_profile(zone_protection_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-zpp-create-{random_id}"

    payload = ZoneProtectionProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test zone protection profile for create",
        discard_icmp_embedded_error=True,
        icmp_frag_discard=True,
    )

    created_obj = perform(
        zone_protection_profiles_api.create_zone_protection_profiles_with_http_info,
        response_type=ZoneProtectionProfiles,
        zone_protection_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    zone_protection_profiles_api.delete_zone_protection_profiles_by_id(id=created_obj.id)


def test_get_zone_protection_profile_by_id(zone_protection_profiles_api, clean_zone_protection_profile):
    fetched_obj = zone_protection_profiles_api.get_zone_protection_profiles_by_id(id=clean_zone_protection_profile.id)
    assert fetched_obj.id == clean_zone_protection_profile.id
    assert fetched_obj.name == clean_zone_protection_profile.name


def test_update_zone_protection_profile(zone_protection_profiles_api, clean_zone_protection_profile):
    update_payload = clean_zone_protection_profile
    update_payload.description = "Updated zone protection profile"
    update_payload.icmp_frag_discard = True
    update_payload.discard_icmp_embedded_error = True

    updated_obj = zone_protection_profiles_api.update_zone_protection_profiles_by_id(
        id=clean_zone_protection_profile.id,
        zone_protection_profiles=update_payload,
    )

    assert updated_obj.id == clean_zone_protection_profile.id


def test_list_zone_protection_profiles(zone_protection_profiles_api, clean_zone_protection_profile):
    response = zone_protection_profiles_api.list_zone_protection_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_zone_protection_profile.id:
            found = True
            break
    assert found is True


def test_fetch_zone_protection_profiles(zone_protection_profiles_api, clean_zone_protection_profile):
    fetched_obj = zone_protection_profiles_api.fetch_zone_protection_profiles(
        name=clean_zone_protection_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_zone_protection_profile.id
    assert fetched_obj.name == clean_zone_protection_profile.name
    logger.info(f"\n[SUCCESS] fetch_zone_protection_profiles found object: {fetched_obj.name}")

    not_found = zone_protection_profiles_api.fetch_zone_protection_profiles(
        name="non-existent-zpp-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_zone_protection_profiles correctly returned None for non-existent object")


def test_delete_zone_protection_profile_by_id(zone_protection_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-zpp-del-{random_id}"

    payload = ZoneProtectionProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
    )

    created_obj = perform(
        zone_protection_profiles_api.create_zone_protection_profiles_with_http_info,
        response_type=ZoneProtectionProfiles,
        zone_protection_profiles=payload,
    )

    zone_protection_profiles_api.delete_zone_protection_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        zone_protection_profiles_api.get_zone_protection_profiles_by_id(id=created_obj.id)
        pytest.fail("Zone Protection Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
