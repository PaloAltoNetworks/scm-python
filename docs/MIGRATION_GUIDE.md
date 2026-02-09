# Migration Guide: pan-scm-sdk → scm-python

**Version**: 1.0
**Date**: 2026-02-08
**Audience**: Developers migrating from pan-scm-sdk to scm-python

---

## Table of Contents

1. [Overview](#overview)
2. [Key Differences](#key-differences)
3. [Installation](#installation)
4. [Client Initialization](#client-initialization)
5. [API Access Patterns](#api-access-patterns)
6. [CRUD Operations](#crud-operations)
7. [Exception Handling](#exception-handling)
8. [Helper Methods](#helper-methods)
9. [Pagination](#pagination)
10. [Common Migration Patterns](#common-migration-patterns)
11. [Troubleshooting](#troubleshooting)

---

## Overview

This guide helps you migrate from `pan-scm-sdk` to `scm-python` (auto-generated OpenAPI SDK).

### Why Migrate?

- ✅ **Broader API Coverage**: 120+ endpoints vs 50+
- ✅ **Auto-generated**: Always in sync with API specs
- ✅ **Better Token Management**: File-based caching, JWT passing
- ✅ **Auto-pagination in fetch()**: Handles 10,000+ objects
- ✅ **Automatic Exception Handling**: Decorators convert exceptions automatically
- ✅ **98.8% Test Coverage**: Production-ready

### What's Different?

- **API Access**: Namespace-based instead of unified interface
- **Import Patterns**: Import API classes instead of client methods
- **Model Names**: OpenAPI-generated models instead of custom Pydantic
- **Exception Handling**: Automatic conversion via decorators

### Compatibility

Both SDKs:
- ✅ Work with the same SCM API
- ✅ Use OAuth2 client credentials
- ✅ Support Pydantic v2 models
- ✅ Have custom exception classes
- ✅ Support fetch() for name-based lookups

---

## Key Differences

### Quick Comparison

| Feature | pan-scm-sdk | scm-python |
|---------|-------------|------------|
| **Client Access** | `client.address.list()` | `AddressesApi(...).list_addresses()` |
| **Imports** | `from scm.client import Scm` | `from scm import Scm`<br>`from scm.objects.api.addresses_api import AddressesApi` |
| **Models** | `AddressCreateModel` | `Addresses` |
| **Exceptions** | Manual parsing | Automatic via decorators |
| **fetch()** | Single page (max 5000) | Auto-pagination (unlimited) |
| **Container Validation** | Client-side | Server-side |

---

## Installation

### pan-scm-sdk

```bash
pip install pan-scm-sdk
```

### scm-python

```bash
# From source
cd scm-python
pip install .

# Development mode
pip install -e .

# From PyPI (when published)
pip install scm-python
```

---

## Client Initialization

### pan-scm-sdk

```python
from scm.client import Scm

# Standard initialization
client = Scm(
    client_id="your-client-id",
    client_secret="your-client-secret",
    tsg_id="1234567890"
)
```

### scm-python

```python
from scm import Scm

# Standard initialization (same as pan-scm-sdk!)
client = Scm(
    client_id="your-client-id",
    client_secret="your-client-secret",
    tsg_id="1234567890"
)

# Or load from config file
client = Scm()  # Reads from ~/.scm/config.json

# Or pass JWT directly
client = Scm(
    client_id="your-client-id",
    client_secret="your-client-secret",
    tsg_id="1234567890",
    jwt="eyJ0eXAi...",
    jwt_expires_at="2026-02-08T10:30:00Z"
)
```

**Migration**: ✅ Same initialization, but scm-python has extra options (config file, JWT passing)

---

## API Access Patterns

### pan-scm-sdk - Unified Interface

```python
# Clean attribute-based access
addresses_api = client.address
services_api = client.service
tags_api = client.tag

# All resources follow same pattern
addresses = addresses_api.list(folder="Texas")
```

### scm-python - Namespace-based

```python
# Import API class
from scm.objects.api.addresses_api import AddressesApi
from scm.objects.api.services_api import ServicesApi
from scm.objects.api.tags_api import TagsApi

# Instantiate API
addresses_api = AddressesApi(client.objects.api_client)
services_api = ServicesApi(client.objects.api_client)
tags_api = TagsApi(client.objects.api_client)

# Call methods
addresses = addresses_api.list_addresses(folder="Texas")
```

**Migration Steps**:

1. Replace `client.{resource}` with API class import and instantiation
2. Add resource name to method calls (e.g., `list()` → `list_addresses()`)

**Helper Pattern** (recommended):

```python
# Create a helper to reduce boilerplate
class ScmClient:
    def __init__(self, client):
        self.client = client
        self._apis = {}

    def get_api(self, api_class):
        """Cache API instances."""
        if api_class not in self._apis:
            self._apis[api_class] = api_class(self.client.objects.api_client)
        return self._apis[api_class]

# Usage
from scm import Scm
from scm.objects.api.addresses_api import AddressesApi

client = Scm()
scm = ScmClient(client)

# Now access is simpler
addresses_api = scm.get_api(AddressesApi)
addresses = addresses_api.list_addresses(folder="Texas")
```

---

## CRUD Operations

### Create

#### pan-scm-sdk

```python
from scm.models import AddressCreateModel

# Create model
address = AddressCreateModel(
    name="web-server",
    ip_netmask="10.0.0.1/32",
    folder="Texas",
    description="Web server"
)

# Create object
created = client.address.create(address)
print(f"Created: {created.name} (ID: {created.id})")
```

#### scm-python

```python
from scm.objects.models.addresses import Addresses
from scm.objects.api.addresses_api import AddressesApi

# Create API instance
api = AddressesApi(client.objects.api_client)

# Create model (must include id="")
address = Addresses(
    id="",  # Required for create!
    name="web-server",
    ip_netmask="10.0.0.1/32",
    folder="Texas",
    description="Web server"
)

# Create object
created = api.create_addresses(addresses=address)
print(f"Created: {created.name} (ID: {created.id})")
```

**Migration Changes**:
- ✅ Import `Addresses` instead of `AddressCreateModel`
- ✅ Add `id=""` to model (required by Pydantic)
- ✅ Call `create_addresses(addresses=...)` instead of `create(...)`

---

### Read (Get by ID)

#### pan-scm-sdk

```python
# Get by ID
address = client.address.get(address_id)
print(f"Name: {address.name}")
```

#### scm-python

```python
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# Get by ID
address = api.get_addresses_by_id(id=address_id)
print(f"Name: {address.name}")
```

**Migration Changes**:
- ✅ `get(id)` → `get_addresses_by_id(id=id)`
- ✅ Parameter must be named (`id=`)

---

### Update

#### pan-scm-sdk

```python
# Get object
address = client.address.get(address_id)

# Modify
address.description = "Updated description"

# Update
updated = client.address.update(address)
print(f"Updated: {updated.name}")
```

#### scm-python

```python
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# Get object
address = api.get_addresses_by_id(id=address_id)

# Modify
address.description = "Updated description"

# Update
updated = api.update_addresses_by_id(
    id=address_id,
    addresses=address
)
print(f"Updated: {updated.name}")
```

**Migration Changes**:
- ✅ `update(obj)` → `update_addresses_by_id(id=..., addresses=...)`
- ✅ Must pass both ID and object

---

### Delete

#### pan-scm-sdk

```python
# Delete by ID
client.address.delete(address_id)
print("Deleted successfully")
```

#### scm-python

```python
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# Delete by ID
api.delete_addresses_by_id(id=address_id)
print("Deleted successfully")
```

**Migration Changes**:
- ✅ `delete(id)` → `delete_addresses_by_id(id=id)`
- ✅ Parameter must be named (`id=`)

---

### List

#### pan-scm-sdk

```python
# List with filter
addresses = client.address.list(
    folder="Texas",
    limit=100
)

for addr in addresses:
    print(f"  - {addr.name}")
```

#### scm-python

```python
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# List with filter
response = api.list_addresses(
    folder="Texas",
    limit=100
)

for addr in response.data:  # Note: response.data!
    print(f"  - {addr.name}")
```

**Migration Changes**:
- ✅ `list()` → `list_addresses()`
- ✅ Result is in `response.data` (not direct list)
- ✅ Response includes pagination info (`total`, `offset`, `limit`)

---

## Exception Handling

### pan-scm-sdk - Manual Parsing

```python
from scm.exceptions import (
    NameNotUniqueError,
    ObjectNotPresentError,
    InvalidObjectError
)

try:
    address = client.address.create(data)
except NameNotUniqueError as e:
    print(f"Name exists: {e.object_name} in {e.container}")
except ObjectNotPresentError as e:
    print(f"Not found: {e.object_id}")
except InvalidObjectError as e:
    print(f"Validation failed: {e.errors}")
```

### scm-python - Automatic Conversion

```python
from scm.exceptions import (
    NameNotUniqueError,
    ObjectNotPresentError,
    InvalidObjectError
)
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

try:
    # Exceptions are AUTOMATICALLY converted by decorators!
    address = api.create_addresses(addresses=data)
except NameNotUniqueError as e:
    # Already converted - no manual parsing needed!
    print(f"Name exists: {e.object_name} in {e.container}")
    print(f"Error code: {e.error_code}")
    print(f"HTTP status: {e.http_status_code}")
except ObjectNotPresentError as e:
    print(f"Not found: {e.object_id}")
except InvalidObjectError as e:
    print(f"Validation failed: {e.errors}")
```

**Migration Changes**:
- ✅ Same exception classes!
- ✅ **NO manual parsing needed** - decorators handle conversion automatically
- ✅ More structured error details (`error_code`, `http_status_code`, `details`)

**Exception Mapping**:

| API Error | pan-scm-sdk | scm-python |
|-----------|-------------|------------|
| 409 / E006 / "object already exists" | NameNotUniqueError | NameNotUniqueError ✅ |
| 404 / E005 / "object not present" | ObjectNotPresentError | ObjectNotPresentError ✅ |
| 409 / E009 / "reference not zero" | ReferenceNotZeroError | ReferenceNotZeroError ✅ |
| 400 / E003 / "Invalid Object" | InvalidObjectError | InvalidObjectError ✅ |
| 400 / E003 / "Missing Query Parameter" | MissingQueryParameterError | MissingQueryParameterError ✅ |

---

## Helper Methods

### fetch() - Get by Name

#### pan-scm-sdk

```python
# Fetch by name (single page, max 5000 results)
address = client.address.fetch(
    name="web-server",
    folder="Texas"
)

if address:
    print(f"Found: {address.name}")
else:
    print("Not found")
```

#### scm-python

```python
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# Fetch by name (AUTOMATIC PAGINATION - unlimited results!)
address = api.fetch_addresses(
    name="web-server",
    folder="Texas"
)

if address:
    print(f"Found: {address.name}")
else:
    print("Not found")
```

**Migration Changes**:
- ✅ `fetch()` → `fetch_addresses()`
- ✅ Same parameters
- ✅ **scm-python auto-paginates** - handles 10,000+ objects!

**Advantages in scm-python**:
```python
# pan-scm-sdk: Limited to 5000 results
# If object is at position 6000, it won't be found!

# scm-python: Unlimited pagination
# Will find object even if it's at position 10,000
address = api.fetch_addresses(name="my-object", folder="Shared")
# Automatically paginates through ALL results
```

---

## Pagination

### pan-scm-sdk

```python
# Manual pagination with limit
addresses = client.address.list(
    folder="Texas",
    limit=5000  # Max allowed
)

# If more than 5000, results are truncated!
# No built-in way to get all results
```

### scm-python

```python
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# Manual pagination
all_addresses = []
offset = 0
limit = 1000

while True:
    response = api.list_addresses(
        folder="Texas",
        limit=limit,
        offset=offset
    )

    all_addresses.extend(response.data)

    if len(response.data) < limit:
        break

    offset += limit

print(f"Total: {len(all_addresses)} addresses")
```

**OR use fetch() with auto-pagination**:

```python
# fetch() handles pagination automatically!
address = api.fetch_addresses(name="my-object", folder="Texas")
# Will paginate through ALL objects until found
```

**Migration**:
- ✅ Use manual pagination for list operations
- ✅ Use fetch() for name-based lookups (auto-paginates)
- 🔜 `list_all_*()` helpers coming soon for automatic pagination

---

## Common Migration Patterns

### Pattern 1: Basic CRUD

#### Before (pan-scm-sdk)

```python
from scm.client import Scm
from scm.models import AddressCreateModel

client = Scm(client_id="...", client_secret="...", tsg_id="...")

# Create
address = AddressCreateModel(
    name="server",
    ip_netmask="10.0.0.1/32",
    folder="Texas"
)
created = client.address.create(address)

# Read
found = client.address.get(created.id)

# Update
found.description = "Updated"
updated = client.address.update(found)

# Delete
client.address.delete(updated.id)
```

#### After (scm-python)

```python
from scm import Scm
from scm.objects.models.addresses import Addresses
from scm.objects.api.addresses_api import AddressesApi

client = Scm(client_id="...", client_secret="...", tsg_id="...")
api = AddressesApi(client.objects.api_client)

# Create
address = Addresses(
    id="",  # Required!
    name="server",
    ip_netmask="10.0.0.1/32",
    folder="Texas"
)
created = api.create_addresses(addresses=address)

# Read
found = api.get_addresses_by_id(id=created.id)

# Update
found.description = "Updated"
updated = api.update_addresses_by_id(id=found.id, addresses=found)

# Delete
api.delete_addresses_by_id(id=updated.id)
```

---

### Pattern 2: Fetch and Update

#### Before (pan-scm-sdk)

```python
# Find by name and update
address = client.address.fetch(name="web-server", folder="Texas")

if address:
    address.description = "Production server"
    client.address.update(address)
```

#### After (scm-python)

```python
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# Find by name and update
address = api.fetch_addresses(name="web-server", folder="Texas")

if address:
    address.description = "Production server"
    api.update_addresses_by_id(id=address.id, addresses=address)
```

---

### Pattern 3: Exception Handling

#### Before (pan-scm-sdk)

```python
from scm.exceptions import NameNotUniqueError, ObjectNotPresentError

try:
    address = client.address.fetch(name="server", folder="Texas")
    if address:
        client.address.delete(address.id)
except ObjectNotPresentError:
    print("Address not found")
except NameNotUniqueError:
    print("Duplicate name")
```

#### After (scm-python)

```python
from scm.exceptions import NameNotUniqueError, ObjectNotPresentError
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

try:
    address = api.fetch_addresses(name="server", folder="Texas")
    if address:
        api.delete_addresses_by_id(id=address.id)
except ObjectNotPresentError as e:
    # Automatic conversion by decorator!
    print(f"Address not found: {e.object_id}")
except NameNotUniqueError as e:
    print(f"Duplicate: {e.object_name} in {e.container}")
```

---

### Pattern 4: Bulk Operations

#### Before (pan-scm-sdk)

```python
# Create multiple addresses
addresses = []
for i in range(10):
    addr = AddressCreateModel(
        name=f"server-{i}",
        ip_netmask=f"10.0.0.{i}/32",
        folder="Texas"
    )
    created = client.address.create(addr)
    addresses.append(created)

print(f"Created {len(addresses)} addresses")
```

#### After (scm-python)

```python
from scm.objects.models.addresses import Addresses
from scm.objects.api.addresses_api import AddressesApi

api = AddressesApi(client.objects.api_client)

# Create multiple addresses
addresses = []
for i in range(10):
    addr = Addresses(
        id="",
        name=f"server-{i}",
        ip_netmask=f"10.0.0.{i}/32",
        folder="Texas"
    )
    created = api.create_addresses(addresses=addr)
    addresses.append(created)

print(f"Created {len(addresses)} addresses")
```

---

## Troubleshooting

### Issue: Import Errors

**Error**:
```python
ModuleNotFoundError: No module named 'scm.models'
```

**Solution**:
```python
# Wrong (pan-scm-sdk style)
from scm.models import AddressCreateModel

# Correct (scm-python style)
from scm.objects.models.addresses import Addresses
```

---

### Issue: Model Validation Errors

**Error**:
```python
ValidationError: 1 validation error for Addresses
id
  Field required [type=missing]
```

**Solution**:
```python
# Wrong
address = Addresses(name="server", folder="Texas")

# Correct - always include id="" for creates
address = Addresses(id="", name="server", folder="Texas")
```

---

### Issue: Method Not Found

**Error**:
```python
AttributeError: 'AddressesApi' object has no attribute 'list'
```

**Solution**:
```python
# Wrong (pan-scm-sdk style)
api.list(folder="Texas")

# Correct (scm-python style)
api.list_addresses(folder="Texas")
```

---

### Issue: Response is not iterable

**Error**:
```python
TypeError: 'AddressList' object is not iterable
```

**Solution**:
```python
# Wrong
addresses = api.list_addresses(folder="Texas")
for addr in addresses:  # Error!
    print(addr.name)

# Correct
response = api.list_addresses(folder="Texas")
for addr in response.data:  # Use response.data!
    print(addr.name)
```

---

### Issue: Exception not caught

**Error**:
```python
# Exception raised but not caught
NotFoundException: (404) Not Found
```

**Solution**:
```python
# The decorator automatically converts to custom exceptions
# Just catch the custom exception directly

from scm.exceptions import ObjectNotPresentError

try:
    api.get_addresses_by_id(id="non-existent")
except ObjectNotPresentError as e:  # Automatically converted!
    print(f"Not found: {e.object_id}")
```

---

## Migration Checklist

Use this checklist to migrate your code:

### Client Initialization
- [ ] Replace `from scm.client import Scm` with `from scm import Scm`
- [ ] Update config file path if using custom location
- [ ] Consider using JWT passing if available

### API Access
- [ ] Import API classes (e.g., `from scm.objects.api.addresses_api import AddressesApi`)
- [ ] Instantiate API classes with `api_client`
- [ ] Replace `client.{resource}.method()` with `api.method_{resource}()`

### Models
- [ ] Replace `from scm.models import ...` with `from scm.{namespace}.models.{resource} import ...`
- [ ] Replace model names (e.g., `AddressCreateModel` → `Addresses`)
- [ ] Add `id=""` to all create models

### Method Calls
- [ ] Add resource name to all methods (e.g., `list()` → `list_addresses()`)
- [ ] Add `_by_id` suffix to get/update/delete (e.g., `get()` → `get_addresses_by_id()`)
- [ ] Use named parameters (e.g., `id=address_id`)
- [ ] Access list results via `.data` (e.g., `response.data`)

### Exception Handling
- [ ] Update import paths for exceptions
- [ ] Remove manual error parsing (decorators handle it)
- [ ] Catch custom exceptions directly

### Helper Methods
- [ ] Update `fetch()` to `fetch_{resource}()`
- [ ] Enjoy automatic pagination in fetch()!

### Testing
- [ ] Test all CRUD operations
- [ ] Test exception handling
- [ ] Test pagination scenarios
- [ ] Verify fetch() works for large datasets

---

## Need Help?

- **Documentation**: [README.md](../README.md)
- **Examples**: [docs/EXAMPLES.md](./EXAMPLES.md)
- **Common Patterns**: [docs/COMMON_PATTERNS.md](./COMMON_PATTERNS.md)
- **Issues**: [GitHub Issues](https://github.com/PaloAltoNetworks/scm-python/issues)

---

## Summary

### Key Takeaways

✅ **Same Credentials**: No changes to authentication
✅ **Same Exceptions**: Same exception classes, automatic conversion
✅ **Better fetch()**: Auto-pagination handles unlimited results
✅ **Auto-generated**: Always in sync with API specs
✅ **More Coverage**: 120+ endpoints vs 50+

### Main Changes

1. **Imports**: API classes instead of client attributes
2. **Methods**: Resource name in method names
3. **Models**: `id=""` required for creates
4. **Results**: Use `response.data` for lists
5. **Exceptions**: Automatic conversion (no manual parsing)

### Migration Effort

- **Small projects** (< 10 files): ~2-4 hours
- **Medium projects** (10-50 files): ~1-2 days
- **Large projects** (50+ files): ~3-5 days

Most changes are mechanical and can be scripted or search-replaced.

---

**Version**: 1.0
**Last Updated**: 2026-02-08
**Maintained By**: SCM Python SDK Team
