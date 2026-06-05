
import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.iptag_match_list import IptagMatchList
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
def iptag_match_list_api(client):
    return client.network_services.IptagMatchListApi(client.network_services.api_client)


@pytest.fixture
def clean_iptag_match_list(iptag_match_list_api):
    """
    Fixture to create a temporary iptag match list for testing and automatically delete it after.
    """
    object_name = f"test-iptag-{uuid.uuid4().hex[:6]}"

    payload = IptagMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        filter="All Logs",
        send_syslog=["test-syslog"],
        send_http=["some-http-profile"],
        send_snmptrap=["snmp_test"],
        send_email=["test-email"],
        quarantine=False,
        send_to_panorama=False
    )

    logger.info(f"\n[SETUP] Creating IP Tag Match List: {object_name}")
    created_obj = perform(
        iptag_match_list_api.create_iptag_match_list_with_http_info,
        response_type=IptagMatchList,
        iptag_match_list=payload
    )

    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting IP Tag Match List ID: {created_obj.id}")
    try:
        perform(
            iptag_match_list_api.delete_iptag_match_list_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_iptag_match_list(iptag_match_list_api):
    """
    Test manual creation and deletion of an iptag match list.
    """
    object_name = f"test-iptag-create-{uuid.uuid4().hex[:6]}"
    payload = IptagMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test iptag match list for create API testing",
        filter="All Logs",
        send_syslog=["test-syslog"],
        send_to_panorama=False
    )

    created_obj = perform(
        iptag_match_list_api.create_iptag_match_list_with_http_info,
        response_type=IptagMatchList,
        iptag_match_list=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER

    perform(
        iptag_match_list_api.delete_iptag_match_list_by_id,
        id=created_obj.id
    )


def test_get_iptag_match_list_by_id(iptag_match_list_api, clean_iptag_match_list):
    """
    Test retrieving an iptag match list by ID.
    """
    fetched_obj = perform(
        iptag_match_list_api.get_iptag_match_list_by_id,
        response_type=IptagMatchList,
        id=clean_iptag_match_list.id
    )

    assert fetched_obj.id == clean_iptag_match_list.id
    assert fetched_obj.name == clean_iptag_match_list.name
    assert fetched_obj.folder == clean_iptag_match_list.folder


def test_update_iptag_match_list(iptag_match_list_api, clean_iptag_match_list):
    """
    Test updating an iptag match list.
    """
    update_payload = clean_iptag_match_list
    update_payload.description = "Updated Description via Pytest"

    updated_obj = perform(
        iptag_match_list_api.update_iptag_match_list_by_id,
        response_type=IptagMatchList,
        id=clean_iptag_match_list.id,
        iptag_match_list=update_payload
    )

    assert updated_obj.description == "Updated Description via Pytest"
    assert updated_obj.id == clean_iptag_match_list.id


def test_list_iptag_match_list(iptag_match_list_api, clean_iptag_match_list):
    """
    Test listing iptag match lists with folder filter.
    """
    response = perform(
        iptag_match_list_api.list_iptag_match_list,
        folder=clean_iptag_match_list.folder
    )

    assert response is not None
    assert len(response.data) > 0
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_fetch_iptag_match_list(iptag_match_list_api, clean_iptag_match_list):
    """
    Test fetching a single iptag match list by name using the fetch convenience method.
    """
    fetched_obj = iptag_match_list_api.fetch_iptag_match_list(
        name=clean_iptag_match_list.name,
        folder=clean_iptag_match_list.folder
    )

    assert fetched_obj is not None, f"Should have found iptag match list '{clean_iptag_match_list.name}'"
    assert fetched_obj.id == clean_iptag_match_list.id
    assert fetched_obj.name == clean_iptag_match_list.name
    assert fetched_obj.folder == clean_iptag_match_list.folder
    logger.info(f"\n[SUCCESS] fetch_iptag_match_list found object: {fetched_obj.name}")

    not_found = iptag_match_list_api.fetch_iptag_match_list(
        name="non-existent-iptag-match-list-xyz-12345",
        folder=clean_iptag_match_list.folder
    )
    assert not_found is None, "Should return None for non-existent iptag match list"
    logger.info(f"\n[SUCCESS] fetch_iptag_match_list correctly returned None for non-existent object")


def test_delete_iptag_match_list_by_id(iptag_match_list_api):
    """
    Test deletion specifically.
    """
    from scm.exceptions import ObjectNotPresentError, InternalServerError

    object_name = f"test-iptag-del-{uuid.uuid4().hex[:6]}"
    payload = IptagMatchList(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test iptag match list for delete API testing",
        filter="All Logs",
        send_to_panorama=False
    )

    created_obj = perform(
        iptag_match_list_api.create_iptag_match_list_with_http_info,
        response_type=IptagMatchList,
        iptag_match_list=payload
    )

    perform(
        iptag_match_list_api.delete_iptag_match_list_by_id,
        id=created_obj.id
    )

    try:
        iptag_match_list_api.get_iptag_match_list_by_id(id=created_obj.id)
        pytest.fail("IP Tag Match List should have been deleted but was found.")
    except (ObjectNotPresentError, InternalServerError) as e:
        logger.info(f"✅ Correctly raised exception for deleted object: {type(e).__name__}")
        logger.info(f"   Object ID: {created_obj.id}")
