import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.decryption_exclusions import DecryptionExclusions
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
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def decryption_exclusions_api(client):
    return client.security_services.DecryptionExclusionsApi(client.security_services.api_client)


@pytest.fixture
def clean_decryption_exclusion(decryption_exclusions_api):
    """
    Setup/Teardown for a simple Decryption Exclusion.
    """
    exclusion_name = f"scm-decexcl-{uuid.uuid4().hex[:6]}"

    payload = DecryptionExclusions(
        id="",
        folder=TARGET_FOLDER,
        name=exclusion_name,
        description="Test decryption exclusion"
    )

    logger.info(f"\n[SETUP] Creating Decryption Exclusion: {exclusion_name}")
    created_exclusion = perform(
        decryption_exclusions_api.create_decryption_exclusions_with_http_info,
        response_type=DecryptionExclusions,
        decryption_exclusions=payload
    )

    yield created_exclusion

    logger.info(f"\n[TEARDOWN] Deleting Decryption Exclusion: {created_exclusion.id}")
    try:
        perform(
            decryption_exclusions_api.delete_decryption_exclusions_by_id_with_http_info,
            id=created_exclusion.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Decryption Exclusion: {e}")


def test_create_decryption_exclusion(decryption_exclusions_api):
    """Test creation of a Decryption Exclusion."""
    exclusion_name = f"scm-decexcl-create-{uuid.uuid4().hex[:6]}"

    payload = DecryptionExclusions(
        id="",
        folder=TARGET_FOLDER,
        name=exclusion_name,
        description="Test decryption exclusion for create API testing"
    )

    created_obj = perform(
        decryption_exclusions_api.create_decryption_exclusions_with_http_info,
        response_type=DecryptionExclusions,
        decryption_exclusions=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == exclusion_name
    assert created_obj.description == "Test decryption exclusion for create API testing"

    perform(
        decryption_exclusions_api.delete_decryption_exclusions_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_decryption_exclusion_by_id(decryption_exclusions_api, clean_decryption_exclusion):
    """Test retrieving a Decryption Exclusion by ID."""
    fetched_obj = perform(
        decryption_exclusions_api.get_decryption_exclusions_by_id_with_http_info,
        id=clean_decryption_exclusion.id
    )

    assert fetched_obj.id == clean_decryption_exclusion.id
    assert fetched_obj.name == clean_decryption_exclusion.name


def test_update_decryption_exclusion(decryption_exclusions_api, clean_decryption_exclusion):
    """Test updating a Decryption Exclusion."""
    update_payload = clean_decryption_exclusion
    update_payload.description = "Updated test decryption exclusion description"

    updated_obj = perform(
        decryption_exclusions_api.update_decryption_exclusions_by_id_with_http_info,
        id=clean_decryption_exclusion.id,
        decryption_exclusions=update_payload
    )

    assert updated_obj.id == clean_decryption_exclusion.id
    assert updated_obj.description == "Updated test decryption exclusion description"


def test_list_decryption_exclusions(decryption_exclusions_api):
    """Test listing Decryption Exclusions (read-only)."""
    response = perform(
        decryption_exclusions_api.list_decryption_exclusions_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    logger.info(f"Successfully listed decryption exclusions, total: {len(response.data)}")


def test_fetch_decryption_exclusions(decryption_exclusions_api, clean_decryption_exclusion):
    """
    Test fetching a single Decryption Exclusion by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = decryption_exclusions_api.fetch_decryption_exclusions(
        name=clean_decryption_exclusion.name,
        folder=clean_decryption_exclusion.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found Decryption Exclusion '{clean_decryption_exclusion.name}'"
    assert fetched_obj.id == clean_decryption_exclusion.id
    assert fetched_obj.name == clean_decryption_exclusion.name
    assert fetched_obj.folder == clean_decryption_exclusion.folder
    logger.info(f"\n[SUCCESS] fetch_decryption_exclusions found object: {fetched_obj.name}")

    # Test fetching non-existent exclusion (should return None)
    not_found = decryption_exclusions_api.fetch_decryption_exclusions(
        name="non-existent-exclusion-xyz-12345",
        folder=clean_decryption_exclusion.folder
    )
    assert not_found is None, "Should return None for non-existent Decryption Exclusion"
    logger.info(f"\n[SUCCESS] fetch_decryption_exclusions correctly returned None for non-existent exclusion")


def test_delete_decryption_exclusion_by_id(decryption_exclusions_api):
    """Test deleting a Decryption Exclusion."""
    exclusion_name = f"scm-decexcl-delete-{uuid.uuid4().hex[:6]}"

    payload = DecryptionExclusions(
        id="",
        folder=TARGET_FOLDER,
        name=exclusion_name,
        description="Test decryption exclusion for delete API testing"
    )

    created_obj = perform(
        decryption_exclusions_api.create_decryption_exclusions_with_http_info,
        response_type=DecryptionExclusions,
        decryption_exclusions=payload
    )

    perform(
        decryption_exclusions_api.delete_decryption_exclusions_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        decryption_exclusions_api.get_decryption_exclusions_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Exclusion should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
