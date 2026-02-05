# SCM Python SDK

Auto-generated SDK for Palo Alto Networks Strata Cloud Manager.

[![PyPI version](https://badge.fury.io/py/scm-python.svg)](https://badge.fury.io/py/scm-python)

NOTE: This SDK code is auto-generated.

---
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

## Installation

```bash
pip install .
```

For development:

```bash
pip install -e .
```

## Using scm-python

### Configuration File

Create a configuration file at `~/.scm/config.json` (or specify a custom path via `SCM_CONFIG_FILE` environment variable):

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

# Initialize the client (loads config from ~/.scm/config.json by default)
client = Scm()

# Or specify config explicitly
client = Scm(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    tsg_id="YOUR_TSG_ID"
)

# Example: List addresses
addresses_api = client.objects.addresses_api
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

## JWT Token Caching for Concurrent Operations

### Overview

The Strata Cloud Manager authentication API has rate limits on token requests (approximately 10 concurrent requests per tenant). When running multiple concurrent operations (e.g., parallel Python scripts, CI/CD pipelines), these rate limits can cause authentication failures.

To work around this limitation, you can implement a token caching solution that allows multiple client instances to share the same JWT token.

### How It Works

The scm-python SDK supports loading JWT tokens from the configuration file. The following fields can be included in your `~/.scm/config.json`:

**Preferred format (consistent with scm-go):**

```json
{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "scope": "tsg_id:1234567890",
  "host": "api.sase.paloaltonetworks.com",
  "jwt": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "jwt_expires_at": "2026-01-21T10:30:00Z",
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
  "token_expires_at": "2026-01-21T10:30:00Z"
}
```

**Important Security Note**: Only share JWT tokens among client instances that use the **same** `client_id` and `client_secret`. Different service principals with different RBAC permissions should never share tokens, as this would be a privilege escalation risk.

### Token Caching Features

The SDK includes the following enhancements for production use:

1. **Automatic Token Caching**: Reads cached JWT from config file if valid
2. **Expiration Buffer**: 60-second buffer before token expiry (avoids edge cases)
3. **Retry Logic**: Exponential backoff for auth failures (3 retries)
4. **Manual Refresh**: `client.refresh_token()` method for long-running scripts
5. **Expiration Check**: `client.token_expires_soon` property

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
                         │  ~/.scm/config.json  │
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

2. **Shared Config File** (`~/.scm/config.json` or similar)
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
import tempfile
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
                                  os.path.expanduser('~/.scm/config.json')))

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
2. **File Permissions**: Restrict config file access (e.g., `chmod 600 ~/.scm/config.json`)
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

# Run auth tests specifically
pytest auth/test/test_jwt_caching.py -v
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
├── auth/
│   └── test/                # Authentication tests
├── tests/                   # Additional tests
└── README.md
```

## Support

This is auto-generated code provided as-is for experimental purposes. For issues or questions:

1. Check the [GitHub Issues](https://github.com/PaloAltoNetworks/scm-python/issues)
2. Review the API documentation
3. Contact Palo Alto Networks support for production issues

## License

This software is provided "as is" without warranty. See LICENSE file for details.
