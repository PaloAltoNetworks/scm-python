
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.addresses import Addresses
from scm.objects.models.address_groups import AddressGroups

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Prisma Access"
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (To manage dependent Address objects)
# -----------------------------------------------------------------------------
def create_test_address(api, name, ip_netmask):
    """Helper to create a single address object for group membership."""
    payload = Addresses(
        id="",
        name=name,
        ip_netmask=ip_netmask,
        folder=TARGET_FOLDER,
        description="Temp address for AddressGroup test"
    )
    return api.create_addresses(addresses=payload)

def delete_test_address(api, address_id):
    """Helper to delete a single address object."""
    try:
        api.delete_addresses_by_id(id=address_id)
    except Exception as e:
        logger.warning(f"Failed to cleanup address {address_id}: {e}")

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
def addresses_api(client):
    return client.objects.AddressesApi(client.objects.api_client)

@pytest.fixture(scope="module")
def address_groups_api(client):
    return client.objects.AddressGroupsApi(client.objects.api_client)

@pytest.fixture
def clean_address_group(addresses_api, address_groups_api):
    """
    Fixture to create a temporary Address Group AND its dependent Addresses.
    Automatically cleans up the Group first, then the Addresses.
    """
    # 1. SETUP: Create Dependencies (Addresses)
    random_id = uuid.uuid4().hex[:6]
    addr1 = create_test_address(addresses_api, f"grp-dep-1-{random_id}", "10.100.1.1/32")
    addr2 = create_test_address(addresses_api, f"grp-dep-2-{random_id}", "10.100.1.2/32")

    # 2. SETUP: Create Address Group
    group_name = f"test-group-{random_id}"
    payload = AddressGroups(
        id="",
        name=group_name,
        folder=TARGET_FOLDER,
        static=[addr1.name, addr2.name], # Link to created addresses
        description="Created via Automated Pytest Fixture"
    )
    
    logger.info(f"\n[SETUP] Creating Address Group: {group_name}")
    created_group = address_groups_api.create_address_groups(address_groups=payload)
    
    # Pass control to test
    yield created_group

    # 3. TEARDOWN: Delete Group first (to remove reference)
    logger.info(f"\n[TEARDOWN] Deleting Address Group ID: {created_group.id}")
    try:
        address_groups_api.delete_address_groups_by_id(id=created_group.id)
    except Exception as e:
        logger.info(f"Group teardown failed (might be deleted in test): {e}")

    # 4. TEARDOWN: Delete Dependencies
    delete_test_address(addresses_api, addr1.id)
    delete_test_address(addresses_api, addr2.id)


# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def test_create_address_group(addresses_api, address_groups_api):
    """
    Test manual creation and deletion of an address group.
    Equivalent to Go: Test_objects_AddressGroupsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    
    # 1. Create dependencies
    addr1 = create_test_address(addresses_api, f"test-addr-1-{random_suffix}", "192.168.1.1/32")
    addr2 = create_test_address(addresses_api, f"test-addr-2-{random_suffix}", "192.168.1.2/32")

    # 2. Create Group
    group_name = f"test-group-create-{random_suffix}"
    payload = AddressGroups(
        id="",
        name=group_name,
        folder=TARGET_FOLDER,
        static=[addr1.name, addr2.name],
        description="Test address group for create API testing"
    )
    
    try:
        created_group = address_groups_api.create_address_groups(address_groups=payload)
        
        # Verify
        assert created_group.name == group_name
        assert created_group.id is not None
        assert set(created_group.static) == set([addr1.name, addr2.name])
        assert created_group.folder == TARGET_FOLDER or created_group.folder == "Shared"

        # Cleanup Group
        address_groups_api.delete_address_groups_by_id(id=created_group.id)
    
    finally:
        # Cleanup Addresses (always run even if assertions fail)
        delete_test_address(addresses_api, addr1.id)
        delete_test_address(addresses_api, addr2.id)


def test_get_address_group_by_id(address_groups_api, clean_address_group):
    """
    Test retrieving an address group by ID.
    Equivalent to Go: Test_objects_AddressGroupsAPIService_GetByID
    """
    # Retrieve
    fetched_obj = address_groups_api.get_address_groups_by_id(id=clean_address_group.id)
    
    # Verify
    assert fetched_obj.id == clean_address_group.id
    assert fetched_obj.name == clean_address_group.name
    assert fetched_obj.folder == clean_address_group.folder
    # Check static list contents (using set for unordered comparison)
    assert set(fetched_obj.static) == set(clean_address_group.static)


def test_update_address_group(addresses_api, address_groups_api, clean_address_group):
    """
    Test updating an address group.
    Equivalent to Go: Test_objects_AddressGroupsAPIService_Update
    """
    # 1. Create NEW addresses to update the group with
    random_suffix = uuid.uuid4().hex[:6]
    new_addr1 = create_test_address(addresses_api, f"upd-addr-1-{random_suffix}", "192.168.3.1/32")
    new_addr2 = create_test_address(addresses_api, f"upd-addr-2-{random_suffix}", "192.168.3.2/32")
    new_addr3 = create_test_address(addresses_api, f"upd-addr-3-{random_suffix}", "192.168.3.3/32")

    try:
        # 2. Prepare Update Payload
        update_payload = clean_address_group
        update_payload.description = "Updated test address group description"
        update_payload.static = [new_addr1.name, new_addr2.name, new_addr3.name]
        
        # 3. Perform Update
        updated_obj = address_groups_api.update_address_groups_by_id(
            id=clean_address_group.id, 
            address_groups=update_payload
        )
        
        # 4. Verify
        assert updated_obj.description == "Updated test address group description"
        assert set(updated_obj.static) == set([new_addr1.name, new_addr2.name, new_addr3.name])
        assert updated_obj.id == clean_address_group.id
    
    finally:
        # 5. Cleanup the NEW addresses
        # (The original addresses and the group itself are handled by the fixture)
        delete_test_address(addresses_api, new_addr1.id)
        delete_test_address(addresses_api, new_addr2.id)
        delete_test_address(addresses_api, new_addr3.id)


def test_list_address_groups(address_groups_api, clean_address_group):
    """
    Test listing address groups with folder filter.
    Equivalent to Go: Test_objects_AddressGroupsAPIService_List
    """
    # List with filter
    response = address_groups_api.list_address_groups(folder=clean_address_group.folder)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our specific object is in the list
    found = False
    for item in response.data:
        if item.id == clean_address_group.id:
            found = True
            break
    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_delete_address_group_by_id(addresses_api, address_groups_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_AddressGroupsAPIService_DeleteByID
    """
    random_suffix = uuid.uuid4().hex[:6]

    # 1. Create Dependencies
    addr1 = create_test_address(addresses_api, f"del-addr-1-{random_suffix}", "192.168.5.1/32")
    
    # 2. Create Group
    payload = AddressGroups(
        id="",
        name=f"test-group-del-{random_suffix}",
        folder=TARGET_FOLDER,
        static=[addr1.name],
        description="Test address group for delete API testing"
    )
    created_group = address_groups_api.create_address_groups(address_groups=payload)

    # 3. Perform Delete
    address_groups_api.delete_address_groups_by_id(id=created_group.id)

    # 4. Verify Deletion (Expect 404 on Get)
    try:
        address_groups_api.get_address_groups_by_id(id=created_group.id)
        pytest.fail("Address Group should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)

    # 5. Cleanup Dependency
    delete_test_address(addresses_api, addr1.id)
