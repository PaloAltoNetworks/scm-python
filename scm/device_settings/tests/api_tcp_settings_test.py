
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
def tcp_settings_api(client):
    return client.device_settings.TCPSettingsApi(client.device_settings.api_client)


def test_list_tcp_settings(tcp_settings_api):
    """Test listing TCP settings (singleton per folder)."""
    response = tcp_settings_api.list_tcp_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No TCP settings items found")
    logger.info(f"Listed {len(response)} TCP settings items")


def test_get_tcp_settings_by_id(tcp_settings_api):
    """Test getting TCP settings by ID."""
    response = tcp_settings_api.list_tcp_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = tcp_settings_api.get_tcp_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got TCP settings by ID: {obj.id}")


def test_update_tcp_settings(tcp_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = tcp_settings_api.list_tcp_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = tcp_settings_api.update_tcp_settings_by_id(
        id=existing.id,
        tcp_settings=existing,
    )
    assert updated is not None
    logger.info(f"Updated TCP settings (no-op): {updated.id}")
