
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
def auto_tag_actions_api(client):
    return client.security_services.AutoTagActionsApi(client.security_services.api_client)


def test_list_auto_tag_actions(auto_tag_actions_api):
    """Test listing auto tag actions."""
    response = auto_tag_actions_api.list_auto_tag_actions()
    assert response is not None
    logger.info(f"Listed {len(response.data) if response.data else 0} auto tag actions")


def test_fetch_auto_tag_actions(auto_tag_actions_api):
    """Test fetch method for auto tag actions."""
    # First list to find an existing object
    response = auto_tag_actions_api.list_auto_tag_actions()
    if response is None or not hasattr(response, 'data') or not response.data:
        pytest.skip("No auto tag actions found to test fetch")

    target = response.data[0]
    target_name = target.name
    logger.info(f"Testing fetch for: {target_name}")

    # Use fetch method
    fetched = auto_tag_actions_api.fetch_auto_tag_actions(name=target_name)
    assert fetched is not None
    assert fetched.name == target_name
    logger.info(f"Successfully fetched auto tag action: {fetched.name}")


def test_fetch_auto_tag_actions_not_found(auto_tag_actions_api):
    """Test fetch returns None for non-existent object."""
    result = auto_tag_actions_api.fetch_auto_tag_actions(
        name="non-existent-autotag-xyz-12345",
    )
    assert result is None
    logger.info("Correctly returned None for non-existent auto tag action")
