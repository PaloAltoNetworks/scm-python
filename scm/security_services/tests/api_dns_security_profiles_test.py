import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.dns_security_profiles import DnsSecurityProfiles
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
def dns_security_profiles_api(client):
    return client.security_services.DNSSecurityProfilesApi(client.security_services.api_client)


@pytest.fixture
def clean_dns_security_profile(dns_security_profiles_api):
    """
    Setup/Teardown for a simple DNS Security Profile.
    """
    profile_name = f"scm-dns-{uuid.uuid4().hex[:6]}"

    payload = DnsSecurityProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    logger.info(f"\n[SETUP] Creating DNS Security Profile: {profile_name}")
    created_profile = perform(
        dns_security_profiles_api.create_dns_security_profiles_with_http_info,
        response_type=DnsSecurityProfiles,
        dns_security_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting DNS Security Profile: {created_profile.id}")
    try:
        perform(
            dns_security_profiles_api.delete_dns_security_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup DNS Security Profile: {e}")


def test_create_dns_security_profile(dns_security_profiles_api):
    """Test creation of a DNS Security Profile."""
    profile_name = f"scm-dns-create-{uuid.uuid4().hex[:6]}"

    payload = DnsSecurityProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        dns_security_profiles_api.create_dns_security_profiles_with_http_info,
        response_type=DnsSecurityProfiles,
        dns_security_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name

    perform(
        dns_security_profiles_api.delete_dns_security_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_dns_security_profile_by_id(dns_security_profiles_api, clean_dns_security_profile):
    """Test retrieving a DNS Security Profile by ID."""
    fetched_obj = perform(
        dns_security_profiles_api.get_dns_security_profiles_by_id_with_http_info,
        id=clean_dns_security_profile.id
    )

    assert fetched_obj.id == clean_dns_security_profile.id
    assert fetched_obj.name == clean_dns_security_profile.name


def test_update_dns_security_profile(dns_security_profiles_api, clean_dns_security_profile):
    """Test updating a DNS Security Profile."""
    update_payload = clean_dns_security_profile
    update_payload.description = "Updated description"

    updated_obj = perform(
        dns_security_profiles_api.update_dns_security_profiles_by_id_with_http_info,
        id=clean_dns_security_profile.id,
        dns_security_profiles=update_payload
    )

    assert updated_obj.id == clean_dns_security_profile.id
    assert updated_obj.description == "Updated description"


def test_list_dns_security_profiles(dns_security_profiles_api, clean_dns_security_profile):
    """Test listing DNS Security Profiles."""
    response = perform(
        dns_security_profiles_api.list_dns_security_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_dns_security_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_dns_security_profile.name} not found in list response"




def test_fetch_dns_security_profiles(dns_security_profiles_api, clean_dns_security_profile):
    """
    Test fetching a single dns_security_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = dns_security_profiles_api.fetch_dns_security_profiles(
        name=clean_dns_security_profile.name,
        folder=clean_dns_security_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found dns_security_profiles '{clean_dns_security_profile.name}'"
    assert fetched_obj.id == clean_dns_security_profile.id
    assert fetched_obj.name == clean_dns_security_profile.name
    assert fetched_obj.folder == clean_dns_security_profile.folder
    logger.info(f"\n[SUCCESS] fetch_dns_security_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent dns_security_profiles (should return None)
    not_found = dns_security_profiles_api.fetch_dns_security_profiles(
        name="non-existent-dns_security_profiles-xyz-12345",
        folder=clean_dns_security_profile.folder
    )
    assert not_found is None, "Should return None for non-existent dns_security_profiles"
    logger.info(f"\n[SUCCESS] fetch_dns_security_profiles correctly returned None for non-existent dns_security_profiles")


def test_delete_dns_security_profile_by_id(dns_security_profiles_api):
    """Test deleting a DNS Security Profile."""
    profile_name = f"scm-dns-delete-{uuid.uuid4().hex[:6]}"

    payload = DnsSecurityProfiles(
        id="",
        folder=TARGET_FOLDER,
        name=profile_name
    )

    created_obj = perform(
        dns_security_profiles_api.create_dns_security_profiles_with_http_info,
        response_type=DnsSecurityProfiles,
        dns_security_profiles=payload
    )

    perform(
        dns_security_profiles_api.delete_dns_security_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        dns_security_profiles_api.get_dns_security_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
