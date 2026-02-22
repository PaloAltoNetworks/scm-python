import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.ospf_auth_profiles import OspfAuthProfiles
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
def ospf_authentication_profiles_api(client):
    return client.network_services.OSPFAuthenticationProfilesApi(client.network_services.api_client)


@pytest.fixture
def clean_ospf_auth_profile(ospf_authentication_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-ospf-auth-{random_id}"

    payload = OspfAuthProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        password="testpw1",
    )

    logger.info(f"\n[SETUP] Creating OSPF Authentication Profile: {object_name}")
    created_obj = perform(
        ospf_authentication_profiles_api.create_ospf_authentication_profiles_with_http_info,
        response_type=OspfAuthProfiles,
        ospf_auth_profiles=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting OSPF Authentication Profile ID: {created_obj.id}")
    try:
        ospf_authentication_profiles_api.delete_ospf_authentication_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_ospf_authentication_profile(ospf_authentication_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-ospf-auth-create-{random_id}"

    payload = OspfAuthProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        password="testpw2",
    )

    created_obj = perform(
        ospf_authentication_profiles_api.create_ospf_authentication_profiles_with_http_info,
        response_type=OspfAuthProfiles,
        ospf_auth_profiles=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    ospf_authentication_profiles_api.delete_ospf_authentication_profiles_by_id(id=created_obj.id)


def test_get_ospf_authentication_profile_by_id(ospf_authentication_profiles_api, clean_ospf_auth_profile):
    fetched_obj = ospf_authentication_profiles_api.get_ospf_authentication_profiles_by_id(id=clean_ospf_auth_profile.id)
    assert fetched_obj.id == clean_ospf_auth_profile.id
    assert fetched_obj.name == clean_ospf_auth_profile.name


def test_update_ospf_authentication_profile(ospf_authentication_profiles_api, clean_ospf_auth_profile):
    update_payload = clean_ospf_auth_profile
    update_payload.password = "updpw4"

    updated_obj = ospf_authentication_profiles_api.update_ospf_authentication_profiles_by_id(
        id=clean_ospf_auth_profile.id,
        ospf_auth_profiles=update_payload,
    )

    assert updated_obj.id == clean_ospf_auth_profile.id
    assert updated_obj.name == clean_ospf_auth_profile.name


def test_list_ospf_authentication_profiles(ospf_authentication_profiles_api, clean_ospf_auth_profile):
    response = ospf_authentication_profiles_api.list_ospf_authentication_profiles(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert response.data is not None


def test_fetch_ospf_authentication_profiles(ospf_authentication_profiles_api, clean_ospf_auth_profile):
    fetched_obj = ospf_authentication_profiles_api.fetch_ospf_authentication_profiles(
        name=clean_ospf_auth_profile.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_ospf_auth_profile.id
    assert fetched_obj.name == clean_ospf_auth_profile.name
    logger.info(f"\n[SUCCESS] fetch_ospf_authentication_profiles found object: {fetched_obj.name}")

    not_found = ospf_authentication_profiles_api.fetch_ospf_authentication_profiles(
        name="non-existent-ospf-auth-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_ospf_authentication_profiles correctly returned None for non-existent object")


def test_delete_ospf_authentication_profile_by_id(ospf_authentication_profiles_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-ospf-auth-del-{random_id}"

    payload = OspfAuthProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        password="delpw5",
    )

    created_obj = perform(
        ospf_authentication_profiles_api.create_ospf_authentication_profiles_with_http_info,
        response_type=OspfAuthProfiles,
        ospf_auth_profiles=payload,
    )

    ospf_authentication_profiles_api.delete_ospf_authentication_profiles_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        ospf_authentication_profiles_api.get_ospf_authentication_profiles_by_id(id=created_obj.id)
        pytest.fail("OSPF Authentication Profile should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
