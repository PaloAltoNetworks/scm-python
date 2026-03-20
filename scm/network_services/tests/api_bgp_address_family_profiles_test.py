import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.bgp_address_family_profiles import BgpAddressFamilyProfiles
from scm.network_services.models.bgp_address_family_profiles_ipv4 import BgpAddressFamilyProfilesIpv4
from scm.network_services.models.bgp_address_family import BgpAddressFamily
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
def bgp_address_family_profiles_api(client):
    return client.network_services.BGPAddressFamilyProfilesApi(client.network_services.api_client)


def _make_bgp_af_payload(name):
    unicast = BgpAddressFamily(enable=True)
    ipv4 = BgpAddressFamilyProfilesIpv4(unicast=unicast)
    return BgpAddressFamilyProfiles(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        ipv4=ipv4,
    )


@pytest.fixture
def clean_bgp_address_family_profile(bgp_address_family_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-af-{random_id}"

    payload = _make_bgp_af_payload(object_name)

    logger.info(f"\n[SETUP] Creating BGP Address Family Profile: {object_name}")
    created_obj = perform(
        bgp_address_family_profiles_api.create_bgp_address_family_profiles_with_http_info,
        response_type=BgpAddressFamilyProfiles,
        bgp_address_family_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting BGP Address Family Profile ID: {created_obj.id}")
    try:
        bgp_address_family_profiles_api.delete_bgp_address_family_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_bgp_address_family_profile(bgp_address_family_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-af-create-{random_id}"

    payload = _make_bgp_af_payload(object_name)

    created_obj = perform(
        bgp_address_family_profiles_api.create_bgp_address_family_profiles_with_http_info,
        response_type=BgpAddressFamilyProfiles,
        bgp_address_family_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    bgp_address_family_profiles_api.delete_bgp_address_family_profiles_by_id(id=created_obj.id)


def test_get_bgp_address_family_profile_by_id(bgp_address_family_profiles_api, clean_bgp_address_family_profile):
    fetched_obj = bgp_address_family_profiles_api.get_bgp_address_family_profiles_by_id(id=clean_bgp_address_family_profile.id)
    assert fetched_obj.id == clean_bgp_address_family_profile.id
    assert fetched_obj.name == clean_bgp_address_family_profile.name


def test_update_bgp_address_family_profile(bgp_address_family_profiles_api, clean_bgp_address_family_profile):
    unicast = BgpAddressFamily(enable=True)
    multicast = BgpAddressFamily(enable=True)
    updated_ipv4 = BgpAddressFamilyProfilesIpv4(unicast=unicast, multicast=multicast)

    update_payload = clean_bgp_address_family_profile
    update_payload.ipv4 = updated_ipv4

    updated_obj = bgp_address_family_profiles_api.update_bgp_address_family_profiles_by_id(
        id=clean_bgp_address_family_profile.id,
        bgp_address_family_profiles=update_payload,
    )

    assert updated_obj.id == clean_bgp_address_family_profile.id
    assert updated_obj.name == clean_bgp_address_family_profile.name


def test_list_bgp_address_family_profiles(bgp_address_family_profiles_api, clean_bgp_address_family_profile):
    response = bgp_address_family_profiles_api.list_bgp_address_family_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert response.data is not None


def test_fetch_bgp_address_family_profiles(bgp_address_family_profiles_api, clean_bgp_address_family_profile):
    fetched_obj = bgp_address_family_profiles_api.fetch_bgp_address_family_profiles(
        name=clean_bgp_address_family_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_bgp_address_family_profile.id
    assert fetched_obj.name == clean_bgp_address_family_profile.name
    logger.info(f"\n[SUCCESS] fetch_bgp_address_family_profiles found object: {fetched_obj.name}")

    not_found = bgp_address_family_profiles_api.fetch_bgp_address_family_profiles(
        name="non-existent-bgp-af-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_bgp_address_family_profiles correctly returned None for non-existent object")


def test_delete_bgp_address_family_profile_by_id(bgp_address_family_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-af-del-{random_id}"

    payload = _make_bgp_af_payload(object_name)

    created_obj = perform(
        bgp_address_family_profiles_api.create_bgp_address_family_profiles_with_http_info,
        response_type=BgpAddressFamilyProfiles,
        bgp_address_family_profiles=payload,
    )

    bgp_address_family_profiles_api.delete_bgp_address_family_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        bgp_address_family_profiles_api.get_bgp_address_family_profiles_by_id(id=created_obj.id)
        pytest.fail("BGP Address Family Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
