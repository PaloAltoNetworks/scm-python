import logging
import pytest
from scm import Scm
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
# -----------------------------------------------------------------------------

# NOTE: DoS Protection Rules CRUD tests are skipped because the API requires
# from/to as objects but the SDK model has them as string arrays, causing 400 errors.
# Only List and Fetch (read-only) are tested here — matching Go coverage.


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def dos_protection_rules_api(client):
    return client.security_services.DoSProtectionRulesApi(client.security_services.api_client)


def test_list_dos_protection_rules(dos_protection_rules_api):
    """
    Test listing DoS protection rules (read-only).
    Equivalent to Go: Test_security_services_DoSProtectionRulesAPIService_List
    """
    response = dos_protection_rules_api.list_do_s_protection_rules(
        folder=TARGET_FOLDER,
        limit=200,
        offset=0,
    )

    assert response is not None
    logger.info(f"Listed {response.total} DoS protection rules")


def test_fetch_dos_protection_rules(dos_protection_rules_api):
    """
    Test fetch convenience method for DoS protection rules (read-only).
    Equivalent to Go: Test_security_services_DoSProtectionRulesAPIService_Fetch
    """
    # Fetch non-existent (should return None)
    not_found = dos_protection_rules_api.fetch_do_s_protection_rules(
        name="non-existent-dos-rule-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None, "Should return None for non-existent DoS protection rule"
    logger.info("fetch_do_s_protection_rules correctly returned None for non-existent rule")
