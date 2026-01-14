import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.tls_service_profiles import TlsServiceProfiles
from scm.identity_services.models.tls_service_profiles_protocol_settings import TlsServiceProfilesProtocolSettings
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
def tls_profiles_api(client):
    return client.identity_services.TLSServiceProfilesApi(client.identity_services.api_client)

@pytest.fixture
def clean_tls_profile(tls_profiles_api):
    profile_name = f"test-tls-prof-{uuid.uuid4().hex[:6]}"

    protocol_settings = TlsServiceProfilesProtocolSettings(
        min_version="tls1-1",  # Explicitly set to valid enum value
        max_version="tls1-3",  # Explicitly set to valid enum value
        keyxchg_algo_rsa=True,
        keyxchg_algo_ecdhe=True,
        keyxchg_algo_dhe=True,
        enc_algo_aes_128_gcm=True,
        enc_algo_aes_256_gcm=True,
        enc_algo_aes_256_cbc=True,
        auth_algo_sha256=True
    )

    payload = TlsServiceProfiles(
        id="",  # Workaround: id incorrectly marked as required in model
        name=profile_name,
        folder=TARGET_FOLDER,
        certificate="Forward-Trust-CA",
        protocol_settings=protocol_settings
    )

    logger.info(f"\n[SETUP] Creating TLS Service Profile: {profile_name}")
    created_obj = perform(
        tls_profiles_api.create_tls_service_profiles_with_http_info,
        tls_service_profiles=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting TLS Service Profile ID: {created_obj.id}")
    try:
        perform(
            tls_profiles_api.delete_tls_service_profiles_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_tls_profile(tls_profiles_api):
    profile_name = f"test-tls-create-{uuid.uuid4().hex[:6]}"

    protocol_settings = TlsServiceProfilesProtocolSettings(
        keyxchg_algo_rsa=True,
        min_version=None,  # Workaround: auto-generated model has invalid defaults '2' and '3'
        max_version=None   # See CLAUDE_README.md for details
    )

    payload = TlsServiceProfiles(
        id="",  # Workaround: id incorrectly marked as required in model
        name=profile_name,
        folder=TARGET_FOLDER,
        certificate="Forward-UnTrust-CA",
        protocol_settings=protocol_settings
    )

    created_obj = perform(
        tls_profiles_api.create_tls_service_profiles_with_http_info,
        tls_service_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name

    perform(
        tls_profiles_api.delete_tls_service_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_tls_profile_by_id(tls_profiles_api, clean_tls_profile):
    fetched_obj = perform(
        tls_profiles_api.get_tls_service_profiles_by_id_with_http_info,
        id=clean_tls_profile.id
    )

    assert fetched_obj.id == clean_tls_profile.id
    assert fetched_obj.name == clean_tls_profile.name


def test_update_tls_profile(tls_profiles_api, clean_tls_profile):
    update_payload = clean_tls_profile
    update_payload.protocol_settings.min_version = "tls1-0"
    update_payload.protocol_settings.max_version = "tls1-2"

    updated_obj = perform(
        tls_profiles_api.update_tls_service_profiles_by_id_with_http_info,
        id=clean_tls_profile.id,
        tls_service_profiles=update_payload
    )

    assert updated_obj.id == clean_tls_profile.id
    assert updated_obj.protocol_settings.min_version == "tls1-0"
    assert updated_obj.protocol_settings.max_version == "tls1-2"


def test_list_tls_profiles(tls_profiles_api, clean_tls_profile):
    response = perform(
        tls_profiles_api.list_tls_service_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_tls_profile.id:
            found = True
            break
    assert found is True, f"Created profile {clean_tls_profile.id} not found in list response"


def test_delete_tls_profile_by_id(tls_profiles_api):
    profile_name = f"test-tls-del-{uuid.uuid4().hex[:6]}"

    protocol_settings = TlsServiceProfilesProtocolSettings(
        keyxchg_algo_rsa=True,
        min_version=None,  # Workaround: auto-generated model has invalid defaults '2' and '3'
        max_version=None   # See CLAUDE_README.md for details
    )

    payload = TlsServiceProfiles(
        id="",  # Workaround: id incorrectly marked as required in model
        name=profile_name,
        folder=TARGET_FOLDER,
        certificate="Forward-UnTrust-CA",
        protocol_settings=protocol_settings
    )

    created_obj = perform(
        tls_profiles_api.create_tls_service_profiles_with_http_info,
        tls_service_profiles=payload
    )

    perform(
        tls_profiles_api.delete_tls_service_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        tls_profiles_api.get_tls_service_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
