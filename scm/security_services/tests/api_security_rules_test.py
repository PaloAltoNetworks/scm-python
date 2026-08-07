import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.security_rules import SecurityRules
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
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def security_rules_api(client):
    return client.security_services.SecurityRulesApi(client.security_services.api_client)


@pytest.fixture
def clean_security_rule(security_rules_api):
    """
    Setup/Teardown for a simple Security Rule.
    """
    rule_name = f"scm-rule-{uuid.uuid4().hex[:6]}"

    payload = SecurityRules(
        folder=TARGET_FOLDER,
        name=rule_name,
        policy_type="Security",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        application=["any"],
        service=["any"],
        category=["any"],
        source_user=["any"],
        action="allow",
        # Explicitly set Internet-rule fields to None so they're not serialized
        negate_user=None,
        negate_source=None,
        negate_destination=None
    )

    logger.info(f"\n[SETUP] Creating Security Rule: {rule_name}")
    created_rule = perform(
        security_rules_api.create_security_rules_with_http_info,
        response_type=SecurityRules,
        security_rules=payload,
        position="pre"
    )

    yield created_rule

    logger.info(f"\n[TEARDOWN] Deleting Security Rule: {created_rule.id}")
    try:
        perform(
            security_rules_api.delete_security_rules_by_id_with_http_info,
            id=created_rule.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Security Rule: {e}")


def test_create_security_rule(security_rules_api):
    """Test creation of a Security Rule."""
    rule_name = f"scm-rule-create-{uuid.uuid4().hex[:6]}"

    payload = SecurityRules(
        folder=TARGET_FOLDER,
        name=rule_name,
        policy_type="Security",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        application=["any"],
        service=["any"],
        category=["any"],
        source_user=["any"],
        action="allow",
        # Explicitly set Internet-rule fields to None so they're not serialized
        negate_user=None,
        negate_source=None,
        negate_destination=None
    )

    created_obj = perform(
        security_rules_api.create_security_rules_with_http_info,
        response_type=SecurityRules,
        security_rules=payload,
        position="pre"
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == rule_name
    assert created_obj.action == "allow"

    perform(
        security_rules_api.delete_security_rules_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_security_rule_by_id(security_rules_api, clean_security_rule):
    """Test retrieving a Security Rule by ID."""
    fetched_obj = perform(
        security_rules_api.get_security_rules_by_id_with_http_info,
        id=clean_security_rule.id
    )

    assert fetched_obj.id == clean_security_rule.id
    assert fetched_obj.name == clean_security_rule.name
    assert fetched_obj.action == "allow"


def test_update_security_rule(security_rules_api, clean_security_rule):
    """Test updating a Security Rule."""
    # Create fresh payload for update (matching Go test pattern)
    # Don't reuse the created object as it contains fields from the API response
    update_payload = SecurityRules(
        name=clean_security_rule.name,
        description="Updated security rule",
        policy_type="Security",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        application=["any"],
        service=["any"],
        category=["any"],
        source_user=["any"],
        action="deny",  # Changed from "allow"
        # Explicitly set Internet-rule fields to None so they're not serialized
        negate_user=None,
        negate_source=None,
        negate_destination=None
    )

    updated_obj = perform(
        security_rules_api.update_security_rules_by_id_with_http_info,
        id=clean_security_rule.id,
        security_rules=update_payload
    )

    assert updated_obj.id == clean_security_rule.id
    assert updated_obj.description == "Updated security rule"
    assert updated_obj.action == "deny"


def test_list_security_rules(security_rules_api, clean_security_rule):
    """Test listing Security Rules."""
    response = perform(
        security_rules_api.list_rules_with_http_info,
        folder=TARGET_FOLDER,
        position="pre",
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_security_rule.name:
            found = True
            break
    assert found is True, f"Created rule {clean_security_rule.name} not found in list response"



def test_delete_security_rule_by_id(security_rules_api):
    """Test deleting a Security Rule."""
    rule_name = f"scm-rule-delete-{uuid.uuid4().hex[:6]}"

    payload = SecurityRules(
        folder=TARGET_FOLDER,
        name=rule_name,
        policy_type="Security",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        application=["any"],
        service=["any"],
        category=["any"],
        source_user=["any"],
        action="allow",
        # Explicitly set Internet-rule fields to None so they're not serialized
        negate_user=None,
        negate_source=None,
        negate_destination=None
    )

    created_obj = perform(
        security_rules_api.create_security_rules_with_http_info,
        response_type=SecurityRules,
        security_rules=payload,
        position="pre"
    )

    perform(
        security_rules_api.delete_security_rules_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        security_rules_api.get_security_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")


def test_fetch_security_rules(security_rules_api, clean_security_rule):
    """
    Test fetching a single security rule by name using the fetch convenience method.
    Equivalent to Go: Test_security_services_SecurityRulesAPIService_FetchSecurityRules
    """
    # Fetch by exact name (position is required for rules APIs)
    fetched_obj = security_rules_api.fetch_security_rules(
        name=clean_security_rule.name,
        folder=clean_security_rule.folder,
        position="pre"
    )

    # Verify
    assert fetched_obj is not None, f"Should have found rule '{clean_security_rule.name}'"
    assert fetched_obj.id == clean_security_rule.id
    assert fetched_obj.name == clean_security_rule.name
    logger.info(f"\n[SUCCESS] fetch_security_rules found object: {fetched_obj.name}")

    # Test fetching non-existent rule (should return None)
    not_found = security_rules_api.fetch_security_rules(
        name="non-existent-security-rule-xyz-12345",
        folder=clean_security_rule.folder,
        position="pre"
    )
    assert not_found is None, "Should return None for non-existent rule"
    logger.info(f"\n[SUCCESS] fetch_security_rules correctly returned None for non-existent rule")
