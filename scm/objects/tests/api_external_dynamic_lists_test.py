

import logging
import uuid
import pytest
from scm import Scm

from scm.objects.models import (
    ExternalDynamicLists,
    ExternalDynamicListsType,
    
    # Domain specific models
    ExternalDynamicListsTypeDomain,
    ExternalDynamicListsTypeDomainRecurring,
    ExternalDynamicListsTypeDomainRecurringDaily,
    
    # IP specific models
    ExternalDynamicListsTypeIp,
    ExternalDynamicListsTypeIpRecurring,
    
    # URL specific models
    ExternalDynamicListsTypeUrl,
    ExternalDynamicListsTypeUrlRecurring,
    ExternalDynamicListsTypeUrlRecurringWeekly,
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "Prisma Access"

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def edl_api(client):
    return client.objects.ExternalDynamicListsApi(client.objects.api_client)

@pytest.fixture
def clean_edl(edl_api):
    random_id = uuid.uuid4().hex[:6]
    edl_name = f"test-edl-{random_id}"
    
    payload = ExternalDynamicLists(
        id="",
        name=edl_name,
        folder=TARGET_FOLDER,
        type=ExternalDynamicListsType(
            domain=ExternalDynamicListsTypeDomain(
                url="http://example.com/fixture-domains.txt",
                description="Created via Automated Pytest Fixture",
                recurring=ExternalDynamicListsTypeDomainRecurring(
                    daily=ExternalDynamicListsTypeDomainRecurringDaily(at="03")
                )
            )
        )
    )
    
    logger.info(f"\n[SETUP] Creating EDL: {edl_name}")
    created_obj = edl_api.create_external_dynamic_lists(external_dynamic_lists=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting EDL ID: {created_obj.id}")
    try:
        edl_api.delete_external_dynamic_lists_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_edl(edl_api):
    random_suffix = uuid.uuid4().hex[:6]
    edl_name = f"test-edl-create-{random_suffix}"
    
    payload = ExternalDynamicLists(
        id="",
        name=edl_name,
        folder=TARGET_FOLDER,
        type=ExternalDynamicListsType(
            domain=ExternalDynamicListsTypeDomain(
                url="http://example.com/domains.txt",
                description="Test EDL for create API",
                recurring=ExternalDynamicListsTypeDomainRecurring(
                    daily=ExternalDynamicListsTypeDomainRecurringDaily(at="03")
                )
            )
        )
    )

    created_obj = edl_api.create_external_dynamic_lists(external_dynamic_lists=payload)
    assert created_obj.name == edl_name
    assert created_obj.id is not None
    
    # Cleanup
    edl_api.delete_external_dynamic_lists_by_id(id=created_obj.id)


def test_get_edl_by_id(edl_api):
    random_suffix = uuid.uuid4().hex[:6]
    edl_name = f"test-edl-get-{random_suffix}"

    # 2. FIX: Use empty dict {} for five_minute
    payload = ExternalDynamicLists(
        id="",
        name=edl_name,
        folder=TARGET_FOLDER,
        type=ExternalDynamicListsType(
            ip=ExternalDynamicListsTypeIp(
                url="http://example.com/ips.txt",
                recurring=ExternalDynamicListsTypeIpRecurring(
                    five_minute={}  # Empty object in YAML = Dict in Python
                )
            )
        )
    )
    created_obj = edl_api.create_external_dynamic_lists(external_dynamic_lists=payload)

    try:
        fetched_obj = edl_api.get_external_dynamic_lists_by_id(id=created_obj.id)
        assert fetched_obj.id == created_obj.id
        assert fetched_obj.type.ip.url == "http://example.com/ips.txt"
    finally:
        edl_api.delete_external_dynamic_lists_by_id(id=created_obj.id)


def test_update_edl(edl_api):
    random_suffix = uuid.uuid4().hex[:6]
    edl_name = f"test-edl-update-{random_suffix}"

    # 3. FIX: Use empty dict {} for hourly
    payload = ExternalDynamicLists(
        id="",
        name=edl_name,
        folder=TARGET_FOLDER,
        type=ExternalDynamicListsType(
            url=ExternalDynamicListsTypeUrl(
                url="http://example.com/initial-urls.txt",
                recurring=ExternalDynamicListsTypeUrlRecurring(
                    hourly={}  # Empty object in YAML = Dict in Python
                )
            )
        )
    )
    created_obj = edl_api.create_external_dynamic_lists(external_dynamic_lists=payload)

    try:
        # Prepare Update (Change to Weekly)
        update_payload = created_obj
        update_payload.type.url.description = "Updated URL description"
        update_payload.type.url.url = "http://example.com/updated-urls.txt"
        
        # Explicitly replace the recurring object with the URL-specific Weekly object
        update_payload.type.url.recurring = ExternalDynamicListsTypeUrlRecurring(
            weekly=ExternalDynamicListsTypeUrlRecurringWeekly(
                day_of_week="sunday",
                at="14"
            )
        )

        updated_obj = edl_api.update_external_dynamic_lists_by_id(
            id=created_obj.id, 
            external_dynamic_lists=update_payload
        )
        
        assert updated_obj.type.url.description == "Updated URL description"
        assert updated_obj.type.url.recurring.weekly.day_of_week == "sunday"

    finally:
        edl_api.delete_external_dynamic_lists_by_id(id=created_obj.id)


def test_list_edls(edl_api, clean_edl):
    response = edl_api.list_external_dynamic_lists(folder=clean_edl.folder)
    assert response is not None
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_edl.id:
            found = True
            break
    assert found is True




def test_fetch_external_dynamic_lists(edl_api, clean_edl):
    """
    Test fetching a single external_dynamic_lists by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = edl_api.fetch_external_dynamic_lists(
        name=clean_edl.name,
        folder=clean_edl.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found external_dynamic_lists '{clean_edl.name}'"
    assert fetched_obj.id == clean_edl.id
    assert fetched_obj.name == clean_edl.name
    assert fetched_obj.folder == clean_edl.folder
    logger.info(f"\n[SUCCESS] fetch_external_dynamic_lists found object: {fetched_obj.name}")

    # Test fetching non-existent external_dynamic_lists (should return None)
    not_found = edl_api.fetch_external_dynamic_lists(
        name="non-existent-external_dynamic_lists-xyz-12345",
        folder=clean_edl.folder
    )
    assert not_found is None, "Should return None for non-existent external_dynamic_lists"
    logger.info(f"\n[SUCCESS] fetch_external_dynamic_lists correctly returned None for non-existent external_dynamic_lists")


def test_delete_edl_by_id(edl_api):
    random_suffix = uuid.uuid4().hex[:6]
    edl_name = f"test-edl-del-{random_suffix}"
    
    # 4. FIX: Use empty dict {} for hourly (Domain type)
    payload = ExternalDynamicLists(
        id="",
        name=edl_name,
        folder=TARGET_FOLDER,
        type=ExternalDynamicListsType(
            domain=ExternalDynamicListsTypeDomain(
                url="http://example.com/delete-me.txt",
                recurring=ExternalDynamicListsTypeDomainRecurring(
                    hourly={}  # Empty object in YAML = Dict in Python
                )
            )
        )
    )
    created_obj = edl_api.create_external_dynamic_lists(external_dynamic_lists=payload)

    edl_api.delete_external_dynamic_lists_by_id(id=created_obj.id)

    from scm.objects.exceptions import NotFoundException
    from scm.error_parser import parse_scm_error
    from scm.exceptions import ObjectNotPresentError

    try:
        edl_api.get_external_dynamic_lists_by_id(id=created_obj.id)
        pytest.fail("EDL should have been deleted")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
