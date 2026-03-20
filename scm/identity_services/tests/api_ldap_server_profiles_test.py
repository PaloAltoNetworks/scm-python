
import logging
import pytest
from scm import Scm

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
def ldap_server_profiles_api(client):
    return client.identity_services.LDAPServerProfilesApi(client.identity_services.api_client)


def test_fetch_ldap_server_profiles(ldap_server_profiles_api):
    """Test fetching a non-existent LDAP Server Profile returns None."""
    result = ldap_server_profiles_api.fetch_ldap_server_profiles(
        name="non-existent-ldap-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert result is None, "Should return None for non-existent ldap server profile"
    logger.info("fetch_ldap_server_profiles correctly returned None for non-existent object")
