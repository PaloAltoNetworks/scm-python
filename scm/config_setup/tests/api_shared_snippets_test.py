
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
def shared_snippets_api(client):
    return client.config_setup.SharedSnippetsApi(client.config_setup.api_client)


def test_list_shared_snippets(shared_snippets_api):
    """Test listing Shared Snippets (read-only resource)."""
    response = shared_snippets_api.list_shared_snippets()
    assert response is not None
    logger.info(f"Listed Shared Snippets successfully")
