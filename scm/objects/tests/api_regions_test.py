
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.regions import Regions
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Prisma Access"
# -----------------------------------------------------------------------------

# NOTE: Regions do NOT support List or Fetch operations.
# Go removed List/Fetch because predefined regions lack the 'id' field.
# Only Create, GetByID, Update, and DeleteByID are tested.


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
def regions_api(client):
    """
    Fixture to return the Regions API instance.
    """
    return client.objects.RegionsApi(client.objects.api_client)


def test_create_region(regions_api):
    """
    Test creation and deletion of a region object.
    Equivalent to Go: Test_objects_RegionsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    region_name = f"test-rgn-create-{random_suffix}"

    payload = Regions(
        id="",
        name=region_name,
        folder=TARGET_FOLDER,
        address=["10.0.0.0/8"],
    )

    # Create using perform helper
    created_obj = perform(
        regions_api.create_regions_with_http_info,
        response_type=Regions,
        regions=payload,
    )

    # Verify
    assert created_obj.name == region_name
    assert created_obj.id is not None

    logger.info(f"Successfully created region: {region_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        regions_api.delete_regions_by_id,
        id=created_obj.id,
    )
    logger.info(f"Successfully cleaned up region: {created_obj.id}")


def test_get_region_by_id(regions_api):
    """
    Test retrieving a region by ID.
    Equivalent to Go: Test_objects_RegionsAPIService_GetByID
    """
    # Create a region first
    random_suffix = uuid.uuid4().hex[:6]
    region_name = f"test-rgn-getbyid-{random_suffix}"

    payload = Regions(
        id="",
        name=region_name,
        folder=TARGET_FOLDER,
        address=["172.16.0.0/12"],
    )

    created_obj = perform(
        regions_api.create_regions_with_http_info,
        response_type=Regions,
        regions=payload,
    )
    assert created_obj.id is not None

    # Get by ID using perform helper
    fetched_obj = perform(
        regions_api.get_regions_by_id,
        response_type=Regions,
        id=created_obj.id,
    )

    # Verify
    assert fetched_obj.id == created_obj.id
    assert fetched_obj.name == region_name

    logger.info(f"Successfully retrieved region: {fetched_obj.name}")

    # Cleanup
    perform(
        regions_api.delete_regions_by_id,
        id=created_obj.id,
    )
    logger.info(f"Successfully cleaned up region: {created_obj.id}")


def test_update_region(regions_api):
    """
    Test updating an existing region.
    Equivalent to Go: Test_objects_RegionsAPIService_Update
    """
    # Create a region first
    random_suffix = uuid.uuid4().hex[:6]
    region_name = f"test-rgn-update-{random_suffix}"

    payload = Regions(
        id="",
        name=region_name,
        folder=TARGET_FOLDER,
        address=["192.168.0.0/16"],
    )

    created_obj = perform(
        regions_api.create_regions_with_http_info,
        response_type=Regions,
        regions=payload,
    )
    assert created_obj.id is not None

    # Update with additional address
    update_payload = Regions(
        id=created_obj.id,
        name=region_name,
        folder=TARGET_FOLDER,
        address=["192.168.0.0/16", "10.10.0.0/16"],
    )

    updated_obj = perform(
        regions_api.update_regions_by_id,
        response_type=Regions,
        id=created_obj.id,
        regions=update_payload,
    )

    # Verify
    assert updated_obj.name == region_name
    assert len(updated_obj.address) == 2

    logger.info(f"Successfully updated region: {region_name}")

    # Cleanup
    perform(
        regions_api.delete_regions_by_id,
        id=created_obj.id,
    )
    logger.info(f"Successfully cleaned up region: {created_obj.id}")


def test_delete_region_by_id(regions_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_RegionsAPIService_DeleteByID
    """
    from scm.exceptions import ObjectNotPresentError

    # Create a region first
    random_suffix = uuid.uuid4().hex[:6]
    region_name = f"test-rgn-delete-{random_suffix}"

    payload = Regions(
        id="",
        name=region_name,
        folder=TARGET_FOLDER,
        address=["10.200.0.0/16"],
    )

    created_obj = perform(
        regions_api.create_regions_with_http_info,
        response_type=Regions,
        regions=payload,
    )
    assert created_obj.id is not None

    # Delete using perform helper
    perform(
        regions_api.delete_regions_by_id,
        id=created_obj.id,
    )

    logger.info(f"Successfully deleted region: {created_obj.id}")

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    try:
        regions_api.get_regions_by_id(id=created_obj.id)
        pytest.fail("Region should have been deleted but was found.")
    except ObjectNotPresentError:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
