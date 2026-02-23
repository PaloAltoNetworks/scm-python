import logging
import uuid
import pytest
from scm import Scm
from scm.network_services.models.dns_proxies import DnsProxies
from scm.network_services.models.dns_proxies_default import DnsProxiesDefault
from scm.test_helpers import perform

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "All"


@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")


@pytest.fixture(scope="module")
def dns_proxies_api(client):
    return client.network_services.DNSProxiesApi(client.network_services.api_client)


@pytest.fixture
def clean_dns_proxy(dns_proxies_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-dnsproxy-{random_id}"

    payload = DnsProxies(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        default=DnsProxiesDefault(
            primary="8.8.8.8",
            secondary="8.8.4.4",
        ),
        enabled=True,
    )

    logger.info(f"\n[SETUP] Creating DNS Proxy: {object_name}")
    created_obj = perform(
        dns_proxies_api.create_dns_proxies_with_http_info,
        response_type=DnsProxies,
        dns_proxies=payload,
    )
    assert created_obj.id is not None
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting DNS Proxy ID: {created_obj.id}")
    try:
        dns_proxies_api.delete_dns_proxies_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_dns_proxy(dns_proxies_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-dnsproxy-create-{random_id}"

    payload = DnsProxies(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        default=DnsProxiesDefault(
            primary="8.8.8.8",
            secondary="8.8.4.4",
        ),
        enabled=True,
    )

    created_obj = perform(
        dns_proxies_api.create_dns_proxies_with_http_info,
        response_type=DnsProxies,
        dns_proxies=payload,
    )
    assert created_obj.id is not None
    assert created_obj.name == object_name

    # Cleanup
    dns_proxies_api.delete_dns_proxies_by_id(id=created_obj.id)


def test_get_dns_proxy_by_id(dns_proxies_api, clean_dns_proxy):
    fetched_obj = dns_proxies_api.get_dns_proxies_by_id(id=clean_dns_proxy.id)
    assert fetched_obj.id == clean_dns_proxy.id
    assert fetched_obj.name == clean_dns_proxy.name


def test_update_dns_proxy(dns_proxies_api, clean_dns_proxy):
    update_payload = clean_dns_proxy
    update_payload.default = DnsProxiesDefault(
        primary="1.1.1.1",
        secondary="1.0.0.1",
    )
    update_payload.enabled = False

    updated_obj = dns_proxies_api.update_dns_proxies_by_id(
        id=clean_dns_proxy.id,
        dns_proxies=update_payload,
    )

    assert updated_obj.id == clean_dns_proxy.id
    assert updated_obj.default.primary == "1.1.1.1"


def test_list_dns_proxies(dns_proxies_api, clean_dns_proxy):
    response = dns_proxies_api.list_dns_proxies(folder=TARGET_FOLDER, limit=200)
    assert response is not None
    assert len(response.data) > 0

    found = False
    for item in response.data:
        if item.id == clean_dns_proxy.id:
            found = True
            break
    assert found is True


def test_fetch_dns_proxies(dns_proxies_api, clean_dns_proxy):
    fetched_obj = dns_proxies_api.fetch_dns_proxies(
        name=clean_dns_proxy.name,
        folder=TARGET_FOLDER,
    )
    assert fetched_obj is not None
    assert fetched_obj.id == clean_dns_proxy.id
    assert fetched_obj.name == clean_dns_proxy.name
    logger.info(f"\n[SUCCESS] fetch_dns_proxies found object: {fetched_obj.name}")

    not_found = dns_proxies_api.fetch_dns_proxies(
        name="non-existent-dns-proxy-xyz-12345",
        folder=TARGET_FOLDER,
    )
    assert not_found is None
    logger.info(f"\n[SUCCESS] fetch_dns_proxies correctly returned None for non-existent object")


def test_delete_dns_proxy_by_id(dns_proxies_api):
    random_id = uuid.uuid4().hex[:6]
    object_name = f"test-dnsproxy-del-{random_id}"

    payload = DnsProxies(
        id="",
        name=object_name,
        folder=TARGET_FOLDER,
        default=DnsProxiesDefault(
            primary="8.8.8.8",
        ),
    )

    created_obj = perform(
        dns_proxies_api.create_dns_proxies_with_http_info,
        response_type=DnsProxies,
        dns_proxies=payload,
    )

    dns_proxies_api.delete_dns_proxies_by_id(id=created_obj.id)

    from scm.exceptions import ObjectNotPresentError
    try:
        dns_proxies_api.get_dns_proxies_by_id(id=created_obj.id)
        pytest.fail("DNS Proxy should be deleted")
    except ObjectNotPresentError:
        logger.info("Correctly raised ObjectNotPresentError for deleted object")
