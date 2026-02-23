
import logging
import pytest
from scm import Scm

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


def test_list_bandwidth_allocations(bandwidth_allocations_api):
    """Test listing Bandwidth Allocations."""
    response = bandwidth_allocations_api.list_bandwidth_allocations()
    assert response is not None
    logger.info(f"Listed Bandwidth Allocations successfully")


def test_fetch_bandwidth_allocations(bandwidth_allocations_api):
    """Test fetching a non-existent Bandwidth Allocation returns None."""
    result = bandwidth_allocations_api.fetch_bandwidth_allocations(
        name="non-existent-bandwidth-alloc-xyz-12345"
    )
    assert result is None, "Should return None for non-existent bandwidth allocation"
    logger.info("fetch_bandwidth_allocations correctly returned None for non-existent object")
