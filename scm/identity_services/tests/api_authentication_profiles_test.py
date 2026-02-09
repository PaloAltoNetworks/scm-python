import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.authentication_profiles import AuthenticationProfiles
from scm.identity_services.models.authentication_profiles_method import AuthenticationProfilesMethod
from scm.identity_services.models.authentication_profiles_lockout import AuthenticationProfilesLockout
from scm.identity_services.models.authentication_profiles_single_sign_on import AuthenticationProfilesSingleSignOn
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
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
def auth_profiles_api(client):
    """
    Fixture to return the Authentication Profiles API instance.
    """
    return client.identity_services.AuthenticationProfilesApi(client.identity_services.api_client)

@pytest.fixture
def clean_auth_profile(auth_profiles_api):
    """
    Fixture to create a temporary Authentication Profile for testing and automatically delete it after.
    """
    profile_name = f"test-auth-prof-{uuid.uuid4().hex[:6]}"

    # Create method with local database
    method = AuthenticationProfilesMethod(
        local_database={}
    )

    # Create lockout settings
    lockout = AuthenticationProfilesLockout(
        failed_attempts=9,
        lockout_time=5
    )

    # Create single sign-on settings
    sso = AuthenticationProfilesSingleSignOn(
        realm="EXAMPLE.COM"
    )

    payload = AuthenticationProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        allow_list=["all"],
        method=method,
        lockout=lockout,
        single_sign_on=sso,
        user_domain="default",
        username_modifier="%USERINPUT%"
    )

    logger.info(f"\n[SETUP] Creating Authentication Profile: {profile_name}")
    created_obj = perform(
        auth_profiles_api.create_authentication_profiles_with_http_info,
        response_type=AuthenticationProfiles,
        authentication_profiles=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Authentication Profile ID: {created_obj.id}")
    try:
        perform(
            auth_profiles_api.delete_authentication_profiles_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_auth_profile(auth_profiles_api):
    """
    Test manual creation and deletion of an Authentication Profile with logging.
    Mirrors Test_identityservices_AuthenticationProfilesAPIService__CreateLocalDB_Full
    """
    profile_name = f"test-auth-create-{uuid.uuid4().hex[:6]}"

    # Create method with local database
    method = AuthenticationProfilesMethod(
        local_database={}
    )

    # Create lockout settings
    lockout = AuthenticationProfilesLockout(
        failed_attempts=9,
        lockout_time=5
    )

    # Create single sign-on settings
    sso = AuthenticationProfilesSingleSignOn(
        realm="EXAMPLE.COM"
    )

    payload = AuthenticationProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        allow_list=["all"],
        method=method,
        lockout=lockout,
        single_sign_on=sso,
        user_domain="default",
        username_modifier="%USERINPUT%"
    )

    # Create with logging
    created_obj = perform(
        auth_profiles_api.create_authentication_profiles_with_http_info,
        response_type=AuthenticationProfiles,
        authentication_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert created_obj.user_domain == "default"
    assert created_obj.username_modifier == "%USERINPUT%"
    assert "all" in created_obj.allow_list
    assert created_obj.lockout.failed_attempts == 9
    assert created_obj.lockout.lockout_time == 5
    assert created_obj.single_sign_on.realm == "EXAMPLE.COM"

    # Cleanup with logging
    perform(
        auth_profiles_api.delete_authentication_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_auth_profile_by_id(auth_profiles_api, clean_auth_profile):
    """
    Test retrieving an Authentication Profile by ID with logging.
    Mirrors Test_identityservices_AuthenticationProfilesAPIService__GetByID
    """
    fetched_obj = perform(
        auth_profiles_api.get_authentication_profiles_by_id_with_http_info,
        id=clean_auth_profile.id
    )

    assert fetched_obj.id == clean_auth_profile.id
    assert fetched_obj.name == clean_auth_profile.name


def test_update_auth_profile(auth_profiles_api, clean_auth_profile):
    """
    Test updating an Authentication Profile with logging.
    Mirrors Test_identityservices_AuthenticationProfilesAPIService__UpdateLocalDB
    """
    update_payload = clean_auth_profile
    update_payload.user_domain = "paloaltonetworks.com"

    updated_obj = perform(
        auth_profiles_api.update_authentication_profiles_by_id_with_http_info,
        id=clean_auth_profile.id,
        authentication_profiles=update_payload
    )

    assert updated_obj.id == clean_auth_profile.id
    assert updated_obj.user_domain == "paloaltonetworks.com"


def test_list_auth_profiles(auth_profiles_api, clean_auth_profile):
    """
    Test listing Authentication Profiles with logging.
    """
    response = perform(
        auth_profiles_api.list_authentication_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify the fixture object is in the list
    found = False
    for item in response.data:
        if item.id == clean_auth_profile.id:
            found = True
            break
    assert found is True, f"Created profile {clean_auth_profile.id} not found in list response"




def test_fetch_authentication_profiles(auth_profiles_api, clean_auth_profile):
    """
    Test fetching a single authentication_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = auth_profiles_api.fetch_authentication_profiles(
        name=clean_auth_profile.name,
        folder=clean_auth_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found authentication_profiles '{clean_auth_profile.name}'"
    assert fetched_obj.id == clean_auth_profile.id
    assert fetched_obj.name == clean_auth_profile.name
    assert fetched_obj.folder == clean_auth_profile.folder
    logger.info(f"\n[SUCCESS] fetch_authentication_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent authentication_profiles (should return None)
    not_found = auth_profiles_api.fetch_authentication_profiles(
        name="non-existent-authentication_profiles-xyz-12345",
        folder=clean_auth_profile.folder
    )
    assert not_found is None, "Should return None for non-existent authentication_profiles"
    logger.info(f"\n[SUCCESS] fetch_authentication_profiles correctly returned None for non-existent authentication_profiles")


def test_delete_auth_profile_by_id(auth_profiles_api):
    """
    Test deletion specifically with logging.
    """
    # Setup
    profile_name = f"test-auth-del-{uuid.uuid4().hex[:6]}"

    method = AuthenticationProfilesMethod(
        local_database={}
    )

    payload = AuthenticationProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        allow_list=["all"],
        method=method
    )

    created_obj = perform(
        auth_profiles_api.create_authentication_profiles_with_http_info,
        response_type=AuthenticationProfiles,
        authentication_profiles=payload
    )

    # Perform Delete with logging
    perform(
        auth_profiles_api.delete_authentication_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    # Verify Deletion
    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        auth_profiles_api.get_authentication_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
