
import logging
import uuid
import pytest
from scm import Scm

# Assuming the models follow the standard SCM SDK naming convention
from scm.identity_services.models import AuthenticationPortals
from scm.identity_services.models import AuthenticationProfiles  # Needed for dependency

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# --- Test Constants ---
TARGET_FOLDER = "All"
TEST_REDIRECT_HOST = "192.168.255.254"
CERT_PROFILE_NAME = "EDL-Hosting-Service-Profile"

@pytest.fixture(scope="module")
def client():
"""Initializes the SCM client."""
try:
return Scm(log_level="DEBUG")
except Exception as e:
pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def auth_portals_api(client):
"""Returns the Authentication Portals API instance."""
return client.identity_services.AuthenticationPortalsApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def auth_profiles_api(client):
"""Returns the Authentication Profiles API instance for prerequisite setup."""
return client.identity_services.AuthenticationProfilesApi(client.identity_services.api_client)

@pytest.fixture(scope="module")
def test_auth_profile(auth_profiles_api):
"""
Setup/Teardown for the prerequisite Authentication Profile.
Mirrors the 'setupTestAuthProfile' function in the Go test.
"""
random_id = uuid.uuid4().hex[:6]
profile_name = f"test-auth-prof-{random_id}"

# Create a minimal Authentication Profile required for the portal
# Note: Adjust fields based on actual AuthenticationProfiles model requirements
payload = AuthenticationProfiles(
id="",
name=profile_name,
folder=TARGET_FOLDER,
allow_list=[], # Minimal defaults
method={} # Assuming some method configuration is needed
)

logger.info(f"\n[SETUP] Creating Prerequisite Auth Profile: {profile_name}")
try:
created_profile = auth_profiles_api.create_authentication_profiles(authentication_profiles=payload)
except Exception as e:
# Fallback if creation fails or strict schema is required;
# in a real env, you might skip or use a static existing profile.
logger.warning(f"Could not create auth profile fixture: {e}")
yield "Existing-Auth-Profile"
return

yield created_profile.name

logger.info(f"\n[TEARDOWN] Deleting Auth Profile: {created_profile.name}")
try:
auth_profiles_api.delete_authentication_profiles_by_id(id=created_profile.id)
except Exception as e:
logger.error(f"Failed to cleanup auth profile: {e}")

@pytest.fixture
def clean_auth_portal(auth_portals_api, test_auth_profile):
"""
Creates an Authentication Portal for tests that require an existing object (like List).
"""
random_id = uuid.uuid4().hex[:6]
portal_name = f"test-portal-fixture-{random_id}" # Portals usually don't have a 'name' field, but if they do.
# Note: Auth Portals in the Go test seem to depend on RedirectHost/Folder primarily.

payload = AuthenticationPortals(
folder=TARGET_FOLDER,
redirect_host=TEST_REDIRECT_HOST,
authentication_profile=test_auth_profile,
certificate_profile=CERT_PROFILE_NAME,
gp_udp_port=10,
idle_timer=10,
timer=12
)

logger.info(f"\n[SETUP] Creating Auth Portal for fixture")
created_obj = auth_portals_api.create_authentication_portals(authentication_portals=payload)
yield created_obj

logger.info(f"\n[TEARDOWN] Deleting Auth Portal ID: {created_obj.id}")
try:
auth_portals_api.delete_authentication_portals_by_id(id=created_obj.id)
except Exception as e:
logger.info(f"Teardown failed: {e}")


# ---------------------------------------------------------------------------------------------------------------------

def test_create_auth_portal(auth_portals_api, test_auth_profile):
"""
Mirrors Test_identityservices_AuthenticationPortalsAPIService__Create
"""
# Prepare payload
payload = AuthenticationPortals(
folder=TARGET_FOLDER,
redirect_host=TEST_REDIRECT_HOST,
authentication_profile=test_auth_profile,
certificate_profile=CERT_PROFILE_NAME,
gp_udp_port=10,
idle_timer=10,
timer=12
)

logger.info(f"Creating Authentication Portal with fixed host: {TEST_REDIRECT_HOST}")
created_obj = auth_portals_api.create_authentication_portals(authentication_portals=payload)

# Verification
assert created_obj.id is not None
assert created_obj.redirect_host == TEST_REDIRECT_HOST
assert created_obj.gp_udp_port == 10

# Cleanup
auth_portals_api.delete_authentication_portals_by_id(id=created_obj.id)


def test_get_auth_portal_by_id(auth_portals_api, test_auth_profile):
"""
Mirrors Test_identityservices_AuthenticationPortalsAPIService__GetByID
"""
# 1. Setup: Create a portal
payload = AuthenticationPortals(
folder=TARGET_FOLDER,
redirect_host=TEST_REDIRECT_HOST,
authentication_profile=test_auth_profile,
certificate_profile=CERT_PROFILE_NAME,
gp_udp_port=10,
idle_timer=10,
timer=12
)
created_obj = auth_portals_api.create_authentication_portals(authentication_portals=payload)

try:
# 2. Test: Retrieve the portal
fetched_obj = auth_portals_api.get_authentication_portals_by_id(id=created_obj.id)

# 3. Verify
assert fetched_obj.id == created_obj.id
assert fetched_obj.redirect_host == TEST_REDIRECT_HOST
assert fetched_obj.timer == 12

finally:
# Cleanup
auth_portals_api.delete_authentication_portals_by_id(id=created_obj.id)


def test_update_auth_portal(auth_portals_api, test_auth_profile):
"""
Mirrors Test_identityservices_AuthenticationPortalsAPIService__Update
"""
# 1. Setup: Create a portal
payload = AuthenticationPortals(
folder=TARGET_FOLDER,
redirect_host=TEST_REDIRECT_HOST,
authentication_profile=test_auth_profile,
certificate_profile=CERT_PROFILE_NAME,
gp_udp_port=10,
idle_timer=10,
timer=12
)
created_obj = auth_portals_api.create_authentication_portals(authentication_portals=payload)

try:
# 2. Prepare updated object
# Note: In Python SDK, we often modify the object or create a new one with the same ID.
updated_gp_port = 20
updated_timer = 30

# We modify the created object directly for the update payload
update_payload = created_obj
update_payload.gp_udp_port = updated_gp_port
update_payload.timer = updated_timer

# 3. Test: Update the portal
updated_res = auth_portals_api.update_authentication_portals_by_id(
id=created_obj.id,
authentication_portals=update_payload
)

# 4. Verify
assert updated_res.id == created_obj.id
assert updated_res.gp_udp_port == updated_gp_port
assert updated_res.timer == updated_timer

finally:
# Cleanup
auth_portals_api.delete_authentication_portals_by_id(id=created_obj.id)


def test_list_auth_portals(auth_portals_api, clean_auth_portal):
"""
Mirrors Test_identityservices_AuthenticationPortalsAPIService__List
"""
# 1. Test: List portals filtered by folder
# Note: Go test also filtered by host, assume API supports it if SDK does
response = auth_portals_api.list_authentication_portals(folder=TARGET_FOLDER)

assert response is not None
# Depending on pagination, 'data' attribute usually holds the list
assert len(response.data) > 0

# 2. Verify the fixture object is in the list
found = False
for item in response.data:
if item.id == clean_auth_portal.id:
found = True
break
assert found is True, f"Created portal {clean_auth_portal.id} not found in list response"


def test_delete_auth_portal_by_id(auth_portals_api, test_auth_profile):
"""
Mirrors Test_identityservices_AuthenticationPortalsAPIService__DeleteByID
"""
# 1. Setup: Create a portal
payload = AuthenticationPortals(
folder=TARGET_FOLDER,
redirect_host=TEST_REDIRECT_HOST,
authentication_profile=test_auth_profile,
certificate_profile=CERT_PROFILE_NAME,
gp_udp_port=10,
idle_timer=10,
timer=12
)
created_obj = auth_portals_api.create_authentication_portals(authentication_portals=payload)

# 2. Test: Delete the portal
logger.info(f"Deleting Authentication Portal with ID: {created_obj.id}")
auth_portals_api.delete_authentication_portals_by_id(id=created_obj.id)

# 3. Verify Deletion (Expect 404 on Get)
try:
auth_portals_api.get_authentication_portals_by_id(id=created_obj.id)
pytest.fail("Authentication Portal should have been deleted")
except Exception as e:
# Check for 404 Not Found in exception message
assert "404" in str(e) or "Not Found" in str(e)
