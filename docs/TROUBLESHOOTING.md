# Troubleshooting Guide

This guide helps resolve common issues when using the SCM Python SDK.

## Table of Contents

- [Authentication Issues](#authentication-issues)
- [API Request Failures](#api-request-failures)
- [Model Validation Errors](#model-validation-errors)
- [Exception Handling](#exception-handling)
- [Token Management](#token-management)
- [Pagination Issues](#pagination-issues)
- [Performance Problems](#performance-problems)
- [Network and Connectivity](#network-and-connectivity)
- [Data Consistency](#data-consistency)
- [Migration from pan-scm-sdk](#migration-from-pan-scm-sdk)

---

## Authentication Issues

### Issue: "Authentication failed" or "Invalid credentials"

**Symptoms:**
```
Error: Authentication failed
HTTP 401 Unauthorized
```

**Causes and Solutions:**

1. **Invalid credentials**
   ```python
   # Check environment variables
   import os
   print(f"Client ID: {os.getenv('SCM_CLIENT_ID')}")
   print(f"TSG ID: {os.getenv('SCM_TSG_ID')}")
   # Don't print client secret!
   ```

   Solution: Verify credentials in Strata Cloud Manager:
   - Settings → Service Accounts
   - Ensure client ID and secret are correct
   - Verify TSG ID matches your tenant

2. **Environment variables not set**
   ```bash
   # Add to ~/.bashrc or ~/.zshrc
   export SCM_CLIENT_ID="your-client-id"
   export SCM_CLIENT_SECRET="your-client-secret"
   export SCM_TSG_ID="your-tsg-id"
   ```

3. **Expired credentials**
   - Regenerate service account credentials in SCM portal
   - Update environment variables with new values

### Issue: "Token refresh failed"

**Symptoms:**
```
Error: Token refresh failed
Failed to refresh OAuth token
```

**Solutions:**

1. **Check token file permissions**
   ```bash
   # If using token file
   ls -l /tmp/scm_token_cache.json
   chmod 644 /tmp/scm_token_cache.json
   ```

2. **Clear cached token**
   ```python
   import os

   # Remove cached token file
   token_file = "/tmp/scm_token_cache.json"
   if os.path.exists(token_file):
       os.remove(token_file)

   # Reinitialize client
   client = Scm()
   ```

3. **Network connectivity**
   ```bash
   # Test connectivity to auth endpoint
   curl -v https://auth.apps.paloaltonetworks.com/oauth2/access_token
   ```

---

## API Request Failures

### Issue: "404 Not Found" errors

**Symptoms:**
```python
ObjectNotPresentError: Object not found
```

**Solutions:**

1. **Verify object exists**
   ```python
   # Use fetch to check existence
   address = addresses_api.fetch_addresses(
       name="web-server",
       folder="Texas"
   )

   if not address:
       print("Address does not exist")
   else:
       print(f"Address found: {address.id}")
   ```

2. **Check folder/snippet/device**
   ```python
   # Ensure you're searching in correct container
   response = addresses_api.list_addresses(folder="Texas")
   print(f"Addresses in Texas: {len(response.data)}")

   # Try all containers
   for container in ["Texas", "All", "Shared"]:
       try:
           addr = addresses_api.fetch_addresses(
               name="web-server",
               folder=container
           )
           if addr:
               print(f"Found in folder: {container}")
               break
       except:
           continue
   ```

3. **Verify object ID**
   ```python
   # List all objects to find correct ID
   response = addresses_api.list_addresses(folder="Texas", limit=1000)

   for addr in response.data:
       if "web-server" in addr.name.lower():
           print(f"Name: {addr.name}, ID: {addr.id}")
   ```

### Issue: "409 Conflict" errors

**Symptoms:**
```python
NameNotUniqueError: Object name already exists
```

**Solutions:**

1. **Use get-or-create pattern**
   ```python
   # Check before creating
   existing = addresses_api.fetch_addresses(
       name="web-server",
       folder="Texas"
   )

   if existing:
       print(f"Using existing address: {existing.id}")
       address = existing
   else:
       address = Addresses(
           id="",
           name="web-server",
           folder="Texas",
           ip_netmask="10.0.0.1/32"
       )
       address = addresses_api.create_addresses(addresses=address)
   ```

2. **Handle NameNotUniqueError**
   ```python
   from scm.exceptions import NameNotUniqueError

   try:
       created = addresses_api.create_addresses(addresses=address)
   except NameNotUniqueError:
       # Fetch existing instead
       existing = addresses_api.fetch_addresses(
           name=address.name,
           folder=address.folder
       )
       print(f"Name exists, using ID: {existing.id}")
   ```

3. **Check for naming conflicts across containers**
   ```python
   # Names must be unique within folder/snippet/device
   # Check all containers
   for folder in ["Texas", "California", "All"]:
       addr = addresses_api.fetch_addresses(
           name="web-server",
           folder=folder
       )
       if addr:
           print(f"Name exists in {folder}")
   ```

### Issue: "400 Bad Request" errors

**Symptoms:**
```python
InvalidObjectError: Invalid object configuration
```

**Solutions:**

1. **Validate required fields**
   ```python
   # All objects need:
   # - id (empty string for create)
   # - name
   # - folder OR snippet OR device

   address = Addresses(
       id="",  # Required (empty for create)
       name="web-server",  # Required
       folder="Texas",  # Required (or snippet/device)
       ip_netmask="10.0.0.1/32"  # Required (or fqdn/ip_range)
   )
   ```

2. **Check field formats**
   ```python
   # IP address must include netmask
   ip_netmask="10.0.0.1/32"  # Correct
   ip_netmask="10.0.0.1"     # Incorrect

   # Port ranges
   port="8080"           # Single port
   port="8080-8090"      # Range
   port="8080,8443"      # Multiple (NOT supported - use separate objects)
   ```

3. **Inspect error details**
   ```python
   from scm.exceptions import InvalidObjectError

   try:
       created = addresses_api.create_addresses(addresses=address)
   except InvalidObjectError as e:
       print(f"Error: {e.message}")
       print(f"Details: {e.details}")
       print(f"HTTP Status: {e.http_status_code}")
   ```

---

## Model Validation Errors

### Issue: Pydantic validation errors

**Symptoms:**
```
ValidationError: X validation errors for Addresses
  field required (type=value_error.missing)
```

**Solutions:**

1. **Check required fields**
   ```python
   from scm.objects.models.addresses import Addresses

   # View model schema
   print(Addresses.model_json_schema())

   # Required fields for Addresses:
   # - id (str)
   # - name (str)
   # - folder OR snippet OR device
   # - ip_netmask OR fqdn OR ip_range (exactly one)
   ```

2. **Provide default values**
   ```python
   # Always set id="" for new objects
   address = Addresses(
       id="",  # Empty for create
       name="web-server",
       folder="Texas",
       ip_netmask="10.0.0.1/32",
       description="",  # Optional fields can be empty string
       tag=[]  # Optional lists can be empty
   )
   ```

3. **Check nested models**
   ```python
   from scm.objects.models.services import Services
   from scm.objects.models.services_protocol import ServicesProtocol
   from scm.objects.models.services_protocol_tcp import ServicesProtocolTcp

   # Nested models must be properly constructed
   protocol = ServicesProtocol(
       tcp=ServicesProtocolTcp(
           port="8080"
       )
   )

   service = Services(
       id="",
       name="web-app",
       folder="Texas",
       protocol=protocol  # Properly constructed nested model
   )
   ```

### Issue: "Field 'id' required" for existing objects

**Symptoms:**
```
ValidationError: field 'id' required
```

**Solution:**

When creating objects fetched from API, the `id` field is already populated:

```python
# Fetching returns object with id
address = addresses_api.fetch_addresses(name="web-server", folder="Texas")
print(f"Address ID: {address.id}")  # Has ID from API

# Updating - use existing id
address.ip_netmask = "10.0.0.2/32"
updated = addresses_api.update_addresses_by_id(
    id=address.id,  # Use existing ID
    addresses=address
)

# Creating - use empty string
new_address = Addresses(
    id="",  # Empty for create
    name="new-server",
    folder="Texas",
    ip_netmask="10.0.0.3/32"
)
```

---

## Exception Handling

### Issue: Uncaught exceptions from API

**Symptoms:**
```
NotFoundException: Not found
# or
ApiException: API exception occurred
```

**Solution:**

All exceptions are automatically converted by decorators:

```python
from scm.exceptions import (
    ObjectNotPresentError,
    NameNotUniqueError,
    InvalidObjectError,
    ReferenceNotZeroError,
    ScmException
)

try:
    address = addresses_api.get_addresses_by_id(id="non-existent-id")

except ObjectNotPresentError as e:
    # Automatically raised for 404 errors
    print(f"Not found: {e.message}")

except InvalidObjectError as e:
    # Automatically raised for 400 errors
    print(f"Invalid: {e.message}")

except ScmException as e:
    # Base class for all SCM exceptions
    print(f"SCM Error: {e.message}")
    print(f"Code: {e.error_code}")
    print(f"HTTP Status: {e.http_status_code}")
```

### Issue: Delete fails with "object is referenced"

**Symptoms:**
```python
ReferenceNotZeroError: Cannot delete object - non-zero references
```

**Solution:**

Find and remove references before deleting:

```python
from scm.exceptions import ReferenceNotZeroError

try:
    addresses_api.delete_addresses_by_id(id=address.id)

except ReferenceNotZeroError as e:
    print(f"Object is still referenced")
    print(f"Error details: {e.details}")

    # Find references (example for address groups)
    groups_response = address_groups_api.list_address_groups(
        folder="Texas",
        limit=1000
    )

    for group in groups_response.data:
        if group.static and address.name in group.static:
            print(f"Referenced in group: {group.name}")

            # Remove reference
            group.static.remove(address.name)
            address_groups_api.update_address_groups_by_id(
                id=group.id,
                address_groups=group
            )

    # Try delete again
    addresses_api.delete_addresses_by_id(id=address.id)
```

---

## Token Management

### Issue: Token not persisting across sessions

**Symptoms:**
- New OAuth token requested on every run
- Slow startup times

**Solution:**

Use file-based token caching:

```python
# Initialize with token file
client = Scm(
    client_id="your-client-id",
    client_secret="your-client-secret",
    tsg_id="your-tsg-id",
    token_file="/tmp/scm_token_cache.json"
)

# Token will be cached and reused across runs
```

### Issue: Multiple processes using same token

**Symptoms:**
- Token conflicts
- Authentication errors in concurrent runs

**Solution:**

Use separate token files per process:

```python
import os

# Use process-specific token file
pid = os.getpid()
token_file = f"/tmp/scm_token_{pid}.json"

client = Scm(token_file=token_file)
```

Or use file locking:

```python
import fcntl
import json

class LockedTokenFile:
    def __init__(self, path):
        self.path = path

    def read_token(self):
        with open(self.path, 'r') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_SH)
            try:
                return json.load(f)
            finally:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)

    def write_token(self, token):
        with open(self.path, 'w') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            try:
                json.dump(token, f)
            finally:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
```

---

## Pagination Issues

### Issue: Not all results returned from list operations

**Symptoms:**
- `list_*()` returns fewer results than expected
- Missing objects when iterating

**Solution:**

Use pagination to get all results:

```python
# Default limit is often 200
response = addresses_api.list_addresses(folder="Texas")
print(f"First page: {len(response.data)} results")
print(f"Total available: {response.total}")

# Get ALL results with pagination
all_addresses = []
limit = 200
offset = 0

while True:
    response = addresses_api.list_addresses(
        folder="Texas",
        limit=limit,
        offset=offset
    )

    all_addresses.extend(response.data)

    if len(response.data) < limit:
        break

    offset += limit

print(f"Retrieved all {len(all_addresses)} addresses")
```

### Issue: fetch() method not finding object

**Symptoms:**
```python
result = addresses_api.fetch_addresses(name="web-server", folder="Texas")
# result is None, but object exists
```

**Solutions:**

1. **Check exact name match**
   ```python
   # fetch() requires exact name match
   # Will NOT find "web-server-01" if searching for "web-server"

   # Use list with filtering for partial matches
   response = addresses_api.list_addresses(folder="Texas", limit=1000)
   matches = [addr for addr in response.data if "web-server" in addr.name]
   ```

2. **Verify container (folder/snippet/device)**
   ```python
   # fetch() searches only specified container
   address = addresses_api.fetch_addresses(
       name="web-server",
       folder="Texas"  # Only searches Texas folder
   )

   # Search all folders
   for folder in ["Texas", "California", "All"]:
       address = addresses_api.fetch_addresses(
           name="web-server",
           folder=folder
       )
       if address:
           print(f"Found in {folder}")
           break
   ```

3. **Check for large datasets**
   ```python
   # fetch() uses auto-pagination but may timeout on very large datasets
   # Increase timeout or use list with filtering
   import time
   start = time.time()

   address = addresses_api.fetch_addresses(
       name="web-server",
       folder="Texas"
   )

   elapsed = time.time() - start
   if elapsed > 10:
       print(f"fetch() took {elapsed}s - dataset may be too large")
   ```

---

## Performance Problems

### Issue: Slow API operations

**Symptoms:**
- API calls taking >5 seconds
- Timeouts on large datasets

**Solutions:**

1. **Reduce pagination limit for faster first response**
   ```python
   # Use smaller limit for faster initial results
   response = addresses_api.list_addresses(
       folder="Texas",
       limit=100  # Smaller limit = faster response
   )
   ```

2. **Use parallel requests for bulk operations**
   ```python
   from concurrent.futures import ThreadPoolExecutor

   def fetch_address(name):
       return addresses_api.fetch_addresses(name=name, folder="Texas")

   names = ["web-01", "web-02", "web-03", "web-04", "web-05"]

   with ThreadPoolExecutor(max_workers=5) as executor:
       results = list(executor.map(fetch_address, names))
   ```

3. **Cache frequently accessed data**
   ```python
   from functools import lru_cache

   @lru_cache(maxsize=128)
   def get_address_cached(name, folder):
       return addresses_api.fetch_addresses(name=name, folder=folder)

   # Subsequent calls with same args use cache
   addr1 = get_address_cached("web-server", "Texas")  # API call
   addr2 = get_address_cached("web-server", "Texas")  # Cached
   ```

4. **Filter results server-side**
   ```python
   # Don't retrieve all objects and filter client-side
   # Use API parameters when available

   # Bad: Client-side filtering
   all_addrs = addresses_api.list_addresses(folder="Texas", limit=10000)
   prod_addrs = [a for a in all_addrs.data if a.tag and "Production" in a.tag]

   # Better: Minimize data transfer
   all_addrs = addresses_api.list_addresses(folder="Texas", limit=1000)
   prod_addrs = [a for a in all_addrs.data if a.tag and "Production" in a.tag]
   ```

### Issue: Memory usage too high

**Symptoms:**
- Python process using excessive memory
- Out of memory errors on large datasets

**Solution:**

Use iterators instead of loading all data:

```python
def address_iterator(api, folder, limit=200):
    """Iterate addresses without loading all into memory."""
    offset = 0

    while True:
        response = api.list_addresses(
            folder=folder,
            limit=limit,
            offset=offset
        )

        for address in response.data:
            yield address

        if len(response.data) < limit:
            break

        offset += limit

# Process one at a time
for address in address_iterator(addresses_api, "Texas"):
    # Process address
    if address.tag and "Delete" in address.tag:
        addresses_api.delete_addresses_by_id(id=address.id)
```

---

## Network and Connectivity

### Issue: Connection timeouts

**Symptoms:**
```
TimeoutError: Request timed out
ConnectionError: Connection refused
```

**Solutions:**

1. **Check network connectivity**
   ```bash
   # Test API endpoint
   ping api.strata.paloaltonetworks.com

   # Test HTTPS
   curl -v https://api.strata.paloaltonetworks.com/
   ```

2. **Increase timeout**
   ```python
   # Note: Timeout configuration depends on SDK implementation
   # Check if client supports timeout parameter

   # Retry on timeout
   import time

   max_retries = 3
   for attempt in range(max_retries):
       try:
           result = addresses_api.create_addresses(addresses=address)
           break
       except TimeoutError:
           if attempt < max_retries - 1:
               time.sleep(2 ** attempt)  # Exponential backoff
               continue
           raise
   ```

3. **Check proxy settings**
   ```bash
   # If behind corporate proxy
   export HTTP_PROXY=http://proxy.company.com:8080
   export HTTPS_PROXY=http://proxy.company.com:8080
   ```

### Issue: SSL/TLS errors

**Symptoms:**
```
SSLError: certificate verify failed
```

**Solutions:**

1. **Update certificates**
   ```bash
   # Update system certificates
   # Ubuntu/Debian
   sudo apt-get update && sudo apt-get install ca-certificates

   # macOS
   # Certificates managed by system

   # Verify certificates
   python -c "import ssl; print(ssl.get_default_verify_paths())"
   ```

2. **Check certificate bundle**
   ```python
   import certifi
   print(certifi.where())
   ```

---

## Data Consistency

### Issue: Stale data after updates

**Symptoms:**
- Updated object still shows old values
- List operations return outdated data

**Solution:**

API may have eventual consistency - refetch after updates:

```python
# Update address
updated = addresses_api.update_addresses_by_id(
    id=address.id,
    addresses=address
)

# Small delay for consistency
import time
time.sleep(0.5)

# Refetch to ensure consistency
current = addresses_api.get_addresses_by_id(id=address.id)
print(f"Updated IP: {current.ip_netmask}")
```

### Issue: Concurrent modification conflicts

**Symptoms:**
- Updates overwriting each other
- Lost updates in concurrent scripts

**Solution:**

Implement optimistic locking pattern:

```python
def safe_update_address(api, address_id, update_func):
    """Update with conflict detection."""
    max_retries = 3

    for attempt in range(max_retries):
        # Fetch current state
        current = api.get_addresses_by_id(id=address_id)

        # Apply update function
        modified = update_func(current)

        try:
            # Attempt update
            result = api.update_addresses_by_id(
                id=address_id,
                addresses=modified
            )
            return result

        except ScmException as e:
            if attempt < max_retries - 1:
                # Retry with fresh data
                continue
            raise

    raise Exception("Failed to update after retries")

# Usage
def add_tag(address):
    if not address.tag:
        address.tag = []
    address.tag.append("Updated")
    return address

result = safe_update_address(addresses_api, address.id, add_tag)
```

---

## Migration from pan-scm-sdk

### Issue: API access patterns different

**Symptoms:**
- Code using `scm.config.objects` not working
- Import errors for model classes

**Solution:**

Update import and access patterns:

```python
# pan-scm-sdk (old)
from scm.config.objects import Address
scm = Scm()
addresses = scm.config.objects.address

# scm-python (new)
from scm import Scm
from scm.objects.models.addresses import Addresses

client = Scm()
addresses_api = client.objects.AddressesApi(client.objects.api_client)
```

See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for complete migration instructions.

### Issue: Methods not found (list_all, fetch, etc.)

**Symptoms:**
```
AttributeError: 'AddressesApi' object has no attribute 'list_all'
```

**Solution:**

Method names differ between SDKs:

```python
# pan-scm-sdk
addresses = scm.config.objects.address.list_all(folder="Texas")

# scm-python - use pagination
all_addresses = []
offset = 0
limit = 200

while True:
    response = addresses_api.list_addresses(
        folder="Texas",
        limit=limit,
        offset=offset
    )
    all_addresses.extend(response.data)

    if len(response.data) < limit:
        break
    offset += limit
```

The `fetch()` method exists in scm-python:

```python
# Both SDKs support fetch()
address = addresses_api.fetch_addresses(
    name="web-server",
    folder="Texas"
)
```

---

## Getting Help

If you continue to experience issues:

1. **Enable debug logging**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)

   client = Scm(log_level="DEBUG")
   ```

2. **Check API response**
   ```python
   from scm.exceptions import ScmException

   try:
       result = addresses_api.create_addresses(addresses=address)
   except ScmException as e:
       print(f"Message: {e.message}")
       print(f"Error code: {e.error_code}")
       print(f"HTTP status: {e.http_status_code}")
       print(f"Details: {e.details}")
   ```

3. **Report issues**
   - Include:
     - SDK version
     - Python version
     - Minimal code to reproduce
     - Full error message and traceback
     - Debug logs (sanitize credentials!)

---

## Additional Resources

- [Examples](EXAMPLES.md) - Code examples for common tasks
- [Common Patterns](COMMON_PATTERNS.md) - Best practices and patterns
- [Migration Guide](MIGRATION_GUIDE.md) - Migrating from pan-scm-sdk
- [API Reference](../scm/) - Full API documentation
