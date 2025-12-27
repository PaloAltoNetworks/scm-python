# PayloadFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**List[PayloadFormatHeadersInner]**](PayloadFormatHeadersInner.md) |  | [optional] 
**name** | **str** | The name of the payload format | [optional] [default to 'Default']
**params** | [**List[PayloadFormatParamsInner]**](PayloadFormatParamsInner.md) |  | [optional] 
**payload** | **str** | The log payload format.  The accepted log field values are as follows. * &#x60;receive_time&#x60; * &#x60;serial&#x60; * &#x60;seqno&#x60; * &#x60;actionflags&#x60; * &#x60;type&#x60; * &#x60;subtype&#x60; * &#x60;time_generated&#x60; * &#x60;high_res_timestamp&#x60; * &#x60;dg_hier_level_1&#x60; * &#x60;dg_hier_level_2&#x60; * &#x60;dg_hier_level_3&#x60; * &#x60;dg_hier_level_4&#x60; * &#x60;vsys_name&#x60; * &#x60;device_name&#x60; * &#x60;vsys_id&#x60; * &#x60;host&#x60; * &#x60;vsys&#x60; * &#x60;cmd&#x60; * &#x60;admin&#x60; * &#x60;client&#x60; * &#x60;result&#x60; * &#x60;path&#x60; * &#x60;dg_id&#x60; * &#x60;comment&#x60; * &#x60;tpl_id&#x60; * &#x60;sender_sw_version&#x60; * &#x60;cef-formatted-receive_time&#x60; * &#x60;cef-formatted-time_generated&#x60; * &#x60;before-change-detail&#x60; * &#x60;after-change-detail&#x60;  | [optional] 
**url_format** | **str** | The URL path of the HTTP server | [optional] 

## Example

```python
from scm_objects.models.payload_format import PayloadFormat

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadFormat from a JSON string
payload_format_instance = PayloadFormat.from_json(json)
# print the JSON string representation of the object
print(PayloadFormat.to_json())

# convert the object into a dict
payload_format_dict = payload_format_instance.to_dict()
# create an instance of PayloadFormat from a dict
payload_format_from_dict = PayloadFormat.from_dict(payload_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


