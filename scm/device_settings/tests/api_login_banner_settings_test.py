
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
def login_banner_settings_api(client):
    return client.device_settings.LoginBannerSettingsApi(client.device_settings.api_client)


def test_list_login_banner_settings(login_banner_settings_api):
    """Test listing login banner settings (singleton per folder)."""
    response = login_banner_settings_api.list_login_banner_settings(folder=TARGET_FOLDER)
    assert response is not None
    logger.info(f"Listed {len(response)} login banner settings items")


def test_get_login_banner_settings_by_id(login_banner_settings_api):
    """Test getting login banner settings by ID."""
    response = login_banner_settings_api.list_login_banner_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = login_banner_settings_api.get_login_banner_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got login banner settings by ID: {obj.id}")


def test_update_login_banner_settings(login_banner_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = login_banner_settings_api.list_login_banner_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = login_banner_settings_api.update_login_banner_settings_by_id(
        id=existing.id,
        motd_banner_settings=existing,
    )
    assert updated is not None
    logger.info(f"Updated login banner settings (no-op): {updated.id}")
