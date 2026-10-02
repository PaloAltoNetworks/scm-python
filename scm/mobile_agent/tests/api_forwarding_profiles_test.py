
import logging
import uuid
import json
import pytest
from scm import Scm
from scm.mobile_agent.models.forwarding_profiles import ForwardingProfiles
from scm.mobile_agent.models.forwarding_profiles_type import ForwardingProfilesType
from scm.mobile_agent.models.forwarding_profile_global_protect_proxy_global_protect_proxy import ForwardingProfileGlobalProtectProxyGlobalProtectProxy
from scm.mobile_agent.models.forwarding_profile_ztna_agent_ztna_agent import ForwardingProfileZtnaAgentZtnaAgent
from scm.mobile_agent.models.forwarding_rule_ztna import ForwardingRuleZtna
from scm.mobile_agent.models.block_rule_ztna import BlockRuleZtna
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Folder to use for testing. Ensure this exists in your SCM environment.
TARGET_FOLDER = "Mobile Users"
# -----------------------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    """
    Fixture to initialize the SCM client once for the module.
    Assumes SCM_CLIENT_ID, SCM_CLIENT_SECRET, SCM_TSG_ID are set in env.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def forwarding_profiles_api(client):
    """
    Fixture to return the ForwardingProfiles API instance.
    """
    return client.mobile_agent.ForwardingProfilesApi(client.mobile_agent.api_client)

@pytest.fixture
def clean_forwarding_profile(forwarding_profiles_api):
    """
    Fixture to create a temporary forwarding profile for testing and automatically delete it after.
    This mimics the 'Setup' and 'Cleanup' phases of your Go tests.
    """
    # 1. SETUP: Create ForwardingProfiles
    object_name = f"test-fwdprofile-{uuid.uuid4().hex[:6]}"

    # Create a minimal valid forwarding profile
    # The API requires the 'type' node even though the OpenAPI schema marks only 'name' as required
    # GlobalProtectProxy has all-optional sub-fields so an empty struct satisfies the server
    global_protect_proxy = ForwardingProfileGlobalProtectProxyGlobalProtectProxy()

    profile_type = ForwardingProfilesType(
        global_protect_proxy=global_protect_proxy
    )

    # NOTE: 'id' is required by the Pydantic model but excluded from the API request.
    # We pass an empty string to satisfy validation.
    payload = ForwardingProfiles(
        id="",
        name=object_name,
        type=profile_type,
        description="Created via Automated Pytest Fixture"
    )

    # Use perform helper with _with_http_info
    logger.info(f"\n[SETUP] Creating ForwardingProfile: {object_name}")
    created_obj = perform(
        forwarding_profiles_api.create_global_protect_forwarding_profile_with_http_info,
        response_type=ForwardingProfiles,
        folder=TARGET_FOLDER,
        forwarding_profiles=payload
    )

    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete ForwardingProfile
    logger.info(f"\n[TEARDOWN] Deleting ForwardingProfile ID: {created_obj.id}")
    try:
        perform(
            forwarding_profiles_api.delete_global_protect_forwarding_profile,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_forwarding_profile(forwarding_profiles_api):
    """
    Test manual creation and deletion of a forwarding profile using ztna_agent type
    with forwarding rule and block rule fully populated.
    Equivalent to Go: Test_mobile_agent_ForwardingProfilesAPIService_Create
    """
    object_name = f"test-fwdprofile-create-{uuid.uuid4().hex[:6]}"

    # Create forwarding rule
    forwarding_rule = ForwardingRuleZtna(
        name="rule-1",
        traffic_type="dns",
        enabled=True,
        user_locations="Any",
        source_applications="Any",
        destinations="Any",
        connectivity="direct"
    )

    # Create block rule
    block_rule = BlockRuleZtna(
        block_all_other_unmatched_outbound_connections=False,
        block_outbound_lan_access_when_connected_to_tunnel=False,
        block_inbound_access_when_connected_to_tunnel=False,
        block_non_tcp_non_udp_traffic_when_connected_to_tunnel=False,
        allow_icmp_for_troubleshooting=False,
        enforcer_fqdn_dns_resolution_via_dns_servers=True,
        resolve_all_fqdns_using_dns_servers_assigned_by_the_tunnel=True
    )

    # Create ztna_agent type
    ztna_agent = ForwardingProfileZtnaAgentZtnaAgent(
        pac_upload=False,
        forwarding_rules=[forwarding_rule],
        block_rule=block_rule
    )

    profile_type = ForwardingProfilesType(
        ztna_agent=ztna_agent
    )

    payload = ForwardingProfiles(
        id="",
        name=object_name,
        description="Test forwarding profile for create",
        definition_method="rules",
        type=profile_type,
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfile: {object_name}")

    # Create using perform helper
    created_obj = perform(
        forwarding_profiles_api.create_global_protect_forwarding_profile_with_http_info,
        response_type=ForwardingProfiles,
        folder=TARGET_FOLDER,
        forwarding_profiles=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.description == "Test forwarding profile for create"

    # Verify type and ztna_agent
    assert created_obj.type is not None
    assert created_obj.type.ztna_agent is not None

    returned_ztna = created_obj.type.ztna_agent
    assert returned_ztna.pac_upload is False

    # Verify forwarding rule
    assert len(returned_ztna.forwarding_rules) == 1
    rule = returned_ztna.forwarding_rules[0]
    assert rule.name == "rule-1"
    assert rule.traffic_type == "dns"
    assert rule.enabled is True
    assert rule.user_locations == "Any"
    assert rule.source_applications == "Any"
    assert rule.destinations == "Any"
    assert rule.connectivity == "direct"

    # Verify block rule
    assert returned_ztna.block_rule is not None
    br = returned_ztna.block_rule
    assert br.block_all_other_unmatched_outbound_connections is False
    assert br.block_outbound_lan_access_when_connected_to_tunnel is False
    assert br.block_inbound_access_when_connected_to_tunnel is False
    assert br.block_non_tcp_non_udp_traffic_when_connected_to_tunnel is False
    assert br.allow_icmp_for_troubleshooting is False
    assert br.enforcer_fqdn_dns_resolution_via_dns_servers is True
    assert br.resolve_all_fqdns_using_dns_servers_assigned_by_the_tunnel is True

    logger.info(f"Successfully created and validated ForwardingProfile: {object_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        forwarding_profiles_api.delete_global_protect_forwarding_profile,
        id=created_obj.id
    )


def test_get_forwarding_profile_by_id(forwarding_profiles_api, clean_forwarding_profile):
    """
    Test retrieving a forwarding profile by ID.
    Equivalent to Go: Test_mobile_agent_ForwardingProfilesAPIService_GetByID
    Uses 'clean_forwarding_profile' fixture to handle creation/deletion automatically.
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        forwarding_profiles_api.get_global_protect_forwarding_profile_by_id,
        response_type=ForwardingProfiles,
        id=clean_forwarding_profile.id
    )

    # Verify
    assert fetched_obj.id == clean_forwarding_profile.id
    assert fetched_obj.name == clean_forwarding_profile.name
    logger.info(f"Successfully retrieved ForwardingProfile by ID: {fetched_obj.id}")


def test_update_forwarding_profile(forwarding_profiles_api, clean_forwarding_profile):
    """
    Test updating an existing forwarding profile.
    Equivalent to Go: Test_mobile_agent_ForwardingProfilesAPIService_Update
    """
    # Prepare Update
    update_payload = clean_forwarding_profile
    update_payload.description = "Updated description"

    # Perform Update using helper
    updated_obj = perform(
        forwarding_profiles_api.update_global_protect_forwarding_profile_by_id,
        response_type=ForwardingProfiles,
        id=clean_forwarding_profile.id,
        forwarding_profiles=update_payload
    )

    # Verify
    assert updated_obj.description == "Updated description"
    assert updated_obj.name == clean_forwarding_profile.name
    assert updated_obj.id == clean_forwarding_profile.id
    logger.info(f"Successfully updated ForwardingProfile: {updated_obj.id}")


def test_list_forwarding_profiles(forwarding_profiles_api, clean_forwarding_profile):
    """
    Test listing forwarding profiles with folder filter.
    Equivalent to Go: Test_mobile_agent_ForwardingProfilesAPIService_List
    """
    # List with filter using helper
    response = perform(
        forwarding_profiles_api.list_global_protect_forwarding_profiles,
        folder=TARGET_FOLDER,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our profile is in the list
    found_profile = False
    for profile in response.data:
        if profile.name == clean_forwarding_profile.name:
            found_profile = True
            break

    assert found_profile, f"Created ForwardingProfile '{clean_forwarding_profile.name}' should be found in the list"
    logger.info(f"List returned {len(response.data)} items and found our profile")


def test_delete_forwarding_profile_by_id(forwarding_profiles_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_mobile_agent_ForwardingProfilesAPIService_DeleteByID
    We manually create and delete here to verify the delete logic explicitly.
    """
    from scm.exceptions import ObjectNotPresentError

    # Setup
    object_name = f"test-fwdprofile-delete-{uuid.uuid4().hex[:6]}"

    global_protect_proxy = ForwardingProfileGlobalProtectProxyGlobalProtectProxy()
    profile_type = ForwardingProfilesType(
        global_protect_proxy=global_protect_proxy
    )

    payload = ForwardingProfiles(
        id="",
        name=object_name,
        type=profile_type,
        description="Test forwarding profile for delete API testing"
    )

    created_obj = perform(
        forwarding_profiles_api.create_global_protect_forwarding_profile_with_http_info,
        response_type=ForwardingProfiles,
        folder=TARGET_FOLDER,
        forwarding_profiles=payload
    )

    # Perform Delete using helper
    perform(
        forwarding_profiles_api.delete_global_protect_forwarding_profile,
        id=created_obj.id
    )

    logger.info(f"Successfully deleted ForwardingProfile: {created_obj.id}")


def test_fetch_forwarding_profiles(forwarding_profiles_api, clean_forwarding_profile):
    """
    Test fetching a single forwarding profile by name using the fetch convenience method.
    Equivalent to Go: Test_mobile_agent_ForwardingProfilesAPIService_FetchForwardingProfiles
    """
    # Test 1: Fetch existing object by name
    fetched_obj = forwarding_profiles_api.fetch_forwarding_profiles(
        name=clean_forwarding_profile.name,
        folder=TARGET_FOLDER
    )

    # Verify
    assert fetched_obj is not None, f"Should have found forwarding profile '{clean_forwarding_profile.name}'"
    assert fetched_obj.id == clean_forwarding_profile.id
    assert fetched_obj.name == clean_forwarding_profile.name
    logger.info(f"fetch_forwarding_profiles found object: {fetched_obj.name}")

    # Test 2: Fetch non-existent object (should return None)
    not_found = forwarding_profiles_api.fetch_forwarding_profiles(
        name="non-existent-forwarding-profile-xyz-12345",
        folder=TARGET_FOLDER
    )
    assert not_found is None, "Should return None for non-existent forwarding profile"
    logger.info(f"fetch_forwarding_profiles correctly returned None for non-existent forwarding profile")
