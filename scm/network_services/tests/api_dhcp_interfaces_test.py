
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
def dhcp_interfaces_api(client):
    return client.network_services.DHCPInterfacesApi(client.network_services.api_client)


def test_list_dhcp_interfaces(dhcp_interfaces_api):
    """Test listing DHCP Interfaces."""
    response = dhcp_interfaces_api.list_dhcp_interfaces(folder=TARGET_FOLDER, limit=200, offset=0)
    assert response is not None
    logger.info(f"Listed DHCP Interfaces successfully")


def test_fetch_dhcp_interfaces(dhcp_interfaces_api):
    """Test fetching a non-existent DHCP Interface returns None."""
    result = dhcp_interfaces_api.fetch_dhcp_interfaces(
        name="non-existent-dhcp-interface-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert result is None, "Should return None for non-existent dhcp interface"
    logger.info("fetch_dhcp_interfaces correctly returned None for non-existent object")
