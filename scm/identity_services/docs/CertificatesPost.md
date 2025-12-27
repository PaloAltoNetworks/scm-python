# CertificatesPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**CertificatesPostAlgorithm**](CertificatesPostAlgorithm.md) |  | 
**alternate_email** | **List[str]** | Alternate email | [optional] 
**certificate_name** | **str** | Certificate name | 
**common_name** | **str** | Common name | 
**country_code** | **str** | Country code | [optional] 
**day_till_expiration** | **int** | Expiration (days) | [optional] 
**department** | **List[str]** | Department | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**digest** | **str** | Hash algorithm | 
**email** | **str** | Email | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**hostname** | **List[str]** | Hostname | [optional] 
**ip** | **List[str]** | IP address | [optional] 
**is_block_private_key** | **bool** | Block private key export? | [optional] 
**is_certificate_authority** | **bool** | Certificate authority certificate? | [optional] 
**locality** | **str** | Locality | [optional] 
**ocsp_responder_url** | **str** | OCSP responder URL | [optional] 
**signed_by** | **str** | Signed by | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**state** | **str** | State | [optional] 

## Example

```python
from scm_identity_services.models.certificates_post import CertificatesPost

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesPost from a JSON string
certificates_post_instance = CertificatesPost.from_json(json)
# print the JSON string representation of the object
print(CertificatesPost.to_json())

# convert the object into a dict
certificates_post_dict = certificates_post_instance.to_dict()
# create an instance of CertificatesPost from a dict
certificates_post_from_dict = CertificatesPost.from_dict(certificates_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


