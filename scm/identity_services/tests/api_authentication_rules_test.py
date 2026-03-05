import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.authentication_rules import AuthenticationRules
from scm.identity_services.models.authentication_profiles import AuthenticationProfiles
from scm.identity_services.models.authentication_profiles_method import AuthenticationProfilesMethod
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
def auth_rules_api(client):
    return client.identity_services.AuthenticationRulesApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def auth_profiles_api(client):
    return client.identity_services.AuthenticationProfilesApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def test_auth_profile(auth_profiles_api):
    """
    Setup/Teardown for the prerequisite Authentication Profile.
    """
    profile_name = f"scm-authprofile-{uuid.uuid4().hex[:4]}"

    method = AuthenticationProfilesMethod(
        local_database={}
    )

    payload = AuthenticationProfiles(
        name=profile_name,
        folder=TARGET_FOLDER,
        allow_list=["all"],
        method=method
    )

    logger.info(f"\n[SETUP] Creating Prerequisite Auth Profile: {profile_name}")
    created_profile = perform(
        auth_profiles_api.create_authentication_profiles_with_http_info,
        response_type=AuthenticationProfiles,
        authentication_profiles=payload
    )

    yield created_profile.name

    logger.info(f"\n[TEARDOWN] Deleting Auth Profile: {created_profile.name}")
    try:
        perform(
            auth_profiles_api.delete_authentication_profiles_by_id_with_http_info,
            id=created_profile.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup auth profile: {e}")

@pytest.fixture
def clean_auth_rule(auth_rules_api, test_auth_profile):
    rule_name = f"test-auth-rule-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationRules(
        name=rule_name,
        folder=TARGET_FOLDER,
        destination=["any"],
        var_from=["any"],
        service=["any"],
        source=["any"],
        to=["any"],
        authentication_enforcement=test_auth_profile,
        timeout=1000,
        description="Test rule for Auth Rule CRUD",
        log_authentication_timeout=True
    )

    logger.info(f"\n[SETUP] Creating Authentication Rule: {rule_name}")
    created_obj = perform(
        auth_rules_api.create_authentication_rules_with_http_info,
        response_type=AuthenticationRules,
        authentication_rules=payload,
        position="pre"
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Authentication Rule ID: {created_obj.id}")
    try:
        perform(
            auth_rules_api.delete_authentication_rules_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_auth_rule(auth_rules_api, test_auth_profile):
    rule_name = f"test-auth-create-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationRules(
        name=rule_name,
        folder=TARGET_FOLDER,
        destination=["any"],
        var_from=["any"],
        service=["any"],
        source=["any"],
        to=["any"],
        authentication_enforcement=test_auth_profile,
        timeout=1000,
        description="Test rule for Auth Rule CRUD",
        log_authentication_timeout=True
    )

    created_obj = perform(
        auth_rules_api.create_authentication_rules_with_http_info,
        response_type=AuthenticationRules,
        authentication_rules=payload,
        position="pre"
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == rule_name
    assert created_obj.timeout == 1000

    perform(
        auth_rules_api.delete_authentication_rules_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_auth_rule_by_id(auth_rules_api, clean_auth_rule):
    fetched_obj = perform(
        auth_rules_api.get_authentication_rules_by_id_with_http_info,
        id=clean_auth_rule.id
    )

    assert fetched_obj.id == clean_auth_rule.id
    assert fetched_obj.name == clean_auth_rule.name
    assert fetched_obj.service == ["any"]


def test_update_auth_rule(auth_rules_api, clean_auth_rule):
    update_payload = clean_auth_rule
    update_payload.timeout = 900
    update_payload.description = "Updated auth rule description"

    updated_obj = perform(
        auth_rules_api.update_authentication_rules_by_id_with_http_info,
        id=clean_auth_rule.id,
        authentication_rules=update_payload
    )

    assert updated_obj.id == clean_auth_rule.id
    assert updated_obj.timeout == 900
    assert updated_obj.description == "Updated auth rule description"


def test_list_auth_rules(auth_rules_api, clean_auth_rule):
    """Test listing Authentication Rules."""
    response = perform(
        auth_rules_api.list_authentication_rules_with_http_info,
        folder=TARGET_FOLDER,
        position="pre",
        limit=10,
        offset=15  # Skip default rules that may have deserialization issues
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_auth_rule.id:
            found = True
            break
    assert found is True, f"Created rule {clean_auth_rule.id} not found in list response"



def test_delete_auth_rule_by_id(auth_rules_api, test_auth_profile):
    rule_name = f"test-auth-del-{uuid.uuid4().hex[:6]}"

    payload = AuthenticationRules(
        name=rule_name,
        folder=TARGET_FOLDER,
        destination=["any"],
        var_from=["any"],
        service=["any"],
        source=["any"],
        to=["any"],
        authentication_enforcement=test_auth_profile,
        timeout=1000
    )

    created_obj = perform(
        auth_rules_api.create_authentication_rules_with_http_info,
        response_type=AuthenticationRules,
        authentication_rules=payload,
        position="pre"
    )

    perform(
        auth_rules_api.delete_authentication_rules_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        auth_rules_api.get_authentication_rules_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Rule should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
