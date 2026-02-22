
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
def authentication_settings_api(client):
    return client.device_settings.AuthenticationSettingsApi(client.device_settings.api_client)


def test_list_authentication_settings(authentication_settings_api):
    """Test listing authentication settings (singleton per folder)."""
    response = authentication_settings_api.list_authentication_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No authentication settings items found")
    logger.info(f"Listed {len(response)} authentication settings items")


def test_get_authentication_settings_by_id(authentication_settings_api):
    """Test getting authentication settings by ID."""
    response = authentication_settings_api.list_authentication_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = authentication_settings_api.get_authentication_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got authentication settings by ID: {obj.id}")


def test_update_authentication_settings(authentication_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = authentication_settings_api.list_authentication_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = authentication_settings_api.update_authentication_settings_by_id(
        id=existing.id,
        authentication_settings=existing,
    )
    assert updated is not None
    logger.info(f"Updated authentication settings (no-op): {updated.id}")
