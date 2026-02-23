
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.schedules import Schedules
from scm.objects.models.schedules_schedule_type import SchedulesScheduleType
from scm.objects.models.schedules_schedule_type_recurring import SchedulesScheduleTypeRecurring
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
def schedules_api(client):
    """
    Fixture to return the Schedules API instance.
    """
    return client.objects.SchedulesApi(client.objects.api_client)


@pytest.fixture
def clean_schedule(schedules_api):
    """
    Fixture to create a temporary Schedule for testing and automatically delete it after.
    """
    # 1. SETUP: Create Schedule
    random_id = uuid.uuid4().hex[:6]
    schedule_name = f"test-sched-{random_id}"

    schedule_type = SchedulesScheduleType(
        recurring=SchedulesScheduleTypeRecurring(
            daily=["00:00-23:59"]
        )
    )

    payload = Schedules(
        id="",
        name=schedule_name,
        folder=TARGET_FOLDER,
        schedule_type=schedule_type,
    )

    logger.info(f"\n[SETUP] Creating Schedule: {schedule_name}")
    created_obj = perform(
        schedules_api.create_schedules_with_http_info,
        response_type=Schedules,
        schedules=payload,
    )
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Schedule
    logger.info(f"\n[TEARDOWN] Deleting Schedule ID: {created_obj.id}")
    try:
        perform(
            schedules_api.delete_schedules_by_id,
            id=created_obj.id,
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_schedule(schedules_api):
    """
    Test manual creation and deletion of a schedule.
    Equivalent to Go: Test_objects_SchedulesAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    schedule_name = f"test-sched-create-{random_suffix}"

    schedule_type = SchedulesScheduleType(
        recurring=SchedulesScheduleTypeRecurring(
            daily=["00:00-23:59"]
        )
    )

    payload = Schedules(
        id="",
        name=schedule_name,
        folder=TARGET_FOLDER,
        schedule_type=schedule_type,
    )

    # Create using perform helper
    created_obj = perform(
        schedules_api.create_schedules_with_http_info,
        response_type=Schedules,
        schedules=payload,
    )

    # Verify
    assert created_obj.name == schedule_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER or created_obj.folder == "Shared"

    # Cleanup
    perform(
        schedules_api.delete_schedules_by_id,
        id=created_obj.id,
    )


def test_get_schedule_by_id(schedules_api, clean_schedule):
    """
    Test retrieving a schedule by ID.
    Equivalent to Go: Test_objects_SchedulesAPIService_GetByID
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        schedules_api.get_schedules_by_id,
        response_type=Schedules,
        id=clean_schedule.id,
    )

    # Verify
    assert fetched_obj.id == clean_schedule.id
    assert fetched_obj.name == clean_schedule.name


def test_update_schedule(schedules_api, clean_schedule):
    """
    Test updating an existing schedule.
    Equivalent to Go: Test_objects_SchedulesAPIService_Update
    """
    # Prepare Update with different schedule time
    updated_schedule_type = SchedulesScheduleType(
        recurring=SchedulesScheduleTypeRecurring(
            daily=["08:00-17:00"]
        )
    )

    update_payload = Schedules(
        id=clean_schedule.id,
        name=clean_schedule.name,
        folder=TARGET_FOLDER,
        schedule_type=updated_schedule_type,
    )

    # Perform Update using helper
    updated_obj = perform(
        schedules_api.update_schedules_by_id,
        response_type=Schedules,
        id=clean_schedule.id,
        schedules=update_payload,
    )

    # Verify
    assert updated_obj.id == clean_schedule.id
    if updated_obj.schedule_type and updated_obj.schedule_type.recurring and updated_obj.schedule_type.recurring.daily:
        assert updated_obj.schedule_type.recurring.daily[0] == "08:00-17:00"


def test_list_schedules(schedules_api, clean_schedule):
    """
    Test listing schedules with folder filter.
    Equivalent to Go: Test_objects_SchedulesAPIService_List
    """
    # List with filter using helper
    response = perform(
        schedules_api.list_schedules,
        folder=TARGET_FOLDER,
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.id == clean_schedule.id:
            found = True
            assert item.name == clean_schedule.name
            break

    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_fetch_schedules(schedules_api, clean_schedule):
    """
    Test fetching a single schedule by name using the fetch convenience method.
    Equivalent to Go: Test_objects_SchedulesAPIService_FetchSchedules
    """
    # Fetch by exact name
    fetched_obj = schedules_api.fetch_schedules(
        name=clean_schedule.name,
        folder=clean_schedule.folder,
    )

    # Verify
    assert fetched_obj is not None, f"Should have found schedule '{clean_schedule.name}'"
    assert fetched_obj.id == clean_schedule.id
    assert fetched_obj.name == clean_schedule.name
    logger.info(f"\n[SUCCESS] fetch_schedules found object: {fetched_obj.name}")

    # Test fetching non-existent schedule (should return None)
    not_found = schedules_api.fetch_schedules(
        name="non-existent-schedules-xyz-12345",
        folder=clean_schedule.folder,
    )
    assert not_found is None, "Should return None for non-existent schedule"
    logger.info(f"\n[SUCCESS] fetch_schedules correctly returned None for non-existent schedule")


def test_delete_schedule_by_id(schedules_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_SchedulesAPIService_DeleteByID
    """
    from scm.exceptions import ObjectNotPresentError

    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    schedule_name = f"test-sched-delete-{random_suffix}"

    schedule_type = SchedulesScheduleType(
        recurring=SchedulesScheduleTypeRecurring(
            daily=["00:00-23:59"]
        )
    )

    payload = Schedules(
        id="",
        name=schedule_name,
        folder=TARGET_FOLDER,
        schedule_type=schedule_type,
    )

    created_obj = perform(
        schedules_api.create_schedules_with_http_info,
        response_type=Schedules,
        schedules=payload,
    )

    # Perform Delete using helper
    perform(
        schedules_api.delete_schedules_by_id,
        id=created_obj.id,
    )

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    try:
        schedules_api.get_schedules_by_id(id=created_obj.id)
        pytest.fail("Schedule should have been deleted but was found.")
    except ObjectNotPresentError:
        logger.info(f"Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
