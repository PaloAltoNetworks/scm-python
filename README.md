# SCM Python SDK

Auto-generated SDK for Palo Alto Networks Strata Cloud Manager.

## Installation

```bash
pip install .
```

## Usage

```python
from scm import Scm

client = Scm(
    client_id="YOUR_ID",
    client_secret="YOUR_SECRET",
    tsg_id="YOUR_TSG"
)

# Example usage (depending on generated structure)
# addresses = client.objects.AddressesApi(client.objects_client).list()
```
