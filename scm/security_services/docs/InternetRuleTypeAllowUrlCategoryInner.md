# InternetRuleTypeAllowUrlCategoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_action** | **str** |  | [optional] [default to 'none']
**credential_enforcement** | **str** |  | [optional] [default to 'enabled']
**decryption** | **str** |  | [optional] [default to 'enabled']
**dlp** | **str** |  | [optional] 
**file_control** | [**InternetRuleTypeAllowUrlCategoryInnerFileControl**](InternetRuleTypeAllowUrlCategoryInnerFileControl.md) |  | [optional] 
**isolation_profiles** | **str** |  | [optional] [default to 'none']
**name** | **str** |  | [optional] 

## Example

```python
from scm.security_services.models.internet_rule_type_allow_url_category_inner import InternetRuleTypeAllowUrlCategoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of InternetRuleTypeAllowUrlCategoryInner from a JSON string
internet_rule_type_allow_url_category_inner_instance = InternetRuleTypeAllowUrlCategoryInner.from_json(json)
# print the JSON string representation of the object
print(InternetRuleTypeAllowUrlCategoryInner.to_json())

# convert the object into a dict
internet_rule_type_allow_url_category_inner_dict = internet_rule_type_allow_url_category_inner_instance.to_dict()
# create an instance of InternetRuleTypeAllowUrlCategoryInner from a dict
internet_rule_type_allow_url_category_inner_from_dict = InternetRuleTypeAllowUrlCategoryInner.from_dict(internet_rule_type_allow_url_category_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


