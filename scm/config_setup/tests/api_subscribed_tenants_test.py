
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
def snippet_categories_api(client):
    return client.config_setup.SnippetCategoriesApi(client.config_setup.api_client)


@pytest.fixture(scope="module")
def subscribed_tenants_api(client):
    return client.config_setup.SubscribedTenantsApi(client.config_setup.api_client)


def test_list_subscribed_tenants(snippet_categories_api, subscribed_tenants_api):
    """Test listing Subscribed Tenants for a known snippet."""
    # First, find a snippet ID via snippet categories
    snippet = snippet_categories_api.fetch_snippet_categories(name="app-tagging")
    if snippet is None:
        pytest.skip("Could not find 'app-tagging' snippet category - skipping subscribed tenants test")

    snippet_id = snippet.id
    logger.info(f"Found snippet 'app-tagging' with ID: {snippet_id}")

    # List subscribed tenants for the snippet
    response = subscribed_tenants_api.list_subscribed_tenants_by_id(id=snippet_id)
    assert response is not None
    logger.info(f"Listed Subscribed Tenants for snippet ID {snippet_id} successfully")
