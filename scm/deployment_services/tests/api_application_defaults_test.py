
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
def application_defaults_api(client):
    return client.deployment_services.ApplicationDefaultsApi(client.deployment_services.api_client)


def test_create_application_defaults(application_defaults_api):
    """
    Test creating/enabling application defaults (idempotent POST /enable operation).
    This is safe to call repeatedly.
    Equivalent to Go: Test_deployment_services_ApplicationDefaultsAPIService_Create
    """
    # This is an idempotent enable operation - no payload, no response body
    application_defaults_api.create_application_defaults()
    logger.info(f"Successfully created/enabled application defaults")
