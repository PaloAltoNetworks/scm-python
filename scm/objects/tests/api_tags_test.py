
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.tags import Tags

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
def tags_api(client):
    """
    Fixture to return the Tags API instance.
    """
    return client.objects.TagsApi(client.objects.api_client)

@pytest.fixture
def clean_tag(tags_api):
    """
    Fixture to create a temporary Tag for testing and automatically delete it after.
    """
    # 1. SETUP: Create Tag
    random_id = uuid.uuid4().hex[:6]
    tag_name = f"test-tag-{random_id}"
    
    payload = Tags(
        id="",
        name=tag_name,
        folder=TARGET_FOLDER,
        color="Blue",
        comments="Created via Automated Pytest Fixture"
    )
    
    logger.info(f"\n[SETUP] Creating Tag: {tag_name}")
    created_obj = tags_api.create_tags(tags=payload)
    assert created_obj.id is not None
    
    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Tag
    logger.info(f"\n[TEARDOWN] Deleting Tag ID: {created_obj.id}")
    try:
        tags_api.delete_tags_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_tag(tags_api):
    """
    Test manual creation and deletion of a tag object.
    Equivalent to Go: Test_objects_TagsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    tag_name = f"test-tag-create-{random_suffix}"
    
    payload = Tags(
        id="",
        name=tag_name,
        folder=TARGET_FOLDER,
        color="Red",
        comments="Test tag for create API testing"
    )

    # Create
    created_obj = tags_api.create_tags(tags=payload)
    
    # Verify
    assert created_obj.name == tag_name
    assert created_obj.id is not None
    assert created_obj.color == "Red"
    assert created_obj.comments == "Test tag for create API testing"
    assert created_obj.folder == TARGET_FOLDER or created_obj.folder == "Shared"

    # Cleanup
    tags_api.delete_tags_by_id(id=created_obj.id)


def test_get_tag_by_id(tags_api, clean_tag):
    """
    Test retrieving a tag by ID.
    Equivalent to Go: Test_objects_TagsAPIService_GetByID
    """
    # Retrieve
    fetched_obj = tags_api.get_tags_by_id(id=clean_tag.id)
    
    # Verify
    assert fetched_obj.id == clean_tag.id
    assert fetched_obj.name == clean_tag.name
    assert fetched_obj.color == clean_tag.color
    # assert fetched_obj.folder == clean_tag.folder


def test_update_tag(tags_api, clean_tag):
    """
    Test updating an existing tag.
    Equivalent to Go: Test_objects_TagsAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_tag
    update_payload.color = "Yellow"
    update_payload.comments = "Updated test tag description"

    # Perform Update
    updated_obj = tags_api.update_tags_by_id(
        id=clean_tag.id, 
        tags=update_payload
    )
    
    # Verify
    assert updated_obj.id == clean_tag.id
    assert updated_obj.name == clean_tag.name
    assert updated_obj.color == "Yellow"
    assert updated_obj.comments == "Updated test tag description"


def test_list_tags(tags_api, clean_tag):
    """
    Test listing tags with folder filter.
    Equivalent to Go: Test_objects_TagsAPIService_List
    """
    # List with filter
    response = tags_api.list_tags(folder=TARGET_FOLDER, limit=10000)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.name == clean_tag.name:
            found = True
            break
            
    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")




def test_fetch_tags(tags_api, clean_tag):
    """
    Test fetching a single tags by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = tags_api.fetch_tags(
        name=clean_tag.name,
        folder=clean_tag.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found tags '{clean_tag.name}'"
    assert fetched_obj.id == clean_tag.id
    assert fetched_obj.name == clean_tag.name
    assert fetched_obj.folder == clean_tag.folder
    logger.info(f"\n[SUCCESS] fetch_tags found object: {fetched_obj.name}")

    # Test fetching non-existent tags (should return None)
    not_found = tags_api.fetch_tags(
        name="non-existent-tags-xyz-12345",
        folder=clean_tag.folder
    )
    assert not_found is None, "Should return None for non-existent tags"
    logger.info(f"\n[SUCCESS] fetch_tags correctly returned None for non-existent tags")


def test_delete_tag_by_id(tags_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_TagsAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    tag_name = f"test-tag-delete-{random_suffix}"
    
    payload = Tags(
        id="",
        name=tag_name,
        folder=TARGET_FOLDER,
        color="Orange",
        comments="Test tag for delete API testing"
    )
    created_obj = tags_api.create_tags(tags=payload)

    # Perform Delete
    tags_api.delete_tags_by_id(id=created_obj.id)

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    from scm.exceptions import ObjectNotPresentError
    # Decorator already converts NotFoundException to ObjectNotPresentError

    try:
        tags_api.get_tags_by_id(id=created_obj.id)
        pytest.fail("Tag should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
