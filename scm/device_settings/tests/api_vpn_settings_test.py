
import logging
import pytest
from scm import Scm

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
def vpn_settings_api(client):
    return client.device_settings.VPNSettingsApi(client.device_settings.api_client)


def test_list_vpn_settings(vpn_settings_api):
    """Test listing VPN settings (singleton per folder)."""
    response = vpn_settings_api.list_vpn_settings(folder=TARGET_FOLDER)
    assert response is not None
    logger.info(f"Listed {len(response)} VPN settings items")


def test_get_vpn_settings_by_id(vpn_settings_api):
    """Test getting VPN settings by ID."""
    response = vpn_settings_api.list_vpn_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = vpn_settings_api.get_vpn_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got VPN settings by ID: {obj.id}")


def test_update_vpn_settings(vpn_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = vpn_settings_api.list_vpn_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = vpn_settings_api.update_vpn_settings_by_id(
        id=existing.id,
        vpn_settings=existing,
    )
    assert updated is not None
    logger.info(f"Updated VPN settings (no-op): {updated.id}")
