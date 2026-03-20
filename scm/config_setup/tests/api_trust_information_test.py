
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
def trust_information_api(client):
    return client.config_setup.TrustInformationApi(client.config_setup.api_client)


def test_list_trusted_tenants_with_snippets(trust_information_api):
    """Test listing Trusted Tenants with Snippets."""
    response = trust_information_api.list_trusted_tenants_with_snippets(type="subscriber")
    assert response is not None
    logger.info(f"Listed Trusted Tenants with Snippets successfully")
