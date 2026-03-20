import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.bgp_route_maps import BgpRouteMaps
from scm.network_services.models.bgp_route_maps_route_map_inner import BgpRouteMapsRouteMapInner
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "Prisma Access"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def bgp_route_maps_api(client):
    return client.network_services.BGPRouteMapsApi(client.network_services.api_client)


def _make_bgp_route_map_payload(name, description=None):
    entry = BgpRouteMapsRouteMapInner(
        action="permit",
        name=1,
    )
    kwargs = dict(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        route_map=[entry],
    )
    if description:
        kwargs["description"] = description
    return BgpRouteMaps(**kwargs)


@pytest.fixture
def clean_bgp_route_map(bgp_route_maps_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-rmap-{random_id}"

    payload = _make_bgp_route_map_payload(object_name, description="Test BGP route map")

    logger.info(f"\n[SETUP] Creating BGP Route Map: {object_name}")
    created_obj = perform(
        bgp_route_maps_api.create_bgp_route_maps_with_http_info,
        response_type=BgpRouteMaps,
        bgp_route_maps=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting BGP Route Map ID: {created_obj.id}")
    try:
        bgp_route_maps_api.delete_bgp_route_maps_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_bgp_route_map(bgp_route_maps_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-rmap-create-{random_id}"

    payload = _make_bgp_route_map_payload(object_name, description="Test BGP route map for create")

    created_obj = perform(
        bgp_route_maps_api.create_bgp_route_maps_with_http_info,
        response_type=BgpRouteMaps,
        bgp_route_maps=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    bgp_route_maps_api.delete_bgp_route_maps_by_id(id=created_obj.id)


def test_get_bgp_route_map_by_id(bgp_route_maps_api, clean_bgp_route_map):
    fetched_obj = bgp_route_maps_api.get_bgp_route_maps_by_id(id=clean_bgp_route_map.id)
    assert fetched_obj.id == clean_bgp_route_map.id
    assert fetched_obj.name == clean_bgp_route_map.name


def test_update_bgp_route_map(bgp_route_maps_api, clean_bgp_route_map):
    entry1 = BgpRouteMapsRouteMapInner(action="permit", name=1)
    entry2 = BgpRouteMapsRouteMapInner(action="deny", name=2)

    update_payload = clean_bgp_route_map
    update_payload.description = "Updated description"
    update_payload.route_map = [entry1, entry2]

    updated_obj = bgp_route_maps_api.update_bgp_route_maps_by_id(
        id=clean_bgp_route_map.id,
        bgp_route_maps=update_payload,
    )

    assert updated_obj.id == clean_bgp_route_map.id
    assert updated_obj.name == clean_bgp_route_map.name


def test_list_bgp_route_maps(bgp_route_maps_api, clean_bgp_route_map):
    response = bgp_route_maps_api.list_bgp_route_maps(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert response.data is not None


def test_fetch_bgp_route_maps(bgp_route_maps_api, clean_bgp_route_map):
    fetched_obj = bgp_route_maps_api.fetch_bgp_route_maps(
        name=clean_bgp_route_map.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_bgp_route_map.id
    assert fetched_obj.name == clean_bgp_route_map.name
    logger.info(f"\n[SUCCESS] fetch_bgp_route_maps found object: {fetched_obj.name}")

    not_found = bgp_route_maps_api.fetch_bgp_route_maps(
        name="non-existent-bgp-rmap-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_bgp_route_maps correctly returned None for non-existent object")


def test_delete_bgp_route_map_by_id(bgp_route_maps_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-rmap-del-{random_id}"

    payload = _make_bgp_route_map_payload(object_name)

    created_obj = perform(
        bgp_route_maps_api.create_bgp_route_maps_with_http_info,
        response_type=BgpRouteMaps,
        bgp_route_maps=payload,
    )

    bgp_route_maps_api.delete_bgp_route_maps_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        bgp_route_maps_api.get_bgp_route_maps_by_id(id=created_obj.id)
        pytest.fail("BGP Route Map should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
