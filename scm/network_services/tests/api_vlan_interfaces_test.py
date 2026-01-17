
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    VlanInterfaces,
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
def vlan_api(client):
    return client.network_services.VLANInterfacesApi(client.network_services.api_client)

def create_vlan_interface_payload(name_prefix):
    """Helper to create a VLAN Interface payload."""
    random_id = uuid.uuid4().hex[:6]
    name = f"$scm_vlan_if-{random_id}" # VLAN interfaces often need specific naming or prefixes
    
    return VlanInterfaces(
        name=name,
        folder=TARGET_FOLDER,
        mtu=1500,
        comment="Test VLAN Interface"
    )

@pytest.fixture
def clean_vlan_interface(vlan_api):
    """Fixture for standard CRUD tests."""
    payload = create_vlan_interface_payload("get-")
    
    logger.info(f"\n[SETUP] Creating VLAN Interface: {payload.name}")
    created_obj = vlan_api.create_vlan_interfaces(vlan_interfaces=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting VLAN Interface ID: {created_obj.id}")
    try:
        vlan_api.delete_vlan_interfaces_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_vlan_interface(vlan_api):
    """Test creation of a VLAN Interface."""
    payload = create_vlan_interface_payload("create-")

    try:
        created_obj = vlan_api.create_vlan_interfaces(vlan_interfaces=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == payload.name
    assert created_obj.mtu == 1500

    # Cleanup
    vlan_api.delete_vlan_interfaces_by_id(id=created_obj.id)


def test_get_vlan_interface_by_id(vlan_api, clean_vlan_interface):
    """Test retrieving a VLAN Interface by ID."""
    fetched_obj = vlan_api.get_vlan_interfaces_by_id(id=clean_vlan_interface.id)
    assert fetched_obj.id == clean_vlan_interface.id
    assert fetched_obj.name == clean_vlan_interface.name
    assert fetched_obj.comment == "Test VLAN Interface"


def test_update_vlan_interface(vlan_api, clean_vlan_interface):
    """Test updating a VLAN Interface."""
    update_payload = clean_vlan_interface
    update_payload.comment = "Updated comment for VLAN 30"
    update_payload.mtu = 1400
    
    # NOTE: SetVlanTag("300") logic from Go maps to 'vlan_tag' in Python if model supports it
    # update_payload.vlan_tag = "300"
    
    updated_obj = vlan_api.update_vlanl_interfaces_by_id(
        id=clean_vlan_interface.id,
        vlan_interfaces=update_payload
    )
    
    assert updated_obj.id == clean_vlan_interface.id
    assert updated_obj.comment == "Updated comment for VLAN 30"
    assert updated_obj.mtu == 1400


def test_list_vlan_interfaces(vlan_api, clean_vlan_interface):
    """Test listing VLAN Interfaces."""
    response = vlan_api.list_vlan_interfaces(folder=TARGET_FOLDER, limit=10)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_vlan_interface.id:
            found = True
            break
    assert found is True


def test_delete_vlan_interface_by_id(vlan_api):
    """Test deleting a VLAN Interface."""
    payload = create_vlan_interface_payload("del-")
    created_obj = vlan_api.create_vlan_interfaces(vlan_interfaces=payload)
    
    vlan_api.delete_vlan_interfaces_by_id(id=created_obj.id)
    
    try:
        vlan_api.get_vlan_interfaces_by_id(id=created_obj.id)
        pytest.fail("Interface should be deleted")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
