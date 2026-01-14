import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.authentication_sequences import AuthenticationSequences
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
# -----------------------------------------------------------------------------

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def auth_sequences_api(client):
    return client.identity_services.AuthenticationSequencesApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def auth_profiles_api(client):
    return client.identity_services.AuthenticationProfilesApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def test_auth_profile(auth_profiles_api):
    """
    Setup/Teardown for the prerequisite Authentication Profile.
    """
    profile_name = f"scm-authprofile-{uuid.uuid4().hex[:4]}"

    method = AuthenticationProfilesMethod(
        local_database={}
    )

    payload = AuthenticationProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        allow_list=["all"],
        method=method
    )

    logger.info(f"\n[SETUP] Creating Prerequisite Auth Profile: {profile_name}")
    created_profile = perform(
        auth_profiles_api.create_authentication_profiles_with_http_info,
        response_type=AuthenticationProfiles,
        authentication_profiles=payload
    )

    yield created_profile.name

    logger.info(f"\n[TEARDOWN] Deleting Auth Profile: {created_profile.name}")
    try:
        perform(
            auth_profiles_api.delete_authentication_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup auth profile: {e}")

@pytest.fixture
def clean_auth_sequence(auth_sequences_api, test_auth_profile):
    """
    Creates an Authentication Sequence for tests that require an existing object.
    """
    sequence_name = f"test-auth-seq-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationSequences(
        name=sequence_name,
        folder=TARGET_FOLDER,
        authentication_profiles=[test_auth_profile],
        use_domain_find_profile=False
    )

    logger.info(f"\n[SETUP] Creating Authentication Sequence: {sequence_name}")
    created_obj = perform(
        auth_sequences_api.create_authentication_sequences_with_http_info,
        response_type=AuthenticationSequences,
        authentication_sequences=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Authentication Sequence ID: {created_obj.id}")
    try:
        perform(
            auth_sequences_api.delete_authentication_sequences_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")

def test_create_auth_sequence(auth_sequences_api, test_auth_profile):
    """
    Test manual creation and deletion of an Authentication Sequence with logging.
    Mirrors Test_identityservices_AuthenticationSequencesAPIService__Create
    """
    sequence_name = f"test-auth-seq-create-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationSequences(
        name=sequence_name,
        folder=TARGET_FOLDER,
        authentication_profiles=[test_auth_profile],
        use_domain_find_profile=False
    )

    created_obj = perform(
        auth_sequences_api.create_authentication_sequences_with_http_info,
        response_type=AuthenticationSequences,
        authentication_sequences=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == sequence_name
    assert created_obj.use_domain_find_profile == False
    assert created_obj.authentication_profiles == [test_auth_profile]

    perform(
        auth_sequences_api.delete_authentication_sequences_by_id_with_http_info,
        id=created_obj.id
    )

def test_get_auth_sequence_by_id(auth_sequences_api, clean_auth_sequence):
    """
    Test retrieving an Authentication Sequence by ID with logging.
    Mirrors Test_identityservices_AuthenticationSequencesAPIService__GetByID
    """
    fetched_obj = perform(
        auth_sequences_api.get_authentication_sequences_by_id_with_http_info,
        id=clean_auth_sequence.id
    )

    assert fetched_obj.id == clean_auth_sequence.id
    assert fetched_obj.name == clean_auth_sequence.name

def test_update_auth_sequence(auth_sequences_api, clean_auth_sequence):
    """
    Test updating an Authentication Sequence with logging.
    Mirrors Test_identityservices_AuthenticationSequencesAPIService__Update
    """
    update_payload = clean_auth_sequence
    update_payload.use_domain_find_profile = True

    updated_obj = perform(
        auth_sequences_api.update_authentication_sequences_by_id_with_http_info,
        id=clean_auth_sequence.id,
        authentication_sequences=update_payload
    )

    assert updated_obj.id == clean_auth_sequence.id
    assert updated_obj.use_domain_find_profile == True

def test_list_auth_sequences(auth_sequences_api, clean_auth_sequence):
    """
    Test listing Authentication Sequences with logging.
    Mirrors Test_identityservices_AuthenticationSequencesAPIService__List
    """
    response = perform(
        auth_sequences_api.list_authentication_sequences_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_auth_sequence.id:
            found = True
            break
    assert found is True, f"Created sequence {clean_auth_sequence.id} not found in list response"

def test_delete_auth_sequence_by_id(auth_sequences_api, test_auth_profile):
    """
    Test deletion specifically with logging.
    Mirrors Test_identityservices_AuthenticationSequencesAPIService__DeleteByID
    """
    sequence_name = f"test-auth-seq-del-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationSequences(
        name=sequence_name,
        folder=TARGET_FOLDER,
        authentication_profiles=[test_auth_profile],
        use_domain_find_profile=False
    )

    created_obj = perform(
        auth_sequences_api.create_authentication_sequences_with_http_info,
        response_type=AuthenticationSequences,
        authentication_sequences=payload
    )

    perform(
        auth_sequences_api.delete_authentication_sequences_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        auth_sequences_api.get_authentication_sequences_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Sequence should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
