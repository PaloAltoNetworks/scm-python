
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
def network_locations_api(client):
    return client.deployment_services.NetworkLocationsApi(client.deployment_services.api_client)


def test_list_locations(network_locations_api):
    """Test listing Network Locations (read-only resource)."""
    response = network_locations_api.list_locations()
    assert response is not None
    logger.info(f"Listed Network Locations successfully")
