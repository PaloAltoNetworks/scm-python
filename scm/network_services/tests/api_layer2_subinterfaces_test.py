
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    EthernetInterfaces,
    EthernetInterfacesLayer2,
    Layer2Subinterfaces,
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
def l2_sub_api(client):
    return client.network_services.Layer2SubinterfacesApi(client.network_services.api_client)

# --- Helper Functions ---

def create_l2_parent_interface(eth_api, name_prefix):
    """Creates a Layer 2 Ethernet Interface to serve as a parent."""
    random_id = uuid.uuid4().hex[:6]
    name = f"${name_prefix}{random_id}"
    
    intf = EthernetInterfaces(
		id="",
        name=name,
        comment="Parent for L2 Subinterface Test",
        folder=TARGET_FOLDER,
        link_duplex="full",
        link_speed="auto",
        link_state="up",
        layer2=EthernetInterfacesLayer2()
    )
    
    created_intf = eth_api.create_ethernet_interfaces(ethernet_interfaces=intf)
    return created_intf

def delete_l2_parent_interface(eth_api, intf_id):
    """Cleans up the parent interface."""
    try:
        eth_api.delete_ethernet_interfaces_by_id(id=intf_id)
    except Exception as e:
        logger.warning(f"Failed to delete parent interface: {e}")

# --- Fixtures ---

@pytest.fixture
def parent_l2_interface(eth_api):
    """Fixture to manage the lifecycle of a parent L2 interface."""
    parent = create_l2_parent_interface(eth_api, "l2-parent-")
    yield parent
    delete_l2_parent_interface(eth_api, parent.id)

@pytest.fixture
def clean_l2_subinterface(l2_sub_api, parent_l2_interface):
    """Fixture for standard CRUD tests on L2 Subinterfaces."""
    vlan_tag = "200"
    sub_name = f"{parent_l2_interface.name}.{vlan_tag}"

    payload = Layer2Subinterfaces(
        name=sub_name,
        folder=TARGET_FOLDER,
        parent_interface=parent_l2_interface.name,
        vlan_tag=vlan_tag,
        comment=f"L2 test subinterface for {sub_name}"
    )
    
    logger.info(f"\n[SETUP] Creating L2 Subinterface: {sub_name}")
    created_obj = l2_sub_api.create_layer2_subinterfaces(layer2_subinterfaces=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting L2 Subinterface ID: {created_obj.id}")
    try:
        l2_sub_api.delete_layer2_subinterfaces_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


# --- Tests ---

def test_create_layer2_subinterface(l2_sub_api, parent_l2_interface):
    """
    Test creation of a Layer 2 Subinterface.
    """
    vlan_tag = "400"
    sub_name = f"{parent_l2_interface.name}.{vlan_tag}"

    payload = Layer2Subinterfaces(
        name=sub_name,
        folder=TARGET_FOLDER,
        parent_interface=parent_l2_interface.name,
        vlan_tag=vlan_tag,
        comment=f"L2 test subinterface for {sub_name}"
    )

    try:
        created_obj = l2_sub_api.create_layer2_subinterfaces(layer2_subinterfaces=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == sub_name
    assert created_obj.parent_interface == parent_l2_interface.name

    # Cleanup
    l2_sub_api.delete_layer2_subinterfaces_by_id(id=created_obj.id)


def test_get_layer2_subinterface_by_id(l2_sub_api, clean_l2_subinterface):
    """
    Test retrieving a Layer 2 Subinterface by ID.
    """
    fetched_obj = l2_sub_api.get_layer2_subinterfaces_by_id(id=clean_l2_subinterface.id)
    assert fetched_obj.id == clean_l2_subinterface.id
    assert fetched_obj.name == clean_l2_subinterface.name
    assert fetched_obj.parent_interface == clean_l2_subinterface.parent_interface


def test_update_layer2_subinterface(l2_sub_api, clean_l2_subinterface):
    """
    Test updating a Layer 2 Subinterface.
    """
    update_payload = clean_l2_subinterface
    update_payload.comment = "Updated Comment"
    
    updated_obj = l2_sub_api.update_layer2_subinterfaces_by_id(
        id=clean_l2_subinterface.id,
        layer2_subinterfaces=update_payload
    )
    
    assert updated_obj.id == clean_l2_subinterface.id
    assert updated_obj.comment == "Updated Comment"


def test_list_layer2_subinterfaces(l2_sub_api, clean_l2_subinterface):
    """
    Test listing Layer 2 Subinterfaces.
    """
    response = l2_sub_api.list_layer2_subinterfaces(folder=TARGET_FOLDER, limit=10)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_l2_subinterface.id:
            found = True
            break
    assert found is True




def test_fetch_layer2_subinterfaces(l2_sub_api, clean_l2_subinterface):
    """
    Test fetching a single layer2_subinterfaces by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = l2_sub_api.fetch_layer2_subinterfaces(
        name=clean_l2_subinterface.name,
        folder=clean_l2_subinterface.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found layer2_subinterfaces '{clean_l2_subinterface.name}'"
    assert fetched_obj.id == clean_l2_subinterface.id
    assert fetched_obj.name == clean_l2_subinterface.name
    assert fetched_obj.folder == clean_l2_subinterface.folder
    logger.info(f"\n[SUCCESS] fetch_layer2_subinterfaces found object: {fetched_obj.name}")

    # Test fetching non-existent layer2_subinterfaces (should return None)
    not_found = l2_sub_api.fetch_layer2_subinterfaces(
        name="non-existent-layer2_subinterfaces-xyz-12345",
        folder=clean_l2_subinterface.folder
    )
    assert not_found is None, "Should return None for non-existent layer2_subinterfaces"
    logger.info(f"\n[SUCCESS] fetch_layer2_subinterfaces correctly returned None for non-existent layer2_subinterfaces")


def test_delete_layer2_subinterface_by_id(l2_sub_api, parent_l2_interface):
    """
    Test deleting a Layer 2 Subinterface.
    """
    vlan_tag = "500"
    sub_name = f"{parent_l2_interface.name}.{vlan_tag}"

    payload = Layer2Subinterfaces(
        name=sub_name,
        folder=TARGET_FOLDER,
        parent_interface=parent_l2_interface.name,
        vlan_tag=vlan_tag
    )
    
    created_obj = l2_sub_api.create_layer2_subinterfaces(layer2_subinterfaces=payload)
    
    l2_sub_api.delete_layer2_subinterfaces_by_id(id=created_obj.id)
    
    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        l2_sub_api.get_layer2_subinterfaces_by_id(id=created_obj.id)
        pytest.fail("Subinterface should be deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
