
import logging
import uuid
import pytest
from scm import Scm
from scm.security_services.models.data_objects import DataObjects
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "ngfw-shared"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def data_objects_api(client):
    return client.security_services.DataObjectsApi(client.security_services.api_client)


@pytest.fixture
def clean_data_object(data_objects_api):
    """
    Fixture to create a temporary data object for testing and automatically delete it after.
    """
    object_name = f"test-do-{uuid.uuid4().hex[:6]}"

    payload = DataObjects(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        pattern_type={
            "predefined": {
                "pattern": [
                    {
                        "name": "ABA-Routing-Number",
                        "file_type": ["text/html"]
                    }
                ]
            }
        }
    )

    logger.info(f"\n[SETUP] Creating Data Object: {object_name}")
    created_obj = perform(
        data_objects_api.create_data_objects_with_http_info,
        response_type=DataObjects,
        data_objects=payload
    )

    assert created_obj.id is not None

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Data Object ID: {created_obj.id}")
    try:
        perform(
            data_objects_api.delete_data_objects_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_data_object(data_objects_api):
    """
    Test manual creation and deletion of a data object.
    """
    object_name = f"test-do-create-{uuid.uuid4().hex[:6]}"
    payload = DataObjects(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test data object for create API testing",
        pattern_type={
            "predefined": {
                "pattern": [
                    {
                        "name": "ABA-Routing-Number",
                        "file_type": ["text/html"]
                    }
                ]
            }
        }
    )

    created_obj = perform(
        data_objects_api.create_data_objects_with_http_info,
        response_type=DataObjects,
        data_objects=payload
    )

    assert created_obj.name == object_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER

    perform(
        data_objects_api.delete_data_objects_by_id,
        id=created_obj.id
    )


def test_get_data_object_by_id(data_objects_api, clean_data_object):
    """
    Test retrieving a data object by ID.
    """
    fetched_obj = perform(
        data_objects_api.get_data_objects_by_id,
        response_type=DataObjects,
        id=clean_data_object.id
    )

    assert fetched_obj.id == clean_data_object.id
    assert fetched_obj.name == clean_data_object.name
    assert fetched_obj.folder == clean_data_object.folder


def test_update_data_object(data_objects_api, clean_data_object):
    """
    Test updating a data object.
    """
    update_payload = clean_data_object
    update_payload.description = "Updated Description via Pytest"

    updated_obj = perform(
        data_objects_api.update_data_objects_by_id,
        response_type=DataObjects,
        id=clean_data_object.id,
        data_objects=update_payload
    )

    assert updated_obj.description == "Updated Description via Pytest"
    assert updated_obj.id == clean_data_object.id


def test_list_data_objects(data_objects_api, clean_data_object):
    """
    Test listing data objects with folder filter.
    """
    response = perform(
        data_objects_api.list_data_objects,
        folder=clean_data_object.folder
    )

    assert response is not None
    assert len(response.data) > 0
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_fetch_data_objects(data_objects_api, clean_data_object):
    """
    Test fetching a single data object by name using the fetch convenience method.
    """
    fetched_obj = data_objects_api.fetch_data_objects(
        name=clean_data_object.name,
        folder=clean_data_object.folder
    )

    assert fetched_obj is not None, f"Should have found data object '{clean_data_object.name}'"
    assert fetched_obj.id == clean_data_object.id
    assert fetched_obj.name == clean_data_object.name
    assert fetched_obj.folder == clean_data_object.folder
    logger.info(f"\n[SUCCESS] fetch_data_objects found object: {fetched_obj.name}")

    not_found = data_objects_api.fetch_data_objects(
        name="non-existent-data-object-xyz-12345",
        folder=clean_data_object.folder
    )
    assert not_found is None, "Should return None for non-existent data object"
    logger.info(f"\n[SUCCESS] fetch_data_objects correctly returned None for non-existent object")


def test_delete_data_object_by_id(data_objects_api):
    """
    Test deletion specifically.
    """
    from scm.exceptions import ObjectNotPresentError

    object_name = f"test-do-del-{uuid.uuid4().hex[:6]}"
    payload = DataObjects(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        description="Test data object for delete API testing",
        pattern_type={
            "predefined": {
                "pattern": [
                    {
                        "name": "ABA-Routing-Number",
                        "file_type": ["text/html"]
                    }
                ]
            }
        }
    )

    created_obj = perform(
        data_objects_api.create_data_objects_with_http_info,
        response_type=DataObjects,
        data_objects=payload
    )

    perform(
        data_objects_api.delete_data_objects_by_id,
        id=created_obj.id
    )

    try:
        data_objects_api.get_data_objects_by_id(id=created_obj.id)
        pytest.fail("Data Object should have been deleted but was found.")
    except ObjectNotPresentError as e:
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
