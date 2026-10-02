
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    QosPolicyRules,
    QosPolicyRulesAction,
    RuleBasedMove
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "All"

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def qos_rules_api(client):
    return client.network_services.QoSRulesApi(client.network_services.api_client)

def create_test_qos_rule_payload(name_prefix):
    """Helper to create a QoS Rule payload."""
    random_id = uuid.uuid4().hex[:6]
    name = f"{name_prefix}{random_id}"
    
    return QosPolicyRules(
        name=name,
        folder=TARGET_FOLDER,
        description="Test rule for QoS Policy CRUD",
        action=QosPolicyRulesAction(var_class="1") # 'class' is a reserved keyword in Python
    )

@pytest.fixture
def clean_qos_rule(qos_rules_api):
    """Fixture for standard CRUD tests."""
    rule = create_test_qos_rule_payload("qos-get-")
    
    logger.info(f"\n[SETUP] Creating QoS Rule: {rule.name}")
    created_obj = qos_rules_api.create_qo_s_policy_rules(qos_policy_rules=rule, position="pre")
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting QoS Rule ID: {created_obj.id}")
    try:
        qos_rules_api.delete_qo_s_policy_rules_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_qos_rule(qos_rules_api):
    """Test creation of a QoS Rule."""
    rule = create_test_qos_rule_payload("qos-create-")

    try:
        created_obj = qos_rules_api.create_qo_s_policy_rules(qos_policy_rules=rule, position="pre")
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == rule.name

    # Cleanup
    qos_rules_api.delete_qo_s_policy_rules_by_id(id=created_obj.id)


def test_get_qos_rule_by_id(qos_rules_api, clean_qos_rule):
    """Test retrieving a QoS Rule by ID."""
    fetched_obj = qos_rules_api.get_qo_s_policy_rules_by_id(id=clean_qos_rule.id)
    assert fetched_obj.id == clean_qos_rule.id
    assert fetched_obj.name == clean_qos_rule.name


def test_update_qos_rule(qos_rules_api, clean_qos_rule):
    """Test updating a QoS Rule."""
    update_payload = clean_qos_rule
    update_payload.description = "Updated QoS rule description"
    
    updated_obj = qos_rules_api.update_qo_s_policy_rules_by_id(
        id=clean_qos_rule.id,
        qos_policy_rules=update_payload
    )
    
    assert updated_obj.id == clean_qos_rule.id
    assert updated_obj.description == "Updated QoS rule description"


def test_list_qos_rules(qos_rules_api, clean_qos_rule):
    """Test listing QoS Rules."""
    response = qos_rules_api.list_qo_s_policy_rules(folder=TARGET_FOLDER, position="pre", limit=50, offset=10)
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_qos_rule.id:
            found = True
            break
    assert found is True



def test_delete_qos_rule_by_id(qos_rules_api):
    """Test deleting a QoS Rule."""
    rule = create_test_qos_rule_payload("qos-del-")
    created_obj = qos_rules_api.create_qo_s_policy_rules(qos_policy_rules=rule, position="pre")
    
    qos_rules_api.delete_qo_s_policy_rules_by_id(id=created_obj.id)
    
    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        qos_rules_api.get_qo_s_policy_rules_by_id(id=created_obj.id)
        pytest.fail("Rule should be deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")


def test_fetch_qos_rules(qos_rules_api, clean_qos_rule):
    """
    Test fetching a single QoS rule by name using the fetch convenience method.
    Equivalent to Go: Test_network_services_QoSRulesAPIService_FetchQoSRules
    """
    # Fetch by exact name (position is required for rules APIs)
    fetched_obj = qos_rules_api.fetch_qos_rules(
        name=clean_qos_rule.name,
        folder=TARGET_FOLDER,
        position="pre"
    )

    # Verify
    assert fetched_obj is not None, f"Should have found rule '{clean_qos_rule.name}'"
    assert fetched_obj.id == clean_qos_rule.id
    assert fetched_obj.name == clean_qos_rule.name
    logger.info(f"\n[SUCCESS] fetch_qos_rules found object: {fetched_obj.name}")

    # Test fetching non-existent rule (should return None)
    not_found = qos_rules_api.fetch_qos_rules(
        name="non-existent-qos-rule-xyz-12345",
        folder=TARGET_FOLDER,
        position="pre"
    )
    assert not_found is None, "Should return None for non-existent rule"
    logger.info(f"\n[SUCCESS] fetch_qos_rules correctly returned None for non-existent rule")


def test_move_qos_rule(qos_rules_api):
    """Test moving a QoS Rule."""
    # Create two rules
    rule_a = create_test_qos_rule_payload("move-A-")
    rule_b = create_test_qos_rule_payload("move-B-")

    obj_b = qos_rules_api.create_qo_s_policy_rules(qos_policy_rules=rule_b, position="pre") # Anchor
    obj_a = qos_rules_api.create_qo_s_policy_rules(qos_policy_rules=rule_a, position="pre") # Target

    # Move A after B
    move_payload = RuleBasedMove(destination="after", destination_rule=obj_b.id, rulebase="pre")
    
    try:
        qos_rules_api.move_qo_s_policy_rules_by_id(id=obj_a.id, rule_based_move=move_payload)
    except Exception as e:
        logger.error(f"Move failed: {e}")
        # Clean up anyway
        qos_rules_api.delete_qo_s_policy_rules_by_id(id=obj_a.id)
        qos_rules_api.delete_qo_s_policy_rules_by_id(id=obj_b.id)
        raise e

    # Cleanup
    qos_rules_api.delete_qo_s_policy_rules_by_id(id=obj_a.id)
    qos_rules_api.delete_qo_s_policy_rules_by_id(id=obj_b.id)
