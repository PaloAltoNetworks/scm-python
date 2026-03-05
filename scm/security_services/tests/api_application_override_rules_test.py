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
    return client.security_services.ApplicationOverrideRulesApi(client.security_services.api_client)


@pytest.fixture
def clean_application_override_rule(application_override_rules_api):
    """
    Setup/Teardown for a simple Application Override rule.
    """
    rule_name = f"scm-appoverride-{uuid.uuid4().hex[:6]}"

    payload = AppOverrideRules(
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        application="web-browsing",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        port="8080",
        protocol="tcp"
    )

    logger.info(f"\n[SETUP] Creating Application Override Rule: {rule_name}")
    created_rule = perform(
        application_override_rules_api.create_application_override_rules_with_http_info,
        response_type=AppOverrideRules,
        position="pre",
        app_override_rules=payload
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
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        application="web-browsing",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        port="8080",
        protocol="tcp"
    )

    created_obj = perform(
        application_override_rules_api.create_application_override_rules_with_http_info,
        response_type=AppOverrideRules,
        position="pre",
        app_override_rules=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == rule_name
    assert created_obj.application == "web-browsing"
    assert created_obj.port == "8080"
    # Verify folder is either what we asked for OR 'Shared' (common SCM behavior)
    assert created_obj.folder == TARGET_FOLDER or created_obj.folder == "Shared"

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
    assert fetched_obj.application == "web-browsing"


def test_update_application_override_rule(application_override_rules_api, clean_application_override_rule):
    """Test updating an Application Override Rule."""
    # Create fresh payload for update (matching Go test pattern)
    # Don't reuse the created object as it contains fields from the API response
    update_payload = AppOverrideRules(
        name=clean_application_override_rule.name,
        application="ssl",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        port="443",
        protocol="tcp"
    )

    updated_obj = perform(
        application_override_rules_api.update_application_override_rules_by_id_with_http_info,
        id=clean_application_override_rule.id,
        app_override_rules=update_payload
    )

    assert updated_obj.id == clean_application_override_rule.id
    assert updated_obj.port == "443"
    assert updated_obj.application == "ssl"


def test_list_application_override_rules(application_override_rules_api, clean_application_override_rule):
    """Test listing Application Override Rules."""
    # Use the folder from the created object (API may use Shared instead of requested folder)
    actual_folder = clean_application_override_rule.folder

    response = perform(
        application_override_rules_api.list_application_override_rules_with_http_info,
        position="pre",
        folder=actual_folder,
        offset=0,
        limit=100
    )

    assert response is not None
    assert hasattr(response, 'total')
    assert response.total > 0
    # Verify folder is either what we asked for OR 'Shared' (common SCM behavior)
    assert actual_folder == TARGET_FOLDER or actual_folder == "Shared"



def test_delete_application_override_rule_by_id(application_override_rules_api):
    """Test deleting an Application Override Rule."""
    rule_name = f"scm-appoverride-delete-{uuid.uuid4().hex[:6]}"

    payload = AppOverrideRules(
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        application="web-browsing",
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"],
        port="8080",
        protocol="tcp"
    )

    created_obj = perform(
        application_override_rules_api.create_application_override_rules_with_http_info,
        response_type=AppOverrideRules,
        position="pre",
        app_override_rules=payload
    )

    perform(
        application_override_rules_api.delete_application_override_rules_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        application_override_rules_api.get_application_override_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
