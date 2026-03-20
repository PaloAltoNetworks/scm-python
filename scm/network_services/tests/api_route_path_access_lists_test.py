import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.route_path_access_lists import RoutePathAccessLists
from scm.network_services.models.route_path_access_lists_aspath_entry_inner import RoutePathAccessListsAspathEntryInner
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "All"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def route_path_access_lists_api(client):
    return client.network_services.RoutePathAccessListsApi(client.network_services.api_client)


def _make_rpal_payload(name, regex="^65001_", description=None):
    entry = RoutePathAccessListsAspathEntryInner(
        name=10,
        action="permit",
        aspath_regex=regex,
    )
    kwargs = dict(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        aspath_entry=[entry],
    )
    if description:
        kwargs["description"] = description
    return RoutePathAccessLists(**kwargs)


@pytest.fixture
def clean_route_path_access_list(route_path_access_lists_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-rpal-{random_id}"

    payload = _make_rpal_payload(object_name)

    logger.info(f"\n[SETUP] Creating Route Path Access List: {object_name}")
    created_obj = perform(
        route_path_access_lists_api.create_route_path_access_lists_with_http_info,
        response_type=RoutePathAccessLists,
        route_path_access_lists=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Route Path Access List ID: {created_obj.id}")
    try:
        route_path_access_lists_api.delete_route_path_access_lists_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_route_path_access_list(route_path_access_lists_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-rpal-create-{random_id}"

    payload = _make_rpal_payload(object_name, description="Test route path access list for create")

    created_obj = perform(
        route_path_access_lists_api.create_route_path_access_lists_with_http_info,
        response_type=RoutePathAccessLists,
        route_path_access_lists=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    route_path_access_lists_api.delete_route_path_access_lists_by_id(id=created_obj.id)


def test_get_route_path_access_list_by_id(route_path_access_lists_api, clean_route_path_access_list):
    fetched_obj = route_path_access_lists_api.get_route_path_access_lists_by_id(id=clean_route_path_access_list.id)
    assert fetched_obj.id == clean_route_path_access_list.id
    assert fetched_obj.name == clean_route_path_access_list.name


def test_update_route_path_access_list(route_path_access_lists_api, clean_route_path_access_list):
    update_payload = clean_route_path_access_list
    update_payload.description = "Updated route path access list description"

    updated_obj = route_path_access_lists_api.update_route_path_access_lists_by_id(
        id=clean_route_path_access_list.id,
        route_path_access_lists=update_payload,
    )

    assert updated_obj.id == clean_route_path_access_list.id
    assert updated_obj.description == "Updated route path access list description"


def test_list_route_path_access_lists(route_path_access_lists_api, clean_route_path_access_list):
    response = route_path_access_lists_api.list_route_path_access_lists(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_route_path_access_list.id:
            found = True
            break
    assert found is True


def test_fetch_route_path_access_lists(route_path_access_lists_api, clean_route_path_access_list):
    fetched_obj = route_path_access_lists_api.fetch_route_path_access_lists(
        name=clean_route_path_access_list.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_route_path_access_list.id
    assert fetched_obj.name == clean_route_path_access_list.name
    logger.info(f"\n[SUCCESS] fetch_route_path_access_lists found object: {fetched_obj.name}")

    not_found = route_path_access_lists_api.fetch_route_path_access_lists(
        name="non-existent-rpal-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_route_path_access_lists correctly returned None for non-existent object")


def test_delete_route_path_access_list_by_id(route_path_access_lists_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-rpal-del-{random_id}"

    payload = _make_rpal_payload(object_name)

    created_obj = perform(
        route_path_access_lists_api.create_route_path_access_lists_with_http_info,
        response_type=RoutePathAccessLists,
        route_path_access_lists=payload,
    )

    route_path_access_lists_api.delete_route_path_access_lists_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        route_path_access_lists_api.get_route_path_access_lists_by_id(id=created_obj.id)
        pytest.fail("Route Path Access List should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
