# SitesQos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_cir** | **float** | The backup CIR in Mbps. This is distributed equally for all tunnels in the site. | [optional] 
**cir** | **float** | The CIR in Mbps. This is distributed equally for all tunnels in the site. | [optional] 
**profile** | **str** | The name of the site QoS profile | [optional] 

## Example

```python
from scm_deployment_services.models.sites_qos import SitesQos

# TODO update the JSON string below
json = "{}"
# create an instance of SitesQos from a JSON string
sites_qos_instance = SitesQos.from_json(json)
# print the JSON string representation of the object
print(SitesQos.to_json())

# convert the object into a dict
sites_qos_dict = sites_qos_instance.to_dict()
# create an instance of SitesQos from a dict
sites_qos_from_dict = SitesQos.from_dict(sites_qos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


