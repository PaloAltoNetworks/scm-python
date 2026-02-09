import logging
import uuid
import json
import pytest
from scm import Scm
from scm.security_services.models.url_categories import UrlCategories
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
    """
    Fixture to initialize the SCM client once for the module.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def url_categories_api(client):
    """
    Fixture to return the URL Categories API instance.
    """
    return client.security_services.URLCategoriesApi(client.security_services.api_client)

@pytest.fixture
def clean_url_category(url_categories_api):
    """
    Fixture to create a temporary URL Category for testing and automatically delete it after.
    """
    category_name = f"test-url-cat-{uuid.uuid4().hex[:6]}"

    payload = UrlCategories(
        id="",
        name=category_name,
        folder=TARGET_FOLDER,
        list=["example.com", "test.com"],
        type="URL List"
    )

    logger.info(f"\n[SETUP] Creating URL Category: {category_name}")
    created_obj = perform(
        url_categories_api.create_url_categories_with_http_info,
        response_type=UrlCategories,
        url_categories=payload
    )

    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting URL Category ID: {created_obj.id}")
    try:
        perform(
            url_categories_api.delete_url_categories_by_id_with_http_info,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_url_category(url_categories_api):
    """
    Test manual creation and deletion of a URL Category with logging.
    """
    category_name = f"test-url-cat-create-{uuid.uuid4().hex[:6]}"

    payload = UrlCategories(
        id="",
        name=category_name,
        folder=TARGET_FOLDER,
        list=["example.com", "test.com"],
        type="URL List"
    )

    # Create with logging
    created_obj = perform(
        url_categories_api.create_url_categories_with_http_info,
        response_type=UrlCategories,
        url_categories=payload
    )

    assert created_obj is not None
    assert created_obj.id is not None
    assert created_obj.name == category_name
    assert created_obj.folder == TARGET_FOLDER
    assert created_obj.type == "URL List"
    assert "example.com" in created_obj.list
    assert "test.com" in created_obj.list

    # Cleanup with logging
    perform(
        url_categories_api.delete_url_categories_by_id_with_http_info,
        id=created_obj.id
    )


def test_get_url_category_by_id(url_categories_api, clean_url_category):
    """
    Test retrieving a URL Category by ID with logging.
    """
    fetched_obj = perform(
        url_categories_api.get_url_categories_by_id_with_http_info,
        id=clean_url_category.id
    )

    assert fetched_obj.id == clean_url_category.id
    assert fetched_obj.name == clean_url_category.name
    assert fetched_obj.type == clean_url_category.type


def test_update_url_category(url_categories_api, clean_url_category):
    """
    Test updating a URL Category with logging.
    """
    update_payload = clean_url_category
    update_payload.description = "Updated description via Pytest"
    update_payload.list = ["example.com", "test.com", "updated.com"]

    updated_obj = perform(
        url_categories_api.update_url_categories_by_id_with_http_info,
        id=clean_url_category.id,
        url_categories=update_payload
    )

    assert updated_obj.id == clean_url_category.id
    assert updated_obj.description == "Updated description via Pytest"
    assert "updated.com" in updated_obj.list


def test_list_url_categories(url_categories_api, clean_url_category):
    """
    Test listing URL Categories with logging.
    """
    response = perform(
        url_categories_api.list_url_categories_with_http_info,
        folder=TARGET_FOLDER
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify the fixture object is in the list
    found = False
    for item in response.data:
        if item.id == clean_url_category.id:
            found = True
            break
    assert found is True, f"Created category {clean_url_category.id} not found in list response"




def test_fetch_url_categories(url_categories_api, clean_url_category):
    """
    Test fetching a single url_categories by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = url_categories_api.fetch_url_categories(
        name=clean_url_category.name,
        folder=clean_url_category.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found url_categories '{clean_url_category.name}'"
    assert fetched_obj.id == clean_url_category.id
    assert fetched_obj.name == clean_url_category.name
    assert fetched_obj.folder == clean_url_category.folder
    logger.info(f"\n[SUCCESS] fetch_url_categories found object: {fetched_obj.name}")

    # Test fetching non-existent url_categories (should return None)
    not_found = url_categories_api.fetch_url_categories(
        name="non-existent-url_categories-xyz-12345",
        folder=clean_url_category.folder
    )
    assert not_found is None, "Should return None for non-existent url_categories"
    logger.info(f"\n[SUCCESS] fetch_url_categories correctly returned None for non-existent url_categories")


def test_delete_url_category_by_id(url_categories_api):
    """
    Test deletion specifically with logging.
    """
    # Setup
    category_name = f"test-url-cat-del-{uuid.uuid4().hex[:6]}"

    payload = UrlCategories(
        id="",
        name=category_name,
        folder=TARGET_FOLDER,
        list=["delete-test.com"],
        type="URL List"
    )

    created_obj = perform(
        url_categories_api.create_url_categories_with_http_info,
        response_type=UrlCategories,
        url_categories=payload
    )

    # Perform Delete with logging
    perform(
        url_categories_api.delete_url_categories_by_id_with_http_info,
        id=created_obj.id
    )

    # Verify Deletion
    from scm.security_services.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        url_categories_api.get_url_categories_by_id_with_http_info(id=created_obj.id)
        pytest.fail("Category should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
