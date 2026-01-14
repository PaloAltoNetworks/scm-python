import logging
import uuid
import json
import pytest
from scm import Scm
from scm.objects.models.addresses import Addresses

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Folder to use for testing. Ensure this exists in your SCM environment.
TARGET_FOLDER = "Prisma Access"
# -----------------------------------------------------------------------------

def perform(func, response_type=None, **kwargs):
    """
    Local utility to call an API function and log the request/response details.
    Handles deserialization for 201 responses where the SDK might return None data.
    """
    func_name = func.__name__
    logger.info(f"\n>>> API REQUEST [{func_name}]")

    # Prepare arguments for logging
    log_kwargs = {}
    for k, v in kwargs.items():
        if hasattr(v, "to_dict"):
            log_kwargs[k] = v.to_dict()
        else:
            log_kwargs[k] = v

    logger.info(json.dumps(log_kwargs, indent=2, default=str))

    # Execute
    response = func(**kwargs)

    # Log raw response info
    logger.info(f"\n<<< API RESPONSE [{func_name}]")

    # Logic to unwrap ApiResponse if present (from _with_http_info calls)
    final_data = response

    if hasattr(response, 'data') and hasattr(response, 'raw_data'):
        logger.info(f"Status Code: {getattr(response, 'status_code', 'N/A')}")

        if response.data is not None:
            final_data = response.data
        elif response.raw_data and response_type:
            # Manual deserialization if SDK returned None for data (common in 201)
            try:
                if hasattr(response_type, 'model_validate_json'):
                    final_data = response_type.model_validate_json(response.raw_data)
                elif hasattr(response_type, 'parse_raw'):
                    final_data = response_type.parse_raw(response.raw_data)
                else:
                    final_data = json.loads(response.raw_data)
            except Exception as e:
                logger.warning(f"Failed to manual deserialize: {e}")
                final_data = response.raw_data

    # Log the final data
    if hasattr(final_data, "to_dict"):
        logger.info(json.dumps(final_data.to_dict(), indent=2, default=str))
    else:
        logger.info(str(final_data))

    return final_data


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


def test_delete_address_by_id(addresses_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_AddressesAPIService_DeleteByID
    We manually create and delete here to verify the delete logic explicitly.
    """
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

    # Verify Deletion (Expect 404 on Get)
    try:
        addresses_api.get_addresses_by_id(id=created_obj.id)
        pytest.fail("Address should have been deleted but was found.")
    except Exception as e:
        # SCM API typically returns 404 or a specific error code for not found
        assert "404" in str(e) or "Not Found" in str(e)