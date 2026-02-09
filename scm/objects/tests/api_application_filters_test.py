
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.application_filters import ApplicationFilters

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Prisma Access"
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
def app_filters_api(client):
    """
    Fixture to return the Application Filters API instance.
    """
    return client.objects.ApplicationFiltersApi(client.objects.api_client)

@pytest.fixture
def clean_application_filter(app_filters_api):
    """
    Fixture to create a temporary Application Filter for testing and automatically delete it after.
    """
    # 1. SETUP: Create Application Filter
    random_id = uuid.uuid4().hex[:6]
    filter_name = f"test-app-filter-{random_id}"
    
    payload = ApplicationFilters(
        id="",
        name=filter_name,
        folder=TARGET_FOLDER,
        category=["business-systems"],
        risk=[2],
        technology=["client-server"],
        description="Created via Automated Pytest Fixture"
    )
    
    logger.info(f"\n[SETUP] Creating Application Filter: {filter_name}")
    created_obj = app_filters_api.create_application_filters(application_filters=payload)
    assert created_obj.id is not None
    
    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Application Filter
    logger.info(f"\n[TEARDOWN] Deleting Application Filter ID: {created_obj.id}")
    try:
        app_filters_api.delete_application_filters_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_application_filter(app_filters_api):
    """
    Test manual creation and deletion of an application filter.
    Equivalent to Go: Test_objects_ApplicationFiltersAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    filter_name = f"test-app-filter-create-{random_suffix}"
    
    payload = ApplicationFilters(
        id="",
        name=filter_name,
        folder=TARGET_FOLDER,
        category=["business-systems"],
        risk=[1],
        evasive=True,
        description="Test application filter for create API testing"
    )

    # Create
    created_obj = app_filters_api.create_application_filters(application_filters=payload)
    
    # Verify
    assert created_obj.name == filter_name
    assert created_obj.id is not None
    assert created_obj.category == ["business-systems"]
    assert created_obj.evasive is True
    assert created_obj.folder == TARGET_FOLDER or created_obj.folder == "Shared"

    # Cleanup
    app_filters_api.delete_application_filters_by_id(id=created_obj.id)


def test_get_application_filter_by_id(app_filters_api, clean_application_filter):
    """
    Test retrieving an application filter by ID.
    Equivalent to Go: Test_objects_ApplicationFiltersAPIService_GetByID
    """
    # Retrieve
    fetched_obj = app_filters_api.get_application_filters_by_id(id=clean_application_filter.id)
    
    # Verify
    assert fetched_obj.id == clean_application_filter.id
    assert fetched_obj.name == clean_application_filter.name
    assert fetched_obj.folder == clean_application_filter.folder
    
    # Verify list fields (using set for robust comparison in case of order differences)
    assert set(fetched_obj.category) == set(clean_application_filter.category)
    assert set(fetched_obj.technology) == set(clean_application_filter.technology)


def test_update_application_filter(app_filters_api, clean_application_filter):
    """
    Test updating an application filter.
    Equivalent to Go: Test_objects_ApplicationFiltersAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_application_filter
    
    # Update fields as per Go test
    update_payload.category = ["business-systems", "networking"]
    update_payload.risk = [3, 4]
    update_payload.technology = ["client-server", "peer-to-peer"]
    # update_payload.exclude = ["ftp"] # Uncomment if 'exclude' is available in your generated model

    # Perform Update
    updated_obj = app_filters_api.update_application_filters_by_id(
        id=clean_application_filter.id, 
        application_filters=update_payload
    )
    
    # Verify
    assert updated_obj.id == clean_application_filter.id
    assert updated_obj.name == clean_application_filter.name
    assert set(updated_obj.category) == {"business-systems", "networking"}
    assert set(updated_obj.risk) == {3, 4}
    assert set(updated_obj.technology) == {"client-server", "peer-to-peer"}


def test_list_application_filters(app_filters_api, clean_application_filter):
    """
    Test listing application filters with folder filter.
    Equivalent to Go: Test_objects_ApplicationFiltersAPIService_List
    """
    # List with filter
    response = app_filters_api.list_application_filters(folder=clean_application_filter.folder)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.id == clean_application_filter.id:
            found = True
            assert item.name == clean_application_filter.name
            break
            
    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")




def test_fetch_application_filters(app_filters_api, clean_application_filter):
    """
    Test fetching a single application_filters by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = app_filters_api.fetch_application_filters(
        name=clean_application_filter.name,
        folder=clean_application_filter.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found application_filters '{clean_application_filter.name}'"
    assert fetched_obj.id == clean_application_filter.id
    assert fetched_obj.name == clean_application_filter.name
    assert fetched_obj.folder == clean_application_filter.folder
    logger.info(f"\n[SUCCESS] fetch_application_filters found object: {fetched_obj.name}")

    # Test fetching non-existent application_filters (should return None)
    not_found = app_filters_api.fetch_application_filters(
        name="non-existent-application_filters-xyz-12345",
        folder=clean_application_filter.folder
    )
    assert not_found is None, "Should return None for non-existent application_filters"
    logger.info(f"\n[SUCCESS] fetch_application_filters correctly returned None for non-existent application_filters")


def test_delete_application_filter_by_id(app_filters_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_ApplicationFiltersAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    filter_name = f"test-app-filter-del-{random_suffix}"
    
    payload = ApplicationFilters(
        id="",
        name=filter_name,
        folder=TARGET_FOLDER,
        category=["business-systems"],
        risk=[2],
        technology=["client-server"],
        description="Test application filter for delete API testing"
    )
    created_obj = app_filters_api.create_application_filters(application_filters=payload)

    # Perform Delete
    app_filters_api.delete_application_filters_by_id(id=created_obj.id)

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    from scm.exceptions import ObjectNotPresentError
    # Decorator already converts NotFoundException to ObjectNotPresentError

    try:
        app_filters_api.get_application_filters_by_id(id=created_obj.id)
        pytest.fail("Application Filter should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
