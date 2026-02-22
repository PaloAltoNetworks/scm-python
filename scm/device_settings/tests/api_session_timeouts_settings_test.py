
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
def session_timeouts_settings_api(client):
    return client.device_settings.SessionTimeoutsSettingsApi(client.device_settings.api_client)


def test_list_session_timeouts_settings(session_timeouts_settings_api):
    """Test listing session timeouts settings (singleton per folder)."""
    response = session_timeouts_settings_api.list_session_timeouts_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No session timeouts settings items found")
    logger.info(f"Listed {len(response)} session timeouts settings items")


def test_get_session_timeouts_settings_by_id(session_timeouts_settings_api):
    """Test getting session timeouts settings by ID."""
    response = session_timeouts_settings_api.list_session_timeouts_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = session_timeouts_settings_api.get_session_timeouts_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got session timeouts settings by ID: {obj.id}")


def test_update_session_timeouts_settings(session_timeouts_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = session_timeouts_settings_api.list_session_timeouts_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = session_timeouts_settings_api.update_session_timeouts_settings_by_id(
        id=existing.id,
        session_timeouts=existing,
    )
    assert updated is not None
    logger.info(f"Updated session timeouts settings (no-op): {updated.id}")
