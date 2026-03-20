
import logging
import uuid
import pytest
from scm import Scm
from scm.deployment_services.models.traffic_steering_rules import TrafficSteeringRules
from scm.deployment_services.models.traffic_steering_rules_action import TrafficSteeringRulesAction
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Service Connections"
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
def traffic_steering_rules_api(client):
    """
    Fixture to return the TrafficSteeringRules API instance.
    """
    return client.deployment_services.TrafficSteeringRulesApi(client.deployment_services.api_client)


@pytest.fixture
def clean_traffic_steering_rule(traffic_steering_rules_api):
    """
    Fixture to create a temporary Traffic Steering Rule for testing and automatically delete it after.
    """
    random_id = uuid.uuid4().hex[:6]
    rule_name = f"test-tsr-{random_id}"

    payload = TrafficSteeringRules(
        id="",
        name=rule_name,
        folder=TARGET_FOLDER,
        service=["any"],
        source=["any"],
        action=TrafficSteeringRulesAction()
    )

    logger.info(f"\n[SETUP] Creating TrafficSteeringRule: {rule_name}")
    created_obj = perform(
        traffic_steering_rules_api.create_traffic_steering_rules_with_http_info,
        response_type=TrafficSteeringRules,
        folder=TARGET_FOLDER,
        traffic_steering_rules=payload
    )
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting TrafficSteeringRule ID: {created_obj.id}")
    try:
        traffic_steering_rules_api.delete_traffic_steering_rules_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_traffic_steering_rule(traffic_steering_rules_api):
    """
    Test manual creation and deletion of a traffic steering rule object.
    Equivalent to Go: Test_deployment_services_TrafficSteeringRulesAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    rule_name = f"test-tsr-create-{random_suffix}"

    payload = TrafficSteeringRules(
        id="",
        name=rule_name,
        folder=TARGET_FOLDER,
        service=["any"],
        source=["any"],
        action=TrafficSteeringRulesAction()
    )

    # Create
    created_obj = perform(
        traffic_steering_rules_api.create_traffic_steering_rules_with_http_info,
        response_type=TrafficSteeringRules,
        folder=TARGET_FOLDER,
        traffic_steering_rules=payload
    )

    # Verify
    assert created_obj.name == rule_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER

    # Cleanup
    traffic_steering_rules_api.delete_traffic_steering_rules_by_id(id=created_obj.id)


def test_get_traffic_steering_rule_by_id(traffic_steering_rules_api, clean_traffic_steering_rule):
    """
    Test retrieving a traffic steering rule by its ID.
    Equivalent to Go: Test_deployment_services_TrafficSteeringRulesAPIService_GetByID
    """
    fetched_obj = perform(
        traffic_steering_rules_api.get_traffic_steering_rules_by_id_with_http_info,
        response_type=TrafficSteeringRules,
        id=clean_traffic_steering_rule.id
    )

    # Verify
    assert fetched_obj.id == clean_traffic_steering_rule.id
    assert fetched_obj.name == clean_traffic_steering_rule.name


def test_update_traffic_steering_rule(traffic_steering_rules_api, clean_traffic_steering_rule):
    """
    Test updating an existing traffic steering rule.
    Equivalent to Go: Test_deployment_services_TrafficSteeringRulesAPIService_Update
    """
    # Prepare Update Payload with modified destination
    update_payload = TrafficSteeringRules(
        id=clean_traffic_steering_rule.id,
        name=clean_traffic_steering_rule.name,
        folder=TARGET_FOLDER,
        service=["any"],
        source=["any"],
        destination=["10.0.0.0/8"],
        action=TrafficSteeringRulesAction()
    )

    # Perform Update
    updated_obj = perform(
        traffic_steering_rules_api.update_traffic_steering_rules_by_id_with_http_info,
        response_type=TrafficSteeringRules,
        id=clean_traffic_steering_rule.id,
        traffic_steering_rules=update_payload
    )

    # Verify
    assert updated_obj.id == clean_traffic_steering_rule.id
    assert updated_obj.name == clean_traffic_steering_rule.name
    assert updated_obj.destination is not None
    assert "10.0.0.0/8" in updated_obj.destination


def test_list_traffic_steering_rules(traffic_steering_rules_api, clean_traffic_steering_rule):
    """
    Test listing traffic steering rules.
    Equivalent to Go: Test_deployment_services_TrafficSteeringRulesAPIService_List
    """
    response = traffic_steering_rules_api.list_traffic_steering_rules(
        folder=TARGET_FOLDER,
        limit=10000
    )

    # Verify
    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_traffic_steering_rule.name:
            found = True
            break
    assert found is True, f"Created rule {clean_traffic_steering_rule.name} not found in list response"


def test_fetch_traffic_steering_rules(traffic_steering_rules_api, clean_traffic_steering_rule):
    """
    Test fetching a single traffic steering rule by name using the fetch convenience method.
    Equivalent to Go: Test_deployment_services_TrafficSteeringRulesAPIService_FetchTrafficSteeringRules
    """
    # Fetch by exact name
    fetched_obj = traffic_steering_rules_api.fetch_traffic_steering_rules(
        name=clean_traffic_steering_rule.name,
        folder=TARGET_FOLDER
    )

    # Verify
    assert fetched_obj is not None, f"Should have found traffic_steering_rules '{clean_traffic_steering_rule.name}'"
    assert fetched_obj.id == clean_traffic_steering_rule.id
    assert fetched_obj.name == clean_traffic_steering_rule.name
    logger.info(f"\n[SUCCESS] fetch_traffic_steering_rules found object: {fetched_obj.name}")

    # Test fetching non-existent traffic_steering_rules (should return None)
    not_found = traffic_steering_rules_api.fetch_traffic_steering_rules(
        name="non-existent-traffic-steering-rules-xyz-12345",
        folder=TARGET_FOLDER
    )
    assert not_found is None, "Should return None for non-existent traffic_steering_rules"
    logger.info(f"\n[SUCCESS] fetch_traffic_steering_rules correctly returned None for non-existent traffic_steering_rules")


def test_delete_traffic_steering_rule_by_id(traffic_steering_rules_api):
    """
    Test deleting a traffic steering rule.
    Equivalent to Go: Test_deployment_services_TrafficSteeringRulesAPIService_DeleteByID
    """
    random_suffix = uuid.uuid4().hex[:6]
    rule_name = f"test-tsr-delete-{random_suffix}"

    payload = TrafficSteeringRules(
        id="",
        name=rule_name,
        folder=TARGET_FOLDER,
        service=["any"],
        source=["any"],
        action=TrafficSteeringRulesAction()
    )

    # Create
    created_obj = perform(
        traffic_steering_rules_api.create_traffic_steering_rules_with_http_info,
        response_type=TrafficSteeringRules,
        folder=TARGET_FOLDER,
        traffic_steering_rules=payload
    )

    # Delete
    traffic_steering_rules_api.delete_traffic_steering_rules_by_id(id=created_obj.id)

    # Verify deletion (expect ObjectNotPresentError)
    from scm.exceptions import ObjectNotPresentError

    try:
        traffic_steering_rules_api.get_traffic_steering_rules_by_id(id=created_obj.id)
        pytest.fail("Traffic steering rule should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
