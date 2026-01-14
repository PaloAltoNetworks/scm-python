import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.authentication_portals import AuthenticationPortals
from scm.identity_services.models.authentication_profiles import AuthenticationProfiles
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
    """
    Fixture to initialize the SCM client once for the module.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def auth_portals_api(client):
    """
    Fixture to return the Authentication Portals API instance.
    """
    return client.identity_services.AuthenticationPortalsApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def auth_profiles_api(client):
    """
    Fixture to return the Authentication Profiles API instance.
    """
    return client.identity_services.AuthenticationProfilesApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def test_auth_profile(auth_profiles_api):
    """
    Setup/Teardown for the prerequisite Authentication Profile.
    Mirrors the 'setupTestAuthProfile' function in the Go test.
    """
    random_id = uuid.uuid4().hex[:6]
    profile_name = f"test-auth-prof-{random_id}"

    # Create a minimal Authentication Profile required for the portal
    payload = AuthenticationProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        allow_list=[],
        method={}
    )

    logger.info(f"\n[SETUP] Creating Prerequisite Auth Profile: {profile_name}")
    try:
        created_profile = perform(
            auth_profiles_api.create_authentication_profiles,
            authentication_profiles=payload
        )
    except Exception as e:
        logger.warning(f"Could not create auth profile fixture: {e}")
        pytest.skip(f"Skipping tests due to auth profile creation failure: {e}")

    yield created_profile.name

    logger.info(f"\n[TEARDOWN] Deleting Auth Profile: {created_profile.name}")
    try:
        perform(
            auth_profiles_api.delete_authentication_profiles_by_id,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup auth profile: {e}")

@pytest.fixture
def clean_auth_portal(auth_portals_api, test_auth_profile):
    """
    Creates an Authentication Portal for tests that require an existing object (like List).
    """
    payload = AuthenticationPortals(
        folder=TARGET_FOLDER,
        redirect_host=TEST_REDIRECT_HOST,
        authentication_profile=test_auth_profile,
        certificate_profile=CERT_PROFILE_NAME,
        gp_udp_port=10,
        idle_timer=10,
        timer=12
    )

    logger.info(f"\n[SETUP] Creating Auth Portal for fixture")
    created_obj = perform(
        auth_portals_api.create_authentication_portals,
        authentication_portals=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Auth Portal ID: {created_obj.id}")
    try:
        perform(
            auth_portals_api.delete_authentication_portals_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")

def test_create_auth_portal(auth_portals_api, test_auth_profile):
    """
    Test manual creation and deletion of an Authentication Portal with logging.
    Mirrors Test_identityservices_AuthenticationPortalsAPIService__Create
    """
    payload = AuthenticationPortals(
        folder=TARGET_FOLDER,
        redirect_host=TEST_REDIRECT_HOST,
        authentication_profile=test_auth_profile,
        certificate_profile=CERT_PROFILE_NAME,
        gp_udp_port=10,
        idle_timer=10,
        timer=12
    )

    # Create with logging
    created_obj = perform(
        auth_portals_api.create_authentication_portals,
        authentication_portals=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.redirect_host == TEST_REDIRECT_HOST
    assert created_obj.gp_udp_port == 10

    # Cleanup with logging
    perform(
        auth_portals_api.delete_authentication_portals_by_id,
        id=created_obj.id
    )

def test_get_auth_portal_by_id(auth_portals_api, clean_auth_portal):
    """
    Test retrieving an Authentication Portal by ID with logging.
    Mirrors Test_identityservices_AuthenticationPortalsAPIService__GetByID
    """
    fetched_obj = perform(
        auth_portals_api.get_authentication_portals_by_id,
        id=clean_auth_portal.id
    )

    assert fetched_obj.id == clean_auth_portal.id
    assert fetched_obj.redirect_host == TEST_REDIRECT_HOST
    assert fetched_obj.timer == clean_auth_portal.timer

def test_update_auth_portal(auth_portals_api, clean_auth_portal):
    """
    Test updating an Authentication Portal with logging.
    Mirrors Test_identityservices_AuthenticationPortalsAPIService__Update
    """
    update_payload = clean_auth_portal
    update_payload.gp_udp_port = 20
    update_payload.timer = 30

    updated_obj = perform(
        auth_portals_api.update_authentication_portals_by_id,
        id=clean_auth_portal.id,
        authentication_portals=update_payload
    )

    assert updated_obj.id == clean_auth_portal.id
    assert updated_obj.gp_udp_port == 20
    assert updated_obj.timer == 30

def test_list_auth_portals(auth_portals_api, clean_auth_portal):
    """
    Test listing Authentication Portals with logging.
    Mirrors Test_identityservices_AuthenticationPortalsAPIService__List
    """
    response = perform(
        auth_portals_api.list_authentication_portals,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify the fixture object is in the list
    found = False
    for item in response.data:
        if item.id == clean_auth_portal.id:
            found = True
            break
    assert found is True, f"Created portal {clean_auth_portal.id} not found in list response"

def test_delete_auth_portal_by_id(auth_portals_api, test_auth_profile):
    """
    Test deletion specifically with logging.
    Mirrors Test_identityservices_AuthenticationPortalsAPIService__DeleteByID
    """
    # Setup
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
        auth_portals_api.create_authentication_portals,
        authentication_portals=payload
    )

    # Perform Delete with logging
    perform(
        auth_portals_api.delete_authentication_portals_by_id,
        id=created_obj.id
    )

    # Verify Deletion
    try:
        auth_portals_api.get_authentication_portals_by_id(id=created_obj.id)
        pytest.fail("Portal should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
