
import logging
import pytest
from scm import Scm

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def folders_api(client):
    return client.config_setup.FoldersApi(client.config_setup.api_client)


def test_list_folders(folders_api):
    """Test listing Folders."""
    response = folders_api.list_folders(limit=200, offset=0)
    assert response is not None
    logger.info(f"Listed Folders successfully")


def test_fetch_folders(folders_api):
    """Test fetching a non-existent Folder returns None."""
    result = folders_api.fetch_folders(
        name="non-existent-folder-xyz-12345"
    )
    assert result is None, "Should return None for non-existent folder"
    logger.info("fetch_folders correctly returned None for non-existent object")
