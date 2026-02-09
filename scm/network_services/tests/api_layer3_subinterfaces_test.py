
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    EthernetInterfaces,
    EthernetInterfacesLayer3,
    Layer3Subinterfaces,
    Layer3SubinterfacesIpInner
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
def eth_api(client):
    return client.network_services.EthernetInterfacesApi(client.network_services.api_client)

@pytest.fixture(scope="module")
def l3_sub_api(client):
    return client.network_services.Layer3SubinterfacesApi(client.network_services.api_client)

# --- Helper Functions ---

def create_l3_parent_interface(eth_api, name_prefix):
    """Creates a Layer 3 Ethernet Interface to serve as a parent."""
    random_id = uuid.uuid4().hex[:6]
    name = f"${name_prefix}{random_id}"
    
    intf = EthernetInterfaces(
		id="",
        name=name,
        comment="Parent for L3 Subinterface Test",
        folder=TARGET_FOLDER,
        link_duplex="full",
        link_speed="auto",
        link_state="up",
        layer3=EthernetInterfacesLayer3()
    )
    
    created_intf = eth_api.create_ethernet_interfaces(ethernet_interfaces=intf)
    return created_intf

def delete_l3_parent_interface(eth_api, intf_id):
    """Cleans up the parent interface."""
    try:
        eth_api.delete_ethernet_interfaces_by_id(id=intf_id)
    except Exception as e:
        logger.warning(f"Failed to delete parent interface: {e}")

# --- Fixtures ---

@pytest.fixture
def parent_l3_interface(eth_api):
    """Fixture to manage the lifecycle of a parent L3 interface."""
    parent = create_l3_parent_interface(eth_api, "l3-parent-")
    yield parent
    delete_l3_parent_interface(eth_api, parent.id)

@pytest.fixture
def clean_l3_subinterface(l3_sub_api, parent_l3_interface):
    """Fixture for standard CRUD tests on L3 Subinterfaces."""
    vlan_tag = 200
    sub_name = f"{parent_l3_interface.name}.{vlan_tag}"
    
    payload = Layer3Subinterfaces(
        name=sub_name,
        folder=TARGET_FOLDER,
        parent_interface=parent_l3_interface.name,
        tag=vlan_tag,
        comment=f"L3 test subinterface for {sub_name}",
        mtu=1500,
        ip=[Layer3SubinterfacesIpInner(name="192.168.10.1/24")]
    )
    
    logger.info(f"\n[SETUP] Creating L3 Subinterface: {sub_name}")
    created_obj = l3_sub_api.create_layer3_subinterfaces(layer3_subinterfaces=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting L3 Subinterface ID: {created_obj.id}")
    try:
        l3_sub_api.delete_layer3_subinterfaces_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


# --- Tests ---

def test_create_layer3_subinterface(l3_sub_api, parent_l3_interface):
    """
    Test creation of a Layer 3 Subinterface.
    """
    vlan_tag = 400
    sub_name = f"{parent_l3_interface.name}.{vlan_tag}"
    
    payload = Layer3Subinterfaces(
        name=sub_name,
        folder=TARGET_FOLDER,
        parent_interface=parent_l3_interface.name,
        tag=vlan_tag,
        comment=f"L3 test subinterface for {sub_name}",
        mtu=1500,
        ip=[Layer3SubinterfacesIpInner(name="192.168.20.1/24")]
    )

    try:
        created_obj = l3_sub_api.create_layer3_subinterfaces(layer3_subinterfaces=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == sub_name
    assert created_obj.parent_interface == parent_l3_interface.name
    assert len(created_obj.ip) == 1

    # Cleanup
    l3_sub_api.delete_layer3_subinterfaces_by_id(id=created_obj.id)


def test_get_layer3_subinterface_by_id(l3_sub_api, clean_l3_subinterface):
    """
    Test retrieving a Layer 3 Subinterface by ID.
    """
    fetched_obj = l3_sub_api.get_layer3_subinterfaces_by_id(id=clean_l3_subinterface.id)
    assert fetched_obj.id == clean_l3_subinterface.id
    assert fetched_obj.name == clean_l3_subinterface.name
    assert fetched_obj.mtu == 1500


def test_update_layer3_subinterface(l3_sub_api, clean_l3_subinterface):
    """
    Test updating a Layer 3 Subinterface.
    """
    update_payload = clean_l3_subinterface
    update_payload.comment = "Updated Comment"
    update_payload.mtu = 1400
    
    updated_obj = l3_sub_api.update_layer3_subinterfaces_by_id(
        id=clean_l3_subinterface.id,
        layer3_subinterfaces=update_payload
    )
    
    assert updated_obj.id == clean_l3_subinterface.id
    assert updated_obj.comment == "Updated Comment"
    assert updated_obj.mtu == 1400


def test_list_layer3_subinterfaces(l3_sub_api, clean_l3_subinterface):
    """
    Test listing Layer 3 Subinterfaces.
    """
    response = l3_sub_api.list_layer3_subinterfaces(folder=TARGET_FOLDER, limit=10)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_l3_subinterface.id:
            found = True
            break
    assert found is True




def test_fetch_layer3_subinterfaces(l3_sub_api, clean_l3_subinterface):
    """
    Test fetching a single layer3_subinterfaces by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = l3_sub_api.fetch_layer3_subinterfaces(
        name=clean_l3_subinterface.name,
        folder=clean_l3_subinterface.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found layer3_subinterfaces '{clean_l3_subinterface.name}'"
    assert fetched_obj.id == clean_l3_subinterface.id
    assert fetched_obj.name == clean_l3_subinterface.name
    assert fetched_obj.folder == clean_l3_subinterface.folder
    logger.info(f"\n[SUCCESS] fetch_layer3_subinterfaces found object: {fetched_obj.name}")

    # Test fetching non-existent layer3_subinterfaces (should return None)
    not_found = l3_sub_api.fetch_layer3_subinterfaces(
        name="non-existent-layer3_subinterfaces-xyz-12345",
        folder=clean_l3_subinterface.folder
    )
    assert not_found is None, "Should return None for non-existent layer3_subinterfaces"
    logger.info(f"\n[SUCCESS] fetch_layer3_subinterfaces correctly returned None for non-existent layer3_subinterfaces")


def test_delete_layer3_subinterface_by_id(l3_sub_api, parent_l3_interface):
    """
    Test deleting a Layer 3 Subinterface.
    """
    vlan_tag = 500
    sub_name = f"{parent_l3_interface.name}.{vlan_tag}"
    
    payload = Layer3Subinterfaces(
        name=sub_name,
        folder=TARGET_FOLDER,
        parent_interface=parent_l3_interface.name,
        tag=vlan_tag
    )
    
    created_obj = l3_sub_api.create_layer3_subinterfaces(layer3_subinterfaces=payload)
    
    l3_sub_api.delete_layer3_subinterfaces_by_id(id=created_obj.id)
    
    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        l3_sub_api.get_layer3_subinterfaces_by_id(id=created_obj.id)
        pytest.fail("Subinterface should be deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
