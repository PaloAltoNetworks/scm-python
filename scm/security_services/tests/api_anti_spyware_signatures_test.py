import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.anti_spyware_signatures import AntiSpywareSignatures
from scm.security_services.models.anti_spyware_signatures_signature import AntiSpywareSignaturesSignature
from scm.security_services.models.anti_spyware_signatures_signature_standard_inner import AntiSpywareSignaturesSignatureStandardInner
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
# Threat ID range for anti-spyware signatures: 6900001-7000000
# -----------------------------------------------------------------------------


def create_signature_block():
    """Create a basic signature block for testing."""
    standard_signature = AntiSpywareSignaturesSignatureStandardInner(
        name="std-sig-1",
        scope="protocol-data-unit"
    )
    return AntiSpywareSignaturesSignature(
        standard=[standard_signature]
    )


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def anti_spyware_signatures_api(client):
    return client.security_services.AntiSpywareSignaturesApi(client.security_services.api_client)


@pytest.fixture
def clean_anti_spyware_signature(anti_spyware_signatures_api):
    """
    Setup/Teardown for a simple Anti-Spyware Signature.
    """
    sig_name = f"test-aspysig-{uuid.uuid4().hex[:6]}"
    signature_block = create_signature_block()

    payload = AntiSpywareSignatures(
        id="",
        folder=TARGET_FOLDER,
        threatname=sig_name,
        threat_id="6900001",
        severity="medium",
        direction="client2server",
        comment="Test anti-spyware signature",
        signature=signature_block
    )

    logger.info(f"\n[SETUP] Creating Anti-Spyware Signature: {sig_name}")
    created_sig = perform(
        anti_spyware_signatures_api.create_anti_spyware_signatures_with_http_info,
        response_type=AntiSpywareSignatures,
        anti_spyware_signatures=payload
    )

    yield created_sig

    logger.info(f"\n[TEARDOWN] Deleting Anti-Spyware Signature: {created_sig.id}")
    try:
        perform(
            anti_spyware_signatures_api.delete_anti_spyware_signatures_by_id_with_http_info,
            id=created_sig.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Anti-Spyware Signature: {e}")


def test_create_anti_spyware_signature(anti_spyware_signatures_api):
    """Test creation of an Anti-Spyware Signature."""
    sig_name = f"test-aspysig-create-{uuid.uuid4().hex[:6]}"
    signature_block = create_signature_block()

    payload = AntiSpywareSignatures(
        id="",
        folder=TARGET_FOLDER,
        threatname=sig_name,
        threat_id="6900001",
        severity="medium",
        direction="client2server",
        comment="Test anti-spyware signature for create API testing",
        signature=signature_block
    )

    created_obj = perform(
        anti_spyware_signatures_api.create_anti_spyware_signatures_with_http_info,
        response_type=AntiSpywareSignatures,
        anti_spyware_signatures=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.threatname == sig_name

    perform(
        anti_spyware_signatures_api.delete_anti_spyware_signatures_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_anti_spyware_signature_by_id(anti_spyware_signatures_api, clean_anti_spyware_signature):
    """Test retrieving an Anti-Spyware Signature by ID."""
    fetched_obj = perform(
        anti_spyware_signatures_api.get_anti_spyware_signatures_by_id_with_http_info,
        id=clean_anti_spyware_signature.id
    )

    assert fetched_obj.id == clean_anti_spyware_signature.id
    assert fetched_obj.threatname == clean_anti_spyware_signature.threatname


def test_update_anti_spyware_signature(anti_spyware_signatures_api, clean_anti_spyware_signature):
    """Test updating an Anti-Spyware Signature."""
    update_payload = clean_anti_spyware_signature
    update_payload.comment = "Updated test anti-spyware signature comment"

    updated_obj = perform(
        anti_spyware_signatures_api.update_anti_spyware_signatures_by_id_with_http_info,
        id=clean_anti_spyware_signature.id,
        anti_spyware_signatures=update_payload
    )

    assert updated_obj.id == clean_anti_spyware_signature.id
    assert updated_obj.comment == "Updated test anti-spyware signature comment"


def test_list_anti_spyware_signatures(anti_spyware_signatures_api):
    """Test listing Anti-Spyware Signatures (read-only)."""
    response = perform(
        anti_spyware_signatures_api.list_anti_spyware_signatures_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    logger.info(f"Successfully listed anti-spyware signatures, total: {len(response.data)}")


def test_delete_anti_spyware_signature_by_id(anti_spyware_signatures_api):
    """Test deleting an Anti-Spyware Signature."""
    sig_name = f"test-aspysig-delete-{uuid.uuid4().hex[:6]}"
    signature_block = create_signature_block()

    payload = AntiSpywareSignatures(
        id="",
        folder=TARGET_FOLDER,
        threatname=sig_name,
        threat_id="6900005",
        severity="medium",
        direction="client2server",
        comment="Test anti-spyware signature for delete API testing",
        signature=signature_block
    )

    created_obj = perform(
        anti_spyware_signatures_api.create_anti_spyware_signatures_with_http_info,
        response_type=AntiSpywareSignatures,
        anti_spyware_signatures=payload
    )

    perform(
        anti_spyware_signatures_api.delete_anti_spyware_signatures_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        anti_spyware_signatures_api.get_anti_spyware_signatures_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Signature should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
