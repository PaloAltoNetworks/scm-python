
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    EthernetInterfaces,
    EthernetInterfacesLayer2,
    EthernetInterfacesLayer3,
    EthernetInterfacesLayer3IpInner,
    EthernetInterfacesLayer3DhcpClient
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

@pytest.fixture
def clean_eth_interface(eth_api):
    """
    Fixture for standard CRUD tests (Get/Update/List/Delete).
    Creates an L2 interface.
    """
    # Create valid payload immediately with Layer 2 to avoid validation error
    random_id = uuid.uuid4().hex[:4]
    name = f"$get-intf-{random_id}"

    intf = EthernetInterfaces(
        id="",
        name=name,
        comment="Managed by Python Test",
        folder=TARGET_FOLDER,
        layer2=EthernetInterfacesLayer2()
    )

    logger.info(f"\n[SETUP] Creating Ethernet Interface: {intf.name}")
    created_obj = eth_api.create_ethernet_interfaces(ethernet_interfaces=intf)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Ethernet Interface ID: {created_obj.id}")
    try:
        eth_api.delete_ethernet_interfaces_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


# --- Create Mode Tests ---

def test_create_ethernet_interface_l2(eth_api):
    """
    Test creation of a Layer 2 Ethernet Interface.
    """
    random_id = uuid.uuid4().hex[:4]
    name = f"$l2-intf-{random_id}"

    # Construct full object at once to satisfy Pydantic validation
    intf = EthernetInterfaces(
        id="",
        name=name,
        comment="Managed by Python Test",
        folder=TARGET_FOLDER,
        link_duplex="full",
        link_speed="auto",
        link_state="up",
        layer2=EthernetInterfacesLayer2()
    )

    try:
        created_obj = eth_api.create_ethernet_interfaces(ethernet_interfaces=intf)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.layer2 is not None
    assert created_obj.layer3 is None

    # Cleanup
    eth_api.delete_ethernet_interfaces_by_id(id=created_obj.id)


def test_create_ethernet_interface_l3_static(eth_api):
    """
    Test creation of a Layer 3 Ethernet Interface with Static IP.
    """
    random_id = uuid.uuid4().hex[:4]
    name = f"$l3-stat-{random_id}"

    # Configure L3 Static IP
    l3_config = EthernetInterfacesLayer3(
        ip=[EthernetInterfacesLayer3IpInner(name="198.18.1.1/24")]
    )

    intf = EthernetInterfaces(
        id="",
        name=name,
        comment="Managed by Python Test",
        folder=TARGET_FOLDER,
        layer3=l3_config
    )

    try:
        created_obj = eth_api.create_ethernet_interfaces(ethernet_interfaces=intf)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.layer3 is not None
    assert len(created_obj.layer3.ip) == 1
    assert created_obj.layer3.ip[0].name == "198.18.1.1/24"

    # Cleanup
    eth_api.delete_ethernet_interfaces_by_id(id=created_obj.id)


def test_create_ethernet_interface_l3_dhcp(eth_api):
    """
    Test creation of a Layer 3 Ethernet Interface with DHCP Client.
    """
    random_id = uuid.uuid4().hex[:4]
    name = f"$l3-dhcp-{random_id}"

    # Configure L3 DHCP
    dhcp_config = EthernetInterfacesLayer3DhcpClient(
        enable=True,
        create_default_route=True,
        default_route_metric=10
    )
    l3_config = EthernetInterfacesLayer3(dhcp_client=dhcp_config)

    intf = EthernetInterfaces(
        id="",
        name=name,
        comment="Managed by Python Test",
        folder=TARGET_FOLDER,
        layer3=l3_config
    )

    try:
        created_obj = eth_api.create_ethernet_interfaces(ethernet_interfaces=intf)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.layer3 is not None
    assert created_obj.layer3.dhcp_client is not None
    assert created_obj.layer3.dhcp_client.enable is True

    # Cleanup
    eth_api.delete_ethernet_interfaces_by_id(id=created_obj.id)


# --- CRUD Tests ---

def test_get_ethernet_interface_by_id(eth_api, clean_eth_interface):
    """
    Test retrieving an Ethernet Interface by ID.
    """
    fetched_obj = eth_api.get_ethernet_interfaces_by_id(id=clean_eth_interface.id)
    assert fetched_obj.id == clean_eth_interface.id
    assert fetched_obj.name == clean_eth_interface.name
    assert fetched_obj.layer2 is not None


def test_update_ethernet_interface(eth_api, clean_eth_interface):
    """
    Test updating an Ethernet Interface (Change comment).
    """
    update_payload = clean_eth_interface
    update_payload.comment = "Updated Comment"

    updated_obj = eth_api.update_ethernet_interfaces_by_id(
        id=clean_eth_interface.id,
        ethernet_interfaces=update_payload
    )

    assert updated_obj.id == clean_eth_interface.id
    assert updated_obj.comment == "Updated Comment"


def test_list_ethernet_interfaces(eth_api, clean_eth_interface):
    """
    Test listing Ethernet Interfaces.
    """
    response = eth_api.list_ethernet_interfaces(folder=TARGET_FOLDER, limit=10)
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_eth_interface.id:
            found = True
            break
    assert found is True


def test_delete_ethernet_interface_by_id(eth_api):
    """
    Test deleting an Ethernet Interface.
    """
    random_id = uuid.uuid4().hex[:4]
    name = f"$del-intf-{random_id}"

    intf = EthernetInterfaces(
        id="",
        name=name,
        comment="Managed by Python Test",
        folder=TARGET_FOLDER,
        layer2=EthernetInterfacesLayer2()
    )

    created_obj = eth_api.create_ethernet_interfaces(ethernet_interfaces=intf)

    eth_api.delete_ethernet_interfaces_by_id(id=created_obj.id)

    try:
        eth_api.get_ethernet_interfaces_by_id(id=created_obj.id)
        pytest.fail("Interface should be deleted")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
