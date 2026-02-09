import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.saml_server_profiles import SamlServerProfiles
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
def saml_profiles_api(client):
    return client.identity_services.SAMLServerProfilesApi(client.identity_services.api_client)

@pytest.fixture
def clean_saml_profile(saml_profiles_api):
    profile_name = f"test-saml-prof-{uuid.uuid4().hex[:6]}"

    payload = SamlServerProfiles(
        id="",  # Workaround: id incorrectly marked as required in model
        name=profile_name,
        folder=TARGET_FOLDER,
        certificate="Global Authentication Cookie Cert",
        entity_id="https://idp.example.com/entity",
        sso_url="https://idp.example.com/sso",
        sso_bindings="redirect"
    )

    logger.info(f"\n[SETUP] Creating SAML Server Profile: {profile_name}")
    created_obj = perform(
        saml_profiles_api.create_saml_server_profiles_with_http_info,
        response_type=SamlServerProfiles,
        saml_server_profiles=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting SAML Server Profile ID: {created_obj.id}")
    try:
        perform(
            saml_profiles_api.delete_saml_server_profiles_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_saml_profile(saml_profiles_api):
    profile_name = f"test-saml-create-{uuid.uuid4().hex[:6]}"

    payload = SamlServerProfiles(
        id="",  # Workaround: id incorrectly marked as required in model
        name=profile_name,
        folder=TARGET_FOLDER,
        certificate="Global Authentication Cookie Cert",
        entity_id="https://idp.complex.com/entity",
        sso_url="https://idp.complex.com/sso",
        sso_bindings="post",
        slo_url="https://idp.complex.com/slo",
        slo_bindings="redirect",
        max_clock_skew=180,
        validate_idp_certificate=False,
        want_auth_requests_signed=True
    )

    created_obj = perform(
        saml_profiles_api.create_saml_server_profiles_with_http_info,
        response_type=SamlServerProfiles,
        saml_server_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name

    perform(
        saml_profiles_api.delete_saml_server_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_saml_profile_by_id(saml_profiles_api, clean_saml_profile):
    fetched_obj = perform(
        saml_profiles_api.get_saml_server_profiles_by_id_with_http_info,
        id=clean_saml_profile.id
    )

    assert fetched_obj.id == clean_saml_profile.id
    assert fetched_obj.name == clean_saml_profile.name


def test_update_saml_profile(saml_profiles_api, clean_saml_profile):
    update_payload = clean_saml_profile
    update_payload.sso_url = "https://idp.updated.com/sso"
    update_payload.max_clock_skew = 500

    updated_obj = perform(
        saml_profiles_api.update_saml_server_profiles_by_id_with_http_info,
        id=clean_saml_profile.id,
        saml_server_profiles=update_payload
    )

    assert updated_obj.id == clean_saml_profile.id
    assert updated_obj.sso_url == "https://idp.updated.com/sso"
    assert updated_obj.max_clock_skew == 500


def test_list_saml_profiles(saml_profiles_api, clean_saml_profile):
    response = perform(
        saml_profiles_api.list_saml_server_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_saml_profile.id:
            found = True
            break
    assert found is True, f"Created profile {clean_saml_profile.id} not found in list response"




def test_fetch_saml_server_profiles(saml_profiles_api, clean_saml_profile):
    """
    Test fetching a single saml_server_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = saml_profiles_api.fetch_saml_server_profiles(
        name=clean_saml_profile.name,
        folder=clean_saml_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found saml_server_profiles '{clean_saml_profile.name}'"
    assert fetched_obj.id == clean_saml_profile.id
    assert fetched_obj.name == clean_saml_profile.name
    assert fetched_obj.folder == clean_saml_profile.folder
    logger.info(f"\n[SUCCESS] fetch_saml_server_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent saml_server_profiles (should return None)
    not_found = saml_profiles_api.fetch_saml_server_profiles(
        name="non-existent-saml_server_profiles-xyz-12345",
        folder=clean_saml_profile.folder
    )
    assert not_found is None, "Should return None for non-existent saml_server_profiles"
    logger.info(f"\n[SUCCESS] fetch_saml_server_profiles correctly returned None for non-existent saml_server_profiles")


def test_delete_saml_profile_by_id(saml_profiles_api):
    profile_name = f"test-saml-del-{uuid.uuid4().hex[:6]}"

    payload = SamlServerProfiles(
        id="",  # Workaround: id incorrectly marked as required in model
        name=profile_name,
        folder=TARGET_FOLDER,
        certificate="Global Authentication Cookie Cert",
        entity_id="https://idp.example.com/entity",
        sso_url="https://idp.example.com/sso",
        sso_bindings="redirect"
    )

    created_obj = perform(
        saml_profiles_api.create_saml_server_profiles_with_http_info,
        response_type=SamlServerProfiles,
        saml_server_profiles=payload
    )

    perform(
        saml_profiles_api.delete_saml_server_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        saml_profiles_api.get_saml_server_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
