
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
def general_settings_api(client):
    return client.device_settings.GeneralSettingsApi(client.device_settings.api_client)


def test_list_general_settings(general_settings_api):
    """Test listing general settings (singleton per folder)."""
    response = general_settings_api.list_general_settings(folder=TARGET_FOLDER)
    assert response is not None
    logger.info(f"Listed {len(response)} general settings items")


def test_get_general_settings_by_id(general_settings_api):
    """Test getting general settings by ID."""
    response = general_settings_api.list_general_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = general_settings_api.get_general_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got general settings by ID: {obj.id}")


def test_update_general_settings(general_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = general_settings_api.list_general_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = general_settings_api.update_general_settings_by_id(
        id=existing.id,
        general_settings=existing,
    )
    assert updated is not None
    logger.info(f"Updated general settings (no-op): {updated.id}")
