
import logging
import uuid
import json
import pytest
from scm import Scm
from scm.mobile_agent.models.forwarding_profile_destinations import ForwardingProfileDestinations
from scm.mobile_agent.models.forwarding_profile_destination_fqdn_entry import ForwardingProfileDestinationFqdnEntry
from scm.mobile_agent.models.forwarding_profile_destination_ip_entry import ForwardingProfileDestinationIpEntry
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
def destinations_api(client):
    """
    Fixture to return the Destinations API instance.
    """
    return client.mobile_agent.DestinationsApi(client.mobile_agent.api_client)

@pytest.fixture
def clean_destination(destinations_api):
    """
    Fixture to create a temporary destination for testing and automatically delete it after.
    This mimics the 'Setup' and 'Cleanup' phases of your Go tests.
    """
    # 1. SETUP: Create ForwardingProfileDestinations
    object_name = f"test-dest-{uuid.uuid4().hex[:6]}"

    # Create FQDN entry
    fqdn_entry = ForwardingProfileDestinationFqdnEntry(
        name="www.google.com",
        port=80
    )

    # NOTE: 'id' is required by the Pydantic model but excluded from the API request.
    # We pass an empty string to satisfy validation.
    payload = ForwardingProfileDestinations(
        id="",
        name=object_name,
        fqdn=[fqdn_entry],
        description="Created via Automated Pytest Fixture"
    )

    # Use perform helper with _with_http_info
    logger.info(f"\n[SETUP] Creating ForwardingProfileDestinations: {object_name}")
    created_obj = perform(
        destinations_api.create_global_protect_destination_with_http_info,
        response_type=ForwardingProfileDestinations,
        folder=TARGET_FOLDER,
        forwarding_profile_destinations=payload
    )

    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete ForwardingProfileDestinations
    logger.info(f"\n[TEARDOWN] Deleting ForwardingProfileDestinations ID: {created_obj.id}")
    try:
        perform(
            destinations_api.delete_global_protect_destination,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_destination(destinations_api):
    """
    Test manual creation and deletion of a destination with both FQDN and IP address entries.
    Equivalent to Go: Test_mobile_agent_DestinationsAPIService_Create
    """
    object_name = f"test-dest-create-{uuid.uuid4().hex[:6]}"

    # Create FQDN entry
    fqdn_entry = ForwardingProfileDestinationFqdnEntry(
        name="www.google.com",
        port=80
    )

    # Create IP address entry
    ip_entry = ForwardingProfileDestinationIpEntry(
        name="10.2.3.4",
        port=345
    )

    payload = ForwardingProfileDestinations(
        id="",
        name=object_name,
        description="test",
        fqdn=[fqdn_entry],
        ip_addresses=[ip_entry]
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfileDestinations: {object_name}")

    # Create using perform helper
    created_obj = perform(
        destinations_api.create_global_protect_destination_with_http_info,
        response_type=ForwardingProfileDestinations,
        folder=TARGET_FOLDER,
        forwarding_profile_destinations=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.description == "test"

    # Verify FQDN entry
    assert len(created_obj.fqdn) == 1
    assert created_obj.fqdn[0].name == "www.google.com"
    assert created_obj.fqdn[0].port == 80

    # Verify IP address entry
    assert len(created_obj.ip_addresses) == 1
    assert created_obj.ip_addresses[0].name == "10.2.3.4"
    assert created_obj.ip_addresses[0].port == 345

    logger.info(f"Successfully created and validated ForwardingProfileDestinations: {object_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        destinations_api.delete_global_protect_destination,
        id=created_obj.id
    )


def test_get_destination_by_id(destinations_api, clean_destination):
    """
    Test retrieving a destination by ID.
    Equivalent to Go: Test_mobile_agent_DestinationsAPIService_GetByID
    Uses 'clean_destination' fixture to handle creation/deletion automatically.
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        destinations_api.get_global_protect_destination_by_id,
        response_type=ForwardingProfileDestinations,
        id=clean_destination.id
    )

    # Verify
    assert fetched_obj.id == clean_destination.id
    assert fetched_obj.name == clean_destination.name
    logger.info(f"Successfully retrieved ForwardingProfileDestinations by ID: {fetched_obj.id}")


def test_update_destination(destinations_api, clean_destination):
    """
    Test updating an existing destination.
    Equivalent to Go: Test_mobile_agent_DestinationsAPIService_Update
    """
    # Prepare Update
    update_payload = clean_destination
    update_payload.description = "Updated description"

    # Perform Update using helper
    updated_obj = perform(
        destinations_api.update_global_protect_destination_by_id,
        response_type=ForwardingProfileDestinations,
        id=clean_destination.id,
        forwarding_profile_destinations=update_payload
    )

    # Verify
    assert updated_obj.description == "Updated description"
    assert updated_obj.name == clean_destination.name
    assert updated_obj.id == clean_destination.id
    logger.info(f"Successfully updated ForwardingProfileDestinations: {updated_obj.id}")


def test_list_destinations(destinations_api, clean_destination):
    """
    Test listing destinations with folder filter.
    Equivalent to Go: Test_mobile_agent_DestinationsAPIService_List
    """
    # List with filter using helper
    response = perform(
        destinations_api.list_global_protect_destinations,
        folder=TARGET_FOLDER,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our destination is in the list
    found_dest = False
    for dest in response.data:
        if dest.name == clean_destination.name:
            found_dest = True
            break

    assert found_dest, f"Created ForwardingProfileDestinations '{clean_destination.name}' should be found in the list"
    logger.info(f"List returned {len(response.data)} items and found our destination")


def test_delete_destination_by_id(destinations_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_mobile_agent_DestinationsAPIService_DeleteByID
    We manually create and delete here to verify the delete logic explicitly.
    """
    from scm.exceptions import ObjectNotPresentError

    # Setup
    object_name = f"test-dest-delete-{uuid.uuid4().hex[:6]}"

    fqdn_entry = ForwardingProfileDestinationFqdnEntry(
        name="www.google.com",
        port=80
    )

    payload = ForwardingProfileDestinations(
        id="",
        name=object_name,
        fqdn=[fqdn_entry],
        description="Test destination for delete API testing"
    )

    created_obj = perform(
        destinations_api.create_global_protect_destination_with_http_info,
        response_type=ForwardingProfileDestinations,
        folder=TARGET_FOLDER,
        forwarding_profile_destinations=payload
    )

    # Perform Delete using helper
    perform(
        destinations_api.delete_global_protect_destination,
        id=created_obj.id
    )

    logger.info(f"Successfully deleted ForwardingProfileDestinations: {created_obj.id}")


def test_delete_destination_verify_gone(destinations_api):
    """
    Test that a deleted destination is no longer retrievable.
    Equivalent to Go: Test_mobile_agent_DestinationsAPIService_DeleteByID_VerifyGone
    """
    from scm.exceptions import ObjectNotPresentError

    # Setup
    object_name = f"test-dest-gone-{uuid.uuid4().hex[:6]}"

    fqdn_entry = ForwardingProfileDestinationFqdnEntry(
        name="www.google.com",
        port=80
    )

    payload = ForwardingProfileDestinations(
        id="",
        name=object_name,
        fqdn=[fqdn_entry],
        description="Test destination for delete-verify test"
    )

    created_obj = perform(
        destinations_api.create_global_protect_destination_with_http_info,
        response_type=ForwardingProfileDestinations,
        folder=TARGET_FOLDER,
        forwarding_profile_destinations=payload
    )

    # Delete
    perform(
        destinations_api.delete_global_protect_destination,
        id=created_obj.id
    )

    # Verify it's gone (should raise ObjectNotPresentError)
    with pytest.raises(ObjectNotPresentError):
        destinations_api.get_global_protect_destination_by_id(id=created_obj.id)

    logger.info(f"Verified destination is gone after deletion")


def test_fetch_destinations(destinations_api, clean_destination):
    """
    Test fetching a single destination by name using the fetch convenience method.
    Equivalent to Go: Test_mobile_agent_DestinationsAPIService_FetchDestinations
    """
    # Test 1: Fetch existing object by name
    fetched_obj = destinations_api.fetch_destinations(
        name=clean_destination.name,
        folder=TARGET_FOLDER
    )

    # Verify
    assert fetched_obj is not None, f"Should have found destination '{clean_destination.name}'"
    assert fetched_obj.id == clean_destination.id
    assert fetched_obj.name == clean_destination.name
    logger.info(f"fetch_destinations found object: {fetched_obj.name}")

    # Test 2: Fetch non-existent object (should return None)
    not_found = destinations_api.fetch_destinations(
        name="non-existent-destination-xyz-12345",
        folder=TARGET_FOLDER
    )
    assert not_found is None, "Should return None for non-existent destination"
    logger.info(f"fetch_destinations correctly returned None for non-existent destination")
