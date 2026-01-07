
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    InterfaceManagementProfiles,
    InterfaceManagementProfilesPermittedIpInner
)

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
def profile_api(client):
    return client.network_services.InterfaceManagementProfilesApi(client.network_services.api_client)

def create_base_profile(name_prefix):
    """Helper to create a base Interface Management Profile."""
    random_id = uuid.uuid4().hex[:6]
    name = f"{name_prefix}{random_id}"
    
    return InterfaceManagementProfiles(
        name=name,
        folder=TARGET_FOLDER,
        http=True,
        https=True,
        ssh=True,
        ping=True,
        telnet=False,
        userid_service=True,
        permitted_ip=[
            InterfaceManagementProfilesPermittedIpInner(name="198.18.0.1/32"),
            InterfaceManagementProfilesPermittedIpInner(name="192.0.2.0/24")
        ]
    )

@pytest.fixture
def clean_profile(profile_api):
    """
    Fixture for standard CRUD tests.
    """
    profile = create_base_profile("profile-get-")
    
    logger.info(f"\n[SETUP] Creating Profile: {profile.name}")
    created_obj = profile_api.create_interface_management_profiles(interface_management_profiles=profile)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting Profile ID: {created_obj.id}")
    try:
        profile_api.delete_interface_management_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_full_profile(profile_api):
    """
    Test creation of a fully configured Interface Management Profile.
    """
    profile = create_base_profile("profile-full-")
    profile.http_ocsp = True
    profile.userid_syslog_listener_ssl = True
    profile.userid_syslog_listener_udp = True

    try:
        created_obj = profile_api.create_interface_management_profiles(interface_management_profiles=profile)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.http is True
    assert created_obj.ssh is True
    assert len(created_obj.permitted_ip) == 2

    # Cleanup
    profile_api.delete_interface_management_profiles_by_id(id=created_obj.id)


def test_get_profile_by_id(profile_api, clean_profile):
    """
    Test retrieving a Profile by ID.
    """
    fetched_obj = profile_api.get_interface_management_profiles_by_id(id=clean_profile.id)
    assert fetched_obj.id == clean_profile.id
    assert fetched_obj.name == clean_profile.name
    assert fetched_obj.http is True


def test_update_profile(profile_api, clean_profile):
    """
    Test updating a Profile (disable SSH, add IP).
    """
    update_payload = clean_profile
    update_payload.ssh = False
    
    new_ip = InterfaceManagementProfilesPermittedIpInner(name="10.0.0.1")
    if update_payload.permitted_ip is None:
        update_payload.permitted_ip = []
    update_payload.permitted_ip.append(new_ip)
    
    updated_obj = profile_api.update_interface_management_profiles_by_id(
        id=clean_profile.id,
        interface_management_profiles=update_payload
    )
    
    assert updated_obj.id == clean_profile.id
    assert updated_obj.ssh is False
    assert len(updated_obj.permitted_ip) == 3


def test_list_profiles(profile_api, clean_profile):
    """
    Test listing Profiles.
    """
    response = profile_api.list_interface_management_profiles(folder=TARGET_FOLDER)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_profile.id:
            found = True
            break
    assert found is True


def test_delete_profile_by_id(profile_api):
    """
    Test deleting a Profile.
    """
    profile = create_base_profile("profile-del-")
    created_obj = profile_api.create_interface_management_profiles(interface_management_profiles=profile)
    
    profile_api.delete_interface_management_profiles_by_id(id=created_obj.id)
    
    try:
        profile_api.get_interface_management_profiles_by_id(id=created_obj.id)
        pytest.fail("Profile should be deleted")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
