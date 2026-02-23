
import logging
import pytest
from scm import Scm
from scm.security_services.models.saas_tenant_restrictions import SaasTenantRestrictions

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def saas_tenant_restrictions_api(client):
    return client.security_services.SaasTenantRestrictionsApi(client.security_services.api_client)


def test_get_saas_tenant_restrictions(saas_tenant_restrictions_api):
    """
    Test retrieving SaaS tenant restrictions using snippet=office365 scope.
    Equivalent to Go: Test_security_services_SaasTenantRestrictionsAPIService_Get
    """
    response = saas_tenant_restrictions_api.get_saas_tenant_restrictions(
        snippet="office365",
        limit=200,
        offset=0,
    )

    assert response is not None
    logger.info(f"Successfully retrieved SaaS tenant restrictions (total: {response.total})")


def test_update_saas_tenant_restrictions(saas_tenant_restrictions_api):
    """
    Test updating SaaS tenant restrictions with a no-op update.
    Gets existing restriction via Get, then performs no-op update with same data.
    Equivalent to Go: Test_security_services_SaasTenantRestrictionsAPIService_Update
    """
    # Get existing restrictions with office365 snippet scope
    response = saas_tenant_restrictions_api.get_saas_tenant_restrictions(
        snippet="office365",
        limit=200,
        offset=0,
    )
    assert response is not None

    if not response.data or len(response.data) == 0:
        pytest.skip("No SaaS tenant restrictions found in office365 snippet to test Update")

    # Perform no-op update with existing restriction data
    existing = response.data[0]
    logger.info(f"Updating existing restriction: {existing.name}")

    updated = saas_tenant_restrictions_api.update_saas_tenant_restrictions(
        snippet="office365",
        saas_tenant_restrictions=existing,
    )

    assert updated is not None
    logger.info(f"Successfully updated SaaS tenant restrictions (no-op)")
