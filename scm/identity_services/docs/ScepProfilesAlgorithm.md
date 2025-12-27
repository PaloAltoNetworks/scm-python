# ScepProfilesAlgorithm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsa** | [**ScepProfilesAlgorithmRsa**](ScepProfilesAlgorithmRsa.md) |  | [optional] 

## Example

```python
from scm.identity_services.models.scep_profiles_algorithm import ScepProfilesAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of ScepProfilesAlgorithm from a JSON string
scep_profiles_algorithm_instance = ScepProfilesAlgorithm.from_json(json)
# print the JSON string representation of the object
print(ScepProfilesAlgorithm.to_json())

# convert the object into a dict
scep_profiles_algorithm_dict = scep_profiles_algorithm_instance.to_dict()
# create an instance of ScepProfilesAlgorithm from a dict
scep_profiles_algorithm_from_dict = ScepProfilesAlgorithm.from_dict(scep_profiles_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


