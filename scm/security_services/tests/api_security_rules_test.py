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
TARGET_FOLDER = "All"
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
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        application=["any"],
        service=["any"],
        action="allow"
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
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        application=["any"],
        service=["any"],
        action="allow"
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
    update_payload = clean_security_rule
    update_payload.description = "Updated security rule"
    update_payload.action = "deny"

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
        security_rules_api.list_security_rules_with_http_info,
        folder=TARGET_FOLDER,
        position="pre"
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
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        application=["any"],
        service=["any"],
        action="allow"
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

    try:
        security_rules_api.get_security_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
