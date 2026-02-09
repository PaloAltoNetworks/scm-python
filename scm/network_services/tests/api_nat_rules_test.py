import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.nat_rules import NatRules
from scm.network_services.models.nat_rules_destination_translation import NatRulesDestinationTranslation
from scm.network_services.models.nat_rules_destination_translation_dns_rewrite import NatRulesDestinationTranslationDnsRewrite
from scm.network_services.models.nat_rules_source_translation import NatRulesSourceTranslation
from scm.network_services.models.nat_rules_source_translation_dynamic_ip_and_port import NatRulesSourceTranslationDynamicIpAndPort
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
def nat_rules_api(client):
    return client.network_services.NATRulesApi(client.network_services.api_client)


@pytest.fixture
def clean_nat_rule(nat_rules_api):
    """
    Setup/Teardown for a NAT Rule.
    """
    rule_name = f"test-nat-get-{uuid.uuid4().hex[:6]}"

    dns_rewrite = NatRulesDestinationTranslationDnsRewrite(
        direction="reverse"
    )

    dynamic_ip_port = NatRulesSourceTranslationDynamicIpAndPort(
        translated_address=["10.1.1.20", "10.2.2.23"]
    )

    destination_translation = NatRulesDestinationTranslation(
        translated_address="10.1.1.10",
        translated_port=443,
        dns_rewrite=dns_rewrite
    )

    source_translation = NatRulesSourceTranslation(
        dynamic_ip_and_port=dynamic_ip_port
    )

    payload = NatRules(
        id="",
        name=rule_name,
        description="Test NAT rule for CRUD",
        var_from=["any"],
        to=["untrust"],
        source=["any"],
        destination=["any"],
        service="service-https",
        folder=TARGET_FOLDER,
        nat_type="ipv4",
        destination_translation=destination_translation,
        source_translation=source_translation,
        active_active_device_binding="1"
    )

    logger.info(f"\n[SETUP] Creating NAT Rule: {rule_name}")
    created_rule = perform(
        nat_rules_api.create_nat_rules_with_http_info,
        response_type=NatRules,
        nat_rules=payload,
        position="pre"
    )

    yield created_rule

    logger.info(f"\n[TEARDOWN] Deleting NAT Rule: {created_rule.id}")
    try:
        perform(
            nat_rules_api.delete_nat_rules_by_id_with_http_info,
            id=created_rule.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup NAT rule: {e}")


def test_create_nat_rule(nat_rules_api):
    """Test creation of a NAT Rule."""
    rule_name = f"test-nat-create-{uuid.uuid4().hex[:6]}"

    dns_rewrite = NatRulesDestinationTranslationDnsRewrite(
        direction="reverse"
    )

    dynamic_ip_port = NatRulesSourceTranslationDynamicIpAndPort(
        translated_address=["10.1.1.20", "10.2.2.23"]
    )

    destination_translation = NatRulesDestinationTranslation(
        translated_address="10.1.1.10",
        translated_port=443,
        dns_rewrite=dns_rewrite
    )

    source_translation = NatRulesSourceTranslation(
        dynamic_ip_and_port=dynamic_ip_port
    )

    payload = NatRules(
        id="",
        name=rule_name,
        description="Test NAT rule for CRUD",
        var_from=["any"],
        to=["untrust"],
        source=["any"],
        destination=["any"],
        service="service-https",
        folder=TARGET_FOLDER,
        nat_type="ipv4",
        destination_translation=destination_translation,
        source_translation=source_translation,
        active_active_device_binding="1"
    )

    created_obj = perform(
        nat_rules_api.create_nat_rules_with_http_info,
        response_type=NatRules,
        nat_rules=payload,
        position="pre"
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == rule_name

    perform(
        nat_rules_api.delete_nat_rules_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_nat_rule_by_id(nat_rules_api, clean_nat_rule):
    """Test retrieving a NAT Rule by ID."""
    fetched_obj = perform(
        nat_rules_api.get_nat_rules_by_id_with_http_info,
        id=clean_nat_rule.id
    )

    assert fetched_obj.id == clean_nat_rule.id
    assert fetched_obj.name == clean_nat_rule.name


def test_update_nat_rule(nat_rules_api, clean_nat_rule):
    """Test updating a NAT Rule."""
    update_payload = clean_nat_rule
    update_payload.name = f"{clean_nat_rule.name}-v2"
    update_payload.description = "Updated NAT rule description"
    update_payload.destination = ["10.0.0.0/8"]

    updated_obj = perform(
        nat_rules_api.update_nat_rules_by_id_with_http_info,
        id=clean_nat_rule.id,
        nat_rules=update_payload,
        position="pre"
    )

    assert updated_obj.id == clean_nat_rule.id
    assert updated_obj.description == "Updated NAT rule description"


def test_list_nat_rules(nat_rules_api, clean_nat_rule):
    """Test listing NAT Rules."""
    # Use offset to skip legacy rules that may have incomplete data
    response = perform(
        nat_rules_api.list_nat_rules_with_http_info,
        position="pre",
        folder=TARGET_FOLDER,
        offset=10,
        limit=10000
    )

    assert response is not None
    assert hasattr(response, 'data')
    logger.info(f"List returned {len(response.data)} items")



def test_delete_nat_rule_by_id(nat_rules_api):
    """Test deleting a NAT Rule."""
    rule_name = f"test-nat-delete-{uuid.uuid4().hex[:6]}"

    dns_rewrite = NatRulesDestinationTranslationDnsRewrite(
        direction="reverse"
    )

    dynamic_ip_port = NatRulesSourceTranslationDynamicIpAndPort(
        translated_address=["10.1.1.20", "10.2.2.23"]
    )

    destination_translation = NatRulesDestinationTranslation(
        translated_address="10.1.1.10",
        translated_port=443,
        dns_rewrite=dns_rewrite
    )

    source_translation = NatRulesSourceTranslation(
        dynamic_ip_and_port=dynamic_ip_port
    )

    payload = NatRules(
        id="",
        name=rule_name,
        description="Test NAT rule for CRUD",
        var_from=["any"],
        to=["untrust"],
        source=["any"],
        destination=["any"],
        service="service-https",
        folder=TARGET_FOLDER,
        nat_type="ipv4",
        destination_translation=destination_translation,
        source_translation=source_translation,
        active_active_device_binding="1"
    )

    created_obj = perform(
        nat_rules_api.create_nat_rules_with_http_info,
        response_type=NatRules,
        nat_rules=payload,
        position="pre"
    )

    perform(
        nat_rules_api.delete_nat_rules_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.network_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        nat_rules_api.get_nat_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
