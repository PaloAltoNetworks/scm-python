
import logging
import uuid
import pytest
from scm import Scm

from scm.network_services.models import (
    QosProfiles,
    QosProfilesClassBandwidthType,
    QosProfilesClassBandwidthTypeMbps,
    QosProfilesClassBandwidthTypeMbpsClassInner,
    QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth,
    QosProfilesAggregateBandwidth
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TARGET_FOLDER = "Service Connections"

@pytest.fixture(scope="module")
def client():
    try:
        return Scm(log_level="DEBUG")
    except Exception as e:
        pytest.skip(f"Skipping tests due to client initialization failure: {e}")

@pytest.fixture(scope="module")
def qos_profiles_api(client):
    return client.network_services.QoSProfilesApi(client.network_services.api_client)

def create_qos_profile_payload(name_prefix):
    """Helper to create a QoS Profile payload."""
    random_id = uuid.uuid4().hex[:6]
    name = f"{name_prefix}{random_id}"
    
    # Define Bandwidth Classes
    test_classes = [
        QosProfilesClassBandwidthTypeMbpsClassInner(
            name="class1",
            priority="low"
        ),
        QosProfilesClassBandwidthTypeMbpsClassInner(
            name="class2",
            priority="real-time",
            class_bandwidth=QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth(
                egress_guaranteed=10,
                egress_max=20
            )
        ),
        QosProfilesClassBandwidthTypeMbpsClassInner(
            name="class3",
            priority="high",
            class_bandwidth=QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth(
                egress_guaranteed=1000,
                egress_max=10000
            )
        )
    ]

    return QosProfiles(
        name=name,
        folder=TARGET_FOLDER,
        class_bandwidth_type=QosProfilesClassBandwidthType(
            mbps=QosProfilesClassBandwidthTypeMbps(var_class=test_classes) # 'class' -> 'var_class'
        ),
        aggregate_bandwidth=QosProfilesAggregateBandwidth(
            egress_guaranteed=300,
            egress_max=1000
        )
    )

@pytest.fixture
def clean_qos_profile(qos_profiles_api):
    """Fixture for standard CRUD tests."""
    payload = create_qos_profile_payload("qos-get-")
    # Simplify payload for generic tests if needed, but using full one is fine
    
    logger.info(f"\n[SETUP] Creating QoS Profile: {payload.name}")
    created_obj = qos_profiles_api.create_qo_s_profiles(qos_profiles=payload)
    yield created_obj

    logger.info(f"\n[TEARDOWN] Deleting QoS Profile ID: {created_obj.id}")
    try:
        qos_profiles_api.delete_qo_s_profiles_by_id(id=created_obj.id)
    except Exception as e:
        logger.info(f"Teardown failed: {e}")


def test_create_qos_profile(qos_profiles_api):
    """Test creation of a QoS Profile."""
    payload = create_qos_profile_payload("qos-create-")

    try:
        created_obj = qos_profiles_api.create_qo_s_profiles(qos_profiles=payload)
    except Exception as e:
        if hasattr(e, 'body'):
            print(f"\n[ERROR] API Response Body: {e.body}")
        raise e

    assert created_obj.id is not None
    assert created_obj.name == payload.name
    assert len(created_obj.class_bandwidth_type.mbps.var_class) == 3

    # Cleanup
    qos_profiles_api.delete_qo_s_profiles_by_id(id=created_obj.id)


def test_get_qos_profile_by_id(qos_profiles_api, clean_qos_profile):
    """Test retrieving a QoS Profile by ID."""
    fetched_obj = qos_profiles_api.get_qo_s_profiles_by_id(id=clean_qos_profile.id)
    assert fetched_obj.id == clean_qos_profile.id
    assert fetched_obj.name == clean_qos_profile.name


def test_update_qos_profile(qos_profiles_api, clean_qos_profile):
    """Test updating a QoS Profile."""
    update_payload = clean_qos_profile
    update_payload.aggregate_bandwidth.egress_max = 200
    
    updated_obj = qos_profiles_api.update_qo_s_profiles_by_id(
        id=clean_qos_profile.id,
        qos_profiles=update_payload
    )
    
    assert updated_obj.id == clean_qos_profile.id
    assert updated_obj.aggregate_bandwidth.egress_max == 200


def test_list_qos_profiles(qos_profiles_api, clean_qos_profile):
    """Test listing QoS Profiles."""
    response = qos_profiles_api.list_qo_s_profiles(folder=TARGET_FOLDER, limit=100)
    assert len(response.data) > 0
    
    found = False
    for item in response.data:
        if item.id == clean_qos_profile.id:
            found = True
            break
    assert found is True


def test_delete_qos_profile_by_id(qos_profiles_api):
    """Test deleting a QoS Profile."""
    payload = create_qos_profile_payload("qos-del-")
    created_obj = qos_profiles_api.create_qo_s_profiles(qos_profiles=payload)
    
    qos_profiles_api.delete_qo_s_profiles_by_id(id=created_obj.id)
    
    try:
        qos_profiles_api.get_qo_s_profiles_by_id(id=created_obj.id)
        pytest.fail("Profile should be deleted")
    except Exception as e:
        assert "404" in str(e) or "Not Found" in str(e)
