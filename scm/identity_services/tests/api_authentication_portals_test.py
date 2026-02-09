import logging
import uuid
import pytest
from scm import Scm
from scm.identity_services.models.authentication_portals import AuthenticationPortals
from scm.identity_services.models.authentication_profiles import AuthenticationProfiles
from scm.identity_services.models.authentication_profiles_method import AuthenticationProfilesMethod
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
TEST_REDIRECT_HOST = "192.168.255.254"
CERT_PROFILE_NAME = "EDL-Hosting-Service-Profile"
# -----------------------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def auth_portals_api(client):
    return client.identity_services.AuthenticationPortalsApi(client.identity_services.api_client)


@pytest.fixture(scope="module")
def auth_profiles_api(client):
    return client.identity_services.AuthenticationProfilesApi(client.identity_services.api_client)


@pytest.fixture(scope="module")
def test_auth_profile(auth_profiles_api):
    """
    Setup/Teardown for prerequisite Authentication Profile.
    """
    profile_name = f"test-auth-prof-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        allow_list=["all"],
        method=AuthenticationProfilesMethod(local_database={})
    )

    logger.info(f"\n[SETUP] Creating Prerequisite Auth Profile: {profile_name}")
    try:
        created_profile = perform(
            auth_profiles_api.create_authentication_profiles_with_http_info,
            response_type=AuthenticationProfiles,
            authentication_profiles=payload
        )
    except Exception as e:
        logger.warning(f"Could not create auth profile fixture: {e}")
        pytest.skip(f"Prerequisite auth profile creation failed: {e}")

    yield created_profile.name

    logger.info(f"\n[TEARDOWN] Deleting Auth Profile: {created_profile.id}")
    try:
        perform(
            auth_profiles_api.delete_authentication_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup auth profile: {e}")


@pytest.fixture
def clean_auth_portal(auth_portals_api, test_auth_profile):
    """
    Setup/Teardown for an Authentication Portal.
    """
    portal_name = f"test-portal-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationPortals(
        folder=TARGET_FOLDER,
        redirect_host=TEST_REDIRECT_HOST,
        authentication_profile=test_auth_profile,
        certificate_profile=CERT_PROFILE_NAME,
        gp_udp_port=10,
        idle_timer=10,
        timer=12
    )

    logger.info(f"\n[SETUP] Creating Auth Portal: {portal_name}")
    created_portal = perform(
        auth_portals_api.create_authentication_portals_with_http_info,
        response_type=AuthenticationPortals,
        authentication_portals=payload
    )

    yield created_portal

    logger.info(f"\n[TEARDOWN] Deleting Auth Portal: {created_portal.id}")
    try:
        perform(
            auth_portals_api.delete_authentication_portals_by_id_with_http_info,
            id=created_portal.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup auth portal: {e}")


def test_create_auth_portal(auth_portals_api, test_auth_profile):
    """Test creation of an Authentication Portal."""
    payload = AuthenticationPortals(
        folder=TARGET_FOLDER,
        redirect_host=TEST_REDIRECT_HOST,
        authentication_profile=test_auth_profile,
        certificate_profile=CERT_PROFILE_NAME,
        gp_udp_port=10,
        idle_timer=10,
        timer=12
    )

    created_obj = perform(
        auth_portals_api.create_authentication_portals_with_http_info,
        response_type=AuthenticationPortals,
        authentication_portals=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.redirect_host == TEST_REDIRECT_HOST
    assert created_obj.gp_udp_port == 10

    perform(
        auth_portals_api.delete_authentication_portals_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_auth_portal_by_id(auth_portals_api, clean_auth_portal):
    """Test retrieving an Authentication Portal by ID."""
    fetched_obj = perform(
        auth_portals_api.get_authentication_portals_by_id_with_http_info,
        id=clean_auth_portal.id
    )

    assert fetched_obj.id == clean_auth_portal.id
    assert fetched_obj.redirect_host == TEST_REDIRECT_HOST
    assert fetched_obj.timer == 12


def test_update_auth_portal(auth_portals_api, clean_auth_portal):
    """Test updating an Authentication Portal."""
    update_payload = clean_auth_portal
    update_payload.gp_udp_port = 20
    update_payload.timer = 30

    updated_obj = perform(
        auth_portals_api.update_authentication_portals_by_id_with_http_info,
        id=clean_auth_portal.id,
        authentication_portals=update_payload
    )

    assert updated_obj.id == clean_auth_portal.id
    assert updated_obj.gp_udp_port == 20
    assert updated_obj.timer == 30


def test_list_auth_portals(auth_portals_api, clean_auth_portal):
    """Test listing Authentication Portals."""
    response = perform(
        auth_portals_api.list_authentication_portals_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_auth_portal.id:
            found = True
            break
    assert found is True, f"Created portal {clean_auth_portal.id} not found in list response"



def test_delete_auth_portal_by_id(auth_portals_api, test_auth_profile):
    """Test deleting an Authentication Portal."""
    payload = AuthenticationPortals(
        folder=TARGET_FOLDER,
        redirect_host=TEST_REDIRECT_HOST,
        authentication_profile=test_auth_profile,
        certificate_profile=CERT_PROFILE_NAME,
        gp_udp_port=10,
        idle_timer=10,
        timer=12
    )

    created_obj = perform(
        auth_portals_api.create_authentication_portals_with_http_info,
        response_type=AuthenticationPortals,
        authentication_portals=payload
    )

    perform(
        auth_portals_api.delete_authentication_portals_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        auth_portals_api.get_authentication_portals_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Portal should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
