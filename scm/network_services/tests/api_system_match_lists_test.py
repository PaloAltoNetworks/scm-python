
import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.system_match_list import SystemMatchList
from scm.objects.models.http_server_profiles import HttpServerProfiles, HttpServerProfilesServerInner
from scm.objects.models.syslog_server_profiles import SyslogServerProfiles, SyslogServerProfilesServerInner
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "ngfw-shared"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def system_match_list_api(client):
    return client.network_services.SystemMatchListApi(client.network_services.api_client)


@pytest.fixture(scope="module")
def http_server_profiles_api(client):
    return client.objects.HTTPServerProfilesApi(client.objects.api_client)


@pytest.fixture(scope="module")
def syslog_server_profiles_api(client):
    return client.objects.SyslogServerProfilesApi(client.objects.api_client)


@pytest.fixture
def dependency_profiles(http_server_profiles_api, syslog_server_profiles_api):
    """
    Creates HTTP and Syslog server profiles as dependencies for System Match List.
    """
    random_id = uuid.uuid4().hex[:6]

    # Create HTTP Server Profile
    http_name = f"test-http-{random_id}"
    http_payload = HttpServerProfiles(
        id="",
        name=http_name,
        folder=TARGET_FOLDER,
        server=[HttpServerProfilesServerInner(
            name="http-server-1",
            address="192.168.1.100",
            port=8080,
            protocol="HTTP",
            http_method="POST"
        )]
    )
    logger.info(f"\n[SETUP] Creating HTTP Server Profile: {http_name}")
    http_obj = http_server_profiles_api.create_http_server_profiles(http_server_profiles=http_payload)

    # Create Syslog Server Profile (shortened name to stay under 31 char limit)
    syslog_name = f"sys-{random_id}"
    syslog_payload = SyslogServerProfiles(
        id="",
        name=syslog_name,
        folder=TARGET_FOLDER,
        server=[SyslogServerProfilesServerInner(
            name="syslog-server-1",
            server="192.168.1.101",
            port=514,
            format="BSD",
            facility="LOG_USER",
            transport="UDP"
        )]
    )
    logger.info(f"\n[SETUP] Creating Syslog Server Profile: {syslog_name}")
    syslog_obj = syslog_server_profiles_api.create_syslog_server_profiles(syslog_server_profiles=syslog_payload)

    yield {
        "http_name": http_name,
        "http_id": http_obj.id,
        "syslog_name": syslog_name,
        "syslog_id": syslog_obj.id
    }

    # Cleanup
    logger.info(f"\n[TEARDOWN] Deleting dependency profiles")
    try:
        http_server_profiles_api.delete_http_server_profiles_by_id(id=http_obj.id)
    except Exception as e:
        logger.info(f"Failed to delete HTTP profile: {e}")
    try:
        syslog_server_profiles_api.delete_syslog_server_profiles_by_id(id=syslog_obj.id)
    except Exception as e:
        logger.info(f"Failed to delete Syslog profile: {e}")


@pytest.fixture
def clean_system_match_list(system_match_list_api, dependency_profiles):
    """
    Fixture to create a temporary system match list for testing and automatically delete it after.
    """
    object_name = f"test-system-{uuid.uuid4().hex[:6]}"

    payload = SystemMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        filter="All Logs",
        send_syslog=[dependency_profiles["syslog_name"]],
        send_http=[dependency_profiles["http_name"]],
        send_to_panorama=False
    )

    logger.info(f"\n[SETUP] Creating System Match List: {object_name}")
    created_obj = perform(
        system_match_list_api.create_system_match_list_with_http_info,
        response_type=SystemMatchList,
        system_match_list=payload
    )

    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting System Match List ID: {created_obj.id}")
    try:
        perform(
            system_match_list_api.delete_system_match_list_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_system_match_list(system_match_list_api, dependency_profiles):
    """
    Test manual creation and deletion of a system match list.
    """
    object_name = f"test-system-create-{uuid.uuid4().hex[:6]}"
    payload = SystemMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test system match list for create API testing",
        filter="All Logs",
        send_syslog=[dependency_profiles["syslog_name"]],
        send_to_panorama=False
    )

    created_obj = perform(
        system_match_list_api.create_system_match_list_with_http_info,
        response_type=SystemMatchList,
        system_match_list=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER

    perform(
        system_match_list_api.delete_system_match_list_by_id,
        id=created_obj.id
    )


def test_get_system_match_list_by_id(system_match_list_api, clean_system_match_list):
    """
    Test retrieving a system match list by ID.
    """
    fetched_obj = perform(
        system_match_list_api.get_system_match_list_by_id,
        response_type=SystemMatchList,
        id=clean_system_match_list.id
    )

    assert fetched_obj.id == clean_system_match_list.id
    assert fetched_obj.name == clean_system_match_list.name
    assert fetched_obj.folder == clean_system_match_list.folder


def test_update_system_match_list(system_match_list_api, clean_system_match_list):
    """
    Test updating a system match list.
    """
    update_payload = clean_system_match_list
    update_payload.description = "Updated Description via Pytest"

    updated_obj = perform(
        system_match_list_api.update_system_match_list_by_id,
        response_type=SystemMatchList,
        id=clean_system_match_list.id,
        system_match_list=update_payload
    )

    assert updated_obj.description == "Updated Description via Pytest"
    assert updated_obj.id == clean_system_match_list.id


def test_list_system_match_list(system_match_list_api, clean_system_match_list):
    """
    Test listing system match lists with folder filter.
    """
    response = perform(
        system_match_list_api.list_system_match_list,
        folder=clean_system_match_list.folder
    )

    assert response is not None
    assert len(response.data) > 0
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_fetch_system_match_list(system_match_list_api, clean_system_match_list):
    """
    Test fetching a single system match list by name using the fetch convenience method.
    """
    fetched_obj = system_match_list_api.fetch_system_match_list(
        name=clean_system_match_list.name,
        folder=clean_system_match_list.folder
    )

    assert fetched_obj is not None, f"Should have found system match list '{clean_system_match_list.name}'"
    assert fetched_obj.id == clean_system_match_list.id
    assert fetched_obj.name == clean_system_match_list.name
    assert fetched_obj.folder == clean_system_match_list.folder
    logger.info(f"\n[SUCCESS] fetch_system_match_list found object: {fetched_obj.name}")

    not_found = system_match_list_api.fetch_system_match_list(
        name="non-existent-system-match-list-xyz-12345",
        folder=clean_system_match_list.folder
    )
    assert not_found is None, "Should return None for non-existent system match list"
    logger.info(f"\n[SUCCESS] fetch_system_match_list correctly returned None for non-existent object")


def test_delete_system_match_list_by_id(system_match_list_api):
    """
    Test deletion specifically.
    """
    from scm.exceptions import ObjectNotPresentError, InternalServerError

    object_name = f"test-system-del-{uuid.uuid4().hex[:6]}"
    payload = SystemMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test system match list for delete API testing",
        filter="All Logs",
        send_to_panorama=False
    )

    created_obj = perform(
        system_match_list_api.create_system_match_list_with_http_info,
        response_type=SystemMatchList,
        system_match_list=payload
    )

    perform(
        system_match_list_api.delete_system_match_list_by_id,
        id=created_obj.id
    )

    try:
        system_match_list_api.get_system_match_list_by_id(id=created_obj.id)
        pytest.fail("System Match List should have been deleted but was found.")
    except (ObjectNotPresentError, InternalServerError) as e:
        logger.info(f"✅ Correctly raised exception for deleted object: {type(e).__name__}")
        logger.info(f"   Object ID: {created_obj.id}")
