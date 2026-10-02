
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.bandwidth_allocations import BandwidthAllocations
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def bandwidth_allocations_api(client):
    return client.deployment_services.BandwidthAllocationsApi(client.deployment_services.api_client)


def test_create_bandwidth_allocation(bandwidth_allocations_api):
    """
    Test creating a bandwidth allocation.
    Equivalent to Go: Test_deployment_services_BandwidthAllocationsAPIService_Create
    """
    test_name = f"test-bw-alloc-{uuid.uuid4().hex[:6]}"

    payload = BandwidthAllocations(
        name=test_name,
        allocated_bandwidth=100,
    )

    # BandwidthAllocations API returns 200, not 201
    created_obj = perform(
        bandwidth_allocations_api.create_bandwidth_allocations_with_http_info,
        response_type=BandwidthAllocations,
        bandwidth_allocations=payload
    )

    assert created_obj is not None
    assert created_obj.name == test_name
    assert created_obj.allocated_bandwidth == 100
    logger.info(f"Created bandwidth allocation: {created_obj.name}")

    # Cleanup - delete requires spn_name_list, best-effort
    try:
        bandwidth_allocations_api.delete_bandwidth_allocations(
            name=test_name,
            spn_name_list="",
        )
        logger.info(f"Cleaned up: {test_name}")
    except Exception as e:
        logger.warning(f"Cleanup skipped (delete requires spn_name_list context): {e}")


def test_list_bandwidth_allocations(bandwidth_allocations_api):
    """Test listing Bandwidth Allocations."""
    response = bandwidth_allocations_api.list_bandwidth_allocations()
    assert response is not None
    logger.info(f"Listed Bandwidth Allocations successfully")


def test_fetch_bandwidth_allocations(bandwidth_allocations_api):
    """
    Test fetch method for bandwidth allocations.
    Uses client-side pagination to find an object by name.
    """
    # First, list to find an existing allocation name
    response = bandwidth_allocations_api.list_bandwidth_allocations()
    if response is None or not hasattr(response, 'data') or not response.data:
        pytest.skip("No bandwidth allocations found to test fetch")

    target = response.data[0]
    target_name = target.name
    logger.info(f"Testing fetch for: {target_name}")

    # Use fetch method (client-side pagination)
    fetched = bandwidth_allocations_api.fetch_bandwidth_allocations(name=target_name)

    assert fetched is not None
    assert fetched.name == target_name
    logger.info(f"Successfully fetched bandwidth allocation: {fetched.name}")


def test_fetch_bandwidth_allocations_not_found(bandwidth_allocations_api):
    """Test fetch returns None for non-existent allocation."""
    result = bandwidth_allocations_api.fetch_bandwidth_allocations(
        name="non-existent-bandwidth-allocation-xyz123"
    )
    assert result is None
    logger.info("Correctly returned None for non-existent bandwidth allocation")
