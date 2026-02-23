
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.http_server_profiles import HttpServerProfiles
from scm.objects.models.http_server_profiles_server_inner import HttpServerProfilesServerInner
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Prisma Access"
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
def http_server_profiles_api(client):
    """
    Fixture to return the HTTP Server Profiles API instance.
    """
    return client.objects.HTTPServerProfilesApi(client.objects.api_client)


@pytest.fixture
def clean_http_server_profile(http_server_profiles_api):
    """
    Fixture to create a temporary HTTP Server Profile for testing and automatically delete it after.
    """
    # 1. SETUP: Create HTTP Server Profile
    random_id = uuid.uuid4().hex[:6]
    profile_name = f"test-http-srv-{random_id}"

    server_list = [
        HttpServerProfilesServerInner(
            name="test-server-1",
            address="192.0.2.1",
            port=443,
            protocol="HTTPS",
            http_method="GET",
        )
    ]

    payload = HttpServerProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        server=server_list,
    )

    logger.info(f"\n[SETUP] Creating HTTP Server Profile: {profile_name}")
    created_obj = perform(
        http_server_profiles_api.create_http_server_profiles_with_http_info,
        response_type=HttpServerProfiles,
        http_server_profiles=payload,
    )
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete HTTP Server Profile
    logger.info(f"\n[TEARDOWN] Deleting HTTP Server Profile ID: {created_obj.id}")
    try:
        perform(
            http_server_profiles_api.delete_http_server_profiles_by_id,
            id=created_obj.id,
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_http_server_profile(http_server_profiles_api):
    """
    Test manual creation and deletion of an HTTP server profile.
    Equivalent to Go: Test_objects_HTTPServerProfilesAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    profile_name = f"test-http-srv-create-{random_suffix}"

    server_list = [
        HttpServerProfilesServerInner(
            name="test-server-1",
            address="192.0.2.1",
            port=443,
            protocol="HTTPS",
            http_method="GET",
        )
    ]

    payload = HttpServerProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        server=server_list,
    )

    # Create using perform helper
    created_obj = perform(
        http_server_profiles_api.create_http_server_profiles_with_http_info,
        response_type=HttpServerProfiles,
        http_server_profiles=payload,
    )

    # Verify
    assert created_obj.name == profile_name
    assert created_obj.id is not None
    assert created_obj.server is not None
    assert len(created_obj.server) > 0
    assert created_obj.server[0].address == "192.0.2.1"
    assert created_obj.server[0].port == 443
    assert created_obj.folder == TARGET_FOLDER or created_obj.folder == "Shared"

    # Cleanup
    perform(
        http_server_profiles_api.delete_http_server_profiles_by_id,
        id=created_obj.id,
    )


def test_get_http_server_profile_by_id(http_server_profiles_api, clean_http_server_profile):
    """
    Test retrieving an HTTP server profile by ID.
    Equivalent to Go: Test_objects_HTTPServerProfilesAPIService_GetByID
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        http_server_profiles_api.get_http_server_profiles_by_id,
        response_type=HttpServerProfiles,
        id=clean_http_server_profile.id,
    )

    # Verify
    assert fetched_obj.id == clean_http_server_profile.id
    assert fetched_obj.name == clean_http_server_profile.name


def test_update_http_server_profile(http_server_profiles_api, clean_http_server_profile):
    """
    Test updating an existing HTTP server profile.
    Equivalent to Go: Test_objects_HTTPServerProfilesAPIService_Update
    """
    # Prepare Update Payload with different server configuration
    updated_server = HttpServerProfilesServerInner(
        name="test-server-1",
        address="192.0.2.2",
        port=8443,
        protocol="HTTPS",
        http_method="POST",
    )

    update_payload = HttpServerProfiles(
        id=clean_http_server_profile.id,
        name=clean_http_server_profile.name,
        folder=TARGET_FOLDER,
        server=[updated_server],
    )

    # Perform Update using helper
    updated_obj = perform(
        http_server_profiles_api.update_http_server_profiles_by_id,
        response_type=HttpServerProfiles,
        id=clean_http_server_profile.id,
        http_server_profiles=update_payload,
    )

    # Verify
    assert updated_obj.id == clean_http_server_profile.id
    if updated_obj.server and len(updated_obj.server) > 0:
        assert updated_obj.server[0].address == "192.0.2.2"
        assert updated_obj.server[0].port == 8443
        assert updated_obj.server[0].http_method == "POST"


def test_list_http_server_profiles(http_server_profiles_api, clean_http_server_profile):
    """
    Test listing HTTP server profiles with folder filter.
    Equivalent to Go: Test_objects_HTTPServerProfilesAPIService_List
    """
    # List with filter using helper
    response = perform(
        http_server_profiles_api.list_http_server_profiles,
        folder=TARGET_FOLDER,
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.id == clean_http_server_profile.id:
            found = True
            assert item.name == clean_http_server_profile.name
            break

    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_fetch_http_server_profiles(http_server_profiles_api, clean_http_server_profile):
    """
    Test fetching a single http_server_profiles by name using the fetch convenience method.
    Equivalent to Go: Test_objects_HTTPServerProfilesAPIService_FetchHTTPServerProfiles
    """
    # Fetch by exact name
    fetched_obj = http_server_profiles_api.fetch_http_server_profiles(
        name=clean_http_server_profile.name,
        folder=clean_http_server_profile.folder,
    )

    # Verify
    assert fetched_obj is not None, f"Should have found http_server_profiles '{clean_http_server_profile.name}'"
    assert fetched_obj.id == clean_http_server_profile.id
    assert fetched_obj.name == clean_http_server_profile.name
    logger.info(f"\n[SUCCESS] fetch_http_server_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent http_server_profiles (should return None)
    not_found = http_server_profiles_api.fetch_http_server_profiles(
        name="non-existent-http-server-profiles-xyz-12345",
        folder=clean_http_server_profile.folder,
    )
    assert not_found is None, "Should return None for non-existent http_server_profiles"
    logger.info(f"\n[SUCCESS] fetch_http_server_profiles correctly returned None for non-existent http_server_profiles")


def test_delete_http_server_profile_by_id(http_server_profiles_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_HTTPServerProfilesAPIService_DeleteByID
    """
    from scm.exceptions import ObjectNotPresentError

    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    profile_name = f"test-http-srv-delete-{random_suffix}"

    server_list = [
        HttpServerProfilesServerInner(
            name="test-server-1",
            address="192.0.2.1",
            port=443,
            protocol="HTTPS",
            http_method="GET",
        )
    ]

    payload = HttpServerProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        server=server_list,
    )

    created_obj = perform(
        http_server_profiles_api.create_http_server_profiles_with_http_info,
        response_type=HttpServerProfiles,
        http_server_profiles=payload,
    )

    # Perform Delete using helper
    perform(
        http_server_profiles_api.delete_http_server_profiles_by_id,
        id=created_obj.id,
    )

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    try:
        http_server_profiles_api.get_http_server_profiles_by_id(id=created_obj.id)
        pytest.fail("HTTP Server Profile should have been deleted but was found.")
    except ObjectNotPresentError:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
