import logging
import pytest
from scm import Scm
from scm.identity_services.models.authentication_portals import AuthenticationPortals

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Note: AuthenticationPortals is a singleton object (one per folder).
# Tests handle this by checking if a portal exists before creating.
TARGET_FOLDER = "All"
# -----------------------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def auth_portals_api(client):
    return client.identity_services.AuthenticationPortalsApi(client.identity_services.api_client)


def test_create_auth_portal(auth_portals_api):
    """
    Test creation of an Authentication Portal (singleton).
    If portal already exists, test passes without creating.
    """
    # First check if a portal already exists
    response = auth_portals_api.list_authentication_portals(folder=TARGET_FOLDER)

    if response is not None and response.data and len(response.data) > 0:
        logger.info("AuthenticationPortals already exists - singleton object, test passes")
        return

    # Create bare minimum portal
    payload = AuthenticationPortals(
        folder=TARGET_FOLDER
    )

    logger.info("Creating Authentication Portal (bare minimum)")
    created_obj = auth_portals_api.create_authentication_portals(
        authentication_portals=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    logger.info(f"Successfully created Authentication Portal with ID: {created_obj.id}")


def test_get_auth_portal_by_id(auth_portals_api):
    """
    Test retrieving an Authentication Portal by ID.
    Lists first to get existing ID since it's a singleton object.
    """
    # First, list to get an existing portal ID
    response = auth_portals_api.list_authentication_portals(folder=TARGET_FOLDER)

    assert response is not None, "List response should not be None"

    # Skip if no portal exists
    if not response.data or len(response.data) == 0:
        pytest.skip("Skipping: No AuthenticationPortals exist - singleton may have been deleted")

    existing_id = response.data[0].id
    logger.info(f"Using existing portal ID: {existing_id}")

    # Test: Retrieve the portal by ID
    fetched_obj = auth_portals_api.get_authentication_portals_by_id(id=existing_id)

    assert fetched_obj is not None, "Get response should not be None"
    assert fetched_obj.id == existing_id, "Retrieved ID should match the existing ID"
    logger.info(f"Successfully retrieved Authentication Portal with ID: {fetched_obj.id}")


def test_update_auth_portal(auth_portals_api):
    """
    Test updating an Authentication Portal.
    Lists first to get existing ID since it's a singleton object.
    """
    # First, list to get an existing portal ID
    response = auth_portals_api.list_authentication_portals(folder=TARGET_FOLDER)

    assert response is not None, "List response should not be None"

    # Skip if no portal exists
    if not response.data or len(response.data) == 0:
        pytest.skip("Skipping: No AuthenticationPortals exist - singleton may have been deleted")

    existing_portal = response.data[0]
    existing_id = existing_portal.id
    logger.info(f"Using existing portal ID: {existing_id}")

    # Prepare updated portal object - change idle_timer to 100
    updated_idle_timer = 100

    update_payload = AuthenticationPortals(
        idle_timer=updated_idle_timer
    )

    logger.info(f"Updating portal idle_timer to: {updated_idle_timer}")
    updated_obj = auth_portals_api.update_authentication_portals_by_id(
        id=existing_id,
        authentication_portals=update_payload
    )

    assert updated_obj is not None, "Update response should not be None"
    assert updated_obj.id == existing_id, "ID should be present in the response"
    assert updated_obj.idle_timer == updated_idle_timer, "Idle timer should be updated to 100"
    logger.info(f"Successfully updated portal idle_timer to: {updated_obj.idle_timer}")


def test_delete_auth_portal(auth_portals_api):
    """
    Test deleting an Authentication Portal by ID.
    Lists first to get existing ID since it's a singleton object.
    """
    # First, list to get an existing portal ID
    response = auth_portals_api.list_authentication_portals(folder=TARGET_FOLDER)

    assert response is not None, "List response should not be None"
    assert response.data and len(response.data) > 0, "Expected at least one portal in the list"

    existing_id = response.data[0].id
    logger.info(f"Attempting to delete existing portal ID: {existing_id}")

    # Test: Delete the portal
    auth_portals_api.delete_authentication_portals_by_id(id=existing_id)

    logger.info(f"Successfully deleted portal ID: {existing_id}")


def test_list_auth_portals(auth_portals_api):
    """
    Test listing Authentication Portals.
    Just lists without creating since it's a singleton object.
    """
    logger.info(f"Test: Listing portals filtered by folder: {TARGET_FOLDER}")
    response = auth_portals_api.list_authentication_portals(folder=TARGET_FOLDER)

    assert response is not None, "List response should not be None"
    logger.info(f"Successfully listed Authentication Portals, total: {response.total}")
