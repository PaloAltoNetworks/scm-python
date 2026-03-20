
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
def bgp_routing_api(client):
    return client.deployment_services.BGPRoutingApi(client.deployment_services.api_client)


def test_get_bgp_routing(bgp_routing_api):
    """Test getting BGP Routing settings (singleton resource)."""
    response = bgp_routing_api.get_bgp_routing()
    assert response is not None
    logger.info(f"Got BGP Routing settings successfully")


def test_update_bgp_routing(bgp_routing_api):
    """No-op update: get existing BGP Routing settings and update with same data."""
    existing = bgp_routing_api.get_bgp_routing()
    assert existing is not None
    updated = bgp_routing_api.update_bgp_routing(bgp_routing=existing)
    assert updated is not None
    logger.info(f"Updated BGP Routing settings (no-op) successfully")
