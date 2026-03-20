
import logging
import pytest
from scm import Scm
from scm.network_services.models.auto_vpn_settings import AutoVpnSettings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def auto_vpn_settings_api(client):
    return client.network_services.AutoVPNSettingsApi(client.network_services.api_client)


def test_get_auto_vpn_settings(auto_vpn_settings_api):
    """
    Test retrieving Auto VPN settings (singleton resource).
    Equivalent to Go: Test_network_services_AutoVPNSettingsAPIService_Get
    """
    result = auto_vpn_settings_api.get_auto_vpn_settings()

    assert result is not None
    logger.info(f"Successfully retrieved auto VPN settings")


def test_update_auto_vpn_settings(auto_vpn_settings_api):
    """
    Test updating Auto VPN settings with a no-op update (read-back existing settings).
    Equivalent to Go: Test_network_services_AutoVPNSettingsAPIService_Update
    """
    # Get existing settings
    existing = auto_vpn_settings_api.get_auto_vpn_settings()
    assert existing is not None

    # Perform no-op update with same data
    updated = auto_vpn_settings_api.update_auto_vpn_settings(
        auto_vpn_settings=existing,
    )

    assert updated is not None
    logger.info(f"Successfully updated auto VPN settings (no-op)")
