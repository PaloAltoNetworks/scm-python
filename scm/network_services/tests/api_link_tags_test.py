import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.link_tags import LinkTags
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "All"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def link_tags_api(client):
    return client.network_services.LinkTagsApi(client.network_services.api_client)


@pytest.fixture
def clean_link_tag(link_tags_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-linktag-{random_id}"

    payload = LinkTags(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        comments="Test link tag",
    )

    logger.info(f"\n[SETUP] Creating Link Tag: {object_name}")
    created_obj = perform(
        link_tags_api.create_link_tags_with_http_info,
        response_type=LinkTags,
        link_tags=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Link Tag ID: {created_obj.id}")
    try:
        link_tags_api.delete_link_tags_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_link_tag(link_tags_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-linktag-create-{random_id}"

    payload = LinkTags(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        comments="Test link tag for create",
    )

    created_obj = perform(
        link_tags_api.create_link_tags_with_http_info,
        response_type=LinkTags,
        link_tags=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    link_tags_api.delete_link_tags_by_id(id=created_obj.id)


def test_get_link_tag_by_id(link_tags_api, clean_link_tag):
    fetched_obj = link_tags_api.get_link_tags_by_id(id=clean_link_tag.id)
    assert fetched_obj.id == clean_link_tag.id
    assert fetched_obj.name == clean_link_tag.name


def test_update_link_tag(link_tags_api, clean_link_tag):
    update_payload = clean_link_tag
    update_payload.comments = "Updated link tag comment"

    updated_obj = link_tags_api.update_link_tags_by_id(
        id=clean_link_tag.id,
        link_tags=update_payload,
    )

    assert updated_obj.id == clean_link_tag.id
    assert updated_obj.comments == "Updated link tag comment"


def test_list_link_tags(link_tags_api, clean_link_tag):
    response = link_tags_api.list_link_tags(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_link_tag.id:
            found = True
            break
    assert found is True


def test_fetch_link_tags(link_tags_api, clean_link_tag):
    fetched_obj = link_tags_api.fetch_link_tags(
        name=clean_link_tag.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_link_tag.id
    assert fetched_obj.name == clean_link_tag.name
    logger.info(f"\n[SUCCESS] fetch_link_tags found object: {fetched_obj.name}")

    not_found = link_tags_api.fetch_link_tags(
        name="non-existent-link-tag-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_link_tags correctly returned None for non-existent object")


def test_delete_link_tag_by_id(link_tags_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-linktag-del-{random_id}"

    payload = LinkTags(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
    )

    created_obj = perform(
        link_tags_api.create_link_tags_with_http_info,
        response_type=LinkTags,
        link_tags=payload,
    )

    link_tags_api.delete_link_tags_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        link_tags_api.get_link_tags_by_id(id=created_obj.id)
        pytest.fail("Link Tag should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
