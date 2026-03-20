
import logging
import pytest
from scm import Scm

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
def sdwan_traffic_distribution_profiles_api(client):
    return client.network_services.SDWANTrafficDistributionProfilesApi(client.network_services.api_client)


def test_list_sdwan_traffic_distribution_profiles(sdwan_traffic_distribution_profiles_api):
    """Test listing SDWAN Traffic Distribution Profiles."""
    response = sdwan_traffic_distribution_profiles_api.list_sdwan_traffic_distribution_profiles(
        folder=TARGET_FOLDER, limit=200, offset=0
    )
    assert response is not None
    logger.info(f"Listed SDWAN Traffic Distribution Profiles successfully")


def test_fetch_sdwan_traffic_distribution_profiles(sdwan_traffic_distribution_profiles_api):
    """Test fetching a non-existent SDWAN Traffic Distribution Profile returns None."""
    result = sdwan_traffic_distribution_profiles_api.fetch_sdwan_traffic_distribution_profiles(
        name="non-existent-sdwan-tdp-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert result is None, "Should return None for non-existent sdwan traffic distribution profile"
    logger.info("fetch_sdwan_traffic_distribution_profiles correctly returned None for non-existent object")
