
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.tags import Tags
from scm.objects.models.dynamic_user_groups import DynamicUserGroups

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Shared"
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (To manage dependent Tag objects)
# -----------------------------------------------------------------------------
def create_test_tag(api, name, color):
    """Helper to create a single tag object for DUG filtering."""
    payload = Tags(
        id="",
        name=name,
        color=color,
        folder=TARGET_FOLDER,
        description="Temp tag for DUG test"
    )
    return api.create_tags(tags=payload)

def delete_test_tag(api, tag_id):
    """Helper to delete a single tag object."""
    try:
        api.delete_tags_by_id(id=tag_id)
    except Exception as e:
        logger.warning(f"Failed to cleanup tag {tag_id}: {e}")

# -----------------------------------------------------------------------------
# FIXTURES
# -----------------------------------------------------------------------------

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def tags_api(client):
    return client.objects.TagsApi(client.objects.api_client)

@pytest.fixture(scope="module")
def dug_api(client):
    return client.objects.DynamicUserGroupsApi(client.objects.api_client)

@pytest.fixture
def clean_dug(tags_api, dug_api):
    """
    Fixture to create a temporary Dynamic User Group AND its dependent Tag.
    Automatically cleans up the Group first, then the Tag.
    """
    # 1. SETUP: Create Dependency (Tag)
    random_id = uuid.uuid4().hex[:6]
    tag_name = f"dug-dep-{random_id}"
    tag_obj = create_test_tag(tags_api, tag_name, "Blue")

    # 2. SETUP: Create Dynamic User Group
    dug_name = f"test-dug-{random_id}"
    payload = DynamicUserGroups(
        id="",
        name=dug_name,
        folder=TARGET_FOLDER,
        filter=f"'Microsoft 365 Access' and '{tag_name}'",
        description="Created via Automated Pytest Fixture"
    )
    
    logger.info(f"\n[SETUP] Creating DUG: {dug_name}")
    created_dug = dug_api.create_dynamic_user_groups(dynamic_user_groups=payload)
    
    # Pass control to test
    yield created_dug

    # 3. TEARDOWN: Delete DUG first
    logger.info(f"\n[TEARDOWN] Deleting DUG ID: {created_dug.id}")
    try:
        dug_api.delete_dynamic_user_groups_by_id(id=created_dug.id)
    except Exception as e:
        logger.info(f"DUG teardown failed (might be deleted in test): {e}")

    # 4. TEARDOWN: Delete Dependency
    delete_test_tag(tags_api, tag_obj.id)


# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def test_create_dynamic_user_group(tags_api, dug_api):
    """
    Test manual creation and deletion of a dynamic user group.
    Equivalent to Go: Test_objects_DynamicUserGroupsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    
    # 1. Create dependency
    tag_name = f"tag-for-dug-{random_suffix}"
    tag_obj = create_test_tag(tags_api, tag_name, "Red")

    # 2. Create DUG
    dug_name = f"test-dug-create-{random_suffix}"
    filter_expr = f"'Microsoft 365 Access' and '{tag_name}'"
    
    payload = DynamicUserGroups(
        id="",
        name=dug_name,
        folder=TARGET_FOLDER,
        filter=filter_expr,
        description="Test DUG for create API"
    )
    
    try:
        created_dug = dug_api.create_dynamic_user_groups(dynamic_user_groups=payload)
        
        # Verify
        assert created_dug.name == dug_name
        assert created_dug.id is not None
        assert created_dug.filter == filter_expr
        assert created_dug.folder == TARGET_FOLDER

        # Cleanup DUG
        dug_api.delete_dynamic_user_groups_by_id(id=created_dug.id)
    
    finally:
        # Cleanup Tag (always run even if assertions fail)
        delete_test_tag(tags_api, tag_obj.id)


def test_get_dynamic_user_group_by_id(dug_api, clean_dug):
    """
    Test retrieving a dynamic user group by ID.
    Equivalent to Go: Test_objects_DynamicUserGroupsAPIService_GetByID
    """
    # Retrieve
    fetched_obj = dug_api.get_dynamic_user_groups_by_id(id=clean_dug.id)
    
    # Verify
    assert fetched_obj.id == clean_dug.id
    assert fetched_obj.name == clean_dug.name
    assert fetched_obj.folder == clean_dug.folder
    assert fetched_obj.filter == clean_dug.filter


def test_update_dynamic_user_group(tags_api, dug_api, clean_dug):
    """
    Test updating a dynamic user group.
    Equivalent to Go: Test_objects_DynamicUserGroupsAPIService_Update
    """
    # 1. Create NEW tags to update the filter with
    random_suffix = uuid.uuid4().hex[:6]
    tag1_name = f"upd-tag-1-{random_suffix}"
    tag2_name = f"upd-tag-2-{random_suffix}"
    
    tag1 = create_test_tag(tags_api, tag1_name, "Green")
    tag2 = create_test_tag(tags_api, tag2_name, "Yellow")

    try:
        # 2. Prepare Update Payload
        # We change the filter to reference the new tags
        new_filter = f"'{tag1_name}' or '{tag2_name}'"
        
        update_payload = clean_dug
        update_payload.filter = new_filter
        
        # 3. Perform Update
        updated_obj = dug_api.update_dynamic_user_groups_by_id(
            id=clean_dug.id, 
            dynamic_user_groups=update_payload
        )
        
        # 4. Verify
        assert updated_obj.filter == new_filter
        assert updated_obj.id == clean_dug.id
    
    finally:
        # 5. Cleanup the NEW tags
        delete_test_tag(tags_api, tag1.id)
        delete_test_tag(tags_api, tag2.id)


def test_list_dynamic_user_groups(dug_api, clean_dug):
    """
    Test listing dynamic user groups with folder filter.
    Equivalent to Go: Test_objects_DynamicUserGroupsAPIService_List
    """
    # List with filter
    response = dug_api.list_dynamic_user_groups(folder=TARGET_FOLDER)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our specific object is in the list
    found = False
    for item in response.data:
        if item.id == clean_dug.id:
            found = True
            break
    assert found is True




def test_fetch_dynamic_user_groups(dug_api, clean_dug):
    """
    Test fetching a single dynamic_user_groups by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = dug_api.fetch_dynamic_user_groups(
        name=clean_dug.name,
        folder=clean_dug.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found dynamic_user_groups '{clean_dug.name}'"
    assert fetched_obj.id == clean_dug.id
    assert fetched_obj.name == clean_dug.name
    assert fetched_obj.folder == clean_dug.folder
    logger.info(f"\n[SUCCESS] fetch_dynamic_user_groups found object: {fetched_obj.name}")

    # Test fetching non-existent dynamic_user_groups (should return None)
    not_found = dug_api.fetch_dynamic_user_groups(
        name="non-existent-dynamic_user_groups-xyz-12345",
        folder=clean_dug.folder
    )
    assert not_found is None, "Should return None for non-existent dynamic_user_groups"
    logger.info(f"\n[SUCCESS] fetch_dynamic_user_groups correctly returned None for non-existent dynamic_user_groups")


def test_delete_dynamic_user_group_by_id(tags_api, dug_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_DynamicUserGroupsAPIService_DeleteByID
    """
    random_suffix = uuid.uuid4().hex[:6]

    # 1. Create Dependency
    tag_name = f"del-tag-{random_suffix}"
    tag_obj = create_test_tag(tags_api, tag_name, "Orange")
    
    # 2. Create DUG
    payload = DynamicUserGroups(
        id="",
        name=f"test-dug-del-{random_suffix}",
        folder=TARGET_FOLDER,
        filter=f"'{tag_name}'",
        description="Test DUG for delete API testing"
    )
    created_dug = dug_api.create_dynamic_user_groups(dynamic_user_groups=payload)

    # 3. Perform Delete
    dug_api.delete_dynamic_user_groups_by_id(id=created_dug.id)

    # 4. Verify Deletion (Expect ObjectNotPresentError on Get)
    from scm.exceptions import ObjectNotPresentError
    # Decorator already converts NotFoundException to ObjectNotPresentError

    try:
        dug_api.get_dynamic_user_groups_by_id(id=created_dug.id)
        pytest.fail("DUG should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_dug.id}")

    # 5. Cleanup Dependency
    delete_test_tag(tags_api, tag_obj.id)
