

import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.radius_server_profiles import RadiusServerProfiles
from scm.identity_services.models.radius_server_profiles_protocol import RadiusServerProfilesProtocol
from scm.identity_services.models.radius_server_profiles_server_inner import RadiusServerProfilesServerInner
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
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
def radius_profiles_api(client):
    """
    Fixture to return the RADIUS Server Profiles API instance.
    """
    return client.identity_services.RADIUSServerProfilesApi(client.identity_services.api_client)

@pytest.fixture
def clean_radius_profile(radius_profiles_api):
    """
    Fixture to create a temporary RADIUS Server Profile for testing and automatically delete it after.
    """
    # 1. SETUP
    server_inner = RadiusServerProfilesServerInner(
        name="radius-server-fixture",
        ip_address="10.1.1.1",
        secret="secret123",
        port=1812
    )
    protocol = RadiusServerProfilesProtocol(pap={})
    object_name = f"scm-radius-test-{uuid.uuid4().hex[:6]}"

    payload = RadiusServerProfiles(
        id="",
        name=object_name,
        protocol=protocol,
        server=[server_inner],
        retries=3,
        timeout=10,
        folder=TARGET_FOLDER
    )

    # Use _with_http_info to ensure we get the object back even on 201 Created
    created_obj = perform(
        radius_profiles_api.create_radius_server_profiles_with_http_info,
        radius_server_profiles=payload
    )

    assert created_obj is not None, "API returned None for creation!"
    assert created_obj.id is not None

    yield created_obj

    # 2. TEARDOWN
    logger.info(f"\n[TEARDOWN] Deleting RADIUS Profile ID: {created_obj.id}")
    try:
        perform(
            radius_profiles_api.delete_radius_server_profiles_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_radius_profile(radius_profiles_api):
    """
    Test manual creation and deletion of a RADIUS Server Profile with logging.
    """
    server_inner = RadiusServerProfilesServerInner(
        name="radius-server-manual",
        ip_address="10.2.2.2",
        secret="manualSecret",
        port=1812
    )
    protocol = RadiusServerProfilesProtocol(pap={})
    object_name = f"scm-radius-create-{uuid.uuid4().hex[:6]}"

    payload = RadiusServerProfiles(
        id="",
        name=object_name,
        protocol=protocol,
        server=[server_inner],
        retries=5,
        timeout=15,
        folder=TARGET_FOLDER
    )

    # Create with logging using _with_http_info
    created_obj = perform(
        radius_profiles_api.create_radius_server_profiles_with_http_info,
        radius_server_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.retries == 5

    # Cleanup with logging
    perform(
        radius_profiles_api.delete_radius_server_profiles_by_id,
        id=created_obj.id
    )


def test_get_radius_profile_by_id(radius_profiles_api, clean_radius_profile):
    """
    Test retrieving a RADIUS Server Profile by ID with logging.
    """
    fetched_obj = perform(
        radius_profiles_api.get_radius_server_profiles_by_id,
        id=clean_radius_profile.id
    )

    assert fetched_obj.id == clean_radius_profile.id
    assert fetched_obj.name == clean_radius_profile.name
    assert fetched_obj.timeout == clean_radius_profile.timeout


def test_update_radius_profile(radius_profiles_api, clean_radius_profile):
    """
    Test updating a RADIUS Server Profile with logging.
    """
    update_payload = clean_radius_profile
    update_payload.retries = 2
    update_payload.timeout = 60
    update_payload.folder = TARGET_FOLDER

    updated_obj = perform(
        radius_profiles_api.update_radius_server_profiles_by_id,
        id=clean_radius_profile.id,
        radius_server_profiles=update_payload
    )

    assert updated_obj.id == clean_radius_profile.id
    assert updated_obj.retries == 2
    assert updated_obj.timeout == 60


def test_list_radius_profiles(radius_profiles_api, clean_radius_profile):
    """
    Test listing RADIUS Server Profiles with logging.
    """
    response = perform(
        radius_profiles_api.list_radius_server_profiles,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0


def test_delete_radius_profile_by_id(radius_profiles_api):
    """
    Test deletion specifically with logging.
    """
    # Setup
    server_inner = RadiusServerProfilesServerInner(
        name="radius-server-del",
        ip_address="10.3.3.3",
        secret="delSecret",
        port=1812
    )
    protocol = RadiusServerProfilesProtocol(pap={})
    object_name = f"scm-radius-del-{uuid.uuid4().hex[:6]}"

    payload = RadiusServerProfiles(
        id="",
        name=object_name,
        protocol=protocol,
        server=[server_inner],
        folder=TARGET_FOLDER
    )

    # Use _with_http_info for setup as well
    created_obj = perform(
        radius_profiles_api.create_radius_server_profiles_with_http_info,
        radius_server_profiles=payload
    )

    # Perform Delete with logging
    perform(
        radius_profiles_api.delete_radius_server_profiles_by_id,
        id=created_obj.id
    )

    # Verify Deletion
    try:
        radius_profiles_api.get_radius_server_profiles_by_id(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
