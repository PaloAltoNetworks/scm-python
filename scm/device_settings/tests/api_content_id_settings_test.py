
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
def content_id_settings_api(client):
    return client.device_settings.ContentIDSettingsApi(client.device_settings.api_client)


def test_list_content_id_settings(content_id_settings_api):
    """Test listing content ID settings (singleton per folder)."""
    response = content_id_settings_api.list_content_id_settings(folder=TARGET_FOLDER)
    assert response is not None
    logger.info(f"Listed {len(response)} content ID settings items")


def test_get_content_id_settings_by_id(content_id_settings_api):
    """Test getting content ID settings by ID."""
    response = content_id_settings_api.list_content_id_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items — device-specific setting, requires managed device")
    obj = content_id_settings_api.get_content_id_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got content ID settings by ID: {obj.id}")


def test_update_content_id_settings(content_id_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = content_id_settings_api.list_content_id_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items — device-specific setting, requires managed device")
    existing = response[0]
    updated = content_id_settings_api.update_content_id_settings_by_id(
        id=existing.id,
        content_id_settings=existing,
    )
    assert updated is not None
    logger.info(f"Updated content ID settings (no-op): {updated.id}")
