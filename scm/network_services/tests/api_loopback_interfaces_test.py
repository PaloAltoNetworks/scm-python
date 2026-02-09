import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.loopback_interfaces import LoopbackInterfaces
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
# -----------------------------------------------------------------------------


def generate_loopback_name(base):
    """Generate a valid loopback interface name starting with $."""
    return f"${base}{uuid.uuid4().hex[:4]}"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def loopback_interfaces_api(client):
    return client.network_services.LoopbackInterfacesApi(client.network_services.api_client)


@pytest.fixture
def clean_loopback_interface(loopback_interfaces_api):
    """
    Setup/Teardown for a simple Loopback Interface.
    """
    interface_name = generate_loopback_name("scm-lb-get-")

    payload = LoopbackInterfaces(
        name=interface_name,
        folder=TARGET_FOLDER,
        mtu=1500,
        comment="Test Loopback Interface"
    )

    logger.info(f"\n[SETUP] Creating Loopback Interface: {interface_name}")
    created_interface = perform(
        loopback_interfaces_api.create_loopback_interfaces_with_http_info,
        response_type=LoopbackInterfaces,
        loopback_interfaces=payload
    )

    yield created_interface

    logger.info(f"\n[TEARDOWN] Deleting Loopback Interface: {created_interface.id}")
    try:
        perform(
            loopback_interfaces_api.delete_loopback_interfaces_by_id_with_http_info,
            id=created_interface.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup loopback interface: {e}")


def test_create_loopback_interface(loopback_interfaces_api):
    """Test creation of a Loopback Interface."""
    interface_name = generate_loopback_name("scm-lb-create-")

    payload = LoopbackInterfaces(
        name=interface_name,
        folder=TARGET_FOLDER,
        mtu=1500,
        comment="Test Loopback Interface"
    )

    created_obj = perform(
        loopback_interfaces_api.create_loopback_interfaces_with_http_info,
        response_type=LoopbackInterfaces,
        loopback_interfaces=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == interface_name
    assert created_obj.mtu == 1500

    perform(
        loopback_interfaces_api.delete_loopback_interfaces_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_loopback_interface_by_id(loopback_interfaces_api, clean_loopback_interface):
    """Test retrieving a Loopback Interface by ID."""
    fetched_obj = perform(
        loopback_interfaces_api.get_loopback_interfaces_by_id_with_http_info,
        id=clean_loopback_interface.id
    )

    assert fetched_obj.id == clean_loopback_interface.id
    assert fetched_obj.name == clean_loopback_interface.name
    assert fetched_obj.comment == "Test Loopback Interface"


def test_update_loopback_interface(loopback_interfaces_api, clean_loopback_interface):
    """Test updating a Loopback Interface."""
    update_payload = clean_loopback_interface
    update_payload.comment = "Updated comment for Loopback"
    update_payload.mtu = 1450
    update_payload.default_value = "loopback.2000"

    updated_obj = perform(
        loopback_interfaces_api.update_loopback_interfaces_by_id_with_http_info,
        id=clean_loopback_interface.id,
        loopback_interfaces=update_payload
    )

    assert updated_obj.id == clean_loopback_interface.id
    assert updated_obj.comment == "Updated comment for Loopback"
    assert updated_obj.mtu == 1450
    assert updated_obj.default_value == "loopback.2000"


def test_list_loopback_interfaces(loopback_interfaces_api, clean_loopback_interface):
    """Test listing Loopback Interfaces."""
    response = perform(
        loopback_interfaces_api.list_loopback_interfaces_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_loopback_interface.id:
            found = True
            break
    assert found is True, f"Created interface {clean_loopback_interface.id} not found in list response"




def test_fetch_loopback_interfaces(loopback_interfaces_api, clean_loopback_interface):
    """
    Test fetching a single loopback_interfaces by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = loopback_interfaces_api.fetch_loopback_interfaces(
        name=clean_loopback_interface.name,
        folder=clean_loopback_interface.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found loopback_interfaces '{clean_loopback_interface.name}'"
    assert fetched_obj.id == clean_loopback_interface.id
    assert fetched_obj.name == clean_loopback_interface.name
    assert fetched_obj.folder == clean_loopback_interface.folder
    logger.info(f"\n[SUCCESS] fetch_loopback_interfaces found object: {fetched_obj.name}")

    # Test fetching non-existent loopback_interfaces (should return None)
    not_found = loopback_interfaces_api.fetch_loopback_interfaces(
        name="non-existent-loopback_interfaces-xyz-12345",
        folder=clean_loopback_interface.folder
    )
    assert not_found is None, "Should return None for non-existent loopback_interfaces"
    logger.info(f"\n[SUCCESS] fetch_loopback_interfaces correctly returned None for non-existent loopback_interfaces")


def test_delete_loopback_interface_by_id(loopback_interfaces_api):
    """Test deleting a Loopback Interface."""
    interface_name = generate_loopback_name("scm-lb-delete-")

    payload = LoopbackInterfaces(
        name=interface_name,
        folder=TARGET_FOLDER,
        mtu=1500,
        comment="Test Loopback Interface"
    )

    created_obj = perform(
        loopback_interfaces_api.create_loopback_interfaces_with_http_info,
        response_type=LoopbackInterfaces,
        loopback_interfaces=payload
    )

    perform(
        loopback_interfaces_api.delete_loopback_interfaces_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        loopback_interfaces_api.get_loopback_interfaces_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Interface should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
