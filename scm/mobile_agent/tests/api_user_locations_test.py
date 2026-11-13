
import logging
import uuid
import json
import pytest
from scm import Scm
from scm.mobile_agent.models.forwarding_profile_user_locations import ForwardingProfileUserLocations
from scm.mobile_agent.models.forwarding_profile_user_locations_internal_host_detection import ForwardingProfileUserLocationsInternalHostDetection
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Folder to use for testing. Ensure this exists in your SCM environment.
TARGET_FOLDER = "Mobile Users"
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
def user_locations_api(client):
    """
    Fixture to return the User Locations API instance.
    """
    return client.mobile_agent.UserLocationsApi(client.mobile_agent.api_client)

@pytest.fixture
def clean_user_location(user_locations_api):
    """
    Fixture to create a temporary user location for testing and automatically delete it after.
    This mimics the 'Setup' and 'Cleanup' phases of your Go tests.
    """
    # 1. SETUP: Create ForwardingProfileUserLocations
    object_name = f"test-userloc-{uuid.uuid4().hex[:6]}"

    # NOTE: 'id' is required by the Pydantic model but excluded from the API request.
    # We pass an empty string to satisfy validation.
    payload = ForwardingProfileUserLocations(
        id="",
        name=object_name,
        description="Created via Automated Pytest Fixture"
    )

    # Use perform helper with _with_http_info
    logger.info(f"\n[SETUP] Creating ForwardingProfileUserLocations: {object_name}")
    created_obj = perform(
        user_locations_api.create_global_protect_user_location_with_http_info,
        response_type=ForwardingProfileUserLocations,
        folder=TARGET_FOLDER,
        forwarding_profile_user_locations=payload
    )

    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete ForwardingProfileUserLocations
    logger.info(f"\n[TEARDOWN] Deleting ForwardingProfileUserLocations ID: {created_obj.id}")
    try:
        perform(
            user_locations_api.delete_global_protect_user_location,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_user_location(user_locations_api):
    """
    Test manual creation and deletion of a user location with all possible attributes.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_Create
    """
    object_name = f"test-userloc-create-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileUserLocations(
        id="",
        name=object_name,
        description="Test user location for create with all attributes",
        ip_addresses=["192.168.1.0/24", "10.0.0.0/8", "172.16.0.1"]
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfileUserLocations: {object_name}")

    # Create using perform helper
    created_obj = perform(
        user_locations_api.create_global_protect_user_location_with_http_info,
        response_type=ForwardingProfileUserLocations,
        folder=TARGET_FOLDER,
        forwarding_profile_user_locations=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.description == "Test user location for create with all attributes"

    # Verify IP addresses
    assert created_obj.ip_addresses is not None
    assert set(created_obj.ip_addresses) == {"192.168.1.0/24", "10.0.0.0/8", "172.16.0.1"}

    logger.info(f"Successfully created and validated ForwardingProfileUserLocations: {object_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        user_locations_api.delete_global_protect_user_location,
        id=created_obj.id
    )


def test_create_user_location_with_internal_host_detection(user_locations_api):
    """
    Test creation of a user location with internal host detection (without ip_addresses).
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_CreateWithInternalHostDetection
    """
    object_name = f"test-userloc-inthost-{uuid.uuid4().hex[:6]}"

    # Create internal host detection
    internal_host_detection = ForwardingProfileUserLocationsInternalHostDetection(
        fqdn="internal.example.com",
        ip_address="192.168.100.1"
    )

    payload = ForwardingProfileUserLocations(
        id="",
        name=object_name,
        description="Test user location with internal host detection",
        internal_host_detection=internal_host_detection
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfileUserLocations with internal host detection: {object_name}")

    # Create using perform helper
    created_obj = perform(
        user_locations_api.create_global_protect_user_location_with_http_info,
        response_type=ForwardingProfileUserLocations,
        folder=TARGET_FOLDER,
        forwarding_profile_user_locations=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.description == "Test user location with internal host detection"

    # Verify internal host detection
    assert created_obj.internal_host_detection is not None
    assert created_obj.internal_host_detection.fqdn == "internal.example.com"
    assert created_obj.internal_host_detection.ip_address == "192.168.100.1"

    logger.info(f"Successfully created and validated ForwardingProfileUserLocations with internal host detection: {object_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        user_locations_api.delete_global_protect_user_location,
        id=created_obj.id
    )


def test_create_user_location_minimal(user_locations_api):
    """
    Test creation of a user location with only a name (minimal required fields).
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_CreateMinimal
    """
    object_name = f"test-userloc-minimal-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileUserLocations(
        id="",
        name=object_name
    )

    logger.info(f"\n[TEST] Attempting to create minimal ForwardingProfileUserLocations: {object_name}")

    # Create using perform helper
    created_obj = perform(
        user_locations_api.create_global_protect_user_location_with_http_info,
        response_type=ForwardingProfileUserLocations,
        folder=TARGET_FOLDER,
        forwarding_profile_user_locations=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None

    logger.info(f"Successfully created minimal ForwardingProfileUserLocations: {object_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        user_locations_api.delete_global_protect_user_location,
        id=created_obj.id
    )


def test_create_user_location_with_ip_addresses_only(user_locations_api):
    """
    Test creating a user location with just name and IP addresses (no internal host detection).
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_CreateWithIPAddressesOnly
    """
    object_name = f"test-userloc-iponly-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileUserLocations(
        id="",
        name=object_name,
        description="User location with IP addresses only",
        ip_addresses=["10.10.0.0/16", "192.168.5.0/24"]
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfileUserLocations with IP addresses only: {object_name}")

    # Create using perform helper
    created_obj = perform(
        user_locations_api.create_global_protect_user_location_with_http_info,
        response_type=ForwardingProfileUserLocations,
        folder=TARGET_FOLDER,
        forwarding_profile_user_locations=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert set(created_obj.ip_addresses) == {"10.10.0.0/16", "192.168.5.0/24"}

    logger.info(f"Successfully created ForwardingProfileUserLocations with IP addresses only: {object_name}")

    # Cleanup
    perform(
        user_locations_api.delete_global_protect_user_location,
        id=created_obj.id
    )


def test_list_user_locations(user_locations_api, clean_user_location):
    """
    Test listing user locations with folder filter.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_List
    """
    # List with filter using helper
    response = perform(
        user_locations_api.list_global_protect_user_locations,
        folder=TARGET_FOLDER,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our user location is in the list
    found_location = False
    for loc in response.data:
        if loc.name == clean_user_location.name:
            found_location = True
            assert loc.id == clean_user_location.id
            break

    assert found_location, f"Created ForwardingProfileUserLocations '{clean_user_location.name}' should be found in the list"
    logger.info(f"List returned {len(response.data)} items and found our user location")


def test_list_user_locations_with_name_filter(user_locations_api, clean_user_location):
    """
    Test listing user locations with a name filter.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_ListWithNameFilter
    """
    # List with name filter using helper
    response = perform(
        user_locations_api.list_global_protect_user_locations,
        folder=TARGET_FOLDER,
        name=clean_user_location.name,
        limit=10
    )

    assert response is not None

    # Verify our user location is in the filtered results
    found_location = False
    for loc in response.data:
        if loc.name == clean_user_location.name:
            found_location = True
            assert loc.id == clean_user_location.id
            break

    assert found_location, f"Created ForwardingProfileUserLocations '{clean_user_location.name}' should be found with name filter"
    logger.info(f"Successfully filtered user locations by name: {clean_user_location.name}")


def test_get_user_location_by_id(user_locations_api, clean_user_location):
    """
    Test retrieving a user location by ID.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_GetByID
    Uses 'clean_user_location' fixture to handle creation/deletion automatically.
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        user_locations_api.get_global_protect_user_location_by_id,
        response_type=ForwardingProfileUserLocations,
        id=clean_user_location.id
    )

    # Verify
    assert fetched_obj.id == clean_user_location.id
    assert fetched_obj.name == clean_user_location.name
    logger.info(f"Successfully retrieved ForwardingProfileUserLocations by ID: {fetched_obj.id}")


def test_update_user_location(user_locations_api, clean_user_location):
    """
    Test updating an existing user location.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_Update
    """
    # Prepare Update
    update_payload = clean_user_location
    update_payload.description = "Updated description for user location"
    update_payload.ip_addresses = ["172.20.0.0/16", "10.5.5.0/24"]

    # Perform Update using helper
    updated_obj = perform(
        user_locations_api.update_global_protect_user_location_by_id,
        response_type=ForwardingProfileUserLocations,
        id=clean_user_location.id,
        forwarding_profile_user_locations=update_payload
    )

    # Verify
    assert updated_obj.description == "Updated description for user location"
    assert updated_obj.name == clean_user_location.name
    assert updated_obj.id == clean_user_location.id
    assert set(updated_obj.ip_addresses) == {"172.20.0.0/16", "10.5.5.0/24"}
    logger.info(f"Successfully updated ForwardingProfileUserLocations: {updated_obj.id}")


def test_update_user_location_with_internal_host_detection(user_locations_api):
    """
    Test updating a user location to use internal host detection instead of IP addresses.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_UpdateWithInternalHostDetection
    """
    # Create initial location with IP addresses
    object_name = f"test-userloc-upd-inthost-{uuid.uuid4().hex[:6]}"

    initial_payload = ForwardingProfileUserLocations(
        id="",
        name=object_name,
        ip_addresses=["10.1.0.0/16"]
    )

    created_obj = perform(
        user_locations_api.create_global_protect_user_location_with_http_info,
        response_type=ForwardingProfileUserLocations,
        folder=TARGET_FOLDER,
        forwarding_profile_user_locations=initial_payload
    )

    # Update to use internal host detection
    internal_host_detection = ForwardingProfileUserLocationsInternalHostDetection(
        fqdn="updated.example.com",
        ip_address="172.20.1.1"
    )

    update_payload = ForwardingProfileUserLocations(
        id=created_obj.id,
        name=object_name,
        description="Updated to use internal host detection",
        internal_host_detection=internal_host_detection
    )

    updated_obj = perform(
        user_locations_api.update_global_protect_user_location_by_id,
        response_type=ForwardingProfileUserLocations,
        id=created_obj.id,
        forwarding_profile_user_locations=update_payload
    )

    # Verify
    assert updated_obj.name == object_name
    assert updated_obj.description == "Updated to use internal host detection"
    assert updated_obj.internal_host_detection is not None
    assert updated_obj.internal_host_detection.fqdn == "updated.example.com"
    assert updated_obj.internal_host_detection.ip_address == "172.20.1.1"

    logger.info(f"Successfully updated ForwardingProfileUserLocations to use internal host detection: {object_name}")

    # Cleanup
    perform(
        user_locations_api.delete_global_protect_user_location,
        id=created_obj.id
    )


def test_delete_user_location_by_id(user_locations_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_DeleteByID
    We manually create and delete here to verify the delete logic explicitly.
    """
    # Setup
    object_name = f"test-userloc-delete-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileUserLocations(
        id="",
        name=object_name,
        description="Test user location for delete API testing"
    )

    created_obj = perform(
        user_locations_api.create_global_protect_user_location_with_http_info,
        response_type=ForwardingProfileUserLocations,
        folder=TARGET_FOLDER,
        forwarding_profile_user_locations=payload
    )

    # Perform Delete using helper
    perform(
        user_locations_api.delete_global_protect_user_location,
        id=created_obj.id
    )

    logger.info(f"Successfully deleted ForwardingProfileUserLocations: {created_obj.id}")


def test_fetch_user_locations(user_locations_api, clean_user_location):
    """
    Test fetching a single user location by name using the fetch convenience method.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_FetchUserLocations
    """
    # Test 1: Fetch existing object by name
    fetched_obj = user_locations_api.fetch_user_locations(
        name=clean_user_location.name,
        folder=TARGET_FOLDER
    )

    # Verify
    assert fetched_obj is not None, f"Should have found user location '{clean_user_location.name}'"
    assert fetched_obj.id == clean_user_location.id
    assert fetched_obj.name == clean_user_location.name
    logger.info(f"fetch_user_locations found object: {fetched_obj.name}")

    # Test 2: Fetch non-existent object (should return None)
    not_found = user_locations_api.fetch_user_locations(
        name="non-existent-user-location-xyz-12345",
        folder=TARGET_FOLDER
    )
    assert not_found is None, "Should return None for non-existent user location"
    logger.info(f"fetch_user_locations correctly returned None for non-existent user location")


def test_list_user_locations_pagination(user_locations_api):
    """
    Test pagination parameters when listing user locations.
    Equivalent to Go: Test_mobile_agent_UserLocationsAPIService_ListPagination
    """
    # Create multiple test objects to test pagination
    created_ids = []
    random_suffix = uuid.uuid4().hex[:6]

    for i in range(3):
        location_name = f"test-userloc-page-{random_suffix}-{i}"

        payload = ForwardingProfileUserLocations(
            id="",
            name=location_name
        )

        created_obj = perform(
            user_locations_api.create_global_protect_user_location_with_http_info,
            response_type=ForwardingProfileUserLocations,
            folder=TARGET_FOLDER,
            forwarding_profile_user_locations=payload
        )

        if created_obj.id:
            created_ids.append(created_obj.id)

    # Cleanup created test objects
    for location_id in created_ids:
        try:
            perform(
                user_locations_api.delete_global_protect_user_location,
                id=location_id
            )
        except Exception as e:
            logger.warning(f"Failed to cleanup user location {location_id}: {e}")

    # Test with limit
    response = perform(
        user_locations_api.list_global_protect_user_locations,
        folder=TARGET_FOLDER,
        limit=2,
        offset=0
    )

    assert response is not None
    logger.info(f"Retrieved {len(response.data)} items with limit=2")

    # Test with offset
    response2 = perform(
        user_locations_api.list_global_protect_user_locations,
        folder=TARGET_FOLDER,
        limit=10,
        offset=1
    )

    assert response2 is not None
    logger.info(f"Retrieved {len(response2.data)} items with offset=1")
    logger.info("Pagination test completed successfully")
