import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.app_override_rules import AppOverrideRules
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
def application_override_rules_api(client):
    return client.security_services.AppOverrideRulesApi(client.security_services.api_client)


@pytest.fixture
def clean_application_override_rule(application_override_rules_api):
    """
    Setup/Teardown for a simple Application Override rule.
    """
    rule_name = f"scm-appoverride-{uuid.uuid4().hex[:6]}"

    payload = AppOverrideRules(
        folder=TARGET_FOLDER,
        name=rule_name,
        application="custom-app",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        port=8080
    )

    logger.info(f"\n[SETUP] Creating Application Override Rule: {rule_name}")
    created_rule = perform(
        application_override_rules_api.create_application_override_rules_with_http_info,
        response_type=AppOverrideRules,
        application_override_rules=payload
    )

    yield created_rule

    logger.info(f"\n[TEARDOWN] Deleting Application Override Rule: {created_rule.id}")
    try:
        perform(
            application_override_rules_api.delete_application_override_rules_by_id_with_http_info,
            id=created_rule.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Application Override rule: {e}")


def test_create_application_override_rule(application_override_rules_api):
    """Test creation of an Application Override Rule."""
    rule_name = f"scm-appoverride-create-{uuid.uuid4().hex[:6]}"

    payload = AppOverrideRules(
        folder=TARGET_FOLDER,
        name=rule_name,
        application="custom-app",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        port=8080
    )

    created_obj = perform(
        application_override_rules_api.create_application_override_rules_with_http_info,
        response_type=AppOverrideRules,
        application_override_rules=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == rule_name
    assert created_obj.application == "custom-app"
    assert created_obj.port == 8080

    perform(
        application_override_rules_api.delete_application_override_rules_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_application_override_rule_by_id(application_override_rules_api, clean_application_override_rule):
    """Test retrieving an Application Override Rule by ID."""
    fetched_obj = perform(
        application_override_rules_api.get_application_override_rules_by_id_with_http_info,
        id=clean_application_override_rule.id
    )

    assert fetched_obj.id == clean_application_override_rule.id
    assert fetched_obj.name == clean_application_override_rule.name
    assert fetched_obj.application == "custom-app"


def test_update_application_override_rule(application_override_rules_api, clean_application_override_rule):
    """Test updating an Application Override Rule."""
    update_payload = clean_application_override_rule
    update_payload.port = 9090
    update_payload.application = "custom-app-updated"

    updated_obj = perform(
        application_override_rules_api.update_application_override_rules_by_id_with_http_info,
        id=clean_application_override_rule.id,
        application_override_rules=update_payload
    )

    assert updated_obj.id == clean_application_override_rule.id
    assert updated_obj.port == 9090
    assert updated_obj.application == "custom-app-updated"


def test_list_application_override_rules(application_override_rules_api, clean_application_override_rule):
    """Test listing Application Override Rules."""
    response = perform(
        application_override_rules_api.list_application_override_rules_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_application_override_rule.name:
            found = True
            break
    assert found is True, f"Created rule {clean_application_override_rule.name} not found in list response"


def test_delete_application_override_rule_by_id(application_override_rules_api):
    """Test deleting an Application Override Rule."""
    rule_name = f"scm-appoverride-delete-{uuid.uuid4().hex[:6]}"

    payload = AppOverrideRules(
        folder=TARGET_FOLDER,
        name=rule_name,
        application="custom-app",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        port=8080
    )

    created_obj = perform(
        application_override_rules_api.create_application_override_rules_with_http_info,
        response_type=AppOverrideRules,
        application_override_rules=payload
    )

    perform(
        application_override_rules_api.delete_application_override_rules_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        application_override_rules_api.get_application_override_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
