
import logging
import uuid
import json
import pytest
from scm import Scm
from scm.objects.models.addresses import Addresses
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Folder to use for testing. Ensure this exists in your SCM environment.
TARGET_FOLDER = "Prisma Access"
# -----------------------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    """
    Fixture to initialize the SCM client once for the module.
    Assumes SCM_CLIENT_ID, SCM_CLIENT_SECRET, SCM_TSG_ID are set in env.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def addresses_api(client):
    """
    Fixture to return the Addresses API instance.
    """
    return client.objects.AddressesApi(client.objects.api_client)

@pytest.fixture
def clean_address(addresses_api):
    """
    Fixture to create a temporary address for testing and automatically delete it after.
    This mimics the 'Setup' and 'Cleanup' phases of your Go tests.
    """
    # 1. SETUP: Create Address
    object_name = f"test-addr-{uuid.uuid4().hex[:6]}"

    # NOTE: 'id' is required by the Pydantic model but excluded from the API request.
    # We pass an empty string to satisfy validation.
    payload = Addresses(
        id="",
        name=object_name,
        ip_netmask="10.0.0.1/32",
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture"
    )

    # Use perform helper with _with_http_info
    logger.info(f"\n[SETUP] Creating Address: {object_name}")
    created_obj = perform(
        addresses_api.create_addresses_with_http_info,
        response_type=Addresses,
        addresses=payload
    )

    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Address
    logger.info(f"\n[TEARDOWN] Deleting Address ID: {created_obj.id}")
    try:
        perform(
            addresses_api.delete_addresses_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_address(addresses_api):
    """
    Test manual creation and deletion of an address.
    Equivalent to Go: Test_objects_AddressesAPIService_Create
    """
    object_name = f"test-addr-create-{uuid.uuid4().hex[:6]}"
    payload = Addresses(
        id="",
        name=object_name,
        fqdn="test.create.example.com",
        folder=TARGET_FOLDER,
        description="Test address for create API testing"
    )

    # Create using perform helper
    created_obj = perform(
        addresses_api.create_addresses_with_http_info,
        response_type=Addresses,
        addresses=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.fqdn == "test.create.example.com"

    # Verify folder is either what we asked for OR 'Shared' (common SCM behavior)
    assert created_obj.folder == TARGET_FOLDER or created_obj.folder == "Shared"

    # Cleanup
    perform(
        addresses_api.delete_addresses_by_id,
        id=created_obj.id
    )


def test_get_address_by_id(addresses_api, clean_address):
    """
    Test retrieving an address by ID.
    Equivalent to Go: Test_objects_AddressesAPIService_GetByID
    Uses 'clean_address' fixture to handle creation/deletion automatically.
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        addresses_api.get_addresses_by_id,
        response_type=Addresses,
        id=clean_address.id
    )

    # Verify
    assert fetched_obj.id == clean_address.id
    assert fetched_obj.name == clean_address.name
    assert fetched_obj.folder == clean_address.folder
    assert fetched_obj.ip_netmask == clean_address.ip_netmask


def test_update_address(addresses_api, clean_address):
    """
    Test updating an address.
    Equivalent to Go: Test_objects_AddressesAPIService_Update
    """
    # Prepare Update
    update_payload = clean_address
    update_payload.description = "Updated Description via Pytest"
    update_payload.fqdn = "updated.test.example.com"

    # Clear mutually exclusive fields if necessary (e.g. ip_netmask vs fqdn)
    update_payload.ip_netmask = None

    # Perform Update using helper
    updated_obj = perform(
        addresses_api.update_addresses_by_id,
        response_type=Addresses,
        id=clean_address.id,
        addresses=update_payload
    )

    # Verify
    assert updated_obj.description == "Updated Description via Pytest"
    assert updated_obj.fqdn == "updated.test.example.com"
    assert updated_obj.id == clean_address.id


def test_list_addresses(addresses_api, clean_address):
    """
    Test listing addresses with folder filter.
    Equivalent to Go: Test_objects_AddressesAPIService_List
    """
    # List with filter using helper
    response = perform(
        addresses_api.list_addresses,
        folder=clean_address.folder
    )

    assert response is not None
    assert len(response.data) > 0
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")




def test_fetch_addresses(addresses_api, clean_address):
    """
    Test fetching a single addresses by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = addresses_api.fetch_addresses(
        name=clean_address.name,
        folder=clean_address.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found addresses '{clean_address.name}'"
    assert fetched_obj.id == clean_address.id
    assert fetched_obj.name == clean_address.name
    assert fetched_obj.folder == clean_address.folder
    logger.info(f"\n[SUCCESS] fetch_addresses found object: {fetched_obj.name}")

    # Test fetching non-existent addresses (should return None)
    not_found = addresses_api.fetch_addresses(
        name="non-existent-addresses-xyz-12345",
        folder=clean_address.folder
    )
    assert not_found is None, "Should return None for non-existent addresses"
    logger.info(f"\n[SUCCESS] fetch_addresses correctly returned None for non-existent addresses")


def test_delete_address_by_id(addresses_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_AddressesAPIService_DeleteByID
    We manually create and delete here to verify the delete logic explicitly.

    UPDATED: Catches ObjectNotPresentError directly (decorator already converts exceptions).
    """
    from scm.exceptions import ObjectNotPresentError

    # Setup
    object_name = f"test-addr-del-{uuid.uuid4().hex[:6]}"
    payload = Addresses(
        id="", # Pass empty ID to satisfy Pydantic
        name=object_name,
        ip_netmask="192.168.99.99/32",
        folder=TARGET_FOLDER,
        description="Test address for delete API testing"
    )

    created_obj = perform(
        addresses_api.create_addresses_with_http_info,
        response_type=Addresses,
        addresses=payload
    )

    # Perform Delete using helper
    perform(
        addresses_api.delete_addresses_by_id,
        id=created_obj.id
    )

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    # Decorator already converts NotFoundException to ObjectNotPresentError
    try:
        addresses_api.get_addresses_by_id(id=created_obj.id)
        pytest.fail("Address should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
