# SCM Python SDK

[![PyPI version](https://img.shields.io/pypi/v/scm-python.svg)](https://pypi.org/project/scm-python/) [![Python versions](https://img.shields.io/pypi/pyversions/scm-python.svg)](https://pypi.org/project/scm-python/) [![License](https://img.shields.io/pypi/l/scm-python.svg)](https://github.com/PaloAltoNetworks/scm-python/blob/main/LICENSE)

Auto-generated Python SDK for [Palo Alto Networks Strata Cloud Manager (SCM)](https://www.paloaltonetworks.com/strata-cloud-manager).

## Beta Release Disclaimer

**This software is a pre-release version and is not ready for production use.**

*   **No Warranty:** This software is provided "as is," without any warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose.
*   **Instability:** The beta software may contain defects, may not operate correctly, and may be substantially modified or withdrawn at any time.
*   **Limitation of Liability:** In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the beta software or the use or other dealings in the beta software.
*   **Feedback:** We encourage and appreciate your feedback and bug reports. However, you acknowledge that any feedback you provide is non-confidential.

By using this software, you agree to these terms.
---


## Warranty
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

THIS SOFTWARE IS RELEASED AS A PROOF OF CONCEPT FOR EXPERIMENTAL PURPOSES ONLY. USE IT AT OWN RISK. THIS SOFTWARE IS NOT SUPPORTED.

## Table of contents

- [Installation](#installation)
- [Using scm-python](#using-scm-python)
- [Configuration File](#configuration-file)
- [Basic Usage Example](#basic-usage-example)

## Installation

Install the released version from PyPI:

```bash
pip install scm-python
```

Install from source (latest `main`):

```bash
pip install git+https://github.com/PaloAltoNetworks/scm-python.git
```

For local development (after cloning):

```bash
pip install -e ".[dev]"
```

## Using scm-python

### Configuration File

Create a configuration file at `config/scm-config.json` in the project root, or specify a custom path via `SCM_CONFIG_FILE` environment variable:

```json
{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "scope": "tsg_id:1234567890",
  "host": "api.sase.paloaltonetworks.com",
  "auth_url": "https://auth.apps.paloaltonetworks.com",
  "protocol": "https",
  "logging": "ERROR"
}
```

### Basic Usage Example

```python
from scm import Scm

# Initialize the client (loads config/scm-config.json or SCM_CONFIG_FILE)
client = Scm()

# Or specify config explicitly
client = Scm(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    tsg_id="YOUR_TSG_ID"
)

# Or pass a pre-existing JWT token directly (see "Direct JWT Passing" section below)
client = Scm(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    tsg_id="YOUR_TSG_ID",
    jwt="eyJ0eXAiOiJKV1Qi...",
    jwt_expires_at="2027-01-01T10:30:00Z",
    jwt_lifetime=900
)

# Example: List addresses
addresses_api = client.objects.AddressesApi(client.objects.api_client)
response = addresses_api.list_addresses(folder="All")

# Print the first address
if response.data and len(response.data) > 0:
    first_address = response.data[0]
    print(f"Address Name: {first_address.name}")
    if hasattr(first_address, 'ip_netmask') and first_address.ip_netmask:
        print(f"IP/Netmask: {first_address.ip_netmask}")
    if hasattr(first_address, 'fqdn') and first_address.fqdn:
        print(f"FQDN: {first_address.fqdn}")
else:
    print("No addresses found")
```

### Environment Variables

The SDK supports multiple configuration methods with the following priority:
1. Constructor arguments
2. Environment variables
3. JSON configuration file

**Preferred (consistent with scm-go SDK):**
- `SCM_CLIENT_ID`: Client ID for authentication
- `SCM_CLIENT_SECRET`: Client secret for authentication
- `SCM_SCOPE`: Scope in format "tsg_id:XXXXX" (e.g., "tsg_id:1234567890")
- `SCM_HOST`: API host (default: api.sase.paloaltonetworks.com)
- `SCM_AUTH_URL`: Authentication URL (default: https://auth.apps.paloaltonetworks.com)
- `SCM_LOGGING`: Logging level (ERROR, WARNING, INFO, DEBUG)
- `SCM_CONFIG_FILE`: Path to JSON configuration file

**Backward Compatibility:**
- `SCM_TSG_ID`: TSG ID (automatically converted to scope format)
- `SCM_LOG_LEVEL`: Same as SCM_LOGGING

## Authentication & JWT Token Management

### Direct JWT Passing

The SDK supports passing pre-existing JWT tokens directly to the client constructor, matching the behavior of the scm-go SDK. This is useful for scenarios where you want to avoid authentication API rate limits or have a centralized token management service.

**Constructor Parameters:**

```python
from scm import Scm
from datetime import datetime, timedelta

# Pass JWT as constructor parameters
client = Scm(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    tsg_id="YOUR_TSG_ID",
    jwt="eyJ0eXAiOiJKV1Qi...",                    # JWT token string
    jwt_expires_at="2027-01-01T10:30:00Z",        # ISO format string
    jwt_lifetime=900                               # Lifetime in seconds
)

# Also accepts datetime object for jwt_expires_at
client = Scm(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    tsg_id="YOUR_TSG_ID",
    jwt="eyJ0eXAiOiJKV1Qi...",
    jwt_expires_at=datetime.now() + timedelta(minutes=15),
    jwt_lifetime=900
)
```

**JWT Token Priority:**

The SDK follows this priority order when loading JWT tokens:

1. **Constructor arguments** (highest priority) - JWT passed directly to `Scm()` constructor
2. **Config file** - JWT loaded from `config/scm-config.json` or `SCM_CONFIG_FILE`
3. **Fetch new token** (lowest priority) - Fetch from authentication API if no valid token available

This matches the scm-go SDK behavior and provides maximum flexibility.

**Use Cases:**

1. **External Token Manager:**
   ```python
   # Token manager process fetches and caches tokens
   def token_manager():
       client = Scm()
       while True:
           if client.token_expires_soon:
               new_token = client.refresh_token()
               # Store in shared cache (Redis, file, etc.)
               cache.set("jwt", client._access_token)
               cache.set("jwt_expires_at", client._token_expires_at.isoformat())
               cache.set("jwt_lifetime", client._jwt_lifetime)
           time.sleep(300)
   
   # Worker processes use cached token
   worker_client = Scm(
       client_id="YOUR_ID",
       client_secret="YOUR_SECRET",
       tsg_id="YOUR_TSG",
       jwt=cache.get("jwt"),
       jwt_expires_at=cache.get("jwt_expires_at"),
       jwt_lifetime=cache.get("jwt_lifetime")
   )
   # ✅ No auth API call - uses cached token
   ```

2. **Serverless Functions (Lambda, Cloud Functions):**
   ```python
   # Lambda handler - token stored in environment variable
   def lambda_handler(event, context):
       client = Scm(
           client_id=os.environ["CLIENT_ID"],
           client_secret=os.environ["CLIENT_SECRET"],
           tsg_id=os.environ["TSG_ID"],
           jwt=os.environ["CACHED_JWT"],
           jwt_expires_at=os.environ["JWT_EXPIRES_AT"],
           jwt_lifetime=int(os.environ["JWT_LIFETIME"])
       )
       # ✅ Fast startup - no auth API call
   
       addresses_api = client.objects.AddressesApi(client.objects.api_client)
       addresses = addresses_api.list_addresses(folder="Texas")
       return addresses
   ```

3. **Testing with Mock Tokens:**
   ```python
   # Unit tests with pre-set token
   def test_api_call():
       mock_jwt = "test_token_12345"
       mock_expires = "2099-12-31T23:59:59Z"
   
       client = Scm(
           client_id="test",
           client_secret="test",
           tsg_id="test",
           jwt=mock_jwt,
           jwt_expires_at=mock_expires,
           jwt_lifetime=999999
       )
       # ✅ No real auth API call in tests
   ```

**Benefits:**

- **Reduced Auth API Load**: 1 token manager → 10 workers = 1 auth call instead of 10 (90% reduction)
- **Faster Startup**: ~50ms initialization (vs ~500ms with auth API call) - 10x faster
- **Better for Serverless**: Cold starts are faster, can pre-warm tokens
- **Full scm-go Parity**: Same capabilities as Go SDK

### Automatic Token Refresh

The SDK automatically refreshes JWT tokens before they expire, ensuring uninterrupted API access.

**How It Works:**

1. **Pre-Request Check**: Before each API call, checks if token expires within 60 seconds
2. **Automatic Refresh**: If expiring soon, refreshes token automatically
3. **401 Retry**: If API returns 401 (unauthorized), refreshes token and retries once
4. **Thread-Safe**: Multiple threads can safely refresh tokens concurrently

**Features:**

- **Exponential Backoff**: 5 retries with backoff (1s → 2s → 4s → 8s → 10s capped)
- **401 Retry Protection**: Prevents infinite retry loops with back-to-back detection
- **Thread-Safe Refresh**: Uses `threading.Lock` to prevent duplicate refreshes
- **60-Second Buffer**: Proactively refreshes before token actually expires

**Manual Refresh:**

You can also manually trigger a token refresh:

```python
from scm import Scm

client = Scm(
    client_id="YOUR_ID",
    client_secret="YOUR_SECRET",
    tsg_id="YOUR_TSG"
)

# Check if token is expiring soon
if client.token_expires_soon:
    print("Token expiring soon, refreshing...")
    new_token = client.refresh_token()
    print(f"New token: {new_token[:50]}...")
```

## JWT Token Caching for Concurrent Operations

### Overview

The Strata Cloud Manager authentication API has rate limits on token requests (approximately 10 concurrent requests per tenant). When running multiple concurrent operations (e.g., parallel Python scripts, CI/CD pipelines), these rate limits can cause authentication failures.

To work around this limitation, you can implement a token caching solution that allows multiple client instances to share the same JWT token.

### How It Works

The scm-python SDK supports loading JWT tokens from the configuration file. The following fields can be included in your `config/scm-config.json`:

**Preferred format (consistent with scm-go):**

```json
{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "scope": "tsg_id:1234567890",
  "host": "api.sase.paloaltonetworks.com",
  "jwt": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "jwt_expires_at": "2027-01-01T10:30:00Z",
  "jwt_lifetime": 900
}
```

**Backward compatible format:**

```json
{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "tsg_id": "1234567890",
  "host": "api.sase.paloaltonetworks.com",
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_expires_at": "2027-01-01T10:30:00Z"
}
```

**Important Security Note**: Only share JWT tokens among client instances that use the **same** `client_id` and `client_secret`. Different service principals with different RBAC permissions should never share tokens, as this would be a privilege escalation risk.

### Token Caching Features

The SDK includes the following enhancements for production use:

1. **Automatic Token Caching**: Reads cached JWT from config file if valid
2. **Automatic Token Refresh**: Transparently refreshes tokens before API calls (see "Automatic Token Refresh" section above)
3. **Expiration Buffer**: 60-second buffer before token expiry (avoids edge cases)
4. **Retry Logic**: Exponential backoff for auth failures (5 retries: 1s → 2s → 4s → 8s → 10s)
5. **401 Retry**: Automatically retries API calls once on 401 errors (with back-to-back protection)
6. **Thread-Safe Refresh**: Uses `threading.Lock` to prevent duplicate concurrent refreshes
7. **Manual Refresh**: `client.refresh_token()` method for long-running scripts
8. **Expiration Check**: `client.token_expires_soon` property
9. **Direct JWT Passing**: Pass JWT as constructor parameters (see "Direct JWT Passing" section above)

### Using Token Refresh

```python
from scm import Scm
import time

client = Scm(
    client_id="YOUR_ID",
    client_secret="YOUR_SECRET",
    tsg_id="YOUR_TSG"
)

# Long-running script
while True:
    if client.token_expires_soon:
        print("Token expiring soon, refreshing...")
        client.refresh_token()

    # Do work...
    # ... your API calls here ...
    time.sleep(300)  # Sleep 5 minutes between iterations
```

### Example Token Caching Implementations

Below are sample implementations of token caching services. These are provided as **examples only** and should be adapted to your specific security requirements and infrastructure.

#### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       Token Caching Architecture                         │
└─────────────────────────────────────────────────────────────────────────┘

                         ┌──────────────────────┐
                         │   SCM Auth API       │
                         │  (Rate Limited ~10   │
                         │  concurrent requests)│
                         └──────────┬───────────┘
                                    │
                                    │ 1. Fetch JWT Token
                                    │    (Once every 10-12 min)
                                    │
                         ┌──────────▼───────────┐
                         │  Token Cache Service │
                         │   (Cron Job/Timer)   │
                         │                      │
                         │  • Checks expiration │
                         │  • Fetches new token │
                         │  • Updates config    │
                         └──────────┬───────────┘
                                    │
                                    │ 2. Write (Atomic)
                                    │    jwt + jwt_expires_at
                                    │
                         ┌──────────▼───────────┐
                         │                      │
                         │  Shared Config File  │
                         │ config/scm-config.json │
                         │                      │
                         └──────────┬───────────┘
                                    │
                         ┌──────────┴───────────┐
                         │                      │
           3. Read       │     3. Read          │     3. Read
         ┌───────────────┤                      ├──────────────┐
         │               │                      │              │
    ┌────▼────┐    ┌────▼────┐           ┌────▼────┐    ┌────▼────┐
    │  SDK    │    │  SDK    │    ...    │  SDK    │    │  SDK    │
    │Instance │    │Instance │           │Instance │    │Instance │
    │    1    │    │    2    │           │   49    │    │   50    │
    └─────────┘    └─────────┘           └─────────┘    └─────────┘
```

**How It Works:**

1. **Token Cache Service** (cron job/systemd timer) runs every 10-12 minutes
   - Checks if cached token is expired or expiring soon (60s buffer)
   - Fetches new JWT token from SCM Auth API if needed
   - Writes updated token to shared config file (atomic write operation)

2. **Shared Config File** (config/scm-config.json or SCM_CONFIG_FILE)
   - Contains `client_id`, `client_secret`, and cached `jwt` fields
   - Updated atomically by token cache service
   - Read by all SDK client instances

3. **Multiple SDK Client Instances** (concurrent operations)
   - Each instance reads the shared config file on initialization
   - Uses cached JWT token (no API call needed)
   - Can run unlimited concurrent operations without hitting rate limits
   - All instances must use the same `client_id`/`client_secret`

**Disclaimer**: This example code is provided "as is" without warranty. It is intended as a reference implementation only. You are responsible for ensuring it meets your organization's security and operational requirements.

#### Example: Python Token Cache Service

```python
#!/usr/bin/env python3
"""
SCM Token Cache Service
Fetches and caches JWT tokens for concurrent SCM operations
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from scm import Scm

def atomic_write(path: Path, data: dict):
    """Write file atomically using temp file + rename"""
    temp_path = path.with_suffix('.tmp')
    with open(temp_path, 'w') as f:
        json.dump(data, f, indent=2)
    temp_path.replace(path)

def should_refresh_token(config_path: Path) -> bool:
    """Check if token needs refresh (missing, expired, or expiring soon)"""
    if not config_path.exists():
        return True

    try:
        with open(config_path) as f:
            config = json.load(f)

        # No JWT cached
        if not config.get('jwt'):
            return True

        # Check expiration with 120s buffer (double the SDK buffer for safety)
        expires_at_str = config.get('jwt_expires_at')
        if not expires_at_str:
            return True

        expires_at = datetime.fromisoformat(expires_at_str.replace('Z', '+00:00'))
        buffer = timedelta(seconds=120)

        return datetime.now(expires_at.tzinfo) >= (expires_at - buffer)

    except Exception as e:
        print(f"Error checking token: {e}", file=sys.stderr)
        return True

def refresh_and_cache_token(config_path: Path):
    """Fetch new token and update config file"""
    try:
        # Initialize SDK client (will fetch token)
        client = Scm()

        # Build config with fresh token
        config = {
            "client_id": client.client_id,
            "client_secret": client.client_secret,
            "host": client.host,
            "auth_url": client.auth_url,
            "protocol": "https",
            "scope": f"tsg_id:{client.tsg_id}",
            "logging": "ERROR",
            "jwt": client._access_token,
            "jwt_expires_at": client._token_expires_at.isoformat(),
            "jwt_lifetime": client._jwt_lifetime
        }

        # Atomic write to prevent race conditions
        atomic_write(config_path, config)
        print(f"Token refreshed successfully, expires at {config['jwt_expires_at']}")

    except Exception as e:
        print(f"Failed to refresh token: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main entry point"""
    config_path = Path(os.getenv('SCM_CONFIG_FILE',
                                  'config/scm-config.json'))

    if should_refresh_token(config_path):
        print("Token expired or expiring soon, refreshing...")
        refresh_and_cache_token(config_path)
    else:
        print("Token still valid, skipping refresh")

if __name__ == '__main__':
    main()
```

**Usage:**

```bash
# Set permissions
chmod +x /path/to/token_cache_service.py

# Test run
/usr/bin/python3 /path/to/token_cache_service.py

# Add to cron (runs every 10 minutes)
*/10 * * * * /usr/bin/python3 /path/to/token_cache_service.py
```

### Best Practices

1. **Token Caching Service**: Implement a separate service that refreshes tokens and updates the config file
2. **File Permissions**: Restrict config file access (e.g., `chmod 600 config/scm-config.json`)
3. **Expiration Buffer**: The SDK automatically uses a 60-second buffer (configurable via `Scm.TOKEN_EXPIRY_BUFFER`)
4. **Error Handling**: Handle token refresh failures gracefully with retry logic
5. **Security Isolation**: Each unique `client_id`/`client_secret` pair should have its own token cache file
6. **Atomic Writes**: Write to temporary file then rename to avoid partial reads
7. **Monitoring**: Log token refreshes to detect authentication issues early

### Related Resources

- [GitHub Issue #77: Limited concurrent IaC operations](https://github.com/PaloAltoNetworks/terraform-provider-scm/issues/77)
- [GitHub Issue #13: Allow passing JWTs to client](https://github.com/PaloAltoNetworks/scm-go/issues/13)

## Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=scm --cov-report=html
```

### Project Structure

```
scm-python/
├── scm/
│   ├── __init__.py          # Main Scm client
│   ├── config_setup/        # Config setup API
│   ├── deployment_services/ # Deployment services API
│   ├── device_settings/     # Device settings API
│   ├── identity_services/   # Identity services API
│   ├── network_services/    # Network services API
│   ├── objects/             # Objects API
│   └── security_services/   # Security services API
├── config/
│   └── scm-config.json      # Local config (gitignored)
└── README.md
```

## Quick Start Examples

### Create an Address

```python
from scm import Scm
from scm.objects.models.addresses import Addresses

# Initialize client
client = Scm()
addresses_api = client.objects.AddressesApi(client.objects.api_client)

# Create IP netmask address
address = Addresses(
    id="",
    name="web-server-01",
    folder="Texas",
    ip_netmask="192.168.1.10/32",
    description="Production web server",
    tag=["Production", "Web"]
)

created = addresses_api.create_addresses(addresses=address)
print(f"Created address: {created.name} (ID: {created.id})")
```

### Fetch Address by Name

```python
# Fetch single address by name (with auto-pagination)
address = addresses_api.fetch_addresses(
    name="web-server-01",
    folder="Texas"
)

if address:
    print(f"Found: {address.name} - {address.ip_netmask}")
else:
    print("Address not found")
```

### List All Addresses with Pagination

```python
# Get all addresses using pagination
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

print(f"Total addresses: {len(all_addresses)}")
```

### Update an Address

```python
# Fetch existing address
address = addresses_api.fetch_addresses(name="web-server-01", folder="Texas")

# Modify fields
address.ip_netmask = "192.168.1.20/32"
address.description = "Migrated web server"

# Update
updated = addresses_api.update_addresses_by_id(
    id=address.id,
    addresses=address
)
print(f"Updated: {updated.name}")
```

### Delete an Address

```python
from scm.exceptions import ObjectNotPresentError, ReferenceNotZeroError

try:
    addresses_api.delete_addresses_by_id(id=address.id)
    print(f"Deleted address: {address.id}")
except ReferenceNotZeroError:
    print("Cannot delete - address is referenced elsewhere")
except ObjectNotPresentError:
    print("Address already deleted or not found")
```

### Create Security Rule

```python
from scm.security_services.models.security_rules import SecurityRules

security_rules_api = client.security_services.SecurityRulesApi(
    client.security_services.api_client
)

rule = SecurityRules(
    id="",
    name="allow-web-traffic",
    folder="Texas",
    source=["Trust-Zone"],
    source_user=["any"],
    destination=["Untrust-Zone"],
    application=["web-browsing", "ssl"],
    service=["application-default"],
    action="allow",
    log_setting="Cortex Data Lake",
    description="Allow web browsing from trust zone"
)

# Note: position is an API parameter, not a model field
created = security_rules_api.create_security_rules(position="pre", security_rules=rule)
print(f"Created security rule: {created.name}")
```

## Exception Handling

The SDK provides custom exceptions for common API errors:

```python
from scm.exceptions import (
    ObjectNotPresentError,      # 404 - Object not found
    NameNotUniqueError,         # 409 - Name already exists
    InvalidObjectError,         # 400 - Invalid object configuration
    ReferenceNotZeroError,      # 409 - Object is referenced elsewhere
    MissingQueryParameterError, # 400 - Missing required parameter
    ScmException                # Base exception class
)

try:
    address = addresses_api.create_addresses(addresses=address)
except NameNotUniqueError as e:
    print(f"Address name already exists: {e.object_name}")
except InvalidObjectError as e:
    print(f"Invalid address configuration: {e.message}")
    print(f"Details: {e.details}")
except ScmException as e:
    print(f"SCM API error: {e.message} (code: {e.error_code})")
```

All exceptions are automatically raised by decorators - you never need to manually parse errors.

## Compatibility

This SDK is **not compatible** with [pan-scm-sdk](https://github.com/cdot65/pan-scm-sdk). They use different API clients, model structures, and authentication patterns. There is no migration path — this is a separate, independently generated SDK.

## Features

- **Auto-generated from OpenAPI specs** - Always up-to-date with latest API
- **Pydantic v2 models** - Strong typing and validation
- **Automatic exception handling** - Custom exceptions for all error types
- **fetch() method** - Fetch single objects by name with auto-pagination
- **Token caching** - Share tokens across multiple processes
- **Automatic token refresh** - Transparent token management
- **Comprehensive test coverage** - Continuously tested against live SCM API
- **Thread-safe** - Safe for concurrent operations

## Support

This is auto-generated code provided as-is for experimental purposes. See [SUPPORT.md](SUPPORT.md) for the support policy.

For issues or questions:

1. Check the [GitHub Issues](https://github.com/PaloAltoNetworks/scm-python/issues)
2. Review the [documentation](docs/)

## License

This software is provided "as is" without warranty. See LICENSE file for details.
