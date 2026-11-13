# BlockRuleZtna

ZTNA block rule configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_icmp_for_troubleshooting** | **bool** | Allow ICMP for troubleshooting | [optional] [default to False]
**block_all_other_unmatched_outbound_connections** | **bool** | Block all other unmatched outbound connections | [optional] [default to False]
**block_inbound_access_when_connected_to_tunnel** | **bool** | Block inbound access when connected to tunnel | [optional] [default to False]
**block_non_tcp_non_udp_traffic_when_connected_to_tunnel** | **bool** | Block Non-TCP Non UDP based traffic when connected to tunnel | [optional] [default to False]
**block_outbound_lan_access_when_connected_to_tunnel** | **bool** | Block outbound LAN access when connected to tunnel | [optional] [default to False]
**enforcer_fqdn_dns_resolution_via_dns_servers** | **bool** | Enforce FQDN DNS resolution via tunnel DNS servers | [optional] [default to True]
**resolve_all_fqdns_using_dns_servers_assigned_by_the_tunnel** | **bool** | Resolve All FQDNs using DNS servers assigned by the tunnel (Windows Only) | [optional] [default to True]

## Example

```python
from scm.mobile_agent.models.block_rule_ztna import BlockRuleZtna

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRuleZtna from a JSON string
block_rule_ztna_instance = BlockRuleZtna.from_json(json)
# print the JSON string representation of the object
print(BlockRuleZtna.to_json())

# convert the object into a dict
block_rule_ztna_dict = block_rule_ztna_instance.to_dict()
# create an instance of BlockRuleZtna from a dict
block_rule_ztna_from_dict = BlockRuleZtna.from_dict(block_rule_ztna_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


