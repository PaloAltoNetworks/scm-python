
import logging
import uuid
import pytest
from scm import Scm
from scm.config_setup.models.snippets import Snippets
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
# -----------------------------------------------------------------------------

@pytest.fixture(scope="module")
def client():
    """
    Fixture to initialize the SCM client once for the module.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def snippets_api(client):
    """
    Fixture to return the Snippets API instance.
    """
    return client.config_setup.SnippetsApi(client.config_setup.api_client)

@pytest.fixture
def clean_snippet(snippets_api):
    """
    Fixture to create a temporary Snippet for testing and automatically delete it after.
    """
    # 1. SETUP: Create Snippet
    random_id = uuid.uuid4().hex[:6]
    snippet_name = f"test-snippet-{random_id}"

    payload = Snippets(
        id="",
        name=snippet_name,
        description="Created via Automated Pytest Fixture"
    )

    logger.info(f"\n[SETUP] Creating Snippet: {snippet_name}")
    created_obj = perform(
        snippets_api.create_snippet_with_http_info,
        response_type=Snippets,
        snippets=payload
    )
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Snippet
    logger.info(f"\n[TEARDOWN] Deleting Snippet ID: {created_obj.id}")
    try:
        perform(
            snippets_api.delete_snippet_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_snippet(snippets_api):
    """
    Test manual creation and deletion of a snippet object.
    Equivalent to Go: Test_config_setup_SnippetsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    snippet_name = f"test-snippet-create-{random_suffix}"

    payload = Snippets(
        id="",
        name=snippet_name,
        description="Test snippet for create API testing"
    )

    # Create using perform helper
    created_obj = perform(
        snippets_api.create_snippet_with_http_info,
        response_type=Snippets,
        snippets=payload
    )

    # Verify
    assert created_obj.name == snippet_name
    assert created_obj.id is not None
    assert created_obj.description == "Test snippet for create API testing"

    # Cleanup
    perform(
        snippets_api.delete_snippet_by_id,
        id=created_obj.id
    )


def test_get_snippet_by_id(snippets_api, clean_snippet):
    """
    Test retrieving a snippet by ID.
    Equivalent to Go: Test_config_setup_SnippetsAPIService_GetByID
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        snippets_api.get_snippet_by_id,
        response_type=Snippets,
        id=clean_snippet.id
    )

    # Verify
    assert fetched_obj.id == clean_snippet.id
    assert fetched_obj.name == clean_snippet.name
    assert fetched_obj.description == clean_snippet.description


def test_update_snippet(snippets_api, clean_snippet):
    """
    Test updating an existing snippet.
    Equivalent to Go: Test_config_setup_SnippetsAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_snippet
    update_payload.description = "Updated test snippet description"
    update_payload.labels = ["test-label-1", "test-label-2"]

    # Perform Update using helper
    updated_obj = perform(
        snippets_api.update_snippet_by_id,
        response_type=Snippets,
        id=clean_snippet.id,
        snippets=update_payload
    )

    # Verify
    assert updated_obj.id == clean_snippet.id
    assert updated_obj.name == clean_snippet.name
    assert updated_obj.description == "Updated test snippet description"
    assert updated_obj.labels is not None
    assert "test-label-1" in updated_obj.labels
    assert "test-label-2" in updated_obj.labels


def test_list_snippets(snippets_api, clean_snippet):
    """
    Test listing snippets.
    Equivalent to Go: Test_config_setup_SnippetsAPIService_List
    """
    # List using perform helper
    response = perform(
        snippets_api.list_snippets,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.name == clean_snippet.name:
            found = True
            break

    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_delete_snippet_by_id(snippets_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_config_setup_SnippetsAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    snippet_name = f"test-snippet-delete-{random_suffix}"

    payload = Snippets(
        id="",
        name=snippet_name,
        description="Test snippet for delete API testing"
    )
    created_obj = perform(
        snippets_api.create_snippet_with_http_info,
        response_type=Snippets,
        snippets=payload
    )

    # Perform Delete using helper
    perform(
        snippets_api.delete_snippet_by_id,
        id=created_obj.id
    )

    # Verify Deletion (Expect 404 on Get)
    try:
        snippets_api.get_snippet_by_id(id=created_obj.id)
        pytest.fail("Snippet should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
