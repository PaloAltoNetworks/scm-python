import logging
import uuid
import pytest
from scm import Scm
from scm.identity_services.models.scep_profiles import ScepProfiles
from scm.identity_services.models.scep_profiles_algorithm import ScepProfilesAlgorithm
from scm.identity_services.models.scep_profiles_algorithm_rsa import ScepProfilesAlgorithmRsa
from scm.identity_services.models.scep_profiles_scep_challenge import ScepProfilesScepChallenge
from scm.identity_services.models.scep_profiles_scep_challenge_dynamic import ScepProfilesScepChallengeDynamic
from scm.identity_services.models.scep_profiles_certificate_attributes import ScepProfilesCertificateAttributes
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
def scep_profiles_api(client):
    return client.identity_services.SCEPProfilesApi(client.identity_services.api_client)


@pytest.fixture
def clean_scep_profile(scep_profiles_api):
    """
    Setup/Teardown for a simple SCEP profile.
    """
    profile_name = f"scm-scep-{uuid.uuid4().hex[:6]}"

    algorithm = ScepProfilesAlgorithm(
        rsa=ScepProfilesAlgorithmRsa(
            rsa_nbits="2048"
        )
    )

    challenge = ScepProfilesScepChallenge(
        fixed="mypassword123"
    )

    payload = ScepProfiles(
        folder=TARGET_FOLDER,
        name=profile_name,
        scep_url="https://scep.example.com/",
        ca_identity_name="Default",
        digest="sha256",
        subject="CN=$USERNAME",
        algorithm=algorithm,
        scep_challenge=challenge
    )

    logger.info(f"\n[SETUP] Creating SCEP Profile: {profile_name}")
    created_profile = perform(
        scep_profiles_api.create_scep_profiles_with_http_info,
        response_type=ScepProfiles,
        scep_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting SCEP Profile: {created_profile.id}")
    try:
        perform(
            scep_profiles_api.delete_scep_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup SCEP profile: {e}")


def test_create_scep_profile(scep_profiles_api):
    """Test creation of a complex SCEP Profile."""
    profile_name = f"scm-scep-create-{uuid.uuid4().hex[:6]}"

    algorithm = ScepProfilesAlgorithm(
        rsa=ScepProfilesAlgorithmRsa(
            rsa_nbits="2048"
        )
    )

    dynamic_settings = ScepProfilesScepChallengeDynamic(
        username="scep-admin",
        password="mypassword123",
        otp_server_url="https://otp.example.com/api/v1/generate"
    )

    challenge = ScepProfilesScepChallenge(
        dynamic=dynamic_settings
    )

    attributes = ScepProfilesCertificateAttributes(
        dnsname="device.example.com"
    )

    payload = ScepProfiles(
        folder=TARGET_FOLDER,
        name=profile_name,
        scep_url="https://scep.example.com/certsrv/mscep/mscep.dll",
        ca_identity_name="Example-Name",
        digest="sha256",
        subject="CN=$USERNAME",
        fingerprint="D14A028C2A3A2BC9476102BB288234C415A2B01F",
        algorithm=algorithm,
        scep_challenge=challenge,
        scep_ca_cert="Forward-Trust-CA",
        scep_client_cert="Forward-UnTrust-CA",
        certificate_attributes=attributes,
        use_as_digital_signature=True,
        use_for_key_encipherment=True
    )

    created_obj = perform(
        scep_profiles_api.create_scep_profiles_with_http_info,
        response_type=ScepProfiles,
        scep_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert created_obj.digest == "sha256"

    perform(
        scep_profiles_api.delete_scep_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_scep_profile_by_id(scep_profiles_api, clean_scep_profile):
    """Test retrieving a SCEP Profile by ID."""
    fetched_obj = perform(
        scep_profiles_api.get_scep_profiles_by_id_with_http_info,
        id=clean_scep_profile.id
    )

    assert fetched_obj.id == clean_scep_profile.id
    assert fetched_obj.name == clean_scep_profile.name
    assert fetched_obj.digest == "sha256"


def test_update_scep_profile(scep_profiles_api, clean_scep_profile):
    """Test updating a SCEP Profile."""
    update_payload = clean_scep_profile
    update_payload.digest = "sha512"
    update_payload.ca_identity_name = "Updated-CA"

    updated_obj = perform(
        scep_profiles_api.update_scep_profiles_by_id_with_http_info,
        id=clean_scep_profile.id,
        scep_profiles=update_payload
    )

    assert updated_obj.id == clean_scep_profile.id
    assert updated_obj.digest == "sha512"
    assert updated_obj.ca_identity_name == "Updated-CA"


def test_list_scep_profiles(scep_profiles_api, clean_scep_profile):
    """Test listing SCEP Profiles."""
    response = perform(
        scep_profiles_api.list_scep_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_scep_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_scep_profile.name} not found in list response"


def test_delete_scep_profile_by_id(scep_profiles_api):
    """Test deleting a SCEP Profile."""
    profile_name = f"scm-scep-delete-{uuid.uuid4().hex[:6]}"

    algorithm = ScepProfilesAlgorithm(
        rsa=ScepProfilesAlgorithmRsa(
            rsa_nbits="2048"
        )
    )

    challenge = ScepProfilesScepChallenge(
        fixed="mypassword123"
    )

    payload = ScepProfiles(
        folder=TARGET_FOLDER,
        name=profile_name,
        scep_url="https://scep.example.com/",
        ca_identity_name="Default",
        digest="sha256",
        subject="CN=$USERNAME",
        algorithm=algorithm,
        scep_challenge=challenge
    )

    created_obj = perform(
        scep_profiles_api.create_scep_profiles_with_http_info,
        response_type=ScepProfiles,
        scep_profiles=payload
    )

    perform(
        scep_profiles_api.delete_scep_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        scep_profiles_api.get_scep_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
