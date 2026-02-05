# Python SDK Authentication Tests

This directory contains comprehensive tests for JWT token caching functionality in scm-python.

## Test File

### test_jwt_caching.py

Unit and integration tests for JWT token caching using pytest.

**Test Coverage:**

#### Positive Test Cases ✅

1. **test_load_fresh_token_from_config**
   - Loads a fresh JWT token from config file
   - Verifies token is used without making auth API call
   - Validates all fields are correctly loaded

2. **test_concurrent_clients_share_token**
   - Tests 5 concurrent clients sharing cached token
   - Verifies no race conditions
   - Ensures all clients get same token

#### Negative Test Cases ❌

1. **test_expired_token_fetches_new**
   - Token expired 1 hour ago
   - Verifies new token is fetched
   - Ensures old token is replaced

2. **test_missing_jwt_fields_fetches_token**
   - Config file without JWT fields
   - Verifies token fetch is triggered
   - Validates new token is obtained

3. **test_invalid_config_file_raises_error**
   - Malformed JSON in config file
   - Expects ValueError for missing credentials

4. **test_missing_config_file_without_env_vars**
   - Config file doesn't exist
   - No environment variables set
   - Expects ValueError

5. **test_token_expiring_soon_is_refreshed**
   - Token expiring in 30 seconds (within 60s buffer)
   - Verifies proactive refresh
   - Prevents race conditions

#### Integration Test 🔗

1. **test_integration_refresh_expired_token**
   - Requires real SCM credentials
   - Tests actual token refresh
   - Validates end-to-end flow

## Running the Tests

### Unit Tests (Fast, No External Dependencies)

```bash
# Run all unit tests
pytest auth/test/test_jwt_caching.py -v

# Run specific test
pytest auth/test/test_jwt_caching.py::TestJWTCaching::test_load_fresh_token_from_config -v

# Run with coverage
pytest auth/test/test_jwt_caching.py --cov=scm --cov-report=html
```

### Integration Tests (Require Real Credentials)

```bash
# Set credentials
export SCM_CLIENT_ID="your-client-id"
export SCM_CLIENT_SECRET="your-client-secret"
export SCM_SCOPE="tsg_id:1234567890"

# Run integration tests
pytest auth/test/test_jwt_caching.py::TestJWTCaching::test_integration_refresh_expired_token -v
```

## Test Categories

### Unit Tests
- ✅ No network access required
- ✅ No real credentials required
- ✅ Fast execution (< 1 second)
- ✅ Can run in CI/CD
- ✅ Use mocks for OAuth2Session
- Tests: All except `test_integration_*`

### Integration Tests
- ⚠️ Requires real SCM credentials
- ⚠️ Makes real API calls
- ⚠️ Slower execution (1-5 seconds)
- Tests: `test_integration_refresh_expired_token`

## Config File Format

Tests validate this JSON structure:

```json
{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "host": "api.sase.paloaltonetworks.com",
  "auth_url": "https://auth.apps.paloaltonetworks.com",
  "protocol": "https",
  "scope": "tsg_id:1234567890",
  "logging": "ERROR",
  "jwt": "eyJ0eXAi...",
  "jwt_expires_at": "2026-01-21T10:30:00+00:00",
  "jwt_lifetime": 900
}
```

## Expected Test Results

### Unit Tests

```
============================= test session starts ==============================
collecting ... collected 8 items

test_jwt_caching.py::TestJWTCaching::test_load_fresh_token_from_config PASSED
test_jwt_caching.py::TestJWTCaching::test_expired_token_fetches_new PASSED
test_jwt_caching.py::TestJWTCaching::test_missing_jwt_fields_fetches_token PASSED
test_jwt_caching.py::TestJWTCaching::test_concurrent_clients_share_token PASSED
test_jwt_caching.py::TestJWTCaching::test_invalid_config_file_raises_error PASSED
test_jwt_caching.py::TestJWTCaching::test_missing_config_file_without_env_vars PASSED
test_jwt_caching.py::TestJWTCaching::test_token_expiring_soon_is_refreshed PASSED
test_jwt_caching.py::TestJWTCaching::test_integration_refresh_expired_token SKIPPED

============================== 7 passed, 1 skipped in 0.45s ===============================
```

### With Integration Tests

```
test_jwt_caching.py::TestJWTCaching::test_integration_refresh_expired_token PASSED

============================== 8 passed in 2.34s ===============================
```

## Continuous Integration

### GitHub Actions Example

```yaml
name: Auth Tests

on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run Unit Tests
        run: pytest auth/test/test_jwt_caching.py -v --cov=scm

  integration-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest

      - name: Run Integration Tests
        env:
          SCM_CLIENT_ID: ${{ secrets.SCM_CLIENT_ID }}
          SCM_CLIENT_SECRET: ${{ secrets.SCM_CLIENT_SECRET }}
          SCM_SCOPE: ${{ secrets.SCM_SCOPE }}
        run: pytest auth/test/test_jwt_caching.py::TestJWTCaching::test_integration_refresh_expired_token -v
```

## Common Issues

### Test: Integration test skipped

```
SKIPPED [1] auth/test/test_jwt_caching.py:XXX: Integration test requires SCM_CLIENT_ID and SCM_CLIENT_SECRET
```

**Solution:** Set environment variables:
```bash
export SCM_CLIENT_ID="your-client-id"
export SCM_CLIENT_SECRET="your-client-secret"
export SCM_SCOPE="tsg_id:1234567890"
```

### Test: Invalid credentials

```
FAILED test_integration_refresh_expired_token - ValueError: Failed to authenticate with SCM via OAuth2
```

**Solution:** Verify your credentials are correct and have proper permissions.

## Test Development Guidelines

1. **Unit tests should be fast**
   - Use pytest fixtures for temp files
   - Mock OAuth2Session for no network calls
   - No real credentials required

2. **Mark integration tests**
   - Use `@pytest.mark.skipif` for credential checks
   - Provide clear skip messages

3. **Clean up resources**
   - Use fixtures with yield for automatic cleanup
   - Don't leave test artifacts

4. **Test error cases**
   - Invalid input
   - Missing files
   - Malformed data
   - Edge cases

5. **Document expected behavior**
   - Clear test names
   - Docstrings explaining what's being tested
   - Assert messages for failures
