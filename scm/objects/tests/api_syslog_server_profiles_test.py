
import logging
import uuid
import pytest
from scm import Scm

from scm.objects.models import (
    SyslogServerProfiles,
    SyslogServerProfilesServerInner,
    SyslogServerProfilesFormat,
    SyslogServerProfilesFormatEscaping
)

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
def syslog_profiles_api(client):
    """
    Fixture to return the Syslog Server Profiles API instance.
    """
    return client.objects.SyslogServerProfilesApi(client.objects.api_client)

@pytest.fixture
def clean_syslog_profile(syslog_profiles_api):
    """
    Fixture to create a MINIMAL temporary Syslog Server Profile for testing.
    Matches Go helper 'createTestSyslogProfile'.
    """
    # 1. SETUP: Create Syslog Profile (Minimal)
    random_id = uuid.uuid4().hex[:6]
    profile_name = f"test-syslog-{random_id}"
    
    # Minimal server list (No transport/port/facility/format)
    server_list = [
        SyslogServerProfilesServerInner(
            name="TestServer-Fixture",
            server="192.0.2.1"
        )
    ]

    payload = SyslogServerProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        server=server_list
    )
    
    logger.info(f"\n[SETUP] Creating Syslog Profile: {profile_name}")
    created_obj = syslog_profiles_api.create_syslog_server_profiles(syslog_server_profiles=payload)
    assert created_obj.id is not None
    
    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Syslog Profile
    logger.info(f"\n[TEARDOWN] Deleting Syslog Profile ID: {created_obj.id}")
    try:
        syslog_profiles_api.delete_syslog_server_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_syslog_profile(syslog_profiles_api):
    """
    Test manual creation and deletion of a COMPLEX Syslog Server Profile.
    Equivalent to Go: Test_objects_SyslogServerProfilesAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    profile_name = f"test-syslog-create-{random_suffix}"
    
    # 1. Define Server List (2 servers)
    server_list = [
        SyslogServerProfilesServerInner(
            name="Server-A",
            server="172.16.10.1",
            transport="UDP",
            port=514,
            format="BSD",
            facility="LOG_LOCAL7"
        ),
        SyslogServerProfilesServerInner(
            name="Server-B",
            server="172.16.10.2",
            transport="TCP",
            port=6514,
            format="IETF",
            facility="LOG_LOCAL3"
        )
    ]

    # 2. Define Format Object
    # Note: Escaped characters might need raw string r"" in Python
    format_config = SyslogServerProfilesFormat(
        escaping=SyslogServerProfilesFormatEscaping(
            escape_character="*",
            escaped_characters=r"&\#"
        ),
        traffic="$error + $errorcode",
        threat="$client_os",
        wildfire="default",
        url="$device_name and $contenttype",
        data="$status",
        gtp="dg_hier_level_4",
        sctp="$srcregion",
        tunnel="$tunnel_type",
        auth="$location",
        userid="$host_id",
        iptag="$vsys_name",
        decryption="default",
        config="custom",
        system="default",
        globalprotect="$type",
        hip_match="$actionflags",
        correlation="$error"
    )

    # 3. Create Payload
    payload = SyslogServerProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        server=server_list,
        format=format_config
    )

    # Create
    created_obj = syslog_profiles_api.create_syslog_server_profiles(syslog_server_profiles=payload)
    
    # Verify
    assert created_obj.name == profile_name
    assert created_obj.id is not None
    assert len(created_obj.server) == 2
    assert created_obj.format.traffic == "$error + $errorcode"
    
    # Cleanup
    syslog_profiles_api.delete_syslog_server_profiles_by_id(id=created_obj.id)


def test_get_syslog_profile_by_id(syslog_profiles_api, clean_syslog_profile):
    """
    Test retrieving a syslog server profile by ID.
    Equivalent to Go: Test_objects_SyslogServerProfilesAPIService_GetByID
    """
    # Retrieve
    fetched_obj = syslog_profiles_api.get_syslog_server_profiles_by_id(id=clean_syslog_profile.id)
    
    # Verify
    assert fetched_obj.id == clean_syslog_profile.id
    assert fetched_obj.name == clean_syslog_profile.name
    assert len(fetched_obj.server) == 1
    assert fetched_obj.server[0].name == "TestServer-Fixture"


def test_update_syslog_profile(syslog_profiles_api, clean_syslog_profile):
    """
    Test updating an existing syslog server profile.
    Equivalent to Go: Test_objects_SyslogServerProfilesAPIService_Update
    """
    # Prepare Update: Add a second server and update format
    update_payload = clean_syslog_profile
    
    # Add second server
    new_server = SyslogServerProfilesServerInner(
        name="TestServer-B",
        server="192.0.2.2",
        transport="TCP",
        port=601,
        format="IETF",
        facility="LOG_LOCAL7"
    )
    
    # Initialize list if None (though fixture provides one)
    if update_payload.server is None:
        update_payload.server = []
    update_payload.server.append(new_server)

    # Add/Update Format
    update_payload.format = SyslogServerProfilesFormat(
        traffic="default",
        threat="default",
        escaping=SyslogServerProfilesFormatEscaping(
            escape_character="\\",
            escaped_characters="&"
        )
    )

    # Perform Update
    updated_obj = syslog_profiles_api.update_syslog_server_profiles_by_id(
        id=clean_syslog_profile.id, 
        syslog_server_profiles=update_payload
    )
    
    # Verify
    assert updated_obj.id == clean_syslog_profile.id
    assert len(updated_obj.server) == 2
    assert updated_obj.format is not None
    assert updated_obj.format.escaping.escape_character == "\\"


def test_list_syslog_profiles(syslog_profiles_api, clean_syslog_profile):
    """
    Test listing syslog server profiles with folder filter.
    Equivalent to Go: Test_objects_SyslogServerProfilesAPIService_List
    """
    # List with filter
    response = syslog_profiles_api.list_syslog_server_profiles(folder=TARGET_FOLDER)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our specific object is in the list
    found = False
    for item in response.data:
        if item.id == clean_syslog_profile.id:
            found = True
            break
            
    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_delete_syslog_profile_by_id(syslog_profiles_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_SyslogServerProfilesAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    profile_name = f"test-syslog-del-{random_suffix}"
    
    # Minimal payload for delete test (matches Go helper createTestSyslogProfile)
    server_list = [
        SyslogServerProfilesServerInner(
            name="DeleteMeServer",
            server="1.1.1.1"
        )
    ]

    payload = SyslogServerProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        server=server_list
    )
    created_obj = syslog_profiles_api.create_syslog_server_profiles(syslog_server_profiles=payload)

    # Perform Delete
    syslog_profiles_api.delete_syslog_server_profiles_by_id(id=created_obj.id)

    # Verify Deletion (Expect 404 on Get)
    try:
        syslog_profiles_api.get_syslog_server_profiles_by_id(id=created_obj.id)
        pytest.fail("Syslog Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
