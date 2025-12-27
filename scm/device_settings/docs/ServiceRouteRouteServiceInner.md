# ServiceRouteRouteServiceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The follow list details the accepted &#x60;name&#x60; values and their corresponding service description. - &#x60;autofocus&#x60; &#x3D; AutoFocus Cloud - &#x60;crl-status&#x60; &#x3D; CRL servers - &#x60;data-services&#x60; &#x3D; Data Services - &#x60;ddns&#x60; &#x3D; DDNS server(s) - &#x60;deployments&#x60; &#x3D; Panorama pushed updates - &#x60;dns&#x60; &#x3D; DNS server(s) - &#x60;edl-updates&#x60; &#x3D; External Dynamic List update server - &#x60;email&#x60; &#x3D; SMTP gateway(s) - &#x60;hsm&#x60; &#x3D; Hardware Security Module server(s) - &#x60;http&#x60; &#x3D; HTTP Forwarding server(s) - &#x60;iot&#x60; &#x3D; IOT service-route - &#x60;kerberos&#x60; &#x3D; Kerberos server - &#x60;ldap&#x60; &#x3D; LDAP server - &#x60;mdm&#x60; &#x3D; MDM servers - &#x60;mfa&#x60; &#x3D; Multi-Factor Authentication - &#x60;netflow&#x60; &#x3D; Netflow server(s) - &#x60;ntp&#x60; &#x3D; NTP server(s) - &#x60;paloalto-networks-services&#x60; &#x3D; Palo Alto Networks Services - &#x60;panorama&#x60; &#x3D; Panorama server - &#x60;panorama-log-forwarding&#x60; &#x3D; Panorama Log Forwarding - &#x60;proxy&#x60; &#x3D; Proxy server - &#x60;radius&#x60; &#x3D; RADIUS server - &#x60;scep&#x60; &#x3D; SCEP - &#x60;snmp&#x60; &#x3D; SNMP server(s) - &#x60;syslog&#x60; &#x3D; Syslog server(s) - &#x60;tacplus&#x60; &#x3D; TACACS+ server - &#x60;uid-&#x60;agent &#x3D; UID agent(s) - &#x60;url-&#x60;updates &#x3D; URL update server - &#x60;vmmonitor&#x60; &#x3D; VM monitor - &#x60;wildfire-&#x60;private &#x3D; WildFire Appliance - &#x60;ztp&#x60; &#x3D; ZTP and Auto-VPN DDNS  | [optional] 
**source** | [**ServiceRouteRouteServiceInnerSource**](ServiceRouteRouteServiceInnerSource.md) |  | [optional] 
**source_v6** | [**ServiceRouteRouteServiceInnerSourceV6**](ServiceRouteRouteServiceInnerSourceV6.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.service_route_route_service_inner import ServiceRouteRouteServiceInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRouteRouteServiceInner from a JSON string
service_route_route_service_inner_instance = ServiceRouteRouteServiceInner.from_json(json)
# print the JSON string representation of the object
print(ServiceRouteRouteServiceInner.to_json())

# convert the object into a dict
service_route_route_service_inner_dict = service_route_route_service_inner_instance.to_dict()
# create an instance of ServiceRouteRouteServiceInner from a dict
service_route_route_service_inner_from_dict = ServiceRouteRouteServiceInner.from_dict(service_route_route_service_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


