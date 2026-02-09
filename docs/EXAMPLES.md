# SCM Python SDK - Usage Examples

This guide provides practical examples for common use cases across different service categories.

## Table of Contents

- [Client Initialization](#client-initialization)
- [Objects Service](#objects-service)
  - [Addresses](#addresses)
  - [Address Groups](#address-groups)
  - [Services](#services)
  - [Service Groups](#service-groups)
  - [Tags](#tags)
  - [Application Groups](#application-groups)
- [Security Services](#security-services)
  - [Security Rules](#security-rules)
  - [Decryption Rules](#decryption-rules)
  - [Anti-Spyware Profiles](#anti-spyware-profiles)
  - [Vulnerability Protection Profiles](#vulnerability-protection-profiles)
- [Network Services](#network-services)
  - [IKE Gateways](#ike-gateways)
  - [IPSec Tunnels](#ipsec-tunnels)
  - [QoS Profiles](#qos-profiles)
- [Identity Services](#identity-services)
  - [LDAP Server Profiles](#ldap-server-profiles)
  - [SAML Server Profiles](#saml-server-profiles)
- [Deployment Services](#deployment-services)
  - [Remote Networks](#remote-networks)
  - [Service Connections](#service-connections)
- [Error Handling](#error-handling)
- [Pagination](#pagination)
- [Bulk Operations](#bulk-operations)

---

## Client Initialization

### Basic Initialization

```python
from scm import Scm

# Initialize with environment variables (SCM_CLIENT_ID, SCM_CLIENT_SECRET, SCM_TSG_ID)
client = Scm()
```

### Custom Configuration

```python
from scm import Scm

# Initialize with explicit credentials
client = Scm(
    client_id="your_client_id",
    client_secret="your_client_secret",
    tsg_id="your_tsg_id",
    log_level="DEBUG"
)
```

### Token Caching (for concurrent operations)

```python
from scm import Scm

# Enable file-based token caching for multiple processes
client = Scm(
    client_id="your_client_id",
    client_secret="your_client_secret",
    tsg_id="your_tsg_id",
    token_file="/tmp/scm_token_cache.json"
)
```

---

## Objects Service

### Addresses

#### Create an Address

```python
from scm.objects.models.addresses import Addresses

# Get API instance
addresses_api = client.objects.AddressesApi(client.objects.api_client)

# Create IP netmask address
ip_address = Addresses(
    id="",
    name="web-server-01",
    folder="Texas",
    ip_netmask="192.168.1.10/32",
    description="Production web server",
    tag=["Production", "Web"]
)

created = addresses_api.create_addresses(addresses=ip_address)
print(f"Created address: {created.name} (ID: {created.id})")
```

#### Create FQDN Address

```python
fqdn_address = Addresses(
    id="",
    name="api-endpoint",
    folder="Texas",
    fqdn="api.example.com",
    description="External API endpoint"
)

created = addresses_api.create_addresses(addresses=fqdn_address)
```

#### Create IP Range Address

```python
range_address = Addresses(
    id="",
    name="dhcp-pool",
    folder="Texas",
    ip_range="192.168.100.50-192.168.100.200",
    description="DHCP address pool"
)

created = addresses_api.create_addresses(addresses=range_address)
```

#### Fetch Address by Name

```python
# Fetch single address by name (with auto-pagination)
address = addresses_api.fetch_addresses(
    name="web-server-01",
    folder="Texas"
)

if address:
    print(f"Found: {address.name} - {address.ip_netmask}")
else:
    print("Address not found")
```

#### List All Addresses

```python
# List with pagination
response = addresses_api.list_addresses(
    folder="Texas",
    limit=100,
    offset=0
)

print(f"Total addresses: {response.total}")
for addr in response.data:
    print(f"  - {addr.name}: {addr.ip_netmask or addr.fqdn or addr.ip_range}")
```

#### Update Address

```python
# Get existing address
address = addresses_api.fetch_addresses(name="web-server-01", folder="Texas")

# Modify fields
address.ip_netmask = "192.168.1.20/32"
address.description = "Migrated web server"

# Update
updated = addresses_api.update_addresses_by_id(
    id=address.id,
    addresses=address
)
print(f"Updated: {updated.name}")
```

#### Delete Address

```python
from scm.exceptions import ObjectNotPresentError

try:
    addresses_api.delete_addresses_by_id(id=address.id)
    print(f"Deleted address: {address.id}")
except ObjectNotPresentError:
    print("Address already deleted or not found")
```

---

### Address Groups

#### Create Static Address Group

```python
from scm.objects.models.address_groups import AddressGroups

address_groups_api = client.objects.AddressGroupsApi(client.objects.api_client)

# Create static group
static_group = AddressGroups(
    id="",
    name="web-servers",
    folder="Texas",
    static=["web-server-01", "web-server-02", "web-server-03"],
    description="All production web servers",
    tag=["Production"]
)

created = address_groups_api.create_address_groups(address_groups=static_group)
print(f"Created group: {created.name}")
```

#### Create Dynamic Address Group

```python
# Create dynamic group using tags
dynamic_group = AddressGroups(
    id="",
    name="production-servers",
    folder="Texas",
    dynamic={"filter": "'Production'"},
    description="All servers tagged as Production"
)

created = address_groups_api.create_address_groups(address_groups=dynamic_group)
```

#### Add Members to Group

```python
# Fetch existing group
group = address_groups_api.fetch_address_groups(
    name="web-servers",
    folder="Texas"
)

# Add new member
if group.static:
    group.static.append("web-server-04")

    updated = address_groups_api.update_address_groups_by_id(
        id=group.id,
        address_groups=group
    )
    print(f"Added member to group: {updated.name}")
```

---

### Services

#### Create TCP Service

```python
from scm.objects.models.services import Services
from scm.objects.models.services_protocol import ServicesProtocol
from scm.objects.models.services_protocol_tcp import ServicesProtocolTcp

services_api = client.objects.ServicesApi(client.objects.api_client)

# Create TCP service
protocol = ServicesProtocol(
    tcp=ServicesProtocolTcp(
        port="8080",
        override_timeout=3600
    )
)

web_service = Services(
    id="",
    name="web-app-8080",
    folder="Texas",
    protocol=protocol,
    description="Custom web application service",
    tag=["Web"]
)

created = services_api.create_services(services=web_service)
print(f"Created service: {created.name}")
```

#### Create UDP Service

```python
from scm.objects.models.services_protocol_udp import ServicesProtocolUdp

protocol = ServicesProtocol(
    udp=ServicesProtocolUdp(
        port="5060",
        override_timeout=300
    )
)

sip_service = Services(
    id="",
    name="sip-custom",
    folder="Texas",
    protocol=protocol,
    description="SIP service"
)

created = services_api.create_services(services=sip_service)
```

#### Create Service with Port Range

```python
protocol = ServicesProtocol(
    tcp=ServicesProtocolTcp(
        port="8000-8100"
    )
)

app_service = Services(
    id="",
    name="app-range",
    folder="Texas",
    protocol=protocol,
    description="Application port range"
)

created = services_api.create_services(services=app_service)
```

---

### Service Groups

#### Create Service Group

```python
from scm.objects.models.service_groups import ServiceGroups

service_groups_api = client.objects.ServiceGroupsApi(client.objects.api_client)

web_services_group = ServiceGroups(
    id="",
    name="web-services-all",
    folder="Texas",
    members=["web-app-8080", "service-http", "service-https"],
    tag=["Web"]
)

created = service_groups_api.create_service_groups(service_groups=web_services_group)
print(f"Created service group: {created.name}")
```

---

### Tags

#### Create Tags

```python
from scm.objects.models.tags import Tags


tags_api = client.objects.TagsApi(client.objects.api_client)

# Create production tag
production_tag = Tags(
    id="",
    name="Production",
    folder="Texas",
    color="Red",
    comments="Production environment resources"
)

created = tags_api.create_tags(tags=production_tag)
print(f"Created tag: {created.name}")

# Create development tag
dev_tag = Tags(
    id="",
    name="Development",
    folder="Texas",
    color="Green",
    comments="Development environment resources"
)

created = tags_api.create_tags(tags=dev_tag)
```

---

### Application Groups

#### Create Application Group

```python
from scm.objects.models.application_groups import ApplicationGroups

app_groups_api = client.objects.ApplicationGroupsApi(client.objects.api_client)

web_apps = ApplicationGroups(
    id="",
    name="web-applications",
    folder="Texas",
    members=["ssl", "web-browsing", "sharepoint-base"],
    tag=["Business-Critical"]
)

created = app_groups_api.create_application_groups(application_groups=web_apps)
print(f"Created application group: {created.name}")
```

---

## Security Services

### Security Rules

#### Create Basic Security Rule

```python
from scm.security_services.models.security_rules import SecurityRules

security_rules_api = client.security_services.SecurityRulesApi(client.security_services.api_client)

basic_rule = SecurityRules(
    id="",
    name="allow-web-traffic",
    folder="Texas",
    position="pre",
    source=["Trust-Zone"],
    source_user=["any"],
    destination=["Untrust-Zone"],
    application=["web-browsing", "ssl"],
    service=["application-default"],
    action="allow",
    log_setting="Cortex Data Lake",
    description="Allow web browsing from trust zone"
)

created = security_rules_api.create_security_rules(security_rules=basic_rule)
print(f"Created security rule: {created.name}")
```

#### Create Rule with Security Profiles

```python
rule_with_profiles = SecurityRules(
    id="",
    name="allow-web-with-protection",
    folder="Texas",
    position="pre",
    source=["Trust-Zone"],
    source_user=["any"],
    destination=["Untrust-Zone"],
    application=["web-browsing", "ssl"],
    service=["application-default"],
    action="allow",
    profile_setting={
        "group": ["best-practice"]
    },
    log_setting="Cortex Data Lake",
    description="Allow web traffic with security profiles"
)

created = security_rules_api.create_security_rules(security_rules=rule_with_profiles)
```

#### Create Deny Rule

```python
deny_rule = SecurityRules(
    id="",
    name="block-p2p",
    folder="Texas",
    position="pre",
    source=["any"],
    source_user=["any"],
    destination=["any"],
    application=["bittorrent", "gnutella"],
    service=["application-default"],
    action="deny",
    log_setting="Cortex Data Lake",
    description="Block peer-to-peer applications"
)

created = security_rules_api.create_security_rules(security_rules=deny_rule)
```

#### Move Rule Position

```python
from scm.security_services.models.rule_move_post_request import RuleMovePostRequest

# Move rule to specific position
move_request = RuleMovePostRequest(
    destination="top",
    rulebase="pre"
)

security_rules_api.move_security_rules_by_id(
    id=created.id,
    rule_move_post_request=move_request
)
print(f"Moved rule to top of rulebase")
```

---

### Decryption Rules

#### Create SSL Forward Proxy Rule

```python
from scm.security_services.models.decryption_rules import DecryptionRules

decryption_rules_api = client.security_services.DecryptionRulesApi(client.security_services.api_client)

ssl_forward_proxy = DecryptionRules(
    id="",
    name="decrypt-outbound-web",
    folder="Texas",
    position="pre",
    source=["Trust-Zone"],
    source_user=["any"],
    destination=["Untrust-Zone"],
    category=["any"],
    service=["service-https"],
    action="decrypt",
    type="ssl-forward-proxy",
    description="Decrypt outbound HTTPS traffic"
)

created = decryption_rules_api.create_decryption_rules(decryption_rules=ssl_forward_proxy)
print(f"Created decryption rule: {created.name}")
```

#### Create No-Decrypt Rule

```python
no_decrypt_rule = DecryptionRules(
    id="",
    name="no-decrypt-financial",
    folder="Texas",
    position="pre",
    source=["Trust-Zone"],
    source_user=["any"],
    destination=["any"],
    category=["financial-services"],
    service=["service-https"],
    action="no-decrypt",
    type="ssl-forward-proxy",
    description="Do not decrypt financial services traffic"
)

created = decryption_rules_api.create_decryption_rules(decryption_rules=no_decrypt_rule)
```

---

### Anti-Spyware Profiles

#### Create Anti-Spyware Profile

```python
from scm.security_services.models.anti_spyware_profiles import AntiSpywareProfiles
from scm.security_services.models.anti_spyware_profiles_rules_inner import AntiSpywareProfilesRulesInner

anti_spyware_api = client.security_services.AntiSpywareProfilesApi(client.security_services.api_client)

# Define rules
rules = [
    AntiSpywareProfilesRulesInner(
        name="critical-severity",
        severity=["critical"],
        action={"reset_both": {}},
        category="any",
        threat_name="any"
    ),
    AntiSpywareProfilesRulesInner(
        name="high-severity",
        severity=["high"],
        action={"alert": {}},
        category="any",
        threat_name="any"
    )
]

profile = AntiSpywareProfiles(
    id="",
    name="strict-anti-spyware",
    folder="Texas",
    rules=rules,
    description="Strict anti-spyware policy"
)

created = anti_spyware_api.create_anti_spyware_profiles(anti_spyware_profiles=profile)
print(f"Created anti-spyware profile: {created.name}")
```

---

### Vulnerability Protection Profiles

#### Create Vulnerability Protection Profile

```python
from scm.security_services.models.vulnerability_protection_profiles import VulnerabilityProtectionProfiles
from scm.security_services.models.vulnerability_protection_profiles_rules_inner import VulnerabilityProtectionProfilesRulesInner

vuln_protect_api = client.security_services.VulnerabilityProtectionProfilesApi(client.security_services.api_client)

rules = [
    VulnerabilityProtectionProfilesRulesInner(
        name="critical-vulns",
        severity=["critical"],
        action={"reset_both": {}},
        cve=["any"],
        threat_name="any",
        host="any",
        vendor_id=["any"]
    ),
    VulnerabilityProtectionProfilesRulesInner(
        name="high-vulns",
        severity=["high"],
        action={"default": {}},
        cve=["any"],
        threat_name="any",
        host="any",
        vendor_id=["any"]
    )
]

profile = VulnerabilityProtectionProfiles(
    id="",
    name="strict-vulnerability-protection",
    folder="Texas",
    rules=rules,
    description="Strict vulnerability protection"
)

created = vuln_protect_api.create_vulnerability_protection_profiles(
    vulnerability_protection_profiles=profile
)
print(f"Created vulnerability protection profile: {created.name}")
```

---

## Network Services

### IKE Gateways

#### Create IKE Gateway

```python
from scm.network_services.models.ike_gateways import IkeGateways
from scm.network_services.models.ike_gateways_authentication import IkeGatewaysAuthentication
from scm.network_services.models.ike_gateways_authentication_pre_shared_key import IkeGatewaysAuthenticationPreSharedKey
from scm.network_services.models.ike_gateways_peer_address import IkeGatewaysPeerAddress
from scm.network_services.models.ike_gateways_protocol import IkeGatewaysProtocol
from scm.network_services.models.ike_gateways_protocol_ikev2 import IkeGatewaysProtocolIkev2
from scm.network_services.models.ike_gateways_protocol_ikev2_dpd import IkeGatewaysProtocolIkev2Dpd

ike_gateways_api = client.network_services.IKEGatewaysApi(client.network_services.api_client)

# Configure authentication
auth = IkeGatewaysAuthentication(
    pre_shared_key=IkeGatewaysAuthenticationPreSharedKey(
        key="your-pre-shared-key"
    )
)

# Configure peer address
peer_address = IkeGatewaysPeerAddress(
    ip="203.0.113.50"
)

# Configure IKEv2 protocol
dpd = IkeGatewaysProtocolIkev2Dpd(
    enable=True
)

ikev2 = IkeGatewaysProtocolIkev2(
    ike_crypto_profile="default",
    dpd=dpd
)

protocol = IkeGatewaysProtocol(
    ikev2=ikev2,
    version="ikev2-preferred"
)

ike_gateway = IkeGateways(
    id="",
    name="branch-office-vpn",
    folder="Texas",
    authentication=auth,
    peer_address=peer_address,
    peer_id={
        "id": "branch-office@example.com",
        "type": "ufqdn"
    },
    local_id={
        "id": "headquarters@example.com",
        "type": "ufqdn"
    },
    protocol=protocol,
    protocol_common={
        "nat_traversal": {"enable": True},
        "fragmentation": {"enable": True}
    }
)

created = ike_gateways_api.create_ike_gateways(ike_gateways=ike_gateway)
print(f"Created IKE gateway: {created.name}")
```

---

### IPSec Tunnels

#### Create IPSec Tunnel

```python
from scm.network_services.models.ipsec_tunnels import IpsecTunnels
from scm.network_services.models.ipsec_tunnels_auto_key import IpsecTunnelsAutoKey
from scm.network_services.models.ipsec_tunnels_auto_key_proxy_id import IpsecTunnelsAutoKeyProxyId

ipsec_tunnels_api = client.network_services.IPsecTunnelsApi(client.network_services.api_client)

# Configure auto-key with proxy-id
proxy_id = IpsecTunnelsAutoKeyProxyId(
    name="proxy-id-1",
    local="10.0.0.0/24",
    remote="192.168.1.0/24",
    protocol={"any": {}}
)

auto_key = IpsecTunnelsAutoKey(
    ike_gateway=[{"name": "branch-office-vpn"}],
    ipsec_crypto_profile="default",
    proxy_id=[proxy_id]
)

tunnel = IpsecTunnels(
    id="",
    name="branch-office-tunnel",
    folder="Texas",
    auto_key=auto_key,
    anti_replay=True,
    tunnel_monitor={
        "enable": True,
        "destination_ip": "192.168.1.1"
    }
)

created = ipsec_tunnels_api.create_ipsec_tunnels(ipsec_tunnels=tunnel)
print(f"Created IPSec tunnel: {created.name}")
```

---

### QoS Profiles

#### Create QoS Profile

```python
from scm.network_services.models.qos_profiles import QosProfiles
from scm.network_services.models.qos_profiles_class_bandwidth_type import QosProfilesClassBandwidthType
from scm.network_services.models.qos_profiles_aggregate_bandwidth import QosProfilesAggregateBandwidth

qos_api = client.network_services.QoSProfilesApi(client.network_services.api_client)

# Define bandwidth classes
bandwidth = QosProfilesClassBandwidthType(
    mbps=100
)

aggregate = QosProfilesAggregateBandwidth(
    egress_max=1000,
    egress_guaranteed=500
)

qos_profile = QosProfiles(
    id="",
    name="high-priority-qos",
    folder="Texas",
    class_bandwidth_type=bandwidth,
    aggregate_bandwidth=aggregate
)

created = qos_api.create_qos_profiles(qos_profiles=qos_profile)
print(f"Created QoS profile: {created.name}")
```

---

## Identity Services

### LDAP Server Profiles

#### Create LDAP Server Profile

```python
from scm.identity_services.models.ldap_server_profiles import LdapServerProfiles
from scm.identity_services.models.ldap_server_profiles_server import LdapServerProfilesServer

ldap_api = client.identity_services.LDAPServerProfilesApi(client.identity_services.api_client)

# Define LDAP servers
servers = [
    LdapServerProfilesServer(
        name="primary-dc",
        server="ldap.example.com",
        port=389
    ),
    LdapServerProfilesServer(
        name="secondary-dc",
        server="ldap2.example.com",
        port=389
    )
]

ldap_profile = LdapServerProfiles(
    id="",
    name="corporate-ldap",
    folder="Texas",
    server=servers,
    ldap_type="active-directory",
    base="dc=example,dc=com",
    bind_dn="cn=ldap-reader,ou=service-accounts,dc=example,dc=com",
    bind_password="your-bind-password",
    ssl=False,
    verify_server_certificate=False
)

created = ldap_api.create_ldap_server_profiles(ldap_server_profiles=ldap_profile)
print(f"Created LDAP profile: {created.name}")
```

---

### SAML Server Profiles

#### Create SAML Server Profile

```python
from scm.identity_services.models.saml_server_profiles import SamlServerProfiles

saml_api = client.identity_services.SAMLServerProfilesApi(client.identity_services.api_client)

saml_profile = SamlServerProfiles(
    id="",
    name="okta-saml",
    folder="Texas",
    entity_id="https://example.okta.com/saml2/idp",
    sso_url="https://example.okta.com/app/example/exk123/sso/saml",
    certificate="-----BEGIN CERTIFICATE-----\nMIIDpDCCAoygAwIBAgIGAXo...\n-----END CERTIFICATE-----",
    max_clock_skew=60,
    sso_binding="post",
    validate_idp_certificate=True
)

created = saml_api.create_saml_server_profiles(saml_server_profiles=saml_profile)
print(f"Created SAML profile: {created.name}")
```

---

## Deployment Services

### Remote Networks

#### Create Remote Network

```python
from scm.deployment_services.models.remote_networks import RemoteNetworks
from scm.deployment_services.models.remote_networks_ecmp_load_balancing import RemoteNetworksEcmpLoadBalancing
from scm.deployment_services.models.remote_networks_protocol import RemoteNetworksProtocol
from scm.deployment_services.models.remote_networks_protocol_bgp import RemoteNetworksProtocolBgp

remote_networks_api = client.deployment_services.RemoteNetworksApi(client.deployment_services.api_client)

# Configure BGP
bgp = RemoteNetworksProtocolBgp(
    enable=True,
    local_ip_address="10.0.1.1",
    peer_as="65001",
    peer_ip_address="10.0.1.2",
    secret="bgp-secret-key"
)

protocol = RemoteNetworksProtocol(
    bgp=bgp
)

# Configure ECMP
ecmp = RemoteNetworksEcmpLoadBalancing(
    enable=True,
    tunnels=["ipsec-tunnel-1", "ipsec-tunnel-2"]
)

remote_network = RemoteNetworks(
    id="",
    name="branch-office-dallas",
    folder="Remote Networks",
    region="us-southwest",
    license_type="FWAAS-AGGREGATE",
    spn_name="branch-dallas-spn",
    ipsec_tunnel="branch-office-tunnel",
    protocol=protocol,
    ecmp_load_balancing=ecmp,
    subnets=["192.168.10.0/24", "192.168.20.0/24"]
)

created = remote_networks_api.create_remote_networks(remote_networks=remote_network)
print(f"Created remote network: {created.name}")
```

---

### Service Connections

#### Create Service Connection

```python
from scm.deployment_services.models.service_connections import ServiceConnections
from scm.deployment_services.models.service_connections_backup_sc import ServiceConnectionsBackupSC
from scm.deployment_services.models.service_connections_protocol import ServiceConnectionsProtocol
from scm.deployment_services.models.service_connections_protocol_bgp import ServiceConnectionsProtocolBgp

service_conn_api = client.deployment_services.ServiceConnectionsApi(client.deployment_services.api_client)

# Configure BGP
bgp = ServiceConnectionsProtocolBgp(
    enable=True,
    local_ip_address="10.1.1.1",
    peer_as="65002",
    peer_ip_address="10.1.1.2",
    secret="bgp-secret"
)

protocol = ServiceConnectionsProtocol(
    bgp=bgp
)

# Configure backup
backup = ServiceConnectionsBackupSC(
    name="backup-sc"
)

service_connection = ServiceConnections(
    id="",
    name="aws-vpc-connection",
    folder="Service Connections",
    region="us-east-1",
    ipsec_tunnel="aws-ipsec-tunnel",
    protocol=protocol,
    backup_sc=backup,
    source_nat=True,
    subnets=["10.100.0.0/16"]
)

created = service_conn_api.create_service_connections(service_connections=service_connection)
print(f"Created service connection: {created.name}")
```

---

## Error Handling

### Basic Exception Handling

```python
from scm.exceptions import (
    ObjectNotPresentError,
    NameNotUniqueError,
    InvalidObjectError,
    ReferenceNotZeroError,
    MissingQueryParameterError
)

# Handle specific exceptions
try:
    address = addresses_api.fetch_addresses(
        name="non-existent",
        folder="Texas"
    )
except ObjectNotPresentError as e:
    print(f"Address not found: {e.message}")
except InvalidObjectError as e:
    print(f"Invalid address object: {e.message}")
    print(f"Details: {e.details}")
```

### Creating Objects with Error Handling

```python
from scm.exceptions import NameNotUniqueError, InvalidObjectError

try:
    # Attempt to create address
    new_address = Addresses(
        id="",
        name="duplicate-name",
        folder="Texas",
        ip_netmask="10.0.0.1/32"
    )
    created = addresses_api.create_addresses(addresses=new_address)
    print(f"Created: {created.name}")

except NameNotUniqueError as e:
    print(f"Address name already exists: {e.object_name}")
    print(f"Use a different name or update existing object")

except InvalidObjectError as e:
    print(f"Invalid address configuration: {e.message}")
    print(f"Error details: {e.details}")
```

### Deleting with Reference Checking

```python
from scm.exceptions import ReferenceNotZeroError

try:
    addresses_api.delete_addresses_by_id(id=address_id)
    print("Address deleted successfully")

except ReferenceNotZeroError as e:
    print(f"Cannot delete - object is referenced elsewhere")
    print(f"Error: {e.message}")
    print(f"Remove references before deleting")

except ObjectNotPresentError as e:
    print(f"Address already deleted or does not exist")
```

---

## Pagination

### Manual Pagination

```python
# Fetch all addresses using manual pagination
all_addresses = []
limit = 100
offset = 0

while True:
    response = addresses_api.list_addresses(
        folder="Texas",
        limit=limit,
        offset=offset
    )

    all_addresses.extend(response.data)

    print(f"Fetched {len(response.data)} addresses (offset: {offset})")

    # Check if we've retrieved all records
    if len(response.data) < limit:
        break

    offset += limit

print(f"Total addresses retrieved: {len(all_addresses)}")
```

### Using fetch() for Auto-Pagination

```python
# fetch() automatically paginates through results
address = addresses_api.fetch_addresses(
    name="web-server-01",
    folder="Texas"
)

# Works even with large datasets - automatically pages through until found
if address:
    print(f"Found address: {address.name}")
else:
    print("Address not found in entire dataset")
```

---

## Bulk Operations

### Bulk Create Addresses

```python
import logging

logger = logging.getLogger(__name__)

# Create multiple addresses
addresses_to_create = [
    ("web-01", "192.168.1.10/32"),
    ("web-02", "192.168.1.11/32"),
    ("web-03", "192.168.1.12/32"),
    ("db-01", "192.168.2.10/32"),
    ("db-02", "192.168.2.11/32"),
]

created_addresses = []
failed_addresses = []

for name, ip in addresses_to_create:
    try:
        address = Addresses(
            id="",
            name=name,
            folder="Texas",
            ip_netmask=ip,
            tag=["Bulk-Import"]
        )
        created = addresses_api.create_addresses(addresses=address)
        created_addresses.append(created)
        logger.info(f"✓ Created: {name}")

    except NameNotUniqueError:
        logger.warning(f"⚠ Skipped (already exists): {name}")
        failed_addresses.append((name, "already_exists"))

    except InvalidObjectError as e:
        logger.error(f"✗ Failed: {name} - {e.message}")
        failed_addresses.append((name, str(e.message)))

print(f"\nCreated: {len(created_addresses)}")
print(f"Failed: {len(failed_addresses)}")
```

### Bulk Update Addresses

```python
# Update all addresses matching criteria
response = addresses_api.list_addresses(
    folder="Texas",
    limit=1000
)

updated_count = 0
for address in response.data:
    # Add tag to all addresses without it
    if "Reviewed" not in (address.tag or []):
        if not address.tag:
            address.tag = []
        address.tag.append("Reviewed")

        try:
            addresses_api.update_addresses_by_id(
                id=address.id,
                addresses=address
            )
            updated_count += 1
            logger.info(f"Updated: {address.name}")
        except Exception as e:
            logger.error(f"Failed to update {address.name}: {e}")

print(f"Updated {updated_count} addresses")
```

### Bulk Delete with Filtering

```python
# Delete all addresses with specific tag
response = addresses_api.list_addresses(
    folder="Texas",
    limit=1000
)

deleted_count = 0
for address in response.data:
    # Delete only addresses with "Temporary" tag
    if address.tag and "Temporary" in address.tag:
        try:
            addresses_api.delete_addresses_by_id(id=address.id)
            deleted_count += 1
            logger.info(f"Deleted: {address.name}")

        except ReferenceNotZeroError:
            logger.warning(f"Cannot delete {address.name} - still referenced")

        except Exception as e:
            logger.error(f"Failed to delete {address.name}: {e}")

print(f"Deleted {deleted_count} addresses")
```

---

## Additional Resources

- [Migration Guide](MIGRATION_GUIDE.md) - Migrating from pan-scm-sdk
- [Common Patterns](COMMON_PATTERNS.md) - Common usage patterns and workflows
- [Troubleshooting Guide](TROUBLESHOOTING.md) - Common issues and solutions
- [API Reference](../scm/) - Full API documentation
