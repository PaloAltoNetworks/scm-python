import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.certificate_profiles import CertificateProfiles
from scm.identity_services.models.certificate_profiles_ca_certificates_inner import CertificateProfilesCaCertificatesInner
from scm.identity_services.models.certificate_profiles_username_field import CertificateProfilesUsernameField
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Shared"
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
def cert_profiles_api(client):
    """
    Fixture to return the Certificate Profiles API instance.
    """
    return client.identity_services.CertificateProfilesApi(client.identity_services.api_client)

@pytest.fixture
def clean_cert_profile(cert_profiles_api):
    """
    Fixture to create a temporary Certificate Profile for testing and automatically delete it after.
    """
    # Create a profile with all fields for comprehensive testing
    profile_name = f"test-cert-prof-{uuid.uuid4().hex[:6]}"

    ca_cert = CertificateProfilesCaCertificatesInner(
        name="Forward-Trust-CA",
        default_ocsp_url="http://test.com",
        ocsp_verify_cert="Forward-Trust-CA-ECDSA",
        template_name="something"
    )

    username_field = CertificateProfilesUsernameField(
        subject="common-name"
    )

    payload = CertificateProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        ca_certificates=[ca_cert],
        domain="test",
        use_crl=True,
        use_ocsp=True,
        block_unknown_cert=True,
        block_timeout_cert=True,
        block_unauthenticated_cert=True,
        block_expired_cert=True,
        username_field=username_field,
        crl_receive_timeout="5",
        ocsp_receive_timeout="5",
        cert_status_timeout="5"
    )

    logger.info(f"\n[SETUP] Creating Certificate Profile: {profile_name}")
    created_obj = perform(
        cert_profiles_api.create_certificate_profiles,
        certificate_profiles=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Certificate Profile ID: {created_obj.id}")
    try:
        perform(
            cert_profiles_api.delete_certificate_profiles_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_cert_profile(cert_profiles_api):
    """
    Test manual creation and deletion of a Certificate Profile with logging.
    Mirrors Test_identityservices_CertificateProfilesAPIService_Create
    """
    profile_name = f"test-cert-create-{uuid.uuid4().hex[:6]}"

    ca_cert = CertificateProfilesCaCertificatesInner(
        name="Forward-Trust-CA",
        default_ocsp_url="http://test.com",
        ocsp_verify_cert="Forward-Trust-CA-ECDSA",
        template_name="something"
    )

    username_field = CertificateProfilesUsernameField(
        subject="common-name"
    )

    payload = CertificateProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        ca_certificates=[ca_cert],
        domain="test",
        use_crl=True,
        use_ocsp=True,
        block_unknown_cert=True,
        block_timeout_cert=True,
        block_unauthenticated_cert=True,
        block_expired_cert=True,
        username_field=username_field,
        crl_receive_timeout="5",
        ocsp_receive_timeout="5",
        cert_status_timeout="5"
    )

    # Create with logging
    created_obj = perform(
        cert_profiles_api.create_certificate_profiles,
        certificate_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert created_obj.folder in ["Shared", "Prisma Access"]
    assert len(created_obj.ca_certificates) == 1
    assert created_obj.ca_certificates[0].name == "Forward-Trust-CA"
    assert created_obj.ca_certificates[0].default_ocsp_url == "http://test.com"
    assert created_obj.ca_certificates[0].ocsp_verify_cert == "Forward-Trust-CA-ECDSA"
    assert created_obj.ca_certificates[0].template_name == "something"
    assert created_obj.domain == "test"
    assert created_obj.use_crl == True
    assert created_obj.use_ocsp == True
    assert created_obj.block_unknown_cert == True
    assert created_obj.block_timeout_cert == True
    assert created_obj.block_unauthenticated_cert == True
    assert created_obj.block_expired_cert == True
    assert created_obj.username_field.subject == "common-name"
    assert created_obj.crl_receive_timeout == "5"
    assert created_obj.ocsp_receive_timeout == "5"
    assert created_obj.cert_status_timeout == "5"

    # Cleanup with logging
    perform(
        cert_profiles_api.delete_certificate_profiles_by_id,
        id=created_obj.id
    )


def test_get_cert_profile_by_id(cert_profiles_api, clean_cert_profile):
    """
    Test retrieving a Certificate Profile by ID with logging.
    Mirrors Test_identityservices_CertificateProfilesAPIService_GetByID
    """
    fetched_obj = perform(
        cert_profiles_api.get_certificate_profiles_by_id,
        id=clean_cert_profile.id
    )

    assert fetched_obj.id == clean_cert_profile.id
    assert fetched_obj.name == clean_cert_profile.name


def test_update_cert_profile(cert_profiles_api, clean_cert_profile):
    """
    Test updating a Certificate Profile with logging.
    Mirrors Test_identityservices_CertificateProfilesAPIService_Update
    """
    update_payload = clean_cert_profile
    update_payload.domain = "updated-domain"
    update_payload.crl_receive_timeout = "10"

    updated_obj = perform(
        cert_profiles_api.update_certificate_profiles_by_id,
        id=clean_cert_profile.id,
        certificate_profiles=update_payload
    )

    assert updated_obj.id == clean_cert_profile.id
    assert updated_obj.domain == "updated-domain"
    assert updated_obj.crl_receive_timeout == "10"


def test_list_cert_profiles(cert_profiles_api, clean_cert_profile):
    """
    Test listing Certificate Profiles with logging.
    Mirrors Test_identityservices_CertificateProfilesAPIService_List
    """
    response = perform(
        cert_profiles_api.list_certificate_profiles,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify the fixture object is in the list
    found = False
    for item in response.data:
        if item.id == clean_cert_profile.id:
            found = True
            break
    assert found is True, f"Created profile {clean_cert_profile.id} not found in list response"




def test_fetch_certificate_profiles(cert_profiles_api, clean_cert_profile):
    """
    Test fetching a single certificate_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = cert_profiles_api.fetch_certificate_profiles(
        name=clean_cert_profile.name,
        folder=clean_cert_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found certificate_profiles '{clean_cert_profile.name}'"
    assert fetched_obj.id == clean_cert_profile.id
    assert fetched_obj.name == clean_cert_profile.name
    assert fetched_obj.folder == clean_cert_profile.folder
    logger.info(f"\n[SUCCESS] fetch_certificate_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent certificate_profiles (should return None)
    not_found = cert_profiles_api.fetch_certificate_profiles(
        name="non-existent-certificate_profiles-xyz-12345",
        folder=clean_cert_profile.folder
    )
    assert not_found is None, "Should return None for non-existent certificate_profiles"
    logger.info(f"\n[SUCCESS] fetch_certificate_profiles correctly returned None for non-existent certificate_profiles")


def test_delete_cert_profile_by_id(cert_profiles_api):
    """
    Test deletion specifically with logging.
    Mirrors Test_identityservices_CertificateProfilesAPIService_DeleteByID
    """
    # Setup
    profile_name = f"test-cert-del-{uuid.uuid4().hex[:6]}"

    ca_cert = CertificateProfilesCaCertificatesInner(
        name="Forward-Trust-CA",
        default_ocsp_url="http://test.com",
        ocsp_verify_cert="Forward-Trust-CA-ECDSA",
        template_name="something"
    )

    payload = CertificateProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        ca_certificates=[ca_cert]
    )

    created_obj = perform(
        cert_profiles_api.create_certificate_profiles,
        certificate_profiles=payload
    )

    # Perform Delete with logging
    perform(
        cert_profiles_api.delete_certificate_profiles_by_id,
        id=created_obj.id
    )

    # Verify Deletion
    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        cert_profiles_api.get_certificate_profiles_by_id(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
