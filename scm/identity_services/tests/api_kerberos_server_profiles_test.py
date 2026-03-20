import logging
import uuid
import pytest
from scm import Scm
from scm.identity_services.models.kerberos_server_profiles import KerberosServerProfiles
from scm.identity_services.models.kerberos_server_profiles_server_inner import KerberosServerProfilesServerInner
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
def kerberos_profiles_api(client):
    """
    Fixture to return the Kerberos Server Profiles API instance.
    """
    return client.identity_services.KerberosServerProfilesApi(client.identity_services.api_client)


@pytest.fixture
def clean_kerberos_profile(kerberos_profiles_api):
    """
    Fixture to create a temporary Kerberos Server Profile for testing and automatically delete it after.
    """
    object_name = f"test-kerb-{uuid.uuid4().hex[:6]}"

    server = KerberosServerProfilesServerInner(
        name="kerb-server-fixture",
        host="10.0.1.50",
        port=88
    )

    payload = KerberosServerProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        server=[server]
    )

    logger.info(f"\n[SETUP] Creating Kerberos Server Profile: {object_name}")
    created_obj = perform(
        kerberos_profiles_api.create_kerberos_server_profiles_with_http_info,
        response_type=KerberosServerProfiles,
        kerberos_server_profiles=payload
    )

    assert created_obj is not None, "API returned None for creation!"
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Kerberos Server Profile ID: {created_obj.id}")
    try:
        perform(
            kerberos_profiles_api.delete_kerberos_server_profiles_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_kerberos_profile(kerberos_profiles_api):
    """
    Test manual creation and deletion of a Kerberos Server Profile with logging.
    Mirrors Test_identity_services_KerberosServerProfilesAPIService_Create
    """
    object_name = f"test-kerb-create-{uuid.uuid4().hex[:6]}"

    servers = [
        KerberosServerProfilesServerInner(
            name="kerb-server-1",
            host="10.0.1.50",
            port=88
        ),
        KerberosServerProfilesServerInner(
            name="kerb-server-2",
            host="kerberos.example.com",
            port=88
        ),
    ]

    payload = KerberosServerProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        server=servers
    )

    created_obj = perform(
        kerberos_profiles_api.create_kerberos_server_profiles_with_http_info,
        response_type=KerberosServerProfiles,
        kerberos_server_profiles=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == object_name
    assert created_obj.folder == TARGET_FOLDER
    assert len(created_obj.server) == 2

    # Cleanup
    perform(
        kerberos_profiles_api.delete_kerberos_server_profiles_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_kerberos_profile_by_id(kerberos_profiles_api, clean_kerberos_profile):
    """
    Test retrieving a Kerberos Server Profile by ID with logging.
    Mirrors Test_identity_services_KerberosServerProfilesAPIService_GetByID
    """
    fetched_obj = perform(
        kerberos_profiles_api.get_kerberos_server_profiles_by_id_with_http_info,
        id=clean_kerberos_profile.id
    )

    assert fetched_obj.id == clean_kerberos_profile.id
    assert fetched_obj.name == clean_kerberos_profile.name


def test_update_kerberos_profile(kerberos_profiles_api, clean_kerberos_profile):
    """
    Test updating a Kerberos Server Profile with logging.
    Mirrors Test_identity_services_KerberosServerProfilesAPIService_Update
    """
    updated_servers = [
        KerberosServerProfilesServerInner(
            name="updated-test-svr-1",
            host="2.2.2.2",
            port=8888
        ),
        KerberosServerProfilesServerInner(
            name="updated-test-svr-2",
            host="192.10.20.115",
            port=10
        ),
    ]

    update_payload = KerberosServerProfiles(
        id="",
        name=clean_kerberos_profile.name,
        server=updated_servers
    )

    updated_obj = perform(
        kerberos_profiles_api.update_kerberos_server_profiles_by_id_with_http_info,
        id=clean_kerberos_profile.id,
        kerberos_server_profiles=update_payload
    )

    assert updated_obj.id == clean_kerberos_profile.id
    assert updated_obj.server[0].name == "updated-test-svr-1"
    assert updated_obj.server[1].name == "updated-test-svr-2"
    assert updated_obj.server[0].port == 8888


def test_list_kerberos_profiles(kerberos_profiles_api, clean_kerberos_profile):
    """
    Test listing Kerberos Server Profiles with logging.
    Mirrors Test_identity_services_KerberosServerProfilesAPIService_List
    """
    response = perform(
        kerberos_profiles_api.list_kerberos_server_profiles_with_http_info,
        folder=TARGET_FOLDER,
        limit=200
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_kerberos_profile.name:
            found = True
            break
    assert found is True, f"Created profile {clean_kerberos_profile.name} not found in list response"


def test_fetch_kerberos_server_profiles(kerberos_profiles_api, clean_kerberos_profile):
    """
    Test fetching a single kerberos_server_profiles by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = kerberos_profiles_api.fetch_kerberos_server_profiles(
        name=clean_kerberos_profile.name,
        folder=clean_kerberos_profile.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found kerberos_server_profiles '{clean_kerberos_profile.name}'"
    assert fetched_obj.id == clean_kerberos_profile.id
    assert fetched_obj.name == clean_kerberos_profile.name
    assert fetched_obj.folder == clean_kerberos_profile.folder
    logger.info(f"\n[SUCCESS] fetch_kerberos_server_profiles found object: {fetched_obj.name}")

    # Test fetching non-existent kerberos_server_profiles (should return None)
    not_found = kerberos_profiles_api.fetch_kerberos_server_profiles(
        name="non-existent-kerberos-server-profiles-xyz-12345",
        folder=clean_kerberos_profile.folder
    )
    assert not_found is None, "Should return None for non-existent kerberos_server_profiles"
    logger.info(f"\n[SUCCESS] fetch_kerberos_server_profiles correctly returned None for non-existent kerberos_server_profiles")


def test_delete_kerberos_profile_by_id(kerberos_profiles_api):
    """
    Test deletion specifically with logging.
    Mirrors Test_identity_services_KerberosServerProfilesAPIService_DeleteByID
    """
    object_name = f"test-kerb-del-{uuid.uuid4().hex[:6]}"

    server = KerberosServerProfilesServerInner(
        name="del-svr",
        host="4.4.4.4"
    )

    payload = KerberosServerProfiles(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        server=[server]
    )

    created_obj = perform(
        kerberos_profiles_api.create_kerberos_server_profiles_with_http_info,
        response_type=KerberosServerProfiles,
        kerberos_server_profiles=payload
    )

    # Perform Delete
    perform(
        kerberos_profiles_api.delete_kerberos_server_profiles_by_id_with_http_info,
        id=created_obj.id
    )

    # Verify Deletion
    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        kerberos_profiles_api.get_kerberos_server_profiles_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
