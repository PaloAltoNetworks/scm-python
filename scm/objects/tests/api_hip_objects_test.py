
import logging
import uuid
import pytest
from scm import Scm

from scm.objects.models import (
    HipObjects,
    HipObjectsHostInfo,
    HipObjectsHostInfoCriteria,
    HipObjectsHostInfoCriteriaOs,
    HipObjectsHostInfoCriteriaOsContains,
    HipObjectsAntiMalware,
    HipObjectsAntiMalwareCriteria,
    HipObjectsDiskBackup,
    HipObjectsDiskBackupCriteria,
    HipObjectsDiskEncryption,
    HipObjectsDiskEncryptionCriteria,
    HipObjectsMobileDevice,
    HipObjectsMobileDeviceCriteria,
    HipObjectsPatchManagement,
    HipObjectsPatchManagementCriteria,
    HipObjectsDataLossPrevention,
    HipObjectsDataLossPreventionCriteria,
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "Shared"
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
def hip_objects_api(client):
    """
    Fixture to return the HIP Objects API instance.
    """
    return client.objects.HIPObjectsApi(client.objects.api_client)

@pytest.fixture
def clean_hip_object(hip_objects_api):
    """
    Fixture to create a temporary HIP object for testing and automatically delete it after.
    """
    # 1. SETUP: Create HIP Object
    random_id = uuid.uuid4().hex[:6]
    hip_name = f"test-hip-obj-{random_id}"
    
    payload = HipObjects(
        id="",
        name=hip_name,
        folder=TARGET_FOLDER,
        description="Created via Automated Pytest Fixture",
        host_info=HipObjectsHostInfo(
            criteria=HipObjectsHostInfoCriteria(
                os=HipObjectsHostInfoCriteriaOs(
                    contains=HipObjectsHostInfoCriteriaOsContains(
                        apple="macOS"
                    )
                )
            )
        )
    )
    
    logger.info(f"\n[SETUP] Creating HIP Object: {hip_name}")
    created_obj = hip_objects_api.create_hip_objects(hip_objects=payload)
    assert created_obj.id is not None
    
    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete HIP Object
    logger.info(f"\n[TEARDOWN] Deleting HIP Object ID: {created_obj.id}")
    try:
        hip_objects_api.delete_hip_objects_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_hip_object(hip_objects_api):
    """
    Test manual creation and deletion of a HIP object.
    Equivalent to Go: Test_objects_HIPObjectsAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    hip_name = f"test-hip-obj-create-{random_suffix}"
    
    # Construct complex nested payload matching Go test
    payload = HipObjects(
        id="",
        name=hip_name,
        folder=TARGET_FOLDER,
        description="Test HIP object for create API",
        host_info=HipObjectsHostInfo(
            criteria=HipObjectsHostInfoCriteria(
                os=HipObjectsHostInfoCriteriaOs(
                    contains=HipObjectsHostInfoCriteriaOsContains(
                        microsoft="Microsoft Windows 10"
                    )
                )
            )
        ),
        anti_malware=HipObjectsAntiMalware(
            criteria=HipObjectsAntiMalwareCriteria(is_installed=True)
        ),
        disk_backup=HipObjectsDiskBackup(
            criteria=HipObjectsDiskBackupCriteria(is_installed=True)
        ),
        disk_encryption=HipObjectsDiskEncryption(
            criteria=HipObjectsDiskEncryptionCriteria(is_installed=True)
        ),
        mobile_device=HipObjectsMobileDevice(
            criteria=HipObjectsMobileDeviceCriteria(jailbroken=False)
        ),
        patch_management=HipObjectsPatchManagement(
            criteria=HipObjectsPatchManagementCriteria(is_installed=True)
        ),
        data_loss_prevention=HipObjectsDataLossPrevention(
            criteria=HipObjectsDataLossPreventionCriteria(is_installed=True)
        )
    )

    # Create
    created_obj = hip_objects_api.create_hip_objects(hip_objects=payload)
    
    # Verify
    assert created_obj.name == hip_name
    assert created_obj.id is not None
    
    # Verify nested structures
    assert created_obj.host_info is not None
    assert created_obj.anti_malware is not None
    assert created_obj.disk_backup is not None
    assert created_obj.disk_encryption is not None
    assert created_obj.mobile_device is not None
    assert created_obj.patch_management is not None
    assert created_obj.data_loss_prevention is not None
    assert created_obj.data_loss_prevention.criteria.is_installed is True

    # Cleanup
    hip_objects_api.delete_hip_objects_by_id(id=created_obj.id)


def test_get_hip_object_by_id(hip_objects_api, clean_hip_object):
    """
    Test retrieving a HIP object by ID.
    Equivalent to Go: Test_objects_HIPObjectsAPIService_GetByID
    """
    # Retrieve
    fetched_obj = hip_objects_api.get_hip_objects_by_id(id=clean_hip_object.id)
    
    # Verify
    assert fetched_obj.id == clean_hip_object.id
    assert fetched_obj.name == clean_hip_object.name
    
    # Verify specific nested field set in fixture (Apple="macOS")
    assert fetched_obj.host_info.criteria.os.contains.apple == "macOS"


def test_update_hip_object(hip_objects_api, clean_hip_object):
    """
    Test updating an existing HIP object.
    Equivalent to Go: Test_objects_HIPObjectsAPIService_Update
    """
    # Prepare Update Payload with all criteria
    update_payload = clean_hip_object
    update_payload.description = "Updated with all criteria"
    
    # Update Host Info to Linux/RedHat
    update_payload.host_info = HipObjectsHostInfo(
        criteria=HipObjectsHostInfoCriteria(
            os=HipObjectsHostInfoCriteriaOs(
                contains=HipObjectsHostInfoCriteriaOsContains(
                    linux="RedHat"
                )
            )
        )
    )
    
    # Add other criteria
    update_payload.anti_malware = HipObjectsAntiMalware(
        criteria=HipObjectsAntiMalwareCriteria(is_installed=True)
    )
    update_payload.disk_backup = HipObjectsDiskBackup(
        criteria=HipObjectsDiskBackupCriteria(is_installed=True)
    )
    update_payload.disk_encryption = HipObjectsDiskEncryption(
        criteria=HipObjectsDiskEncryptionCriteria(is_installed=True)
    )
    update_payload.mobile_device = HipObjectsMobileDevice(
        criteria=HipObjectsMobileDeviceCriteria(jailbroken=False)
    )
    update_payload.patch_management = HipObjectsPatchManagement(
        criteria=HipObjectsPatchManagementCriteria(is_installed=True)
    )
    update_payload.data_loss_prevention = HipObjectsDataLossPrevention(
        criteria=HipObjectsDataLossPreventionCriteria(is_installed=True)
    )

    # Perform Update
    updated_obj = hip_objects_api.update_hip_objects_by_id(
        id=clean_hip_object.id, 
        hip_objects=update_payload
    )
    
    # Verify
    assert updated_obj.id == clean_hip_object.id
    assert updated_obj.description == "Updated with all criteria"
    assert updated_obj.host_info.criteria.os.contains.linux == "RedHat"
    assert updated_obj.data_loss_prevention is not None
    assert updated_obj.data_loss_prevention.criteria.is_installed is True


def test_list_hip_objects(hip_objects_api, clean_hip_object):
    """
    Test listing HIP objects with folder filter.
    Equivalent to Go: Test_objects_HIPObjectsAPIService_List
    """
    # List with filter
    response = hip_objects_api.list_hip_objects(folder=TARGET_FOLDER, limit=10000)
    
    assert response is not None
    assert len(response.data) > 0
    
    # Verify our specific object is in the list
    found = False
    for item in response.data:
        if item.name == clean_hip_object.name:
            found = True
            break
            
    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")




def test_fetch_hip_objects(hip_objects_api, clean_hip_object):
    """
    Test fetching a single hip_objects by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = hip_objects_api.fetch_hip_objects(
        name=clean_hip_object.name,
        folder=clean_hip_object.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found hip_objects '{clean_hip_object.name}'"
    assert fetched_obj.id == clean_hip_object.id
    assert fetched_obj.name == clean_hip_object.name
    assert fetched_obj.folder == clean_hip_object.folder
    logger.info(f"\n[SUCCESS] fetch_hip_objects found object: {fetched_obj.name}")

    # Test fetching non-existent hip_objects (should return None)
    not_found = hip_objects_api.fetch_hip_objects(
        name="non-existent-hip_objects-xyz-12345",
        folder=clean_hip_object.folder
    )
    assert not_found is None, "Should return None for non-existent hip_objects"
    logger.info(f"\n[SUCCESS] fetch_hip_objects correctly returned None for non-existent hip_objects")


def test_delete_hip_object_by_id(hip_objects_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_objects_HIPObjectsAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    hip_name = f"test-hip-obj-delete-{random_suffix}"
    
    payload = HipObjects(
        id="",
        name=hip_name,
        folder=TARGET_FOLDER
    )
    created_obj = hip_objects_api.create_hip_objects(hip_objects=payload)

    # Perform Delete
    hip_objects_api.delete_hip_objects_by_id(id=created_obj.id)

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    from scm.exceptions import ObjectNotPresentError
    # Decorator already converts NotFoundException to ObjectNotPresentError

    try:
        hip_objects_api.get_hip_objects_by_id(id=created_obj.id)
        pytest.fail("HIP Object should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
