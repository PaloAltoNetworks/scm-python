
import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.config_match_list import ConfigMatchList
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
def config_match_list_api(client):
    return client.network_services.ConfigMatchListApi(client.network_services.api_client)


@pytest.fixture
def clean_config_match_list(config_match_list_api):
    """
    Fixture to create a temporary config match list for testing and automatically delete it after.
    """
    object_name = f"test-config-{uuid.uuid4().hex[:6]}"

    payload = ConfigMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        filter="All Logs",
        send_syslog=["test-syslog"],
        send_http=["some-http-profile"],
        send_snmptrap=["snmp_test"],
        send_email=["test-email"],
        send_to_panorama=False
    )

    logger.info(f"\n[SETUP] Creating Config Match List: {object_name}")
    created_obj = perform(
        config_match_list_api.create_config_match_list_with_http_info,
        response_type=ConfigMatchList,
        config_match_list=payload
    )

    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Config Match List ID: {created_obj.id}")
    try:
        perform(
            config_match_list_api.delete_config_match_list_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_config_match_list(config_match_list_api):
    """
    Test manual creation and deletion of a config match list.
    """
    object_name = f"test-config-create-{uuid.uuid4().hex[:6]}"
    payload = ConfigMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test config match list for create API testing",
        filter="All Logs",
        send_syslog=["test-syslog"],
        send_to_panorama=False
    )

    created_obj = perform(
        config_match_list_api.create_config_match_list_with_http_info,
        response_type=ConfigMatchList,
        config_match_list=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER

    perform(
        config_match_list_api.delete_config_match_list_by_id,
        id=created_obj.id
    )


def test_get_config_match_list_by_id(config_match_list_api, clean_config_match_list):
    """
    Test retrieving a config match list by ID.
    """
    fetched_obj = perform(
        config_match_list_api.get_config_match_list_by_id,
        response_type=ConfigMatchList,
        id=clean_config_match_list.id
    )

    assert fetched_obj.id == clean_config_match_list.id
    assert fetched_obj.name == clean_config_match_list.name
    assert fetched_obj.folder == clean_config_match_list.folder


def test_update_config_match_list(config_match_list_api, clean_config_match_list):
    """
    Test updating a config match list.
    """
    update_payload = clean_config_match_list
    update_payload.description = "Updated Description via Pytest"

    updated_obj = perform(
        config_match_list_api.update_config_match_list_by_id,
        response_type=ConfigMatchList,
        id=clean_config_match_list.id,
        config_match_list=update_payload
    )

    assert updated_obj.description == "Updated Description via Pytest"
    assert updated_obj.id == clean_config_match_list.id


def test_list_config_match_list(config_match_list_api, clean_config_match_list):
    """
    Test listing config match lists with folder filter.
    """
    response = perform(
        config_match_list_api.list_config_match_list,
        folder=clean_config_match_list.folder
    )

    assert response is not None
    assert len(response.data) > 0
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_fetch_config_match_list(config_match_list_api, clean_config_match_list):
    """
    Test fetching a single config match list by name using the fetch convenience method.
    """
    fetched_obj = config_match_list_api.fetch_config_match_list(
        name=clean_config_match_list.name,
        folder=clean_config_match_list.folder
    )

    assert fetched_obj is not None, f"Should have found config match list '{clean_config_match_list.name}'"
    assert fetched_obj.id == clean_config_match_list.id
    assert fetched_obj.name == clean_config_match_list.name
    assert fetched_obj.folder == clean_config_match_list.folder
    logger.info(f"\n[SUCCESS] fetch_config_match_list found object: {fetched_obj.name}")

    not_found = config_match_list_api.fetch_config_match_list(
        name="non-existent-system-match-list-xyz-12345",
        folder=clean_config_match_list.folder
    )
    assert not_found is None, "Should return None for non-existent config match list"
    logger.info(f"\n[SUCCESS] fetch_config_match_list correctly returned None for non-existent object")


def test_delete_config_match_list_by_id(config_match_list_api):
    """
    Test deletion specifically.
    """
    from scm.exceptions import ObjectNotPresentError, InternalServerError

    object_name = f"test-config-del-{uuid.uuid4().hex[:6]}"
    payload = ConfigMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test config match list for delete API testing",
        filter="All Logs",
        send_to_panorama=False
    )

    created_obj = perform(
        config_match_list_api.create_config_match_list_with_http_info,
        response_type=ConfigMatchList,
        config_match_list=payload
    )

    perform(
        config_match_list_api.delete_config_match_list_by_id,
        id=created_obj.id
    )

    try:
        config_match_list_api.get_config_match_list_by_id(id=created_obj.id)
        pytest.fail("Config Match List should have been deleted but was found.")
    except (ObjectNotPresentError, InternalServerError) as e:
        logger.info(f"✅ Correctly raised exception for deleted object: {type(e).__name__}")
        logger.info(f"   Object ID: {created_obj.id}")
