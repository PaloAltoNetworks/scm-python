import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.lldp_profiles import LldpProfiles
from scm.network_services.models.lldp_profiles_option_tlvs import LldpProfilesOptionTlvs
from scm.network_services.models.lldp_profiles_option_tlvs_management_address import LldpProfilesOptionTlvsManagementAddress
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
def lldp_profiles_api(client):
    return client.network_services.LLDPProfilesApi(client.network_services.api_client)


@pytest.fixture
def clean_lldp_profile(lldp_profiles_api):
    """
    Setup/Teardown for a simple LLDP profile.
    """
    profile_name = f"test-lldp-{uuid.uuid4().hex[:6]}"

    payload = LldpProfiles(
        name=profile_name,
        folder=TARGET_FOLDER
    )

    logger.info(f"\n[SETUP] Creating LLDP Profile: {profile_name}")
    created_profile = perform(
        lldp_profiles_api.create_lldp_profiles_with_http_info,
        response_type=LldpProfiles,
        lldp_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting LLDP Profile: {created_profile.id}")
    try:
        perform(
            lldp_profiles_api.delete_lldp_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup LLDP profile: {e}")


def test_create_lldp_profile(lldp_profiles_api):
    """Test creation of a complete LLDP Profile."""
    profile_name = f"test-lldp-create-{uuid.uuid4().hex[:6]}"

    option_tlvs = LldpProfilesOptionTlvs(
        port_description=False,
        system_name=True,
        system_description=False,
        system_capabilities=True,
        management_address=LldpProfilesOptionTlvsManagementAddress(
            enabled=False
        )
    )

    payload = LldpProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        mode="transmit-receive",
        snmp_syslog_notification=True,
        option_tlvs=option_tlvs
    )

    created_obj = perform(
        lldp_profiles_api.create_lldp_profiles_with_http_info,
        response_type=LldpProfiles,
        lldp_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert created_obj.mode == "transmit-receive"
    assert created_obj.snmp_syslog_notification is True

    perform(
        lldp_profiles_api.delete_lldp_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_lldp_profile_by_id(lldp_profiles_api, clean_lldp_profile):
    """Test retrieving an LLDP Profile by ID."""
    fetched_obj = perform(
        lldp_profiles_api.get_lldp_profiles_by_id_with_http_info,
        id=clean_lldp_profile.id
    )

    assert fetched_obj.id == clean_lldp_profile.id
    assert fetched_obj.name == clean_lldp_profile.name


def test_update_lldp_profile(lldp_profiles_api, clean_lldp_profile):
    """Test updating an LLDP Profile."""
    update_payload = clean_lldp_profile
    update_payload.mode = "transmit-receive"
    update_payload.snmp_syslog_notification = True
    update_payload.option_tlvs = LldpProfilesOptionTlvs(
        port_description=True,
        system_name=False,
        system_description=False,
        system_capabilities=True,
        management_address=LldpProfilesOptionTlvsManagementAddress(
            enabled=False
        )
    )

    updated_obj = perform(
        lldp_profiles_api.update_lldp_profiles_by_id_with_http_info,
        id=clean_lldp_profile.id,
        lldp_profiles=update_payload
    )

    assert updated_obj.id == clean_lldp_profile.id
    assert updated_obj.option_tlvs.system_name is False
    assert updated_obj.option_tlvs.port_description is True


def test_list_lldp_profiles(lldp_profiles_api, clean_lldp_profile):
    """Test listing LLDP Profiles."""
    response = perform(
        lldp_profiles_api.list_lldp_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_lldp_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_lldp_profile.name} not found in list response"




def test_fetch_lldp_profiles(lldp_profiles_api, clean_lldp_profile):
    """
    Test fetching a single lldp_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = lldp_profiles_api.fetch_lldp_profiles(
        name=clean_lldp_profile.name,
        folder=clean_lldp_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found lldp_profiles '{clean_lldp_profile.name}'"
    assert fetched_obj.id == clean_lldp_profile.id
    assert fetched_obj.name == clean_lldp_profile.name
    assert fetched_obj.folder == clean_lldp_profile.folder
    logger.info(f"\n[SUCCESS] fetch_lldp_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent lldp_profiles (should return None)
    not_found = lldp_profiles_api.fetch_lldp_profiles(
        name="non-existent-lldp_profiles-xyz-12345",
        folder=clean_lldp_profile.folder
    )
    assert not_found is None, "Should return None for non-existent lldp_profiles"
    logger.info(f"\n[SUCCESS] fetch_lldp_profiles correctly returned None for non-existent lldp_profiles")


def test_delete_lldp_profile_by_id(lldp_profiles_api):
    """Test deleting an LLDP Profile."""
    profile_name = f"test-lldp-delete-{uuid.uuid4().hex[:6]}"

    payload = LldpProfiles(
        name=profile_name,
        folder=TARGET_FOLDER
    )

    created_obj = perform(
        lldp_profiles_api.create_lldp_profiles_with_http_info,
        response_type=LldpProfiles,
        lldp_profiles=payload
    )

    perform(
        lldp_profiles_api.delete_lldp_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        lldp_profiles_api.get_lldp_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
