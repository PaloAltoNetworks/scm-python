import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.bgp_route_map_redistributions import BgpRouteMapRedistributions
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
def bgp_route_map_redistributions_api(client):
    return client.network_services.BGPRouteMapRedistributionsApi(client.network_services.api_client)


@pytest.fixture
def clean_bgp_route_map_redistribution(bgp_route_map_redistributions_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-rmr-{random_id}"

    payload = BgpRouteMapRedistributions(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test BGP route map redistribution",
    )

    logger.info(f"\n[SETUP] Creating BGP Route Map Redistribution: {object_name}")
    created_obj = perform(
        bgp_route_map_redistributions_api.create_bgp_route_map_redistributions_with_http_info,
        response_type=BgpRouteMapRedistributions,
        bgp_route_map_redistributions=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting BGP Route Map Redistribution ID: {created_obj.id}")
    try:
        bgp_route_map_redistributions_api.delete_bgp_route_map_redistributions_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_bgp_route_map_redistribution(bgp_route_map_redistributions_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-rmr-create-{random_id}"

    payload = BgpRouteMapRedistributions(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test BGP route map redistribution for create",
    )

    created_obj = perform(
        bgp_route_map_redistributions_api.create_bgp_route_map_redistributions_with_http_info,
        response_type=BgpRouteMapRedistributions,
        bgp_route_map_redistributions=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    bgp_route_map_redistributions_api.delete_bgp_route_map_redistributions_by_id(id=created_obj.id)


def test_get_bgp_route_map_redistribution_by_id(bgp_route_map_redistributions_api, clean_bgp_route_map_redistribution):
    fetched_obj = bgp_route_map_redistributions_api.get_bgp_route_map_redistributions_by_id(id=clean_bgp_route_map_redistribution.id)
    assert fetched_obj.id == clean_bgp_route_map_redistribution.id
    assert fetched_obj.name == clean_bgp_route_map_redistribution.name


def test_update_bgp_route_map_redistribution(bgp_route_map_redistributions_api, clean_bgp_route_map_redistribution):
    update_payload = clean_bgp_route_map_redistribution
    update_payload.description = "Updated description"

    updated_obj = bgp_route_map_redistributions_api.update_bgp_route_map_redistributions_by_id(
        id=clean_bgp_route_map_redistribution.id,
        bgp_route_map_redistributions=update_payload,
    )

    assert updated_obj.id == clean_bgp_route_map_redistribution.id
    assert updated_obj.name == clean_bgp_route_map_redistribution.name


def test_list_bgp_route_map_redistributions(bgp_route_map_redistributions_api, clean_bgp_route_map_redistribution):
    response = bgp_route_map_redistributions_api.list_bgp_route_map_redistributions(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert response.data is not None


def test_fetch_bgp_route_map_redistributions(bgp_route_map_redistributions_api, clean_bgp_route_map_redistribution):
    fetched_obj = bgp_route_map_redistributions_api.fetch_bgp_route_map_redistributions(
        name=clean_bgp_route_map_redistribution.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_bgp_route_map_redistribution.id
    assert fetched_obj.name == clean_bgp_route_map_redistribution.name
    logger.info(f"\n[SUCCESS] fetch_bgp_route_map_redistributions found object: {fetched_obj.name}")

    not_found = bgp_route_map_redistributions_api.fetch_bgp_route_map_redistributions(
        name="non-existent-bgp-rmr-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_bgp_route_map_redistributions correctly returned None for non-existent object")


def test_delete_bgp_route_map_redistribution_by_id(bgp_route_map_redistributions_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-bgp-rmr-del-{random_id}"

    payload = BgpRouteMapRedistributions(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
    )

    created_obj = perform(
        bgp_route_map_redistributions_api.create_bgp_route_map_redistributions_with_http_info,
        response_type=BgpRouteMapRedistributions,
        bgp_route_map_redistributions=payload,
    )

    bgp_route_map_redistributions_api.delete_bgp_route_map_redistributions_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        bgp_route_map_redistributions_api.get_bgp_route_map_redistributions_by_id(id=created_obj.id)
        pytest.fail("BGP Route Map Redistribution should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
