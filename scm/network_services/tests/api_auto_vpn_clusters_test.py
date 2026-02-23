
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
def auto_vpn_clusters_api(client):
    return client.network_services.AutoVPNClustersApi(client.network_services.api_client)


def test_list_auto_vpn_clusters(auto_vpn_clusters_api):
    """Test listing Auto VPN Clusters (read-only resource)."""
    response = auto_vpn_clusters_api.list_auto_vpn_clusters(limit=200, offset=0)
    assert response is not None
    logger.info(f"Listed Auto VPN Clusters successfully")


def test_fetch_auto_vpn_clusters(auto_vpn_clusters_api):
    """Test fetching a non-existent Auto VPN Cluster returns None."""
    result = auto_vpn_clusters_api.fetch_auto_vpn_clusters(
        name="non-existent-auto-vpn-cluster-xyz-12345"
    )
    assert result is None, "Should return None for non-existent auto vpn cluster"
    logger.info("fetch_auto_vpn_clusters correctly returned None for non-existent object")
