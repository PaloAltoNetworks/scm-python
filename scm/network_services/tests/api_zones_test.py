
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    Zones,
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "All"

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def zones_api(client):
    return client.network_services.SecurityZonesApi(client.network_services.api_client)

def create_test_zone(name_prefix):
    """Helper to create a minimal Zone object."""
    random_id = uuid.uuid4().hex[:6]
    name = f"{name_prefix}{random_id}"
    return Zones(name=name)

def create_full_test_zone(name_prefix):
    """Helper to create a comprehensive Zone object."""
    zone = create_test_zone(name_prefix)
    zone.folder = TARGET_FOLDER
    zone.enable_device_identification = True
    zone.enable_user_identification = True
    return zone

@pytest.fixture
def clean_zone(zones_api):
    """Fixture for standard CRUD tests."""
    zone = create_full_test_zone("scm-zone-get-")
    
    logger.info(f"\n[SETUP] Creating Zone: {zone.name}")
    created_obj = zones_api.create_zones(zones=zone)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Zone ID: {created_obj.id}")
    try:
        zones_api.delete_zones_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_zone(zones_api):
    """Test creation of a Security Zone."""
    zone = create_full_test_zone("scm-zone-create-")

    try:
        created_obj = zones_api.create_zones(zones=zone)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == zone.name
    assert created_obj.enable_device_identification is True

    # Cleanup
    zones_api.delete_zones_by_id(id=created_obj.id)


def test_get_zone_by_id(zones_api, clean_zone):
    """Test retrieving a Security Zone by ID."""
    fetched_obj = zones_api.get_zones_by_id(id=clean_zone.id)
    assert fetched_obj.id == clean_zone.id
    assert fetched_obj.name == clean_zone.name
    assert fetched_obj.enable_user_identification is True


def test_update_zone(zones_api, clean_zone):
    """Test updating a Security Zone."""
    update_payload = clean_zone
    update_payload.enable_device_identification = False
    
    updated_obj = zones_api.update_zones_by_id(
        id=clean_zone.id,
        zones=update_payload
    )
    
    assert updated_obj.id == clean_zone.id
    assert updated_obj.enable_device_identification is False


def test_list_zones(zones_api, clean_zone):
    """Test listing Security Zones."""
    response = zones_api.list_zones(folder=TARGET_FOLDER, limit=10)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_zone.id:
            found = True
            break
    assert found is True


def test_delete_zone_by_id(zones_api):
    """Test deleting a Security Zone."""
    zone = create_full_test_zone("scm-zone-del-")
    created_obj = zones_api.create_zones(zones=zone)
    
    zones_api.delete_zones_by_id(id=created_obj.id)
    
    try:
        zones_api.get_zones_by_id(id=created_obj.id)
        pytest.fail("Zone should be deleted")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
