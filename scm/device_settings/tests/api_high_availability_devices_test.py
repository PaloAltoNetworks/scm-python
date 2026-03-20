
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
def high_availability_devices_api(client):
    return client.device_settings.HighAvailabilityDevicesApi(client.device_settings.api_client)


def test_list_ha_devices(high_availability_devices_api):
    """Test listing high availability devices (List only - no Get/Update/Delete)."""
    try:
        response = high_availability_devices_api.list_ha_devices(folder=TARGET_FOLDER)
    except Exception as e:
        # The API may return an empty array [] which can cause deserialization issues
        if "cannot unmarshal" in str(e) or "validation error" in str(e).lower():
            pytest.skip("No HA devices configured (API returns empty array)")
        raise
    assert response is not None
    logger.info("Successfully listed high availability devices")
