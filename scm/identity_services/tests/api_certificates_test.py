
import logging
import base64
import uuid
import pytest
from scm import Scm
from scm.identity_services.models.certificates_post import CertificatesPost
from scm.identity_services.models.certificates_post_algorithm import CertificatesPostAlgorithm
from scm.identity_services.models.certificates_import import CertificatesImport
from scm.identity_services.models.export_certificate_payload import ExportCertificatePayload
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "Prisma Access"


@pytest.fixture(scope="module")
def client():
    """Fixture to initialize the SCM client once for the module."""
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def certificates_api(client):
    """Fixture to return the Certificates API instance."""
    return client.identity_services.CertificatesApi(client.identity_services.api_client)


def test_list_certificates(certificates_api):
    """Test listing certificates."""
    response = perform(
        certificates_api.list_certificates,
        folder=TARGET_FOLDER,
        limit=100
    )

    assert response is not None
    assert hasattr(response, 'data')
    logger.info(f"Retrieved {len(response.data)} certificates")

    # Log first few certificates
    for i, cert in enumerate(response.data[:5]):
        logger.info(f"  Certificate: {cert.name} (ID: {cert.id})")

    logger.info(f"[SUCCESS] list_certificates returned {len(response.data)} certificates")


def test_fetch_certificates_not_found(certificates_api):
    """Test fetching a non-existent certificate returns None."""
    result = certificates_api.fetch_certificates(
        name="non-existent-cert-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert result is None, "Should return None for non-existent certificate"
    logger.info("[SUCCESS] fetch_certificates correctly returned None for non-existent object")


def test_fetch_certificates_existing(certificates_api):
    """Test fetching an existing certificate by name."""
    # First, list certificates to get a name to fetch
    response = perform(
        certificates_api.list_certificates,
        folder=TARGET_FOLDER,
        limit=10
    )

    if not response.data or len(response.data) == 0:
        pytest.skip("No certificates available to test fetch_existing - skipping")
        return

    # Fetch the first certificate by name
    cert_to_fetch = response.data[0]
    cert_name = cert_to_fetch.name

    logger.info(f"Attempting to fetch Certificate with name: {cert_name}")
    fetched_cert = certificates_api.fetch_certificates(
        name=cert_name,
        folder=TARGET_FOLDER,
    )

    assert fetched_cert is not None, "Fetched certificate should not be None"
    assert fetched_cert.name == cert_name, "Fetched certificate name should match"
    assert fetched_cert.id == cert_to_fetch.id, "Fetched certificate ID should match"
    logger.info(f"[SUCCESS] fetch_certificates found certificate: {fetched_cert.name} (ID: {fetched_cert.id})")


def test_create_certificate(certificates_api):
    """Test creating a certificate."""
    cert_name = f"test-cert-create-{uuid.uuid4().hex[:6]}"

    # Create algorithm with RSA 2048 bits
    algorithm = CertificatesPostAlgorithm(
        rsa_number_of_bits=2048.0
    )

    # Create the certificate payload
    cert = CertificatesPost(
        algorithm=algorithm,
        certificate_name=cert_name,
        common_name=f"{cert_name}.example.com",
        digest="sha256",
        signed_by="Root CA",
        folder=TARGET_FOLDER,
    )

    logger.info(f"Attempting to create Certificate with name: {cert_name}")
    created_cert = perform(
        certificates_api.create_certificates,
        certificates_post=cert
    )

    assert created_cert is not None, "Response should not be None"
    assert created_cert.id is not None, "Created certificate should have an ID"
    assert created_cert.name == cert_name, "Created certificate name should match"

    created_cert_id = created_cert.id
    logger.info(f"Successfully created Certificate: {cert_name} with ID: {created_cert_id}")

    # Cleanup: Delete the created certificate
    try:
        perform(
            certificates_api.delete_certificates_by_id,
            id=created_cert_id
        )
        logger.info(f"Cleaned up Certificate with ID: {created_cert_id}")
    except Exception as e:
        logger.warning(f"Cleanup failed: {e}")

    logger.info(f"[SUCCESS] create_certificates created certificate: {cert_name}")


def test_delete_certificate(certificates_api):
    """Test deleting a certificate."""
    # First, create a certificate to delete
    cert_name = f"test-cert-delete-{uuid.uuid4().hex[:6]}"

    algorithm = CertificatesPostAlgorithm(
        rsa_number_of_bits=2048.0
    )

    cert = CertificatesPost(
        algorithm=algorithm,
        certificate_name=cert_name,
        common_name=f"{cert_name}.example.com",
        digest="sha256",
        signed_by="Root CA",
        folder=TARGET_FOLDER,
    )

    logger.info(f"Creating Certificate for delete test with name: {cert_name}")
    created_cert = perform(
        certificates_api.create_certificates,
        certificates_post=cert
    )

    assert created_cert is not None, "Create response should not be None"
    created_cert_id = created_cert.id
    assert created_cert_id is not None, "Created certificate ID should not be empty"
    logger.info(f"Created Certificate for Delete test with ID: {created_cert_id}")

    # Test Delete by ID operation
    logger.info(f"Attempting to delete Certificate with ID: {created_cert_id}")
    perform(
        certificates_api.delete_certificates_by_id,
        id=created_cert_id
    )
    logger.info(f"[SUCCESS] delete_certificates_by_id deleted certificate: {created_cert_id}")

    # Verify the certificate no longer exists
    fetched_cert = certificates_api.fetch_certificates(
        name=cert_name,
        folder=TARGET_FOLDER,
    )
    assert fetched_cert is None, "Certificate should not exist after deletion"
    logger.info("[SUCCESS] Verified certificate no longer exists after deletion")


def test_export_certificate(certificates_api):
    """Test exporting a certificate."""
    # First, create a certificate to export
    cert_name = f"test-cert-export-{uuid.uuid4().hex[:6]}"

    algorithm = CertificatesPostAlgorithm(
        rsa_number_of_bits=2048.0
    )

    cert = CertificatesPost(
        algorithm=algorithm,
        certificate_name=cert_name,
        common_name=f"{cert_name}.example.com",
        digest="sha256",
        signed_by="Root CA",
        folder=TARGET_FOLDER,
    )

    logger.info(f"Creating Certificate for export test with name: {cert_name}")
    created_cert = perform(
        certificates_api.create_certificates,
        certificates_post=cert
    )

    assert created_cert is not None, "Create response should not be None"
    created_cert_id = created_cert.id
    logger.info(f"Created Certificate for Export test with ID: {created_cert_id}")

    try:
        # Test Export operation
        logger.info(f"Attempting to export Certificate with ID: {created_cert_id}")
        export_payload = ExportCertificatePayload(
            format="pem",
            passphrase="Test@Passphrase123"
        )
        export_res = perform(
            certificates_api.export_certificate_by_id,
            id=created_cert_id,
            export_certificate_payload=export_payload
        )

        assert export_res is not None, "Export response should not be None"
        assert export_res.certificate is not None, "Exported certificate data should not be None"
        assert "-----BEGIN CERTIFICATE-----" in export_res.certificate, "Exported certificate should be in PEM format"
        logger.info(f"[SUCCESS] export_certificate_by_id exported certificate: {created_cert_id}")
    finally:
        # Cleanup
        logger.info(f"Cleaning up Certificate with ID: {created_cert_id}")
        try:
            perform(
                certificates_api.delete_certificates_by_id,
                id=created_cert_id
            )
        except Exception as e:
            logger.warning(f"Cleanup failed: {e}")


def test_import_certificate(certificates_api):
    """Test importing a certificate."""
    # Step 1: Create a certificate to export (so we have valid PEM content)
    cert_name = f"test-cert-for-import-{uuid.uuid4().hex[:6]}"

    algorithm = CertificatesPostAlgorithm(
        rsa_number_of_bits=2048.0
    )

    cert = CertificatesPost(
        algorithm=algorithm,
        certificate_name=cert_name,
        common_name=f"{cert_name}.example.com",
        digest="sha256",
        signed_by="Root CA",
        folder=TARGET_FOLDER,
    )

    logger.info(f"Creating source certificate for import test: {cert_name}")
    created_cert = perform(
        certificates_api.create_certificates,
        certificates_post=cert
    )

    assert created_cert is not None, "Create response should not be None"
    source_cert_id = created_cert.id
    logger.info(f"Created source certificate with ID: {source_cert_id}")

    imported_cert_name = None
    try:
        # Step 2: Export the certificate to get the PEM content
        export_payload = ExportCertificatePayload(
            format="pem",
            passphrase="Test@Passphrase123"
        )
        export_res = perform(
            certificates_api.export_certificate_by_id,
            id=source_cert_id,
            export_certificate_payload=export_payload
        )

        assert export_res is not None, "Export response should not be None"
        assert export_res.certificate is not None, "Exported certificate should not be None"

        exported_pem = export_res.certificate
        logger.info(f"Exported certificate PEM (length: {len(exported_pem)} bytes)")

        # Step 3: Parse the exported PEM to separate certificate and key
        cert_start = exported_pem.find("-----BEGIN CERTIFICATE-----")
        cert_end = exported_pem.find("-----END CERTIFICATE-----")
        if cert_start >= 0 and cert_end > cert_start:
            cert_pem = exported_pem[cert_start:cert_end + len("-----END CERTIFICATE-----")]
        else:
            pytest.fail("Failed to extract certificate from exported PEM")

        key_start = exported_pem.find("-----BEGIN ENCRYPTED PRIVATE KEY-----")
        key_end = exported_pem.find("-----END ENCRYPTED PRIVATE KEY-----")
        if key_start >= 0 and key_end > key_start:
            key_pem = exported_pem[key_start:key_end + len("-----END ENCRYPTED PRIVATE KEY-----")]
        else:
            pytest.fail("Failed to extract private key from exported PEM")

        logger.info(f"Extracted certificate ({len(cert_pem)} bytes) and key ({len(key_pem)} bytes)")

        # Base64 encode the certificate and key for import
        cert_base64 = base64.b64encode(cert_pem.encode()).decode()
        key_base64 = base64.b64encode(key_pem.encode()).decode()

        # Step 4: Import the certificate with a new name
        imported_cert_name = f"test-cert-imported-{uuid.uuid4().hex[:6]}"

        import_payload = CertificatesImport(
            name=imported_cert_name,
            certificate_file=cert_base64,
            format="pem",
            folder=TARGET_FOLDER,
            key_file=key_base64,
            passphrase="Test@Passphrase123",
        )

        logger.info(f"Attempting to import certificate with name: {imported_cert_name}")
        import_res = perform(
            certificates_api.import_certificates,
            certificates_import=import_payload
        )

        assert import_res is not None, "Import response should not be None"
        assert import_res.name == imported_cert_name, "Imported certificate name should match"
        logger.info(f"[SUCCESS] import_certificates imported certificate: {imported_cert_name}")

    finally:
        # Cleanup source certificate
        logger.info(f"Cleaning up source certificate with ID: {source_cert_id}")
        try:
            perform(
                certificates_api.delete_certificates_by_id,
                id=source_cert_id
            )
        except Exception as e:
            logger.warning(f"Source cleanup failed: {e}")

        # Cleanup imported certificate
        if imported_cert_name:
            fetched_cert = certificates_api.fetch_certificates(
                name=imported_cert_name,
                folder=TARGET_FOLDER,
            )
            if fetched_cert:
                logger.info(f"Cleaning up imported certificate with ID: {fetched_cert.id}")
                try:
                    perform(
                        certificates_api.delete_certificates_by_id,
                        id=fetched_cert.id
                    )
                except Exception as e:
                    logger.warning(f"Imported cert cleanup failed: {e}")
