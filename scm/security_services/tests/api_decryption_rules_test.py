import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.decryption_rules import DecryptionRules
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
def decryption_rules_api(client):
    return client.security_services.DecryptionRulesApi(client.security_services.api_client)


@pytest.fixture
def clean_decryption_rule(decryption_rules_api):
    """
    Setup/Teardown for a simple Decryption rule.
    """
    rule_name = f"scm-decryption-{uuid.uuid4().hex[:6]}"

    payload = DecryptionRules(
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"]
    )

    logger.info(f"\n[SETUP] Creating Decryption Rule: {rule_name}")
    created_rule = perform(
        decryption_rules_api.create_decryption_rules_with_http_info,
        response_type=DecryptionRules,
        decryption_rules=payload,
        position="pre"
    )

    yield created_rule

    logger.info(f"\n[TEARDOWN] Deleting Decryption Rule: {created_rule.id}")
    try:
        perform(
            decryption_rules_api.delete_decryption_rules_by_id_with_http_info,
            id=created_rule.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Decryption rule: {e}")


def test_create_decryption_rule(decryption_rules_api):
    """Test creation of a Decryption Rule."""
    rule_name = f"scm-decryption-create-{uuid.uuid4().hex[:6]}"

    payload = DecryptionRules(
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"]
    )

    created_obj = perform(
        decryption_rules_api.create_decryption_rules_with_http_info,
        response_type=DecryptionRules,
        decryption_rules=payload,
        position="pre"
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == rule_name

    perform(
        decryption_rules_api.delete_decryption_rules_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_decryption_rule_by_id(decryption_rules_api, clean_decryption_rule):
    """Test retrieving a Decryption Rule by ID."""
    fetched_obj = perform(
        decryption_rules_api.get_decryption_rules_by_id_with_http_info,
        id=clean_decryption_rule.id
    )

    assert fetched_obj.id == clean_decryption_rule.id
    assert fetched_obj.name == clean_decryption_rule.name


def test_update_decryption_rule(decryption_rules_api, clean_decryption_rule):
    """Test updating a Decryption Rule."""
    update_payload = clean_decryption_rule
    update_payload.source = ["10.0.0.0/8"]
    update_payload.destination = ["192.168.0.0/16"]

    updated_obj = perform(
        decryption_rules_api.update_decryption_rules_by_id_with_http_info,
        id=clean_decryption_rule.id,
        decryption_rules=update_payload
    )

    assert updated_obj.id == clean_decryption_rule.id
    assert updated_obj.source == ["10.0.0.0/8"]
    assert updated_obj.destination == ["192.168.0.0/16"]


def test_list_decryption_rules(decryption_rules_api, clean_decryption_rule):
    """Test listing Decryption Rules."""
    response = perform(
        decryption_rules_api.list_decryption_rules_with_http_info,
        folder=TARGET_FOLDER,
        position="pre"
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_decryption_rule.name:
            found = True
            break
    assert found is True, f"Created rule {clean_decryption_rule.name} not found in list response"


def test_delete_decryption_rule_by_id(decryption_rules_api):
    """Test deleting a Decryption Rule."""
    rule_name = f"scm-decryption-delete-{uuid.uuid4().hex[:6]}"

    payload = DecryptionRules(
        id="",
        folder=TARGET_FOLDER,
        name=rule_name,
        var_from=["any"],
        to=["any"],
        source=["any"],
        destination=["any"]
    )

    created_obj = perform(
        decryption_rules_api.create_decryption_rules_with_http_info,
        response_type=DecryptionRules,
        decryption_rules=payload,
        position="pre"
    )

    perform(
        decryption_rules_api.delete_decryption_rules_by_id_with_http_info,
        id=created_obj.id
    )

    try:
        decryption_rules_api.get_decryption_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
