
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
def device_redistribution_collector_settings_api(client):
    return client.device_settings.DeviceRedistributionCollectorSettingsApi(client.device_settings.api_client)


def test_list_device_redistribution_collector_settings(device_redistribution_collector_settings_api):
    """Test listing device redistribution collector settings (singleton per folder)."""
    response = device_redistribution_collector_settings_api.list_device_redistribution_collector_settings(folder=TARGET_FOLDER)
    assert response is not None
    logger.info(f"Listed {len(response)} device redistribution collector settings items")


def test_get_device_redistribution_collector_settings_by_id(device_redistribution_collector_settings_api):
    """Test getting device redistribution collector settings by ID."""
    response = device_redistribution_collector_settings_api.list_device_redistribution_collector_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = device_redistribution_collector_settings_api.get_device_redistribution_collector_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got device redistribution collector settings by ID: {obj.id}")


def test_update_device_redistribution_collector_settings(device_redistribution_collector_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = device_redistribution_collector_settings_api.list_device_redistribution_collector_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = device_redistribution_collector_settings_api.update_device_redistribution_collector_settings_by_id(
        id=existing.id,
        device_redistribution_collector=existing,
    )
    assert updated is not None
    logger.info(f"Updated device redistribution collector settings (no-op): {updated.id}")
