
import logging
import pytest
from scm import Scm

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
def mfa_servers_api(client):
    return client.identity_services.MFAServersApi(client.identity_services.api_client)


def test_list_mfa_servers(mfa_servers_api):
    """Test listing MFA Servers."""
    response = mfa_servers_api.list_mfa_servers(folder=TARGET_FOLDER, position="pre", limit=200, offset=0)
    assert response is not None
    logger.info(f"Listed MFA Servers successfully")


def test_fetch_mfa_servers(mfa_servers_api):
    """Test fetching a non-existent MFA Server returns None."""
    result = mfa_servers_api.fetch_mfa_servers(
        name="non-existent-mfa-server-xyz-12345",
        folder=TARGET_FOLDER,
        position="pre",
    )
    assert result is None, "Should return None for non-existent mfa server"
    logger.info("fetch_mfa_servers correctly returned None for non-existent object")
