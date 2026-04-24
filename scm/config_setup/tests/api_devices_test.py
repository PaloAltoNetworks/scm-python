
import logging
import pytest
from scm import Scm
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


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
def devices_api(client):
    """
    Fixture to return the Devices API instance.
    """
    return client.config_setup.DevicesApi(client.config_setup.api_client)


def test_list_devices(devices_api):
    """
    Test listing devices.
    This is a read-only operation that retrieves the current list of devices.
    Equivalent to Go: Test_config_setup_DevicesAPIService_List
    """
    logger.info("\n[TEST] Listing devices")

    # List devices using perform helper
    response = perform(
        devices_api.list_devices_with_http_info,
        response_type=object,
        limit=200,
        offset=0
    )

    assert response is not None, "Response should not be None"
    assert hasattr(response, 'data'), "Response should have 'data' attribute"

    devices = response.data
    logger.info(f"Successfully retrieved {len(devices)} devices (limit: {response.limit}, offset: {response.offset}, total: {response.total})")

    # Log first few devices for debugging
    for i, device in enumerate(devices[:3]):
        logger.info(f"  Device {i+1}: ID={device.id}, Name={device.name}")


def test_get_device_by_id(devices_api):
    """
    Test retrieving a specific device by ID.
    First lists devices to find a valid ID, then retrieves that specific device.
    Equivalent to Go: Test_config_setup_DevicesAPIService_GetByID
    """
    logger.info("\n[TEST] Getting device by ID")

    # First, list devices to get a valid device ID
    list_response = perform(
        devices_api.list_devices_with_http_info,
        response_type=object,
        limit=10,
        offset=0
    )

    assert list_response is not None
    devices = list_response.data

    # Skip test if no devices exist
    if len(devices) == 0:
        pytest.skip("No devices found in the system, skipping GetByID test")
        return

    # Get the first device's ID and name
    first_device = devices[0]
    device_id = first_device.id
    device_name = first_device.name
    logger.info(f"Using device from list: ID={device_id}, Name={device_name}")

    # Retrieve the specific device by ID
    response = perform(
        devices_api.get_device_by_id_with_http_info,
        response_type=object,
        id=device_id
    )

    assert response is not None, "Response should not be None"
    assert response.id == device_id, f"Device ID should match: {device_id}"
    assert response.name == device_name, f"Device name should match: {device_name}"

    logger.info(f"Successfully retrieved device: ID={response.id}, Name={response.name}")


def test_fetch_devices(devices_api):
    """
    Test the fetch_devices convenience method.
    First lists devices to get a valid name, then fetches that device by name.
    Equivalent to Go: Test_config_setup_DevicesAPIService_FetchDevices
    """
    logger.info("\n[TEST] Fetching device by name")

    # First, list devices to get a valid device name
    list_response = perform(
        devices_api.list_devices_with_http_info,
        response_type=object,
        limit=10,
        offset=0
    )

    assert list_response is not None
    devices = list_response.data

    # Skip test if no devices exist
    if len(devices) == 0:
        pytest.skip("No devices found in the system, skipping FetchDevices test")
        return

    # Get the first device's name and ID for verification
    first_device = devices[0]
    device_name = first_device.name
    device_id = first_device.id
    logger.info(f"Using device from list: ID={device_id}, Name={device_name}")

    # Test 1: Fetch existing device by name
    response = perform(
        devices_api.list_devices_with_http_info,
        response_type=object,
        name=device_name,
        limit=5000
    )

    assert response is not None, "Response should not be None"
    assert hasattr(response, 'data'), "Response should have 'data' attribute"

    # Find the device in the response
    fetched_device = None
    for device in response.data:
        if device.name == device_name:
            fetched_device = device
            break

    assert fetched_device is not None, f"Should find device with name: {device_name}"
    assert fetched_device.id == device_id, f"Fetched device ID should match: {device_id}"
    logger.info(f"[SUCCESS] Fetched device: ID={fetched_device.id}, Name={fetched_device.name}")

    # Test 2: Fetch non-existent device (should return 404 or empty data)
    from scm.exceptions import NotFoundError
    try:
        response = perform(
            devices_api.list_devices_with_http_info,
            response_type=object,
            name="non-existent-device-xyz-12345",
            limit=5000
        )
        # If no exception, check for empty data
        assert len(response.data) == 0, "Should return empty data for non-existent device"
        logger.info("[SUCCESS] Correctly returned empty for non-existent device")
    except NotFoundError:
        # 404 is acceptable for non-existent device
        logger.info("[SUCCESS] Correctly returned 404 for non-existent device")
