
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    AggregateInterfaces,
    AggregateInterfacesLayer2,
    AggregateInterfacesLayer3,
    AggregateInterfacesLayer3IpInner,
    AggEthernetDhcpClientDhcpClient,
    Lacp
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
def agg_api(client):
    return client.network_services.AggregateInterfacesApi(client.network_services.api_client)

def create_base_aggregate_interface(name_prefix):
    """Helper to create a base AggregateInterface object."""
    random_id = uuid.uuid4().hex[:4]
    name = f"${name_prefix}{random_id}"

    return AggregateInterfaces(
        name=name,
        comment="Managed by Python Test",
        folder=TARGET_FOLDER
    )

@pytest.fixture
def clean_agg_interface(agg_api):
    """
    Fixture for standard CRUD tests (L3 Static setup).
    """
    intf = create_base_aggregate_interface("ae-get-")

    # L3 Static Configuration
    l3_config = AggregateInterfacesLayer3(
        ip=[AggregateInterfacesLayer3IpInner(name="198.18.1.1/24")]
    )
    intf.layer3 = l3_config

    logger.info(f"\n[SETUP] Creating Aggregate Interface: {intf.name}")
    created_obj = agg_api.create_aggregate_interfaces(aggregate_interfaces=intf)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Aggregate Interface ID: {created_obj.id}")
    try:
        agg_api.delete_aggregate_interfaces_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_aggregate_interface_l2(agg_api):
    """
    Test creation of a Layer 2 Aggregate Interface with LACP.
    """
    intf = create_base_aggregate_interface("ae-l2-")

    # FIX: Use a valid VLAN ID (1-4094). '6666' causes Pydantic validation error.
    l2_config = AggregateInterfacesLayer2(
        lacp=Lacp(enable=True),
        vlan_tag="200"
    )
    intf.layer2 = l2_config

    try:
        created_obj = agg_api.create_aggregate_interfaces(aggregate_interfaces=intf)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.layer2 is not None
    assert created_obj.layer2.vlan_tag == "200"
    assert created_obj.layer3 is None

    # Cleanup
    agg_api.delete_aggregate_interfaces_by_id(id=created_obj.id)


def test_create_aggregate_interface_l3_dhcp(agg_api):
    """
    Test creation of a Layer 3 Aggregate Interface with DHCP.
    """
    intf = create_base_aggregate_interface("ae-l3-dhcp-")

    # Use the corrected model name 'AggEthernetDhcpClientDhcpClient'
    dhcp_config = AggEthernetDhcpClientDhcpClient(
        enable=True,
        create_default_route=True,
        default_route_metric=10
    )
    l3_config = AggregateInterfacesLayer3(dhcp_client=dhcp_config)
    intf.layer3 = l3_config

    try:
        created_obj = agg_api.create_aggregate_interfaces(aggregate_interfaces=intf)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.layer3 is not None
    assert created_obj.layer3.dhcp_client.enable is True

    # Cleanup
    agg_api.delete_aggregate_interfaces_by_id(id=created_obj.id)


def test_get_aggregate_interface_by_id(agg_api, clean_agg_interface):
    """
    Test retrieving an Aggregate Interface by ID.
    """
    fetched_obj = agg_api.get_aggregate_interfaces_by_id(id=clean_agg_interface.id)
    assert fetched_obj.id == clean_agg_interface.id
    assert fetched_obj.name == clean_agg_interface.name
    assert fetched_obj.layer3 is not None


def test_update_aggregate_interface(agg_api, clean_agg_interface):
    """
    Test updating an Aggregate Interface (Switch from L3 to L2).
    """
    update_payload = clean_agg_interface

    # Switch to L2 with valid VLAN
    update_payload.layer3 = None
    update_payload.layer2 = AggregateInterfacesLayer2(vlan_tag="555")
    update_payload.comment = "Updated to L2"

    updated_obj = agg_api.update_aggregate_interfaces_by_id(
        id=clean_agg_interface.id,
        aggregate_interfaces=update_payload
    )

    assert updated_obj.id == clean_agg_interface.id
    assert updated_obj.layer3 is None
    assert updated_obj.layer2 is not None
    assert updated_obj.layer2.vlan_tag == "555"


def test_list_aggregate_interfaces(agg_api, clean_agg_interface):
    """
    Test listing Aggregate Interfaces.
    """
    response = agg_api.list_aggregate_interfaces(folder=TARGET_FOLDER, limit=10)
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_agg_interface.id:
            found = True
            break
    assert found is True




def test_fetch_aggregate_interfaces(agg_api, clean_agg_interface):
    """
    Test fetching a single aggregate_interfaces by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = agg_api.fetch_aggregate_interfaces(
        name=clean_agg_interface.name,
        folder=clean_agg_interface.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found aggregate_interfaces '{clean_agg_interface.name}'"
    assert fetched_obj.id == clean_agg_interface.id
    assert fetched_obj.name == clean_agg_interface.name
    assert fetched_obj.folder == clean_agg_interface.folder
    logger.info(f"\n[SUCCESS] fetch_aggregate_interfaces found object: {fetched_obj.name}")

    # Test fetching non-existent aggregate_interfaces (should return None)
    not_found = agg_api.fetch_aggregate_interfaces(
        name="non-existent-aggregate_interfaces-xyz-12345",
        folder=clean_agg_interface.folder
    )
    assert not_found is None, "Should return None for non-existent aggregate_interfaces"
    logger.info(f"\n[SUCCESS] fetch_aggregate_interfaces correctly returned None for non-existent aggregate_interfaces")


def test_delete_aggregate_interface_by_id(agg_api):
    """
    Test deleting an Aggregate Interface.
    """
    intf = create_base_aggregate_interface("ae-del-")
    intf.layer2 = AggregateInterfacesLayer2(vlan_tag="100") # Ensure valid L2 config

    created_obj = agg_api.create_aggregate_interfaces(aggregate_interfaces=intf)

    agg_api.delete_aggregate_interfaces_by_id(id=created_obj.id)

    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        agg_api.get_aggregate_interfaces_by_id(id=created_obj.id)
        pytest.fail("Interface should be deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
