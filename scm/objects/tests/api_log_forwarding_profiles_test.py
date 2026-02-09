import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.log_forwarding_profiles import LogForwardingProfiles
from scm.objects.models.log_forwarding_profiles_match_list_inner import LogForwardingProfilesMatchListInner
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
def log_forwarding_profiles_api(client):
    return client.objects.LogForwardingProfilesApi(client.objects.api_client)


@pytest.fixture
def clean_log_forwarding_profile(log_forwarding_profiles_api):
    """
    Setup/Teardown for a simple Log Forwarding Profile.
    """
    profile_name = f"test-log-fwd-get-{uuid.uuid4().hex[:5]}"

    match_list = [
        LogForwardingProfilesMatchListInner(
            name="profile-match",
            log_type="auth",
            filter="All Logs"
        )
    ]

    payload = LogForwardingProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        match_list=match_list
    )

    logger.info(f"\n[SETUP] Creating Log Forwarding Profile: {profile_name}")
    created_profile = perform(
        log_forwarding_profiles_api.create_log_forwarding_profiles_with_http_info,
        response_type=LogForwardingProfiles,
        log_forwarding_profiles=payload
    )

    yield created_profile

    logger.info(f"\n[TEARDOWN] Deleting Log Forwarding Profile: {created_profile.id}")
    try:
        perform(
            log_forwarding_profiles_api.delete_log_forwarding_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup log forwarding profile: {e}")


def test_create_log_forwarding_profile(log_forwarding_profiles_api):
    """Test creation of a complex Log Forwarding Profile."""
    profile_name = f"test-log-fwd-create-{uuid.uuid4().hex[:5]}"

    match_list = [
        LogForwardingProfilesMatchListInner(
            name="profile-match-1",
            action_desc="profile match for tunnel",
            log_type="tunnel",
            filter="(tunnelid neq 123) or (zone.dst eq 192.5.125.155)",
            send_syslog=["syslog-server-prof-mixed"],
            send_http=["test_http"]
        ),
        LogForwardingProfilesMatchListInner(
            name="profile-match-2",
            action_desc="profile match w/ snmp and email",
            log_type="decryption",
            filter="(addr.src in 10.0.0.0/8)",
            send_snmptrap=["snmp_test"],
            send_email=["email_test", "email_test_2"]
        ),
        LogForwardingProfilesMatchListInner(
            name="profile-match-3",
            action_desc="profile match w/ all server profiles",
            log_type="traffic",
            filter="(device_name eq test_device)",
            send_syslog=["syslog-server-prof-mixed", "syslog-server-prof-complete"],
            send_http=["test_http", "t10", "t5"],
            send_snmptrap=["snmp_test"],
            send_email=["email_test", "email_test_2"]
        )
    ]

    payload = LogForwardingProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        description="Log Forwarding w/ Multiple Match Lists",
        match_list=match_list
    )

    created_obj = perform(
        log_forwarding_profiles_api.create_log_forwarding_profiles_with_http_info,
        response_type=LogForwardingProfiles,
        log_forwarding_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == profile_name
    assert len(created_obj.match_list) == 3

    perform(
        log_forwarding_profiles_api.delete_log_forwarding_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_log_forwarding_profile_by_id(log_forwarding_profiles_api, clean_log_forwarding_profile):
    """Test retrieving a Log Forwarding Profile by ID."""
    fetched_obj = perform(
        log_forwarding_profiles_api.get_log_forwarding_profiles_by_id_with_http_info,
        id=clean_log_forwarding_profile.id
    )

    assert fetched_obj.id == clean_log_forwarding_profile.id
    assert fetched_obj.name == clean_log_forwarding_profile.name
    assert len(fetched_obj.match_list) == 1


def test_update_log_forwarding_profile(log_forwarding_profiles_api, clean_log_forwarding_profile):
    """Test updating a Log Forwarding Profile."""
    update_payload = clean_log_forwarding_profile
    update_payload.description = "Updated Description"
    update_payload.match_list.append(
        LogForwardingProfilesMatchListInner(
            name="added-match-during-update",
            log_type="wildfire",
            filter="(imei contains test_server)",
            send_http=["t20"]
        )
    )

    updated_obj = perform(
        log_forwarding_profiles_api.update_log_forwarding_profiles_by_id_with_http_info,
        id=clean_log_forwarding_profile.id,
        log_forwarding_profiles=update_payload
    )

    assert updated_obj.id == clean_log_forwarding_profile.id
    assert len(updated_obj.match_list) == 2
    assert updated_obj.description == "Updated Description"


def test_list_log_forwarding_profiles(log_forwarding_profiles_api, clean_log_forwarding_profile):
    """Test listing Log Forwarding Profiles."""
    response = perform(
        log_forwarding_profiles_api.list_log_forwarding_profiles_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_log_forwarding_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_log_forwarding_profile.name} not found in list response"




def test_fetch_log_forwarding_profiles(log_forwarding_profiles_api, clean_log_forwarding_profile):
    """
    Test fetching a single log_forwarding_profiles by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = log_forwarding_profiles_api.fetch_log_forwarding_profiles(
        name=clean_log_forwarding_profile.name,
        folder=clean_log_forwarding_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found log_forwarding_profiles '{clean_log_forwarding_profile.name}'"
    assert fetched_obj.id == clean_log_forwarding_profile.id
    assert fetched_obj.name == clean_log_forwarding_profile.name
    assert fetched_obj.folder == clean_log_forwarding_profile.folder
    logger.info(f"\n[SUCCESS] fetch_log_forwarding_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent log_forwarding_profiles (should return None)
    not_found = log_forwarding_profiles_api.fetch_log_forwarding_profiles(
        name="non-existent-log_forwarding_profiles-xyz-12345",
        folder=clean_log_forwarding_profile.folder
    )
    assert not_found is None, "Should return None for non-existent log_forwarding_profiles"
    logger.info(f"\n[SUCCESS] fetch_log_forwarding_profiles correctly returned None for non-existent log_forwarding_profiles")


def test_delete_log_forwarding_profile_by_id(log_forwarding_profiles_api):
    """Test deleting a Log Forwarding Profile."""
    profile_name = f"test-log-fwd-delete-{uuid.uuid4().hex[:5]}"

    match_list = [
        LogForwardingProfilesMatchListInner(
            name="profile-match",
            log_type="auth",
            filter="All Logs"
        )
    ]

    payload = LogForwardingProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        match_list=match_list
    )

    created_obj = perform(
        log_forwarding_profiles_api.create_log_forwarding_profiles_with_http_info,
        response_type=LogForwardingProfiles,
        log_forwarding_profiles=payload
    )

    perform(
        log_forwarding_profiles_api.delete_log_forwarding_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.objects.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        log_forwarding_profiles_api.get_log_forwarding_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
