import logging
import uuid
import pytest
from scm import Scm
from scm.identity_services.models.local_user_groups import LocalUserGroups
from scm.test_helpers import perform

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
def local_user_groups_api(client):
    """
    Fixture to return the Local User Groups API instance.
    """
    return client.identity_services.LocalUserGroupsApi(client.identity_services.api_client)


@pytest.fixture
def clean_local_user_group(local_user_groups_api):
    """
    Fixture to create a temporary Local User Group for testing and automatically delete it after.
    """
    object_name = f"test-user-grp-{uuid.uuid4().hex[:6]}"

    payload = LocalUserGroups(
        id="",
        name=object_name,
        folder=TARGET_FOLDER
    )

    logger.info(f"\n[SETUP] Creating Local User Group: {object_name}")
    created_obj = perform(
        local_user_groups_api.create_local_user_groups_with_http_info,
        response_type=LocalUserGroups,
        local_user_groups=payload
    )

    assert created_obj is not None, "API returned None for creation!"
    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Local User Group ID: {created_obj.id}")
    try:
        perform(
            local_user_groups_api.delete_local_user_groups_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_local_user_group(local_user_groups_api):
    """
    Test manual creation and deletion of a Local User Group with logging.
    Mirrors Test_identity_services_LocalUserGroupsAPIService_Create
    """
    object_name = f"test-user-grp-{uuid.uuid4().hex[:6]}"

    payload = LocalUserGroups(
        id="",
        name=object_name,
        folder=TARGET_FOLDER
    )

    created_obj = perform(
        local_user_groups_api.create_local_user_groups_with_http_info,
        response_type=LocalUserGroups,
        local_user_groups=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    perform(
        local_user_groups_api.delete_local_user_groups_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_local_user_group_by_id(local_user_groups_api, clean_local_user_group):
    """
    Test retrieving a Local User Group by ID with logging.
    Mirrors Test_identity_services_LocalUserGroupsAPIService_GetByID
    """
    fetched_obj = perform(
        local_user_groups_api.get_local_user_groups_by_id_with_http_info,
        id=clean_local_user_group.id
    )

    assert fetched_obj.id == clean_local_user_group.id
    assert fetched_obj.name == clean_local_user_group.name


def test_update_local_user_group(local_user_groups_api, clean_local_user_group):
    """
    Test updating a Local User Group with logging.
    Mirrors Test_identity_services_LocalUserGroupsAPIService_Update
    Note: This is a no-op update to verify the API endpoint works (same as Go test).
    """
    update_payload = LocalUserGroups(
        id="",
        name=clean_local_user_group.name,
        folder=TARGET_FOLDER
    )

    updated_obj = perform(
        local_user_groups_api.update_local_user_groups_by_id_with_http_info,
        id=clean_local_user_group.id,
        local_user_groups=update_payload
    )

    assert updated_obj.id == clean_local_user_group.id
    assert updated_obj.name == clean_local_user_group.name


def test_list_local_user_groups(local_user_groups_api, clean_local_user_group):
    """
    Test listing Local User Groups with logging.
    Mirrors Test_identity_services_LocalUserGroupsAPIService_List
    """
    response = perform(
        local_user_groups_api.list_local_user_groups_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_local_user_group.id:
            found = True
            assert item.name == clean_local_user_group.name
            break
    assert found is True, f"Created group {clean_local_user_group.id} not found in list response"


def test_fetch_local_user_groups(local_user_groups_api, clean_local_user_group):
    """
    Test fetching a single local_user_groups by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = local_user_groups_api.fetch_local_user_groups(
        name=clean_local_user_group.name,
        folder=clean_local_user_group.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found local_user_groups '{clean_local_user_group.name}'"
    assert fetched_obj.id == clean_local_user_group.id
    assert fetched_obj.name == clean_local_user_group.name
    assert fetched_obj.folder == clean_local_user_group.folder
    logger.info(f"\n[SUCCESS] fetch_local_user_groups found object: {fetched_obj.name}")

    # Test fetching non-existent local_user_groups (should return None)
    not_found = local_user_groups_api.fetch_local_user_groups(
        name="non-existent-user-group-xyz-12345",
        folder=clean_local_user_group.folder
    )
    assert not_found is None, "Should return None for non-existent local_user_groups"
    logger.info(f"\n[SUCCESS] fetch_local_user_groups correctly returned None for non-existent local_user_groups")


def test_delete_local_user_group_by_id(local_user_groups_api):
    """
    Test deletion specifically with logging.
    Mirrors Test_identity_services_LocalUserGroupsAPIService_DeleteByID
    """
    object_name = f"test-user-grp-{uuid.uuid4().hex[:6]}"

    payload = LocalUserGroups(
        id="",
        name=object_name,
        folder=TARGET_FOLDER
    )

    created_obj = perform(
        local_user_groups_api.create_local_user_groups_with_http_info,
        response_type=LocalUserGroups,
        local_user_groups=payload
    )

    # Perform Delete
    perform(
        local_user_groups_api.delete_local_user_groups_by_id_with_http_info,
        id=created_obj.id
    )

    # Verify Deletion
    from scm.identity_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        local_user_groups_api.get_local_user_groups_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Local User Group should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
