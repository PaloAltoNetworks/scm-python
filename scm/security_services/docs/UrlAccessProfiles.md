# UrlAccessProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **List[str]** |  | [optional] 
**allow** | **List[str]** |  | [optional] 
**block** | **List[str]** |  | [optional] 
**cloud_inline_cat** | **bool** |  | [optional] 
**var_continue** | **List[str]** |  | [optional] 
**credential_enforcement** | [**UrlAccessProfilesCredentialEnforcement**](UrlAccessProfilesCredentialEnforcement.md) |  | [optional] 
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**local_inline_cat** | **bool** |  | [optional] 
**log_container_page_only** | **bool** |  | [optional] [default to True]
**log_http_hdr_referer** | **bool** |  | [optional] [default to False]
**log_http_hdr_user_agent** | **bool** |  | [optional] [default to False]
**log_http_hdr_xff** | **bool** |  | [optional] [default to False]
**mlav_category_exception** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**redirect** | **List[str]** |  | [optional] 
**safe_search_enforcement** | **bool** |  | [optional] [default to False]
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.security_services.models.url_access_profiles import UrlAccessProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of UrlAccessProfiles from a JSON string
url_access_profiles_instance = UrlAccessProfiles.from_json(json)
# print the JSON string representation of the object
print(UrlAccessProfiles.to_json())

# convert the object into a dict
url_access_profiles_dict = url_access_profiles_instance.to_dict()
# create an instance of UrlAccessProfiles from a dict
url_access_profiles_from_dict = UrlAccessProfiles.from_dict(url_access_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


