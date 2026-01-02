
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.applications import Applications
from scm.objects.models.application_groups import ApplicationGroups

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Shared"
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def create_test_application(api, name):
    """Helper to create a single application object."""
    payload = Applications(
        id="",
        name=name,
        folder=TARGET_FOLDER,
        category="business-systems",
        subcategory="database",
        technology="client-server",
        risk=1,
        description="Temp app for ApplicationGroup test"
    )
    return api.create_applications(applications=payload)

def delete_test_application(api, app_id):
    """Helper to delete a single application object."""
    try:
        api.delete_applications_by_id(id=app_id)
    except Exception as e:
        # 404 is acceptable during cleanup
        if "404" not in str(e):
            logger.warning(f"Failed to cleanup application {app_id}: {e}")

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
def applications_api(client):
    return client.objects.ApplicationsApi(client.objects.api_client)

@pytest.fixture(scope="module")
def app_groups_api(client):
    return client.objects.ApplicationGroupsApi(client.objects.api_client)

@pytest.fixture
def clean_application_group(applications_api, app_groups_api):
    """
    Fixture to create a temporary Application Group AND its dependent Application.
    Strictly follows Go logic: Delete Group first, then Applications.
    """
    # 1. SETUP: Create Dependency (Application)
    random_id = uuid.uuid4().hex[:6]
    app1 = create_test_application(applications_api, f"grp-dep-{random_id}")
    group_name = f"test-group-{random_id}"

    created_group = None

    try:
        # 2. SETUP: Create Application Group
        payload = ApplicationGroups(
            id="",
            name=group_name,
            folder=TARGET_FOLDER,
            members=[app1.name],
        )
        
        logger.info(f"\n[SETUP] Creating Application Group: {group_name}")
        created_group = app_groups_api.create_application_groups(application_groups=payload)
        
        yield created_group

    finally:
        # 3. TEARDOWN: Delete Group FIRST
        # If we don't delete the group, we can't delete the app (Reference Error 409)
        if created_group and created_group.id:
            logger.info(f"\n[TEARDOWN] Deleting Application Group ID: {created_group.id}")
            try:
                app_groups_api.delete_application_groups_by_id(id=created_group.id)
            except Exception as e:
                logger.warning(f"Group teardown failed: {e}")

        # 4. TEARDOWN: Delete Dependency SECOND
        if app1 and app1.id:
            logger.info(f"[TEARDOWN] Deleting Application ID: {app1.id}")
            delete_test_application(applications_api, app1.id)


# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def test_create_application_group(applications_api, app_groups_api):
    """
    Test manual creation and deletion of an application group.
    """
    random_suffix = uuid.uuid4().hex[:6]
    
    # 1. Create dependencies
    app1 = create_test_application(applications_api, f"test-app-1-{random_suffix}")
    app2 = create_test_application(applications_api, f"test-app-2-{random_suffix}")
    group_name = f"test-group-create-{random_suffix}"
    
    created_group = None

    try:
        # 2. Create Group
        payload = ApplicationGroups(
            id="",
            name=group_name,
            folder=TARGET_FOLDER,
            members=[app1.name, app2.name],
        )
        
        created_group = app_groups_api.create_application_groups(application_groups=payload)
        
        # Verify
        assert created_group is not None
        assert created_group.name == group_name
        assert created_group.id is not None
        assert set(created_group.members) == set([app1.name, app2.name])

    finally:
        # 3. CLEANUP: Delete Group FIRST
        if created_group and created_group.id:
            try:
                app_groups_api.delete_application_groups_by_id(id=created_group.id)
            except Exception as e:
                logger.warning(f"Delete group failed: {e}")

        # 4. CLEANUP: Delete Applications SECOND
        if app1: delete_test_application(applications_api, app1.id)
        if app2: delete_test_application(applications_api, app2.id)


def test_get_application_group_by_id(app_groups_api, clean_application_group):
    """
    Test retrieving an application group by ID.
    """
    # If fixture failed (SDK returned None), skip
    if not clean_application_group:
        pytest.fail("Fixture failed to create Application Group (SDK issue)")

    fetched_obj = app_groups_api.get_application_groups_by_id(id=clean_application_group.id)
    
    assert fetched_obj.id == clean_application_group.id
    assert fetched_obj.name == clean_application_group.name
    assert set(fetched_obj.members) == set(clean_application_group.members)


def test_update_application_group(applications_api, app_groups_api, clean_application_group):
    """
    Test updating an application group.
    """
    if not clean_application_group:
        pytest.fail("Fixture failed to create Application Group (SDK issue)")

    # 1. Create NEW application
    random_suffix = uuid.uuid4().hex[:6]
    new_app = create_test_application(applications_api, f"upd-app-{random_suffix}")

    try:
        # 2. Update Group (Add new app to members)
        current_members = clean_application_group.members
        new_members = current_members + [new_app.name]

        update_payload = clean_application_group
        update_payload.members = new_members
        
        updated_obj = app_groups_api.update_application_groups_by_id(
            id=clean_application_group.id, 
            application_groups=update_payload
        )
        
        assert set(updated_obj.members) == set(new_members)
    
    finally:
        # 3. Revert Update (Remove new app from group)
        # We must remove the reference before we can delete the new app.
        try:
            revert_members = [m for m in clean_application_group.members if m != new_app.name]
            clean_application_group.members = revert_members
            app_groups_api.update_application_groups_by_id(
                id=clean_application_group.id,
                application_groups=clean_application_group
            )
        except Exception as e:
            logger.warning(f"Failed to revert update: {e}")

        # 4. Delete New App
        delete_test_application(applications_api, new_app.id)


def test_list_application_groups(app_groups_api, clean_application_group):
    """
    Test listing application groups.
    """
    if not clean_application_group:
        pytest.fail("Fixture failed to create Application Group (SDK issue)")

    response = app_groups_api.list_application_groups(folder=TARGET_FOLDER)
    
    found = False
    for item in response.data:
        if item.id == clean_application_group.id:
            found = True
            break
    assert found is True


def test_delete_application_group_by_id(applications_api, app_groups_api):
    """
    Test deletion specifically.
    """
    random_suffix = uuid.uuid4().hex[:6]

    # 1. Create Dependencies
    app1 = create_test_application(applications_api, f"del-app-1-{random_suffix}")
    group_name = f"test-group-del-{random_suffix}"
    
    created_group = None

    try:
        # 2. Create Group
        payload = ApplicationGroups(
            id="",
            name=group_name,
            folder=TARGET_FOLDER,
            members=[app1.name],
        )
        created_group = app_groups_api.create_application_groups(application_groups=payload)
        assert created_group is not None

        # 3. Perform Delete
        app_groups_api.delete_application_groups_by_id(id=created_group.id)

        # 4. Verify 404
        try:
            app_groups_api.get_application_groups_by_id(id=created_group.id)
            pytest.fail("Group should be deleted")
        except Exception as e:
            assert "404" in str(e) or "Not Found" in str(e)

    finally:
        # 5. Cleanup (If delete failed, try again)
        if created_group and created_group.id:
            try:
                # Try getting it to see if it exists
                app_groups_api.get_application_groups_by_id(id=created_group.id)
                # If we are here, it still exists, so delete it
                app_groups_api.delete_application_groups_by_id(id=created_group.id)
            except Exception:
                pass # It's already gone

        # 6. Delete App (Safe now that Group is gone)
        if app1: delete_test_application(applications_api, app1.id)
