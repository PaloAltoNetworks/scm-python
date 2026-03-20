
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
def certificates_api(client):
    return client.identity_services.CertificatesApi(client.identity_services.api_client)


def test_fetch_certificates(certificates_api):
    """Test fetching a non-existent Certificate returns None."""
    result = certificates_api.fetch_certificates(
        name="non-existent-cert-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert result is None, "Should return None for non-existent certificate"
    logger.info("fetch_certificates correctly returned None for non-existent object")
