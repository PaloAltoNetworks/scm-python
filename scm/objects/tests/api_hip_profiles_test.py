
import logging
import uuid
import pytest
from scm import Scm
from scm.objects.models.hip_profiles import HipProfiles

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
def hip_profiles_api(client):
    """
    Fixture to return the HIP Profiles API instance.
    """
    return client.objects.HIPProfilesApi(client.objects.api_client)

@pytest.fixture
def clean_hip_profile(hip_profiles_api):
    """
    Fixture to create a temporary HIP Profile for testing and automatically delete it after.
    """
    # 1. SETUP: Create HIP Profile
    random_id = uuid.uuid4().hex[:6]
    profile_name = f"test-hip-profile-{random_id}"
    
    payload = HipProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        match='"is-win" and "is-anti-malware-and-rtp-enabled"'
    )
    
    logger.info(f"\n[SETUP] Creating HIP Profile: {profile_name}")
    created_obj = hip_profiles_api.create_hip_profiles(hip_profiles=payload)
    assert created_obj.id is not None
    
    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete HIP Profile
    logger.info(f"\n[TEARDOWN] Deleting HIP Profile ID: {created_obj.id}")
    try:
        hip_profiles_api.delete_hip_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_hip_profile(hip_profiles_api):
    """
    Test manual creation and deletion of a HIP profile.
    Equivalent to Go: Test_objects_HIPProfilesAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    profile_name = f"test-hip-create-{random_suffix}"
    
    payload = HipProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        description="Test HIP profile for create API",
        match='"is-win" and "is-anti-malware-and-rtp-enabled"'
    )

    # Create
    created_obj = hip_profiles_api.create_hip_profiles(hip_profiles=payload)
    
    # Verify
    assert created_obj.name == profile_name
    assert created_obj.id is not None
    assert created_obj.match == payload.match
    assert created_obj.folder == TARGET_FOLDER or created_obj.folder == "Shared"

    # Cleanup
    hip_profiles_api.delete_hip_profiles_by_id(id=created_obj.id)


def test_get_hip_profile_by_id(hip_profiles_api, clean_hip_profile):
    """
    Test retrieving a HIP profile by ID.
    Equivalent to Go: Test_objects_HIPProfilesAPIService_GetByID
    """
    # Retrieve
    fetched_obj = hip_profiles_api.get_hip_profiles_by_id(id=clean_hip_profile.id)
    
    # Verify
    assert fetched_obj.id == clean_hip_profile.id
    assert fetched_obj.name == clean_hip_profile.name
    assert fetched_obj.match == clean_hip_profile.match
    # assert fetched_obj.folder == clean_hip_profile.folder


def test_update_hip_profile(hip_profiles_api, clean_hip_profile):
    """
    Test updating an existing HIP profile.
    Equivalent to Go: Test_objects_HIPProfilesAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_hip_profile
    update_payload.description = "Updated description"
    update_payload.match = '"is-win" and "is-rtp-enabled"'

    # Perform Update
    updated_obj = hip_profiles_api.update_hip_profiles_by_id(
        id=clean_hip_profile.id, 
        hip_profiles=update_payload
    )
    
    # Verify
    assert updated_obj.id == clean_hip_profile.id
    assert updated_obj.name == clean_hip_profile.name
    assert updated_obj.description == "Updated description"
    assert updated_obj.match == '"is-win" and "is-rtp-enabled"'


def test_list_hip_profiles(hip_profiles_api, clean_hip_profile):
    """
    Test listing HIP profiles with folder filter.
    Equivalent to Go: Test_objects_HIPProfilesAPIService_List
    """
    # List with filter
    # Using limit=10000 to match Go test logic
    response = hip_profiles_api.list_hip_profiles(folder=clean_hip_profile.folder, limit=10000)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.name == clean_hip_profile.name:
            found = True
            assert item.match == clean_hip_profile.match
            break
            
    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")


def test_delete_hip_profile_by_id(hip_profiles_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_HIPProfilesAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    profile_name = f"test-hip-delete-{random_suffix}"
    
    payload = HipProfiles(
        id="",
        name=profile_name,
        folder=TARGET_FOLDER,
        match='"is-win" and "is-anti-malware-and-rtp-enabled"'
    )
    created_obj = hip_profiles_api.create_hip_profiles(hip_profiles=payload)

    # Perform Delete
    hip_profiles_api.delete_hip_profiles_by_id(id=created_obj.id)

    # Verify Deletion (Expect 404 on Get)
    try:
        hip_profiles_api.get_hip_profiles_by_id(id=created_obj.id)
        pytest.fail("HIP Profile should have been deleted but was found.")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
