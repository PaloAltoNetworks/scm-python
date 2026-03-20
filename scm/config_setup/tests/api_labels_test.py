
import logging
import uuid
import pytest
from scm import Scm
from scm.config_setup.models.labels import Labels

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Labels do not use folder - they are global resources
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
def labels_api(client):
    """
    Fixture to return the Labels API instance.
    """
    return client.config_setup.LabelsApi(client.config_setup.api_client)

@pytest.fixture
def clean_label(labels_api):
    """
    Fixture to create a temporary Label for testing and automatically delete it after.
    """
    # 1. SETUP: Create Label
    random_id = uuid.uuid4().hex[:6]
    label_name = f"test-label-{random_id}"

    payload = Labels(
        id="",
        name=label_name,
        description="Created via Automated Pytest Fixture"
    )

    logger.info(f"\n[SETUP] Creating Label: {label_name}")
    created_obj = labels_api.create_label(labels=payload)
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Label
    logger.info(f"\n[TEARDOWN] Deleting Label ID: {created_obj.id}")
    try:
        labels_api.delete_label_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_label(labels_api):
    """
    Test manual creation and deletion of a label.
    Equivalent to Go: Test_config_setup_LabelsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    label_name = f"test-label-create-{random_suffix}"

    payload = Labels(
        id="",
        name=label_name,
        description="Test label for create API testing"
    )

    # Create
    created_obj = labels_api.create_label(labels=payload)

    # Verify
    assert created_obj.name == label_name
    assert created_obj.id is not None
    assert created_obj.description == "Test label for create API testing"

    logger.info(f"Successfully created label: {label_name} with ID: {created_obj.id}")

    # Cleanup
    labels_api.delete_label_by_id(id=created_obj.id)
    logger.info(f"Successfully cleaned up label: {created_obj.id}")


def test_get_label_by_id(labels_api, clean_label):
    """
    Test retrieving a label by ID.
    Equivalent to Go: Test_config_setup_LabelsAPIService_GetByID
    """
    # Retrieve
    fetched_obj = labels_api.get_label_by_id(id=clean_label.id)

    # Verify
    assert fetched_obj.id == clean_label.id
    assert fetched_obj.name == clean_label.name


def test_update_label(labels_api, clean_label):
    """
    Test updating an existing label.
    Equivalent to Go: Test_config_setup_LabelsAPIService_Update

    NOTE: Skipped because API returns array in update response but model expects object.
    This is a known issue in both Go and Python SDKs.
    """
    pytest.skip("API returns array in update response but model expects object - model deserialization error")


def test_list_labels(labels_api, clean_label):
    """
    Test listing labels.
    Equivalent to Go: Test_config_setup_LabelsAPIService_List

    NOTE: Labels do not use folder filter - they are global resources.
    """
    # List labels (no folder filter for labels)
    response = labels_api.list_labels(limit=500)

    assert response is not None
    assert len(response.data) > 0

    # Verify at least one label exists (our created one should be there)
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")




def test_fetch_labels(labels_api, clean_label):
    """
    Test fetching a single label by name using the fetch convenience method.
    Equivalent to Go: Test_config_setup_LabelsAPIService_FetchLabels
    """
    # Fetch by exact name (no folder for labels)
    fetched_obj = labels_api.fetch_labels(
        name=clean_label.name
    )

    # Verify
    assert fetched_obj is not None, f"Should have found label '{clean_label.name}'"
    assert fetched_obj.id == clean_label.id
    assert fetched_obj.name == clean_label.name
    logger.info(f"\n[SUCCESS] fetch_labels found object: {fetched_obj.name}")

    # Test fetching non-existent label (should return None)
    not_found = labels_api.fetch_labels(
        name="non-existent-labels-xyz-12345"
    )
    assert not_found is None, "Should return None for non-existent label"
    logger.info(f"\n[SUCCESS] fetch_labels correctly returned None for non-existent label")


def test_delete_label_by_id(labels_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_config_setup_LabelsAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    label_name = f"test-label-delete-{random_suffix}"

    payload = Labels(
        id="",
        name=label_name,
        description="Test label for delete API testing"
    )
    created_obj = labels_api.create_label(labels=payload)

    # Perform Delete
    labels_api.delete_label_by_id(id=created_obj.id)

    # Verify Deletion (Expect error on Get)
    from scm.exceptions import ObjectNotPresentError

    try:
        labels_api.get_label_by_id(id=created_obj.id)
        pytest.fail("Label should have been deleted but was found.")
    except (ObjectNotPresentError, Exception) as e:
        logger.info(f"Correctly raised error for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
