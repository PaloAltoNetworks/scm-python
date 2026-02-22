
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
def management_interface_settings_api(client):
    return client.device_settings.ManagementInterfaceSettingsApi(client.device_settings.api_client)


def test_list_management_interface_settings(management_interface_settings_api):
    """Test listing management interface settings (singleton per folder)."""
    response = management_interface_settings_api.list_management_interface_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No management interface settings items found")
    logger.info(f"Listed {len(response)} management interface settings items")


def test_get_management_interface_settings_by_id(management_interface_settings_api):
    """Test getting management interface settings by ID."""
    response = management_interface_settings_api.list_management_interface_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = management_interface_settings_api.get_management_interface_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got management interface settings by ID: {obj.id}")


def test_update_management_interface_settings(management_interface_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = management_interface_settings_api.list_management_interface_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = management_interface_settings_api.update_management_interface_settings_by_id(
        id=existing.id,
        management_interface=existing,
    )
    assert updated is not None
    logger.info(f"Updated management interface settings (no-op): {updated.id}")
