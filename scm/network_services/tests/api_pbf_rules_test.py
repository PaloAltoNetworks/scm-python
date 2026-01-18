import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.pbf_rules import PbfRules
from scm.network_services.models.pbf_rules_from import PbfRulesFrom
from scm.network_services.models.pbf_rules_action import PbfRulesAction
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
def pbf_rules_api(client):
    return client.network_services.PBFRulesApi(client.network_services.api_client)


@pytest.fixture
def clean_pbf_rule(pbf_rules_api):
    """
    Setup/Teardown for a PBF Rule.
    """
    rule_name = f"test-pbf-get-{uuid.uuid4().hex[:6]}"

    valid_zone = "zone-trust"
    valid_address = "192.168.10.0/24"

    rule_action = PbfRulesAction(
        discard={}
    )

    payload = PbfRules(
        name=rule_name,
        description="Test PBF rule for CRUD",
        folder=TARGET_FOLDER,
        var_from=PbfRulesFrom(zone=[valid_zone]),
        source=[valid_address],
        destination=[valid_address],
        application=["web-browsing"],
        service=["service-http"],
        schedule="non-work-hours",
        action=rule_action
    )

    logger.info(f"\n[SETUP] Creating PBF Rule: {rule_name}")
    created_rule = perform(
        pbf_rules_api.create_pbf_rules_with_http_info,
        response_type=PbfRules,
        pbf_rules=payload
    )

    yield created_rule

    logger.info(f"\n[TEARDOWN] Deleting PBF Rule: {created_rule.id}")
    try:
        perform(
            pbf_rules_api.delete_pbf_rules_by_id_with_http_info,
            id=created_rule.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup PBF rule: {e}")


def test_create_pbf_rule(pbf_rules_api):
    """Test creation of a PBF Rule."""
    rule_name = f"test-pbf-create-{uuid.uuid4().hex[:6]}"

    valid_zone = "zone-trust"
    valid_address = "192.168.10.0/24"

    rule_action = PbfRulesAction(
        discard={}
    )

    payload = PbfRules(
        name=rule_name,
        description="Test PBF rule for CRUD",
        folder=TARGET_FOLDER,
        var_from=PbfRulesFrom(zone=[valid_zone]),
        source=[valid_address],
        destination=[valid_address],
        application=["web-browsing"],
        service=["service-http"],
        schedule="non-work-hours",
        action=rule_action
    )

    created_obj = perform(
        pbf_rules_api.create_pbf_rules_with_http_info,
        response_type=PbfRules,
        pbf_rules=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == rule_name

    perform(
        pbf_rules_api.delete_pbf_rules_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_pbf_rule_by_id(pbf_rules_api, clean_pbf_rule):
    """Test retrieving a PBF Rule by ID."""
    fetched_obj = perform(
        pbf_rules_api.get_pbf_rules_by_id_with_http_info,
        id=clean_pbf_rule.id
    )

    assert fetched_obj.id == clean_pbf_rule.id
    assert fetched_obj.name == clean_pbf_rule.name


def test_update_pbf_rule(pbf_rules_api, clean_pbf_rule):
    """Test updating a PBF Rule."""
    update_payload = clean_pbf_rule
    update_payload.description = "Updated PBF rule description"
    update_payload.source = ["10.1.1.1/32"]

    updated_obj = perform(
        pbf_rules_api.update_pbf_rules_by_id_with_http_info,
        id=clean_pbf_rule.id,
        pbf_rules=update_payload
    )

    assert updated_obj.id == clean_pbf_rule.id
    assert updated_obj.description == "Updated PBF rule description"
    assert updated_obj.source == ["10.1.1.1/32"]


def test_list_pbf_rules(pbf_rules_api, clean_pbf_rule):
    """Test listing PBF Rules."""
    response = perform(
        pbf_rules_api.list_pbf_rules_with_http_info,
        limit=50,
        folder=TARGET_FOLDER,
        offset=10
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_pbf_rule.id:
            found = True
            break
    assert found is True, f"Created rule {clean_pbf_rule.id} not found in list response"


def test_delete_pbf_rule_by_id(pbf_rules_api):
    """Test deleting a PBF Rule."""
    rule_name = f"test-pbf-delete-{uuid.uuid4().hex[:6]}"

    valid_zone = "zone-trust"
    valid_address = "192.168.10.0/24"

    rule_action = PbfRulesAction(
        discard={}
    )

    payload = PbfRules(
        name=rule_name,
        description="Test PBF rule for CRUD",
        folder=TARGET_FOLDER,
        var_from=PbfRulesFrom(zone=[valid_zone]),
        source=[valid_address],
        destination=[valid_address],
        application=["web-browsing"],
        service=["service-http"],
        schedule="non-work-hours",
        action=rule_action
    )

    created_obj = perform(
        pbf_rules_api.create_pbf_rules_with_http_info,
        response_type=PbfRules,
        pbf_rules=payload
    )

    perform(
        pbf_rules_api.delete_pbf_rules_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        pbf_rules_api.get_pbf_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
