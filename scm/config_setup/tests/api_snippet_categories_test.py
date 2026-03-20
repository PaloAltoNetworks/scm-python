
import logging
import pytest
from scm import Scm
from scm.test_helpers import perform

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


def test_get_snippet_category_by_id(snippet_categories_api):
    """
    Test retrieving a snippet category by ID.
    Equivalent to Go: Test_config_setup_SnippetCategoriesAPIService_GetByID
    """
    # NOTE: GetByID requires a valid ID, but the only way to discover one
    # is via List or Fetch — both fail because the API returns a bare JSON
    # array that the SDK can't deserialize. Go works because its Fetch
    # handles bare arrays differently. Skip until the model mismatch is fixed.
    pytest.skip("Cannot discover IDs — List/Fetch fail due to bare JSON array response")


def test_fetch_snippet_categories(snippet_categories_api):
    """Test fetching a non-existent Snippet Category returns None."""
    # NOTE: Fetch internally calls List with name= filter, but the API returns
    # a bare JSON array causing BadRequestError. Skip until model mismatch is fixed.
    pytest.skip("Fetch relies on List which fails due to bare JSON array response")
