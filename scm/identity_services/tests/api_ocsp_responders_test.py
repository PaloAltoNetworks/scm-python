import logging
import uuid
import pytest
from scm import Scm
from scm.identity_services.models.ocsp_responders import OcspResponders
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Prisma Access"
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
def ocsp_responders_api(client):
    """
    Fixture to return the OCSP Responders API instance.
    """
    return client.identity_services.OCSPRespondersApi(client.identity_services.api_client)


@pytest.fixture
def clean_ocsp_responder(ocsp_responders_api):
    """
    Fixture to create a temporary OCSP Responder for testing and automatically delete it after.
    Note: Create returns None (no model), so we use Fetch to retrieve the created object.
    """
    object_name = f"test-ocsp-{uuid.uuid4().hex[:6]}"

    payload = OcspResponders(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        host_name="ocsp-fixture.example.com"
    )

    logger.info(f"\n[SETUP] Creating OCSP Responder: {object_name}")
    # Create returns None (no model body in 201 response)
    ocsp_responders_api.create_ocsp_responders(ocsp_responders=payload)

    # Use Fetch to retrieve the created object and get the ID
    created_obj = ocsp_responders_api.fetch_ocsp_responders(
        name=object_name,
        folder=TARGET_FOLDER
    )
    assert created_obj is not None, "Failed to fetch OCSP Responder after creation"
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting OCSP Responder ID: {created_obj.id}")
    try:
        perform(
            ocsp_responders_api.delete_ocsp_responders_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_ocsp_responder(ocsp_responders_api):
    """
    Test manual creation and deletion of an OCSP Responder with logging.
    Mirrors Test_identity_services_OCSPRespondersAPIService_Create
    Note: Create returns no model, so we use Fetch to verify.
    """
    object_name = f"test-ocsp-create-{uuid.uuid4().hex[:6]}"

    payload = OcspResponders(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        host_name="ocsp.example.com"
    )

    # Create (returns None)
    ocsp_responders_api.create_ocsp_responders(ocsp_responders=payload)

    # Use Fetch to verify the object was created and get the ID
    fetched_obj = ocsp_responders_api.fetch_ocsp_responders(
        name=object_name,
        folder=TARGET_FOLDER
    )

    assert fetched_obj is not None, "Failed to fetch OCSP Responder after creation"
    assert fetched_obj.name == object_name
    assert fetched_obj.host_name == "ocsp.example.com"

    # Cleanup
    perform(
        ocsp_responders_api.delete_ocsp_responders_by_id_with_http_info,
        id=fetched_obj.id
    )


def test_get_ocsp_responder_by_id(ocsp_responders_api, clean_ocsp_responder):
    """
    Test retrieving an OCSP Responder by ID with logging.
    Mirrors Test_identity_services_OCSPRespondersAPIService_GetByID
    """
    fetched_obj = perform(
        ocsp_responders_api.get_ocsp_responders_by_id_with_http_info,
        id=clean_ocsp_responder.id
    )

    assert fetched_obj.id == clean_ocsp_responder.id
    assert fetched_obj.name == clean_ocsp_responder.name


def test_update_ocsp_responder(ocsp_responders_api, clean_ocsp_responder):
    """
    Test updating an OCSP Responder with logging.
    Mirrors Test_identity_services_OCSPRespondersAPIService_Update
    """
    update_payload = OcspResponders(
        id="",
        name=clean_ocsp_responder.name,
        host_name="ocsp-updated.example.com"
    )

    updated_obj = perform(
        ocsp_responders_api.update_ocsp_responders_by_id_with_http_info,
        id=clean_ocsp_responder.id,
        ocsp_responders=update_payload
    )

    assert updated_obj.id == clean_ocsp_responder.id
    assert updated_obj.host_name == "ocsp-updated.example.com"


def test_list_ocsp_responders(ocsp_responders_api, clean_ocsp_responder):
    """
    Test listing OCSP Responders with logging.
    Mirrors Test_identity_services_OCSPRespondersAPIService_List
    """
    response = perform(
        ocsp_responders_api.list_ocsp_responders_with_http_info,
        folder=TARGET_FOLDER,
        limit=200
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_ocsp_responder.name:
            found = True
            break
    assert found is True, f"Created OCSP Responder {clean_ocsp_responder.name} not found in list response"


def test_fetch_ocsp_responders(ocsp_responders_api, clean_ocsp_responder):
    """
    Test fetching a single ocsp_responders by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = ocsp_responders_api.fetch_ocsp_responders(
        name=clean_ocsp_responder.name,
        folder=clean_ocsp_responder.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found ocsp_responders '{clean_ocsp_responder.name}'"
    assert fetched_obj.id == clean_ocsp_responder.id
    assert fetched_obj.name == clean_ocsp_responder.name
    assert fetched_obj.folder == clean_ocsp_responder.folder
    logger.info(f"\n[SUCCESS] fetch_ocsp_responders found object: {fetched_obj.name}")

    # Test fetching non-existent ocsp_responders (should return None)
    not_found = ocsp_responders_api.fetch_ocsp_responders(
        name="non-existent-ocsp-responders-xyz-12345",
        folder=clean_ocsp_responder.folder
    )
    assert not_found is None, "Should return None for non-existent ocsp_responders"
    logger.info(f"\n[SUCCESS] fetch_ocsp_responders correctly returned None for non-existent ocsp_responders")


def test_delete_ocsp_responder_by_id(ocsp_responders_api):
    """
    Test deletion specifically with logging.
    Mirrors Test_identity_services_OCSPRespondersAPIService_DeleteByID
    """
    object_name = f"test-ocsp-del-{uuid.uuid4().hex[:6]}"

    payload = OcspResponders(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        host_name="ocsp-delete.example.com"
    )

    # Create (returns None)
    ocsp_responders_api.create_ocsp_responders(ocsp_responders=payload)

    # Use Fetch to get the ID
    fetched_obj = ocsp_responders_api.fetch_ocsp_responders(
        name=object_name,
        folder=TARGET_FOLDER
    )
    assert fetched_obj is not None, "Failed to fetch OCSP Responder for delete test"

    # Perform Delete
    perform(
        ocsp_responders_api.delete_ocsp_responders_by_id_with_http_info,
        id=fetched_obj.id
    )

    # Verify Deletion
    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        ocsp_responders_api.get_ocsp_responders_by_id_with_http_info(id=fetched_obj.id)
        pytest.fail("OCSP Responder should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {fetched_obj.id}")
