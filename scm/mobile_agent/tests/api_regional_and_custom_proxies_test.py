
import logging
import uuid
import pytest
from scm import Scm
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies import ForwardingProfileRegionalAndCustomProxies
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_proxy1 import ForwardingProfileRegionalAndCustomProxiesProxy1
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_proxy2 import ForwardingProfileRegionalAndCustomProxiesProxy2
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_connectivity_preference_inner import ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner
from scm.mobile_agent.models.forwarding_profile_regional_and_custom_proxies_prisma_access_locations_inner import ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Folder to use for testing gp-and-pac proxies. Ensure this exists in your SCM environment.
TARGET_FOLDER = "Mobile Users"
# Folder to use for testing ztna-agent proxies.
ZTNA_FOLDER = "All"
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
def regional_and_custom_proxies_api(client):
    """
    Fixture to return the RegionalAndCustomProxies API instance.
    """
    return client.mobile_agent.RegionalAndCustomProxiesApi(client.mobile_agent.api_client)

@pytest.fixture
def clean_regional_and_custom_proxy(regional_and_custom_proxies_api):
    """
    Fixture to create a temporary gp-and-pac regional and custom proxy for testing
    and automatically delete it after.
    This mimics the 'Setup' and 'Cleanup' phases of your Go tests.
    """
    # 1. SETUP: Create ForwardingProfileRegionalAndCustomProxies
    object_name = f"test-regcustproxy-{uuid.uuid4().hex[:6]}"

    proxy1 = ForwardingProfileRegionalAndCustomProxiesProxy1(
        fqdn="mail.gmail.com",
        port=80,
        location="us"
    )
    proxy2 = ForwardingProfileRegionalAndCustomProxiesProxy2(
        fqdn="www.google.com",
        port=90,
        location="us"
    )

    # NOTE: 'id' is required by the Pydantic model but excluded from the API request.
    # We pass an empty string to satisfy validation.
    # The type "gp-and-pac" is required by the server.
    payload = ForwardingProfileRegionalAndCustomProxies(
        id="",
        name=object_name,
        type="gp-and-pac",
        proxy_1=proxy1,
        proxy_2=proxy2,
        description="Created via Automated Pytest Fixture"
    )

    # Use perform helper with _with_http_info
    logger.info(f"\n[SETUP] Creating ForwardingProfileRegionalAndCustomProxies: {object_name}")
    created_obj = perform(
        regional_and_custom_proxies_api.create_global_protect_regional_and_custom_proxies_with_http_info,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        folder=TARGET_FOLDER,
        forwarding_profile_regional_and_custom_proxies=payload
    )

    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete ForwardingProfileRegionalAndCustomProxies
    logger.info(f"\n[TEARDOWN] Deleting ForwardingProfileRegionalAndCustomProxies ID: {created_obj.id}")
    try:
        perform(
            regional_and_custom_proxies_api.delete_global_protect_regional_and_custom_proxies,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_regional_and_custom_proxy(regional_and_custom_proxies_api):
    """
    Test manual creation and deletion of a gp-and-pac regional and custom proxy.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_Create
    """
    object_name = f"test-regcustproxy-create-{uuid.uuid4().hex[:6]}"

    proxy1 = ForwardingProfileRegionalAndCustomProxiesProxy1(
        fqdn="mail.gmail.com",
        port=80,
        location="us"
    )
    proxy2 = ForwardingProfileRegionalAndCustomProxiesProxy2(
        fqdn="www.google.com",
        port=90,
        location="us"
    )

    payload = ForwardingProfileRegionalAndCustomProxies(
        id="",
        name=object_name,
        type="gp-and-pac",
        proxy_1=proxy1,
        proxy_2=proxy2,
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfileRegionalAndCustomProxies: {object_name}")

    created_obj = perform(
        regional_and_custom_proxies_api.create_global_protect_regional_and_custom_proxies_with_http_info,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        folder=TARGET_FOLDER,
        forwarding_profile_regional_and_custom_proxies=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.type == "gp-and-pac"

    # Validate proxy_1
    assert created_obj.proxy_1 is not None
    assert created_obj.proxy_1.fqdn == "mail.gmail.com"
    assert created_obj.proxy_1.location == "us"
    assert created_obj.proxy_1.port == 80

    # Validate proxy_2
    assert created_obj.proxy_2 is not None
    assert created_obj.proxy_2.fqdn == "www.google.com"
    assert created_obj.proxy_2.location == "us"
    assert created_obj.proxy_2.port == 90

    logger.info(f"Successfully created and validated ForwardingProfileRegionalAndCustomProxies: {object_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        regional_and_custom_proxies_api.delete_global_protect_regional_and_custom_proxies,
        id=created_obj.id
    )


def test_get_regional_and_custom_proxy_by_id(regional_and_custom_proxies_api, clean_regional_and_custom_proxy):
    """
    Test retrieving a regional and custom proxy by ID.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_GetByID
    Uses 'clean_regional_and_custom_proxy' fixture to handle creation/deletion automatically.
    """
    fetched_obj = perform(
        regional_and_custom_proxies_api.get_global_protect_regional_and_custom_proxy_by_id,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        id=clean_regional_and_custom_proxy.id
    )

    assert fetched_obj.id == clean_regional_and_custom_proxy.id
    assert fetched_obj.name == clean_regional_and_custom_proxy.name
    logger.info(f"Successfully retrieved ForwardingProfileRegionalAndCustomProxies by ID: {fetched_obj.id}")


def test_update_regional_and_custom_proxy(regional_and_custom_proxies_api, clean_regional_and_custom_proxy):
    """
    Test updating an existing regional and custom proxy.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_Update
    """
    update_payload = clean_regional_and_custom_proxy
    update_payload.description = "Updated description"

    updated_obj = perform(
        regional_and_custom_proxies_api.update_global_protect_regional_and_custom_proxy_by_id,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        id=clean_regional_and_custom_proxy.id,
        forwarding_profile_regional_and_custom_proxies=update_payload
    )

    assert updated_obj.description == "Updated description"
    assert updated_obj.name == clean_regional_and_custom_proxy.name
    assert updated_obj.id == clean_regional_and_custom_proxy.id
    logger.info(f"Successfully updated ForwardingProfileRegionalAndCustomProxies: {updated_obj.id}")


def test_list_regional_and_custom_proxies(regional_and_custom_proxies_api, clean_regional_and_custom_proxy):
    """
    Test listing regional and custom proxies with folder filter.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_List
    """
    response = perform(
        regional_and_custom_proxies_api.list_global_protect_regional_and_custom_proxies,
        folder=TARGET_FOLDER,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    found_proxy = False
    for p in response.data:
        if p.name == clean_regional_and_custom_proxy.name:
            found_proxy = True
            break

    assert found_proxy, f"Created ForwardingProfileRegionalAndCustomProxies '{clean_regional_and_custom_proxy.name}' should be found in the list"
    logger.info(f"List returned {len(response.data)} items and found our proxy")


def test_delete_regional_and_custom_proxy_by_id(regional_and_custom_proxies_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_DeleteByID
    We manually create and delete here to verify the delete logic explicitly.
    """
    object_name = f"test-regcustproxy-delete-{uuid.uuid4().hex[:6]}"

    proxy1 = ForwardingProfileRegionalAndCustomProxiesProxy1(
        fqdn="mail.gmail.com",
        port=80,
        location="us"
    )
    proxy2 = ForwardingProfileRegionalAndCustomProxiesProxy2(
        fqdn="www.google.com",
        port=90,
        location="us"
    )

    payload = ForwardingProfileRegionalAndCustomProxies(
        id="",
        name=object_name,
        type="gp-and-pac",
        proxy_1=proxy1,
        proxy_2=proxy2,
        description="Test regional and custom proxy for delete API testing"
    )

    created_obj = perform(
        regional_and_custom_proxies_api.create_global_protect_regional_and_custom_proxies_with_http_info,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        folder=TARGET_FOLDER,
        forwarding_profile_regional_and_custom_proxies=payload
    )

    perform(
        regional_and_custom_proxies_api.delete_global_protect_regional_and_custom_proxies,
        id=created_obj.id
    )

    logger.info(f"Successfully deleted ForwardingProfileRegionalAndCustomProxies: {created_obj.id}")


def test_fetch_regional_and_custom_proxies(regional_and_custom_proxies_api, clean_regional_and_custom_proxy):
    """
    Test fetching a single regional and custom proxy by name using the fetch convenience method.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_FetchRegionalAndCustomProxies
    """
    # Test 1: Fetch existing object by name
    fetched_obj = regional_and_custom_proxies_api.fetch_regional_and_custom_proxies(
        name=clean_regional_and_custom_proxy.name,
        folder=TARGET_FOLDER
    )

    assert fetched_obj is not None, f"Should have found regional and custom proxy '{clean_regional_and_custom_proxy.name}'"
    assert fetched_obj.id == clean_regional_and_custom_proxy.id
    assert fetched_obj.name == clean_regional_and_custom_proxy.name
    logger.info(f"fetch_regional_and_custom_proxies found object: {fetched_obj.name}")

    # Test 2: Fetch non-existent object (should return None)
    not_found = regional_and_custom_proxies_api.fetch_regional_and_custom_proxies(
        name="non-existent-regional-custom-proxy-xyz-12345",
        folder=TARGET_FOLDER
    )
    assert not_found is None, "Should return None for non-existent regional and custom proxy"
    logger.info("fetch_regional_and_custom_proxies correctly returned None for non-existent object")


def test_create_ztna_agent_proxy(regional_and_custom_proxies_api):
    """
    Test creation of a ztna-agent type regional and custom proxy.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_ZtnaAgent_Create
    """
    object_name = f"test-ztna-create-{uuid.uuid4().hex[:6]}"

    connectivity_pref = ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner(
        name="masque",
        enabled=True
    )

    prisma_location = ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner(
        name="americas",
        locations=["us-southwest"]
    )

    payload = ForwardingProfileRegionalAndCustomProxies(
        id="",
        name=object_name,
        type="ztna-agent",
        connectivity_preference=[connectivity_pref],
        fallback_option="fail-open",
        location_preference="specific-pa-location",
        prisma_access_locations=[prisma_location]
    )

    logger.info(f"\n[TEST] Attempting to create ZTNA Agent Proxy: {object_name}")

    created_obj = perform(
        regional_and_custom_proxies_api.create_global_protect_regional_and_custom_proxies_with_http_info,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        folder=ZTNA_FOLDER,
        forwarding_profile_regional_and_custom_proxies=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.type == "ztna-agent"
    assert created_obj.fallback_option == "fail-open"
    assert created_obj.location_preference == "specific-pa-location"

    assert len(created_obj.connectivity_preference) == 1
    assert created_obj.connectivity_preference[0].name == "masque"
    assert created_obj.connectivity_preference[0].enabled is True

    assert len(created_obj.prisma_access_locations) == 1
    assert created_obj.prisma_access_locations[0].name == "americas"
    assert created_obj.prisma_access_locations[0].locations == ["us-southwest"]

    logger.info(f"Successfully created and validated ZTNA Agent Proxy: {object_name} with ID: {created_obj.id}")

    # Cleanup
    perform(
        regional_and_custom_proxies_api.delete_global_protect_regional_and_custom_proxies,
        id=created_obj.id
    )


@pytest.fixture
def clean_ztna_proxy(regional_and_custom_proxies_api):
    """
    Fixture to create a temporary ztna-agent proxy for testing and automatically delete it after.
    """
    object_name = f"test-ztna-{uuid.uuid4().hex[:6]}"

    connectivity_pref = ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner(
        name="masque",
        enabled=True
    )

    prisma_location = ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner(
        name="americas",
        locations=["us-southwest"]
    )

    payload = ForwardingProfileRegionalAndCustomProxies(
        id="",
        name=object_name,
        type="ztna-agent",
        connectivity_preference=[connectivity_pref],
        fallback_option="fail-open",
        location_preference="specific-pa-location",
        prisma_access_locations=[prisma_location],
        description="Created via Automated Pytest Fixture"
    )

    logger.info(f"\n[SETUP] Creating ZTNA Agent Proxy: {object_name}")
    created_obj = perform(
        regional_and_custom_proxies_api.create_global_protect_regional_and_custom_proxies_with_http_info,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        folder=ZTNA_FOLDER,
        forwarding_profile_regional_and_custom_proxies=payload
    )

    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting ZTNA Agent Proxy ID: {created_obj.id}")
    try:
        perform(
            regional_and_custom_proxies_api.delete_global_protect_regional_and_custom_proxies,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_get_ztna_agent_proxy_by_id(regional_and_custom_proxies_api, clean_ztna_proxy):
    """
    Test retrieving a ztna-agent proxy by ID.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_ZtnaAgent_GetByID
    """
    fetched_obj = perform(
        regional_and_custom_proxies_api.get_global_protect_regional_and_custom_proxy_by_id,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        id=clean_ztna_proxy.id
    )

    assert fetched_obj.id == clean_ztna_proxy.id
    assert fetched_obj.name == clean_ztna_proxy.name
    logger.info(f"Successfully retrieved ZTNA Agent Proxy by ID: {fetched_obj.id}")


def test_update_ztna_agent_proxy(regional_and_custom_proxies_api, clean_ztna_proxy):
    """
    Test updating an existing ztna-agent proxy.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_ZtnaAgent_Update
    """
    update_payload = clean_ztna_proxy
    update_payload.description = "Updated description"

    updated_obj = perform(
        regional_and_custom_proxies_api.update_global_protect_regional_and_custom_proxy_by_id,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        id=clean_ztna_proxy.id,
        forwarding_profile_regional_and_custom_proxies=update_payload
    )

    assert updated_obj.description == "Updated description"
    assert updated_obj.name == clean_ztna_proxy.name
    assert updated_obj.id == clean_ztna_proxy.id
    logger.info(f"Successfully updated ZTNA Agent Proxy: {updated_obj.id}")


def test_list_ztna_agent_proxies(regional_and_custom_proxies_api, clean_ztna_proxy):
    """
    Test listing ztna-agent proxies with folder filter.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_ZtnaAgent_List
    """
    response = perform(
        regional_and_custom_proxies_api.list_global_protect_regional_and_custom_proxies,
        folder=ZTNA_FOLDER,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    found_proxy = False
    for p in response.data:
        if p.name == clean_ztna_proxy.name:
            found_proxy = True
            break

    assert found_proxy, f"Created ZTNA Agent Proxy '{clean_ztna_proxy.name}' should be found in the list"
    logger.info(f"List returned {len(response.data)} items and found our ZTNA Agent Proxy")


def test_delete_ztna_agent_proxy_by_id(regional_and_custom_proxies_api):
    """
    Test deletion of a ztna-agent proxy specifically.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_ZtnaAgent_DeleteByID
    """
    object_name = f"test-ztna-delete-{uuid.uuid4().hex[:6]}"

    connectivity_pref = ForwardingProfileRegionalAndCustomProxiesConnectivityPreferenceInner(
        name="masque",
        enabled=True
    )

    prisma_location = ForwardingProfileRegionalAndCustomProxiesPrismaAccessLocationsInner(
        name="americas",
        locations=["us-southwest"]
    )

    payload = ForwardingProfileRegionalAndCustomProxies(
        id="",
        name=object_name,
        type="ztna-agent",
        connectivity_preference=[connectivity_pref],
        fallback_option="fail-open",
        location_preference="specific-pa-location",
        prisma_access_locations=[prisma_location]
    )

    created_obj = perform(
        regional_and_custom_proxies_api.create_global_protect_regional_and_custom_proxies_with_http_info,
        response_type=ForwardingProfileRegionalAndCustomProxies,
        folder=ZTNA_FOLDER,
        forwarding_profile_regional_and_custom_proxies=payload
    )

    perform(
        regional_and_custom_proxies_api.delete_global_protect_regional_and_custom_proxies,
        id=created_obj.id
    )

    logger.info(f"Successfully deleted ZTNA Agent Proxy: {created_obj.id}")


def test_fetch_ztna_agent_proxies(regional_and_custom_proxies_api, clean_ztna_proxy):
    """
    Test fetching a single ztna-agent proxy by name using the fetch convenience method.
    Equivalent to Go: Test_mobile_agent_RegionalAndCustomProxiesAPIService_ZtnaAgent_Fetch
    """
    # Test 1: Fetch existing object by name
    fetched_obj = regional_and_custom_proxies_api.fetch_regional_and_custom_proxies(
        name=clean_ztna_proxy.name,
        folder=ZTNA_FOLDER
    )

    assert fetched_obj is not None, f"Should have found ZTNA agent proxy '{clean_ztna_proxy.name}'"
    assert fetched_obj.id == clean_ztna_proxy.id
    assert fetched_obj.name == clean_ztna_proxy.name
    logger.info(f"fetch_regional_and_custom_proxies found object: {fetched_obj.name}")

    # Test 2: Fetch non-existent object (should return None)
    not_found = regional_and_custom_proxies_api.fetch_regional_and_custom_proxies(
        name="non-existent-ztna-proxy-xyz-12345",
        folder=ZTNA_FOLDER
    )
    assert not_found is None, "Should return None for non-existent ZTNA agent proxy"
    logger.info("fetch_regional_and_custom_proxies correctly returned None for non-existent ZTNA agent proxy")
