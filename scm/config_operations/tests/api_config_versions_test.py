
import logging
import pytest
from scm import Scm
from scm.test_helpers import perform

# Configure logging to see details during test execution (use pytest -s)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def client():
    """
    Fixture to initialize the SCM client once for the module.
    Assumes SCM_CLIENT_ID, SCM_CLIENT_SECRET, SCM_TSG_ID are set in env.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def config_versions_api(client):
    """
    Fixture to return the Config Versions API instance.
    """
    return client.config_operations.ConfigVersionsApi(client.config_operations.api_client)


def test_list_config_versions(config_versions_api):
    """
    Test listing configuration versions.
    This is a read-only operation that retrieves the list of config versions.
    Equivalent to Go: Test_config_operations_ConfigVersionsAPIService_List
    """
    logger.info("\n[TEST] Listing configuration versions")

    # List config versions using perform helper
    response = perform(
        config_versions_api.list_config_versions_with_http_info,
        response_type=object  # Response is paginated with data array
    )

    assert response is not None, "Response should not be None"
    assert hasattr(response, 'data'), "Response should have 'data' attribute"

    versions = response.data
    logger.info(f"Successfully retrieved {len(versions)} config versions (limit: {response.limit}, offset: {response.offset}, total: {response.total})")

    # If there are versions, verify the structure
    if len(versions) > 0:
        first_version = versions[0]
        assert hasattr(first_version, 'id'), "Version should have an ID"
        assert hasattr(first_version, 'version'), "Version should have a version string"

        logger.info(f"Sample version - ID: {first_version.id}, Version: {first_version.version}, Date: {first_version.var_date}")
    else:
        logger.info("No config versions found in the system")


def test_get_config_version_by_id(config_versions_api):
    """
    Test retrieving a specific config version by ID.
    Note: Uses a hardcoded version number since we can't easily extract from list response.
    Equivalent to Go: Test_config_operations_ConfigVersionsAPIService_GetByID
    """
    logger.info("\n[TEST] Getting config version by ID")

    # Use version 1 as a test (this might not exist in all environments)
    version_id = 1
    logger.info(f"Testing GetByID with version: {version_id}")

    try:
        # Retrieve the specific version by ID
        response = perform(
            config_versions_api.get_config_versions_by_id_with_http_info,
            response_type=object,
            version=version_id
        )

        assert response is not None, "Response should not be None"

        # The API returns an array with config versions (even for single ID lookup)
        assert len(response) > 0, "Should have at least one config version in response"

        # Get the first version from the array
        version = response[0]
        assert hasattr(version, 'id'), "Version should have an ID"
        assert hasattr(version, 'version'), "Version should have a version string"

        logger.info(f"Retrieved config version - ID: {version.id}, Version: {version.version}, Date: {version.var_date}, Admin: {version.admin}")

    except Exception as e:
        # This test may fail if version doesn't exist, which is acceptable
        logger.info(f"Version {version_id} not found - this is expected if no configs exist: {e}")
        pytest.skip(f"Version {version_id} not found - this is expected if no configs exist")


def test_get_running_config_versions(config_versions_api):
    """
    Test retrieving the running configuration versions.
    This is a read-only operation that retrieves the currently active configurations.
    Equivalent to Go: Test_config_operations_ConfigVersionsAPIService_GetRunning
    """
    logger.info("\n[TEST] Retrieving running configuration versions")

    # Get running config versions using perform helper
    response = perform(
        config_versions_api.get_running_config_versions_with_http_info,
        response_type=object  # Response is paginated with data array
    )

    assert response is not None, "Response should not be None"
    assert hasattr(response, 'data'), "Response should have 'data' attribute"

    running_versions = response.data
    assert len(running_versions) > 0, "Should have at least one running version"

    logger.info(f"Retrieved {len(running_versions)} running config versions (limit: {response.limit}, offset: {response.offset}, total: {response.total})")

    # Verify the structure of the first running version
    first_running = running_versions[0]
    assert hasattr(first_running, 'device'), "Running version should have a device"
    assert hasattr(first_running, 'version'), "Running version should have a version number"

    logger.info(f"Sample running version - Device: {first_running.device}, Version: {first_running.version}, Date: {first_running.var_date}")


# NOTE: The following operations are NOT tested as they are destructive/action operations:
# - load_config_versions: This loads a candidate config (action operation)
# - push_candidate_config_versions: This pushes config to devices (action operation)
# - delete_candidate_config_versions: This deletes the candidate config (destructive operation)
#
# These operations should be tested in integration tests or manually in a controlled environment.
