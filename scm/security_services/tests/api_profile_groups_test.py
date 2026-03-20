import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.profile_groups import ProfileGroups
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
def profile_groups_api(client):
    return client.security_services.ProfileGroupsApi(client.security_services.api_client)


@pytest.fixture
def clean_profile_group(profile_groups_api):
    """
    Setup/Teardown for a simple Profile Group.
    """
    group_name = f"scm-profgrp-{uuid.uuid4().hex[:6]}"

    payload = ProfileGroups(
        id="",
        folder=TARGET_FOLDER,
        name=group_name
    )

    logger.info(f"\n[SETUP] Creating Profile Group: {group_name}")
    created_group = perform(
        profile_groups_api.create_profile_groups_with_http_info,
        response_type=ProfileGroups,
        profile_groups=payload
    )

    yield created_group

    logger.info(f"\n[TEARDOWN] Deleting Profile Group: {created_group.id}")
    try:
        perform(
            profile_groups_api.delete_profile_groups_by_id_with_http_info,
            id=created_group.id
        )
    except Exception as e:
        logger.error(f"Failed to cleanup Profile Group: {e}")


def test_create_profile_group(profile_groups_api):
    """Test creation of a Profile Group."""
    group_name = f"scm-profgrp-create-{uuid.uuid4().hex[:6]}"

    payload = ProfileGroups(
        id="",
        folder=TARGET_FOLDER,
        name=group_name
    )

    created_obj = perform(
        profile_groups_api.create_profile_groups_with_http_info,
        response_type=ProfileGroups,
        profile_groups=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == group_name

    perform(
        profile_groups_api.delete_profile_groups_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_profile_group_by_id(profile_groups_api, clean_profile_group):
    """Test retrieving a Profile Group by ID."""
    fetched_obj = perform(
        profile_groups_api.get_profile_groups_by_id_with_http_info,
        id=clean_profile_group.id
    )

    assert fetched_obj.id == clean_profile_group.id
    assert fetched_obj.name == clean_profile_group.name


def test_update_profile_group(profile_groups_api, clean_profile_group):
    """Test updating a Profile Group."""
    update_payload = clean_profile_group
    update_payload.spyware = ["best-practice"]

    updated_obj = perform(
        profile_groups_api.update_profile_groups_by_id_with_http_info,
        id=clean_profile_group.id,
        profile_groups=update_payload
    )

    assert updated_obj.id == clean_profile_group.id
    assert updated_obj.name == clean_profile_group.name
    assert updated_obj.spyware is not None
    assert "best-practice" in updated_obj.spyware


def test_list_profile_groups(profile_groups_api, clean_profile_group):
    """Test listing Profile Groups."""
    response = perform(
        profile_groups_api.list_profile_groups_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.name == clean_profile_group.name:
            found = True
            break
    assert found is True, f"Created profile group {clean_profile_group.name} not found in list response"


def test_fetch_profile_groups(profile_groups_api, clean_profile_group):
    """
    Test fetching a single Profile Group by name using the fetch convenience method.
    """
    # Fetch by exact name
    fetched_obj = profile_groups_api.fetch_profile_groups(
        name=clean_profile_group.name,
        folder=clean_profile_group.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found Profile Group '{clean_profile_group.name}'"
    assert fetched_obj.id == clean_profile_group.id
    assert fetched_obj.name == clean_profile_group.name
    assert fetched_obj.folder == clean_profile_group.folder
    logger.info(f"\n[SUCCESS] fetch_profile_groups found object: {fetched_obj.name}")

    # Test fetching non-existent profile group (should return None)
    not_found = profile_groups_api.fetch_profile_groups(
        name="non-existent-profilegroup-xyz-12345",
        folder=clean_profile_group.folder
    )
    assert not_found is None, "Should return None for non-existent Profile Group"
    logger.info(f"\n[SUCCESS] fetch_profile_groups correctly returned None for non-existent profile group")


def test_delete_profile_group_by_id(profile_groups_api):
    """Test deleting a Profile Group."""
    group_name = f"scm-profgrp-delete-{uuid.uuid4().hex[:6]}"

    payload = ProfileGroups(
        id="",
        folder=TARGET_FOLDER,
        name=group_name
    )

    created_obj = perform(
        profile_groups_api.create_profile_groups_with_http_info,
        response_type=ProfileGroups,
        profile_groups=payload
    )

    perform(
        profile_groups_api.delete_profile_groups_by_id_with_http_info,
        id=created_obj.id
    )

    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        profile_groups_api.get_profile_groups_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Profile group should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
