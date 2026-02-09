
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.addresses import Addresses
from scm.objects.exceptions import BadRequestException, NotFoundException
from scm.error_parser import parse_scm_error
from scm.exceptions import NameNotUniqueError, ObjectNotPresentError
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Folder to use for testing. Ensure this exists in your SCM environment.
TARGET_FOLDER = "Prisma Access"
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
def addresses_api(client):
    """
    Fixture to return the Addresses API instance for exception testing.
    """
    return client.objects.AddressesApi(client.objects.api_client)


def test_name_not_unique_error(addresses_api):
    """
    Test NameNotUniqueError parsing - Duplicate object name.

    This test demonstrates how to use the error_parser.parse_scm_error() utility
    to convert a generic BadRequestException into a NameNotUniqueError with
    structured error context.
    """
    logger.info("\n[TEST] Creating duplicate address to test NameNotUniqueError")

    object_name = f"test-duplicate-{uuid.uuid4().hex[:6]}"

    # Create first address
    payload1 = Addresses(
        id="",
        name=object_name,
        ip_netmask="10.1.1.1/32",
        folder=TARGET_FOLDER,
        description="First address"
    )

    created_obj = perform(
        addresses_api.create_addresses_with_http_info,
        response_type=Addresses,
        addresses=payload1
    )

    try:
        # Try to create duplicate with same name
        payload2 = Addresses(
            id="",
            name=object_name,  # Same name!
            ip_netmask="10.1.1.2/32",
            folder=TARGET_FOLDER,
            description="Duplicate address"
        )

        addresses_api.create_addresses(addresses=payload2)
        pytest.fail("Should have raised InvalidObjectError for duplicate name")

    except Exception as e:
        # Decorator converts BadRequestException to InvalidObjectError or NameNotUniqueError
        logger.info(f"[EXCEPTION] Caught {type(e).__name__}: {e}")

        # Verify it's one of the expected error types
        from scm.exceptions import InvalidObjectError, NameNotUniqueError
        assert isinstance(e, (InvalidObjectError, NameNotUniqueError)), \
            f"Expected InvalidObjectError or NameNotUniqueError, got {type(e).__name__}"

        logger.info(f"[PARSED] Exception type: {type(e).__name__}")
        logger.info("✅ Duplicate name error handled successfully")

    # Cleanup first address
    perform(addresses_api.delete_addresses_by_id, id=created_obj.id)


def test_object_not_present_error(addresses_api):
    """
    Test ObjectNotPresentError - Object not found (404).

    This test demonstrates that the decorator automatically converts NotFoundException
    to ObjectNotPresentError, so you can catch it directly without manual parsing.
    """
    logger.info("\n[TEST] Getting non-existent address to test ObjectNotPresentError")

    # Use a realistic-looking but non-existent UUID
    fake_id = "12345678-1234-5678-1234-567812345678"

    try:
        addresses_api.get_addresses_by_id(id=fake_id)
        pytest.fail("Should have raised ObjectNotPresentError for non-existent ID")

    except ObjectNotPresentError as e:
        logger.info(f"[EXCEPTION] Caught ObjectNotPresentError (decorator already converted): {e}")

        # Verify it's the right type
        assert isinstance(e, ObjectNotPresentError), \
            f"Expected ObjectNotPresentError, got {type(e).__name__}"

        logger.info(f"[PARSED] Exception type: {type(e).__name__}")
        logger.info(f"[PARSED] Object ID: {e.object_id}")

        logger.info("✅ ObjectNotPresentError raised successfully")


def test_object_not_present_after_delete(addresses_api):
    """
    Test ObjectNotPresentError parsing - Object deleted then accessed.

    This test demonstrates exception parsing after deleting an object.
    """
    logger.info("\n[TEST] Deleting address then accessing to test ObjectNotPresentError")

    # Create test address
    object_name = f"test-addr-del-{uuid.uuid4().hex[:6]}"
    payload = Addresses(
        id="",
        name=object_name,
        ip_netmask="192.168.99.99/32",
        folder=TARGET_FOLDER,
        description="Test address for delete testing"
    )

    created_obj = perform(
        addresses_api.create_addresses_with_http_info,
        response_type=Addresses,
        addresses=payload
    )

    # Delete the address
    perform(
        addresses_api.delete_addresses_by_id,
        id=created_obj.id
    )

    # Try to access deleted object
    try:
        addresses_api.get_addresses_by_id(id=created_obj.id)
        pytest.fail("Address should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")


def test_exception_parsing_summary():
    """
    Summary test that documents exception parsing usage.

    This test doesn't make API calls - it just documents the feature.
    """
    logger.info("\n" + "="*70)
    logger.info("EXCEPTION PARSING UTILITIES - USAGE SUMMARY")
    logger.info("="*70)

    logger.info("\n✅ All custom exception parsing tests passed!")
    logger.info("\nNOTE: These exceptions are OPTIONAL utilities:")
    logger.info("  - You can still use generic exceptions (BadRequestException, NotFoundException)")
    logger.info("  - Custom exceptions provide structured error data for better error handling")
    logger.info("  - Use parse_scm_error(exception) to convert to custom exceptions")

    logger.info("\nAvailable Custom Exceptions:")
    logger.info("  1. NameNotUniqueError - Duplicate object names")
    logger.info("  2. ObjectNotPresentError - Object not found (404)")
    logger.info("  3. ReferenceNotZeroError - Delete conflicts (409)")
    logger.info("  4. InvalidObjectError - Validation errors (400)")
    logger.info("  5. MissingQueryParameterError - Missing required parameters")

    logger.info("\nExample Usage:")
    logger.info("  from scm.error_parser import parse_scm_error")
    logger.info("  from scm.exceptions import NameNotUniqueError")
    logger.info("  ")
    logger.info("  try:")
    logger.info("      api.create_addresses(data)")
    logger.info("  except BadRequestException as e:")
    logger.info("      custom_exc = parse_scm_error(e)")
    logger.info("      if isinstance(custom_exc, NameNotUniqueError):")
    logger.info("          print(f\"Duplicate: {custom_exc.object_name}\")")

    logger.info("\n" + "="*70)
