
import logging
import uuid
import pytest
from scm import Scm
from scm.config_setup.models.variables import Variables
from scm.test_helpers import perform

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
TARGET_FOLDER = "All"
# -----------------------------------------------------------------------------

@pytest.fixture(scope="module")
def client():
    """
    Fixture to initialize the SCM client once for the module.
    """
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def variables_api(client):
    """
    Fixture to return the Variables API instance.
    """
    return client.config_setup.VariablesApi(client.config_setup.api_client)

@pytest.fixture
def clean_variable(variables_api):
    """
    Fixture to create a temporary Variable for testing and automatically delete it after.
    """
    # 1. SETUP: Create Variable
    random_id = uuid.uuid4().hex[:6]
    variable_name = f"$test-var-{random_id}"

    payload = Variables(
        id="",
        name=variable_name,
        folder=TARGET_FOLDER,
        type="ip-netmask",
        value="10.0.0.1/32",
        description="Created via Automated Pytest Fixture"
    )

    logger.info(f"\n[SETUP] Creating Variable: {variable_name}")
    created_obj = perform(
        variables_api.create_variable_with_http_info,
        response_type=Variables,
        variables=payload
    )
    assert created_obj.id is not None

    # Pass control to the test function
    yield created_obj

    # 2. TEARDOWN: Delete Variable
    logger.info(f"\n[TEARDOWN] Deleting Variable ID: {created_obj.id}")
    try:
        perform(
            variables_api.delete_variable_by_id,
            id=created_obj.id
        )
    except Exception as e:
        logger.info(f"Teardown failed (might have been deleted in test): {e}")


def test_create_variable(variables_api):
    """
    Test manual creation and deletion of a variable object.
    Equivalent to Go: Test_config_setup_VariablesAPIService_Create
    """
    random_suffix = uuid.uuid4().hex[:6]
    variable_name = f"$test-var-create-{random_suffix}"

    payload = Variables(
        id="",
        name=variable_name,
        folder=TARGET_FOLDER,
        type="fqdn",
        value="example.com",
        description="Test variable for create API testing"
    )

    # Create using perform helper
    created_obj = perform(
        variables_api.create_variable_with_http_info,
        response_type=Variables,
        variables=payload
    )

    # Verify
    assert created_obj.name == variable_name
    assert created_obj.id is not None
    assert created_obj.folder == TARGET_FOLDER
    assert created_obj.type == "fqdn"
    assert created_obj.value == "example.com"
    assert created_obj.description == "Test variable for create API testing"

    # Cleanup
    perform(
        variables_api.delete_variable_by_id,
        id=created_obj.id
    )


def test_get_variable_by_id(variables_api, clean_variable):
    """
    Test retrieving a variable by ID.
    Equivalent to Go: Test_config_setup_VariablesAPIService_GetByID
    """
    # Retrieve using perform helper
    fetched_obj = perform(
        variables_api.get_variable_by_id,
        response_type=Variables,
        id=clean_variable.id
    )

    # Verify
    assert fetched_obj.id == clean_variable.id
    assert fetched_obj.name == clean_variable.name
    assert fetched_obj.folder == clean_variable.folder
    assert fetched_obj.type == clean_variable.type
    assert fetched_obj.value == clean_variable.value


def test_update_variable(variables_api, clean_variable):
    """
    Test updating an existing variable.
    Equivalent to Go: Test_config_setup_VariablesAPIService_Update
    """
    # Prepare Update Payload
    update_payload = clean_variable
    update_payload.description = "Updated test variable description"
    update_payload.value = "192.168.1.1/32"

    # Perform Update using helper
    updated_obj = perform(
        variables_api.update_variable_by_id,
        response_type=Variables,
        id=clean_variable.id,
        variables=update_payload
    )

    # Verify
    assert updated_obj.id == clean_variable.id
    assert updated_obj.name == clean_variable.name
    assert updated_obj.description == "Updated test variable description"
    assert updated_obj.value == "192.168.1.1/32"
    assert updated_obj.type == clean_variable.type


def test_list_variables(variables_api, clean_variable):
    """
    Test listing variables with folder filter.
    Equivalent to Go: Test_config_setup_VariablesAPIService_List
    """
    # List with folder filter using perform helper
    response = perform(
        variables_api.list_variables,
        folder=TARGET_FOLDER,
        limit=10000
    )

    assert response is not None
    assert len(response.data) > 0

    # Verify our created object is in the list
    found = False
    for item in response.data:
        if item.name == clean_variable.name:
            found = True
            break

    assert found is True
    logger.info(f"\n[SUCCESS] List returned {len(response.data)} items.")




def test_fetch_variables(variables_api, clean_variable):
    """
    Test fetching a single variables by name using the fetch convenience method.
    Equivalent to pan-scm-sdk's fetch() method.
    """
    # Fetch by exact name
    fetched_obj = variables_api.fetch_variables(
        name=clean_variable.name,
        folder=clean_variable.folder
    )

    # Verify
    assert fetched_obj is not None, f"Should have found variables '{clean_variable.name}'"
    assert fetched_obj.id == clean_variable.id
    assert fetched_obj.name == clean_variable.name
    assert fetched_obj.folder == clean_variable.folder
    logger.info(f"\n[SUCCESS] fetch_variables found object: {fetched_obj.name}")

    # Test fetching non-existent variables (should return None)
    not_found = variables_api.fetch_variables(
        name="non-existent-variables-xyz-12345",
        folder=clean_variable.folder
    )
    assert not_found is None, "Should return None for non-existent variables"
    logger.info(f"\n[SUCCESS] fetch_variables correctly returned None for non-existent variables")


def test_delete_variable_by_id(variables_api):
    """
    Test deletion specifically.
    Equivalent to Go: Test_config_setup_VariablesAPIService_DeleteByID
    """
    # Setup
    random_suffix = uuid.uuid4().hex[:6]
    variable_name = f"$test-var-delete-{random_suffix}"

    payload = Variables(
        id="",
        name=variable_name,
        folder=TARGET_FOLDER,
        type="port",
        value="8080",
        description="Test variable for delete API testing"
    )
    created_obj = perform(
        variables_api.create_variable_with_http_info,
        response_type=Variables,
        variables=payload
    )

    # Perform Delete using helper
    perform(
        variables_api.delete_variable_by_id,
        id=created_obj.id
    )

    # Verify Deletion (Expect ObjectNotPresentError on Get)
    from scm.exceptions import ObjectNotPresentError
    # Decorator already converts NotFoundException to ObjectNotPresentError

    try:
        variables_api.get_variable_by_id(id=created_obj.id)
        pytest.fail("Variable should have been deleted but was found.")
    except ObjectNotPresentError as e:
        # Exception is already parsed by decorator
        logger.info(f"✅ Correctly raised ObjectNotPresentError for deleted object")
        logger.info(f"   Object ID: {created_obj.id}")
