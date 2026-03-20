
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
def trusted_certificate_authorities_api(client):
    return client.identity_services.TrustedCertificateAuthoritiesApi(client.identity_services.api_client)


def test_list_trusted_certificate_authorities(trusted_certificate_authorities_api):
    """Test listing Trusted Certificate Authorities."""
    response = trusted_certificate_authorities_api.list_trusted_certificate_authorities(limit=200, offset=0)
    assert response is not None
    assert response.data is not None and len(response.data) > 0
    logger.info(f"Listed {len(response.data)} Trusted Certificate Authorities successfully")
