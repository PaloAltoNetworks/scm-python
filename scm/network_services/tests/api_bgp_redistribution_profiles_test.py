import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.bgp_redistribution_profiles import BgpRedistributionProfiles
from scm.network_services.models.bgp_redistribution_profiles_ipv4 import BgpRedistributionProfilesIpv4
from scm.network_services.models.bgp_redistribution_profiles_ipv4_unicast import BgpRedistributionProfilesIpv4Unicast
from scm.network_services.models.bgp_redistribution_profiles_ipv4_unicast_static import BgpRedistributionProfilesIpv4UnicastStatic
from scm.network_services.models.bgp_redistribution_profiles_ipv4_unicast_connected import BgpRedistributionProfilesIpv4UnicastConnected
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
def bgp_redistribution_profiles_api(client):
    return client.network_services.BGPRedistributionProfilesApi(client.network_services.api_client)


def _make_bgp_redist_payload(name):
    static_config = BgpRedistributionProfilesIpv4UnicastStatic(enable=True)
    unicast = BgpRedistributionProfilesIpv4Unicast(static=static_config)
    ipv4 = BgpRedistributionProfilesIpv4(unicast=unicast)
    return BgpRedistributionProfiles(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        ipv4=ipv4,
    )


@pytest.fixture
def clean_bgp_redistribution_profile(bgp_redistribution_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-redist-{random_id}"

    payload = _make_bgp_redist_payload(object_name)

    logger.info(f"\n[SETUP] Creating BGP Redistribution Profile: {object_name}")
    created_obj = perform(
        bgp_redistribution_profiles_api.create_bgp_redistribution_profiles_with_http_info,
        response_type=BgpRedistributionProfiles,
        bgp_redistribution_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting BGP Redistribution Profile ID: {created_obj.id}")
    try:
        bgp_redistribution_profiles_api.delete_bgp_redistribution_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_bgp_redistribution_profile(bgp_redistribution_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-redist-create-{random_id}"

    payload = _make_bgp_redist_payload(object_name)

    created_obj = perform(
        bgp_redistribution_profiles_api.create_bgp_redistribution_profiles_with_http_info,
        response_type=BgpRedistributionProfiles,
        bgp_redistribution_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    bgp_redistribution_profiles_api.delete_bgp_redistribution_profiles_by_id(id=created_obj.id)


def test_get_bgp_redistribution_profile_by_id(bgp_redistribution_profiles_api, clean_bgp_redistribution_profile):
    fetched_obj = bgp_redistribution_profiles_api.get_bgp_redistribution_profiles_by_id(id=clean_bgp_redistribution_profile.id)
    assert fetched_obj.id == clean_bgp_redistribution_profile.id
    assert fetched_obj.name == clean_bgp_redistribution_profile.name


def test_update_bgp_redistribution_profile(bgp_redistribution_profiles_api, clean_bgp_redistribution_profile):
    # Update with connected enabled in addition to static
    static_config = BgpRedistributionProfilesIpv4UnicastStatic(enable=True)
    connected_config = BgpRedistributionProfilesIpv4UnicastConnected(enable=True)
    updated_unicast = BgpRedistributionProfilesIpv4Unicast(static=static_config, connected=connected_config)
    updated_ipv4 = BgpRedistributionProfilesIpv4(unicast=updated_unicast)

    update_payload = clean_bgp_redistribution_profile
    update_payload.ipv4 = updated_ipv4

    updated_obj = bgp_redistribution_profiles_api.update_bgp_redistribution_profiles_by_id(
        id=clean_bgp_redistribution_profile.id,
        bgp_redistribution_profiles=update_payload,
    )

    assert updated_obj.id == clean_bgp_redistribution_profile.id
    assert updated_obj.name == clean_bgp_redistribution_profile.name


def test_list_bgp_redistribution_profiles(bgp_redistribution_profiles_api, clean_bgp_redistribution_profile):
    response = bgp_redistribution_profiles_api.list_bgp_redistribution_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert response.data is not None


def test_fetch_bgp_redistribution_profiles(bgp_redistribution_profiles_api, clean_bgp_redistribution_profile):
    fetched_obj = bgp_redistribution_profiles_api.fetch_bgp_redistribution_profiles(
        name=clean_bgp_redistribution_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_bgp_redistribution_profile.id
    assert fetched_obj.name == clean_bgp_redistribution_profile.name
    logger.info(f"\n[SUCCESS] fetch_bgp_redistribution_profiles found object: {fetched_obj.name}")

    not_found = bgp_redistribution_profiles_api.fetch_bgp_redistribution_profiles(
        name="non-existent-bgp-redist-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_bgp_redistribution_profiles correctly returned None for non-existent object")


def test_delete_bgp_redistribution_profile_by_id(bgp_redistribution_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-redist-del-{random_id}"

    payload = _make_bgp_redist_payload(object_name)

    created_obj = perform(
        bgp_redistribution_profiles_api.create_bgp_redistribution_profiles_with_http_info,
        response_type=BgpRedistributionProfiles,
        bgp_redistribution_profiles=payload,
    )

    bgp_redistribution_profiles_api.delete_bgp_redistribution_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        bgp_redistribution_profiles_api.get_bgp_redistribution_profiles_by_id(id=created_obj.id)
        pytest.fail("BGP Redistribution Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
