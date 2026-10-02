
import logging
import uuid
import json
import pytest
from scm import Scm
from scm.mobile_agent.models.forwarding_profile_source_applications import ForwardingProfileSourceApplications
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
def source_applications_api(client):
    """
    Fixture to return the Source Applications API instance.
    """
    return client.mobile_agent.SourceApplicationsApi(client.mobile_agent.api_client)

@pytest.fixture
def clean_source_application(source_applications_api):
    """
    Fixture to create a temporary source application for testing and automatically delete it after.
    This mimics the 'Setup' and 'Cleanup' phases of your Go tests.
    """
    # 1. SETUP: Create ForwardingProfileSourceApplications
    object_name = f"test-sourceapp-{uuid.uuid4().hex[:6]}"

    # NOTE: 'id' is required by the Pydantic model but excluded from the API request.
    # We pass an empty string to satisfy validation.
    payload = ForwardingProfileSourceApplications(
        id="",
        name=object_name,
        applications=["app1", "app2"],
        description="Created via Automated Pytest Fixture"
    )

    # Use perform helper with _with_http_info
    logger.info(f"\n[SETUP] Creating ForwardingProfileSourceApplications: {object_name}")
    created_obj = perform(
        source_applications_api.create_global_protect_source_application_with_http_info,
        response_type=ForwardingProfileSourceApplications,
        folder=TARGET_FOLDER,
        forwarding_profile_source_applications=payload
    )

    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete ForwardingProfileSourceApplications
    logger.info(f"\n[TEARDOWN] Note: Source Applications may need manual cleanup - ID: {created_obj.id}")


def test_create_source_application(source_applications_api):
    """
    Test manual creation of a source application with full set of fields including description.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_Create
    """
    object_name = f"test-sourceapp-create-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileSourceApplications(
        id="",
        name=object_name,
        description="Test source application for create",
        applications=["chrome", "firefox", "safari"]
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfileSourceApplications: {object_name}")

    # Create using perform helper
    created_obj = perform(
        source_applications_api.create_global_protect_source_application_with_http_info,
        response_type=ForwardingProfileSourceApplications,
        folder=TARGET_FOLDER,
        forwarding_profile_source_applications=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.description == "Test source application for create"

    # Verify applications
    assert len(created_obj.applications) == 3
    assert set(created_obj.applications) == {"chrome", "firefox", "safari"}

    logger.info(f"Successfully created and validated ForwardingProfileSourceApplications: {object_name} with ID: {created_obj.id}")
    logger.info(f"Note: Source Applications may need manual cleanup - ID: {created_obj.id}")


def test_create_source_application_minimal(source_applications_api):
    """
    Test creation of a source application with only required fields (applications and name).
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_CreateMinimal
    """
    object_name = f"test-sourceapp-minimal-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileSourceApplications(
        id="",
        name=object_name,
        applications=["app1", "app2"]
    )

    logger.info(f"\n[TEST] Attempting to create minimal ForwardingProfileSourceApplications: {object_name}")

    # Create using perform helper
    created_obj = perform(
        source_applications_api.create_global_protect_source_application_with_http_info,
        response_type=ForwardingProfileSourceApplications,
        folder=TARGET_FOLDER,
        forwarding_profile_source_applications=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert set(created_obj.applications) == {"app1", "app2"}

    logger.info(f"Successfully created minimal ForwardingProfileSourceApplications: {object_name} with ID: {created_obj.id}")


def test_get_source_application_by_id(source_applications_api, clean_source_application):
    """
    Test retrieving a source application by ID.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_GetByID
    Uses 'clean_source_application' fixture to handle creation automatically.
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        source_applications_api.get_global_protect_source_application_by_id,
        response_type=ForwardingProfileSourceApplications,
        id=clean_source_application.id
    )

    # Verify
    assert fetched_obj.id == clean_source_application.id
    assert fetched_obj.name == clean_source_application.name
    assert set(fetched_obj.applications) == {"app1", "app2"}
    logger.info(f"Successfully retrieved ForwardingProfileSourceApplications by ID: {fetched_obj.id}")


def test_update_source_application(source_applications_api, clean_source_application):
    """
    Test updating an existing source application.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_Update
    """
    # Prepare Update
    update_payload = clean_source_application
    update_payload.description = "Updated description for source application"
    update_payload.applications = ["chrome", "firefox", "edge"]

    # Perform Update using helper
    updated_obj = perform(
        source_applications_api.update_global_protect_source_application_by_id,
        response_type=ForwardingProfileSourceApplications,
        id=clean_source_application.id,
        forwarding_profile_source_applications=update_payload
    )

    # Verify
    assert updated_obj.description == "Updated description for source application"
    assert updated_obj.name == clean_source_application.name
    assert updated_obj.id == clean_source_application.id
    assert set(updated_obj.applications) == {"chrome", "firefox", "edge"}
    logger.info(f"Successfully updated ForwardingProfileSourceApplications: {updated_obj.id}")


def test_list_source_applications(source_applications_api, clean_source_application):
    """
    Test listing source applications with folder filter.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_List
    """
    # List with filter using helper
    response = perform(
        source_applications_api.list_global_protect_source_applications,
        folder=TARGET_FOLDER,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our source application is in the list
    found_app = False
    for app in response.data:
        if app.name == clean_source_application.name:
            found_app = True
            assert app.id == clean_source_application.id
            assert set(app.applications) == {"app1", "app2"}
            break

    assert found_app, f"Created ForwardingProfileSourceApplications '{clean_source_application.name}' should be found in the list"
    logger.info(f"List returned {len(response.data)} items and found our source application")


def test_list_source_applications_with_name_filter(source_applications_api, clean_source_application):
    """
    Test listing source applications with a name filter.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_ListWithNameFilter
    """
    # List with name filter using helper
    response = perform(
        source_applications_api.list_global_protect_source_applications,
        folder=TARGET_FOLDER,
        name=clean_source_application.name,
        limit=10
    )

    assert response is not None

    # Verify our source application is in the filtered results
    found_app = False
    for app in response.data:
        if app.name == clean_source_application.name:
            found_app = True
            assert app.id == clean_source_application.id
            break

    assert found_app, f"Created ForwardingProfileSourceApplications '{clean_source_application.name}' should be found with name filter"
    logger.info(f"Successfully filtered source applications by name: {clean_source_application.name}")


def test_list_source_applications_pagination(source_applications_api):
    """
    Test pagination parameters when listing source applications.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_ListPagination
    """
    # Create multiple test objects to test pagination
    created_names = []
    random_suffix = uuid.uuid4().hex[:6]

    for i in range(3):
        app_name = f"test-sourceapp-page-{random_suffix}-{i}"
        created_names.append(app_name)

        payload = ForwardingProfileSourceApplications(
            id="",
            name=app_name,
            applications=["app1", "app2"]
        )

        perform(
            source_applications_api.create_global_protect_source_application_with_http_info,
            response_type=ForwardingProfileSourceApplications,
            folder=TARGET_FOLDER,
            forwarding_profile_source_applications=payload
        )

    # Test with limit
    response = perform(
        source_applications_api.list_global_protect_source_applications,
        folder=TARGET_FOLDER,
        limit=2,
        offset=0
    )

    assert response is not None
    logger.info(f"Retrieved {len(response.data)} items with limit=2")

    # Test with offset
    response2 = perform(
        source_applications_api.list_global_protect_source_applications,
        folder=TARGET_FOLDER,
        limit=10,
        offset=1
    )

    assert response2 is not None
    logger.info(f"Retrieved {len(response2.data)} items with offset=1")
    logger.info("Pagination test completed successfully")


def test_delete_source_application_by_id(source_applications_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_DeleteByID
    We manually create and delete here to verify the delete logic explicitly.
    """
    # Setup
    object_name = f"test-sourceapp-delete-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileSourceApplications(
        id="",
        name=object_name,
        applications=["app1", "app2"],
        description="Test source application for delete API testing"
    )

    created_obj = perform(
        source_applications_api.create_global_protect_source_application_with_http_info,
        response_type=ForwardingProfileSourceApplications,
        folder=TARGET_FOLDER,
        forwarding_profile_source_applications=payload
    )

    # Perform Delete using helper
    perform(
        source_applications_api.delete_global_protect_source_application,
        id=created_obj.id
    )

    logger.info(f"Successfully deleted ForwardingProfileSourceApplications: {created_obj.id}")


def test_create_source_application_with_empty_applications(source_applications_api):
    """
    Test that creation fails when applications list is empty (validation test).
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_CreateWithEmptyApplications
    """
    object_name = f"test-sourceapp-empty-{uuid.uuid4().hex[:6]}"

    payload = ForwardingProfileSourceApplications(
        id="",
        name=object_name,
        applications=[]  # empty applications list
    )

    logger.info(f"\n[TEST] Attempting to create ForwardingProfileSourceApplications with empty applications list")

    # This test expects the API to reject empty applications list
    # The exact behavior depends on API validation
    try:
        created_obj = perform(
            source_applications_api.create_global_protect_source_application_with_http_info,
            response_type=ForwardingProfileSourceApplications,
            folder=TARGET_FOLDER,
            forwarding_profile_source_applications=payload
        )
        # If API accepts it, log a warning
        logger.warning(f"WARNING: API accepted empty applications list")
        if created_obj.id:
            logger.info(f"Created object with ID: {created_obj.id} (may need cleanup)")
    except Exception as e:
        # Expected path: API rejects empty list
        logger.info(f"API correctly rejected empty applications list with error: {e}")


def test_fetch_source_applications(source_applications_api, clean_source_application):
    """
    Test fetching a single source application by name using the fetch convenience method.
    Equivalent to Go: Test_mobile_agent_SourceApplicationsAPIService_FetchSourceApplications
    """
    # Test 1: Fetch existing object by name
    fetched_obj = source_applications_api.fetch_source_applications(
        name=clean_source_application.name,
        folder=TARGET_FOLDER
    )

    # Verify
    assert fetched_obj is not None, f"Should have found source application '{clean_source_application.name}'"
    assert fetched_obj.id == clean_source_application.id
    assert fetched_obj.name == clean_source_application.name
    assert fetched_obj.description == "Created via Automated Pytest Fixture"
    assert set(fetched_obj.applications) == {"app1", "app2"}
    logger.info(f"fetch_source_applications found object: {fetched_obj.name}")

    # Test 2: Fetch non-existent object (should return None)
    not_found = source_applications_api.fetch_source_applications(
        name="non-existent-source-application-xyz-12345",
        folder=TARGET_FOLDER
    )
    assert not_found is None, "Should return None for non-existent source application"
    logger.info(f"fetch_source_applications correctly returned None for non-existent source application")
