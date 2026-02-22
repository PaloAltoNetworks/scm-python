
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
def service_route_settings_api(client):
    return client.device_settings.ServiceRouteSettingsApi(client.device_settings.api_client)


def test_list_service_route_settings(service_route_settings_api):
    """Test listing service route settings (singleton per folder)."""
    response = service_route_settings_api.list_service_route_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No service route settings items found")
    logger.info(f"Listed {len(response)} service route settings items")


def test_get_service_route_settings_by_id(service_route_settings_api):
    """Test getting service route settings by ID."""
    response = service_route_settings_api.list_service_route_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to get")
    obj = service_route_settings_api.get_service_route_settings_by_id(id=response[0].id)
    assert obj is not None
    assert obj.id == response[0].id
    logger.info(f"Got service route settings by ID: {obj.id}")


def test_update_service_route_settings(service_route_settings_api):
    """No-op update: get existing settings and update with same data."""
    response = service_route_settings_api.list_service_route_settings(folder=TARGET_FOLDER)
    assert response is not None
    if not response or len(response) == 0:
        pytest.skip("No items to update")
    existing = response[0]
    updated = service_route_settings_api.update_service_route_settings_by_id(
        id=existing.id,
        service_route=existing,
    )
    assert updated is not None
    logger.info(f"Updated service route settings (no-op): {updated.id}")
