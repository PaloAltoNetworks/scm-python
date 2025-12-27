# ZoneProtectionProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asymmetric_path** | **str** | Determine whether to drop or bypass packets that contain out-of-sync ACKs or out-of-window sequence numbers: * &#x60;global&#x60; — Use system-wide setting that is assigned through TCP Settings or the CLI. * &#x60;drop&#x60; — Drop packets that contain an asymmetric path. * &#x60;bypass&#x60; — Bypass scanning on packets that contain an asymmetric path.  | [optional] 
**description** | **str** | The description of the profile | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**discard_icmp_embedded_error** | **bool** | Discard ICMP packets that are embedded with an error message. | [optional] 
**flood** | [**ZoneProtectionProfilesFlood**](ZoneProtectionProfilesFlood.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**fragmented_traffic_discard** | **bool** | Discard fragmented IP packets.  | [optional] 
**icmp_frag_discard** | **bool** | Discard packets that consist of ICMP fragments. | [optional] 
**icmp_large_packet_discard** | **bool** | Discard ICMP packets that are larger than 1024 bytes. | [optional] 
**icmp_ping_zero_id_discard** | **bool** | Discard packets if the ICMP ping packet has an identifier value of 0.  | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**ipv6** | [**ZoneProtectionProfilesIpv6**](ZoneProtectionProfilesIpv6.md) |  | [optional] 
**l2_sec_group_tag_protection** | [**ZoneProtectionProfilesL2SecGroupTagProtection**](ZoneProtectionProfilesL2SecGroupTagProtection.md) |  | [optional] 
**loose_source_routing_discard** | **bool** | Discard packets with the Loose Source Routing IP option set. Loose Source Routing is an option whereby a source of a datagram provides routing information and a gateway or host is allowed to choose any route of a number of intermediate gateways to get the datagram to the next address in the route.  | [optional] 
**malformed_option_discard** | **bool** | Discard packets if they have incorrect combinations of class, number, and length based on RFCs 791, 1108, 1393, and 2113.  | [optional] 
**mismatched_overlapping_tcp_segment_discard** | **bool** | Drop packets with mismatched overlapping TCP segments.  | [optional] 
**mptcp_option_strip** | **str** | MPTCP is an extension of TCP that allows a client to maintain a connection by simultaneously using multiple paths to connect to the destination host. By default, MPTCP support is disabled, based on the global MPTCP setting.  Review or adjust the MPTCP settings for the security zones associated with this profile: * &#x60;no&#x60; — Enable MPTCP support (do not strip the MPTCP option). * &#x60;yes&#x60; — Disable MPTCP support (strip the MPTCP option). With this configured, MPTCP connections are converted to standard TCP connections, as MPTCP is backwards compatible with TCP. * &#x60;global&#x60; — Support MPTCP based on the global MPTCP setting. By default, the global MPTCP setting is set to yes so that MPTCP is disabled (the MPTCP option is stripped from the packet).  | [optional] [default to 'global']
**name** | **str** | The profile name | 
**non_ip_protocol** | [**ZoneProtectionProfilesNonIpProtocol**](ZoneProtectionProfilesNonIpProtocol.md) |  | [optional] 
**record_route_discard** | **bool** | Discard packets with the Record Route IP option set. When a datagram has this option, each router that routes the datagram adds its own IP address to the header, thus providing the path to the recipient.  | [optional] 
**reject_non_syn_tcp** | **str** | Determine whether to reject the packet if the first packet for the TCP session setup is not a SYN packet: * &#x60;global&#x60; — Use system-wide setting that is assigned through the CLI. * &#x60;yes&#x60; — Reject non-SYN TCP. * &#x60;no&#x60; — Accept non-SYN TCP.  | [optional] 
**scan** | [**List[ZoneProtectionProfilesScanInner]**](ZoneProtectionProfilesScanInner.md) |  | [optional] 
**scan_white_list** | [**List[ZoneProtectionProfilesScanWhiteListInner]**](ZoneProtectionProfilesScanWhiteListInner.md) |  | [optional] 
**security_discard** | **bool** | Discard packets if the security option is defined.  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**spoofed_ip_discard** | **bool** | Check that the source IP address of the ingress packet is routable and the routing interface is in the same zone as the ingress interface. If either condition is not true, discard the packet.  | [optional] 
**stream_id_discard** | **bool** | Discard packets if the Stream ID option is defined.  | [optional] 
**strict_ip_check** | **bool** | Check that both conditions are true: * The source IP address is not the subnet broadcast IP address of the ingress interface. * The source IP address is routable over the exact ingress interface. If either condition is not true, discard the packet.  | [optional] 
**strict_source_routing_discard** | **bool** | Discard packets with the Strict Source Routing IP option set. Strict Source Routing is an option whereby a source of a datagram provides routing information through which a gateway or host must send the datagram.  | [optional] 
**suppress_icmp_needfrag** | **bool** | Stop sending ICMP fragmentation needed messages in response to packets that exceed the interface MTU and have the do not fragment (DF) bit set. This setting will interfere with the PMTUD process performed by hosts behind the firewall.  | [optional] 
**suppress_icmp_timeexceeded** | **bool** | Stop sending ICMP TTL expired messages. | [optional] 
**tcp_fast_open_and_data_strip** | **bool** | Strip the TCP Fast Open option (and data payload, if any) from the TCP SYN or SYN-ACK packet during a TCP three-way handshake.  | [optional] 
**tcp_handshake_discard** | **bool** | Drop packets with split handshakes.  | [optional] 
**tcp_syn_with_data_discard** | **bool** | Prevent a TCP session from being established if the TCP SYN packet contains data during a three-way handshake.  | [optional] [default to True]
**tcp_synack_with_data_discard** | **bool** | Prevent a TCP session from being established if the TCP SYN-ACK packet contains data during a three-way handshake.  | [optional] [default to True]
**tcp_timestamp_strip** | **bool** | Determine whether the packet has a TCP timestamp in the header and, if it does, strip the timestamp from the header.  | [optional] 
**timestamp_discard** | **bool** | Discard packets with the Timestamp IP option set.  | [optional] 
**unknown_option_discard** | **bool** | Discard packets if the class and number are unknown.  | [optional] 

## Example

```python
from scm.network_services.models.zone_protection_profiles import ZoneProtectionProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneProtectionProfiles from a JSON string
zone_protection_profiles_instance = ZoneProtectionProfiles.from_json(json)
# print the JSON string representation of the object
print(ZoneProtectionProfiles.to_json())

# convert the object into a dict
zone_protection_profiles_dict = zone_protection_profiles_instance.to_dict()
# create an instance of ZoneProtectionProfiles from a dict
zone_protection_profiles_from_dict = ZoneProtectionProfiles.from_dict(zone_protection_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


