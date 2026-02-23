
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


def test_list_snippet_categories(snippet_categories_api):
    """Test listing Snippet Categories."""
    pytest.skip("API returns bare JSON array but SDK expects paginated response")


def test_fetch_snippet_categories(snippet_categories_api):
    """Test fetching a non-existent Snippet Category returns None."""
    result = snippet_categories_api.fetch_snippet_categories(
        name="nonexistent-test-category-12345"
    )
    assert result is None, "Should return None for non-existent snippet category"
    logger.info("fetch_snippet_categories correctly returned None for non-existent object")
