
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
def local_users_api(client):
    return client.identity_services.LocalUsersApi(client.identity_services.api_client)


def test_fetch_local_users(local_users_api):
    """Test fetching a non-existent Local User returns None."""
    result = local_users_api.fetch_local_users(
        name="non-existent-user-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert result is None, "Should return None for non-existent local user"
    logger.info("fetch_local_users correctly returned None for non-existent object")
