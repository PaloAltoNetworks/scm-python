
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
def jobs_api(client):
    """
    Fixture to return the Jobs API instance.
    """
    return client.config_operations.JobsApi(client.config_operations.api_client)


def test_list_jobs(jobs_api):
    """
    Test listing configuration jobs.
    This is a read-only operation that retrieves the current list of jobs.
    Equivalent to Go: Test_config_operations_JobsAPIService_List
    """
    logger.info("\n[TEST] Listing configuration jobs")

    # List jobs using perform helper
    response = perform(
        jobs_api.list_jobs_with_http_info,
        response_type=object  # Response is JobsListResponse with data array
    )

    assert response is not None, "Response should not be None"
    assert hasattr(response, 'data'), "Response should have 'data' attribute"

    jobs = response.data
    logger.info(f"Successfully retrieved {len(jobs)} jobs (limit: {response.limit}, offset: {response.offset}, total: {response.total})")

    # If there are jobs, verify the structure
    if len(jobs) > 0:
        first_job = jobs[0]
        assert hasattr(first_job, 'id'), "Job should have an ID"
        assert hasattr(first_job, 'job_type'), "Job should have a job_type"
        assert hasattr(first_job, 'status_str'), "Job should have a status_str"

        logger.info(f"Sample job - ID: {first_job.id}, Type: {first_job.job_type}, Status: {first_job.status_str}")
    else:
        logger.info("No jobs found in the system")


def test_get_job_by_id(jobs_api):
    """
    Test retrieving a specific job by ID.
    First lists jobs to find a valid ID, then retrieves that specific job.
    Equivalent to Go: Test_config_operations_JobsAPIService_GetByID
    """
    logger.info("\n[TEST] Getting job by ID")

    # First, list jobs to get a valid job ID
    list_response = perform(
        jobs_api.list_jobs_with_http_info,
        response_type=object
    )

    assert list_response is not None
    jobs = list_response.data

    # Skip test if no jobs exist
    if len(jobs) == 0:
        pytest.skip("No jobs available to test GetByID - skipping test")
        return

    # Get the first job's ID (string type)
    job_id = jobs[0].id
    logger.info(f"Retrieving job with ID: {job_id}")

    # Retrieve the specific job by ID
    response = perform(
        jobs_api.get_jobs_by_id_with_http_info,
        response_type=object,
        id=job_id
    )

    assert response is not None, "Response should not be None"
    assert hasattr(response, 'data'), "Response should have 'data' attribute"

    # Get the data - API returns array with jobs
    retrieved_jobs = response.data
    assert len(retrieved_jobs) > 0, "Should have at least one job in response"

    # Verify we got the job we requested
    found_job = retrieved_jobs[0]
    assert found_job.id == job_id, f"Retrieved job ID should match requested ID: {job_id}"

    logger.info(f"Successfully retrieved job - ID: {found_job.id}, Type: {found_job.job_type}, Status: {found_job.status_str}")
