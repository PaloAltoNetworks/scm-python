
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    TunnelInterfaces,
    TunnelInterfacesIpInner
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
def tunnel_api(client):
    return client.network_services.TunnelInterfacesApi(client.network_services.api_client)

def create_tunnel_interface_payload(name_prefix):
    """Helper to create a Tunnel Interface payload."""
    random_id = uuid.uuid4().hex[:6]
    name = f"${name_prefix}{random_id}"
    
    return TunnelInterfaces(
        name=name,
        folder=TARGET_FOLDER,
        mtu=1450,
        comment="Test Tunnel Interface",
        ip=[TunnelInterfacesIpInner(name="198.18.1.1/32")]
    )

@pytest.fixture
def clean_tunnel_interface(tunnel_api):
    """Fixture for standard CRUD tests."""
    payload = create_tunnel_interface_payload("tun-get-")
    
    logger.info(f"\n[SETUP] Creating Tunnel Interface: {payload.name}")
    created_obj = tunnel_api.create_tunnel_interfaces(tunnel_interfaces=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Tunnel Interface ID: {created_obj.id}")
    try:
        tunnel_api.delete_tunnel_interfaces_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_tunnel_interface(tunnel_api):
    """Test creation of a Tunnel Interface."""
    payload = create_tunnel_interface_payload("tun-create-")

    try:
        created_obj = tunnel_api.create_tunnel_interfaces(tunnel_interfaces=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == payload.name
    assert created_obj.mtu == 1450

    # Cleanup
    tunnel_api.delete_tunnel_interfaces_by_id(id=created_obj.id)


def test_get_tunnel_interface_by_id(tunnel_api, clean_tunnel_interface):
    """Test retrieving a Tunnel Interface by ID."""
    fetched_obj = tunnel_api.get_tunnel_interfaces_by_id(id=clean_tunnel_interface.id)
    assert fetched_obj.id == clean_tunnel_interface.id
    assert fetched_obj.name == clean_tunnel_interface.name
    assert fetched_obj.comment == "Test Tunnel Interface"


def test_update_tunnel_interface(tunnel_api, clean_tunnel_interface):
    """Test updating a Tunnel Interface."""
    update_payload = clean_tunnel_interface
    update_payload.comment = "Updated comment for Tunnel"
    update_payload.mtu = 1400
    # Note: 'defaultValue' logic in Go test maps to 'default_value' in Python if it exists,
    # or it might be specific implementation detail. Focusing on standard fields.
    
    updated_obj = tunnel_api.update_tunnel_interfaces_by_id(
        id=clean_tunnel_interface.id,
        tunnel_interfaces=update_payload
    )
    
    assert updated_obj.id == clean_tunnel_interface.id
    assert updated_obj.comment == "Updated comment for Tunnel"
    assert updated_obj.mtu == 1400


def test_list_tunnel_interfaces(tunnel_api, clean_tunnel_interface):
    """Test listing Tunnel Interfaces."""
    response = tunnel_api.list_tunnel_interfaces(folder=TARGET_FOLDER)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_tunnel_interface.id:
            found = True
            break
    assert found is True


def test_delete_tunnel_interface_by_id(tunnel_api):
    """Test deleting a Tunnel Interface."""
    payload = create_tunnel_interface_payload("tun-del-")
    created_obj = tunnel_api.create_tunnel_interfaces(tunnel_interfaces=payload)
    
    tunnel_api.delete_tunnel_interfaces_by_id(id=created_obj.id)
    
    try:
        tunnel_api.get_tunnel_interfaces_by_id(id=created_obj.id)
        pytest.fail("Interface should be deleted")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
