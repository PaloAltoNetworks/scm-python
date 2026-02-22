import logging
import uuid
import pytest
from scm import Scm
from scm.identity_services.models.tacacs_server_profiles import TacacsServerProfiles
from scm.identity_services.models.tacacs_server_profiles_server_inner import TacacsServerProfilesServerInner
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
    """
    Fixture to initialize the SCM client once for the module.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def tacacs_profiles_api(client):
    """
    Fixture to return the TACACS Server Profiles API instance.
    """
    return client.identity_services.TACACSServerProfilesApi(client.identity_services.api_client)


@pytest.fixture
def clean_tacacs_profile(tacacs_profiles_api):
    """
    Fixture to create a temporary TACACS Server Profile for testing and automatically delete it after.
    """
    object_name = f"test-tacacs-{uuid.uuid4().hex[:6]}"

    server = TacacsServerProfilesServerInner(
        name="tacacs-server-fixture",
        address="200.5.5.100",
        port=20,
        secret="a"
    )

    payload = TacacsServerProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        protocol="CHAP",
        server=[server],
        timeout=15,
        use_single_connection=True
    )

    logger.info(f"\n[SETUP] Creating TACACS Server Profile: {object_name}")
    created_obj = perform(
        tacacs_profiles_api.create_tacacs_server_profiles_with_http_info,
        response_type=TacacsServerProfiles,
        tacacs_server_profiles=payload
    )

    assert created_obj is not None, "API returned None for creation!"
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting TACACS Server Profile ID: {created_obj.id}")
    try:
        perform(
            tacacs_profiles_api.delete_tacacs_server_profiles_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_tacacs_profile(tacacs_profiles_api):
    """
    Test manual creation and deletion of a TACACS Server Profile with logging.
    Mirrors Test_identity_services_TACACSServerProfilesAPIService_Create
    """
    object_name = f"test-tacacs-create-{uuid.uuid4().hex[:6]}"

    servers = [
        TacacsServerProfilesServerInner(
            name="tacacs-server-1",
            address="200.5.5.100",
            port=20,
            secret="a"
        ),
        TacacsServerProfilesServerInner(
            name="tacacs-server-2",
            address="100.2.120.50",
            port=1255,
            secret="secret"
        ),
        TacacsServerProfilesServerInner(
            name="tacacs-server-3",
            address="address_3",
            port=40000,
            secret="68#67p!Z7mR8*ql1XwN8@b04yV0f83sJ6hA9%uC2775&dP8xhoK4*jQ7tW0zS3rK"
        ),
    ]

    payload = TacacsServerProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        protocol="CHAP",
        server=servers,
        timeout=15,
        use_single_connection=True
    )

    created_obj = perform(
        tacacs_profiles_api.create_tacacs_server_profiles_with_http_info,
        response_type=TacacsServerProfiles,
        tacacs_server_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == object_name
    assert created_obj.folder == TARGET_FOLDER
    assert created_obj.protocol == "CHAP"
    assert len(created_obj.server) == 3

    # Cleanup
    perform(
        tacacs_profiles_api.delete_tacacs_server_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_tacacs_profile_by_id(tacacs_profiles_api, clean_tacacs_profile):
    """
    Test retrieving a TACACS Server Profile by ID with logging.
    Mirrors Test_identity_services_TACACSServerProfilesAPIService_GetByID
    """
    fetched_obj = perform(
        tacacs_profiles_api.get_tacacs_server_profiles_by_id_with_http_info,
        id=clean_tacacs_profile.id
    )

    assert fetched_obj.id == clean_tacacs_profile.id
    assert fetched_obj.name == clean_tacacs_profile.name


def test_update_tacacs_profile(tacacs_profiles_api, clean_tacacs_profile):
    """
    Test updating a TACACS Server Profile with logging.
    Mirrors Test_identity_services_TACACSServerProfilesAPIService_Update
    """
    update_payload = clean_tacacs_profile
    update_payload.protocol = "PAP"
    update_payload.timeout = 20

    updated_obj = perform(
        tacacs_profiles_api.update_tacacs_server_profiles_by_id_with_http_info,
        id=clean_tacacs_profile.id,
        tacacs_server_profiles=update_payload
    )

    assert updated_obj.id == clean_tacacs_profile.id
    assert updated_obj.timeout == 20


def test_list_tacacs_profiles(tacacs_profiles_api, clean_tacacs_profile):
    """
    Test listing TACACS Server Profiles with logging.
    Mirrors Test_identity_services_TACACSServerProfilesAPIService_List
    """
    response = perform(
        tacacs_profiles_api.list_tacacs_server_profiles_with_http_info,
        folder=TARGET_FOLDER,
        limit=200
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_tacacs_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_tacacs_profile.name} not found in list response"


def test_fetch_tacacs_server_profiles(tacacs_profiles_api, clean_tacacs_profile):
    """
    Test fetching a single tacacs_server_profiles by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = tacacs_profiles_api.fetch_tacacs_server_profiles(
        name=clean_tacacs_profile.name,
        folder=clean_tacacs_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found tacacs_server_profiles '{clean_tacacs_profile.name}'"
    assert fetched_obj.id == clean_tacacs_profile.id
    assert fetched_obj.name == clean_tacacs_profile.name
    assert fetched_obj.folder == clean_tacacs_profile.folder
    logger.info(f"\n[SUCCESS] fetch_tacacs_server_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent tacacs_server_profiles (should return None)
    not_found = tacacs_profiles_api.fetch_tacacs_server_profiles(
        name="non-existent-tacacs-server-profiles-xyz-12345",
        folder=clean_tacacs_profile.folder
    )
    assert not_found is None, "Should return None for non-existent tacacs_server_profiles"
    logger.info(f"\n[SUCCESS] fetch_tacacs_server_profiles correctly returned None for non-existent tacacs_server_profiles")


def test_delete_tacacs_profile_by_id(tacacs_profiles_api):
    """
    Test deletion specifically with logging.
    Mirrors Test_identity_services_TACACSServerProfilesAPIService_DeleteByID
    """
    object_name = f"test-tacacs-del-{uuid.uuid4().hex[:6]}"

    server = TacacsServerProfilesServerInner(
        name="del-test-svr",
        address="3.3.3.3",
        secret="delSecret"
    )

    payload = TacacsServerProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        protocol="CHAP",
        server=[server]
    )

    created_obj = perform(
        tacacs_profiles_api.create_tacacs_server_profiles_with_http_info,
        response_type=TacacsServerProfiles,
        tacacs_server_profiles=payload
    )

    # Perform Delete
    perform(
        tacacs_profiles_api.delete_tacacs_server_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    # Verify Deletion
    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        tacacs_profiles_api.get_tacacs_server_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
