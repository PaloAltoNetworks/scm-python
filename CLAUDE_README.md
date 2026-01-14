# Claude Code Assistant - SCM Python SDK Guidelines

## ⚠️ CRITICAL: Test Files Are Also Auto-Generated!

### **Test Regeneration Workflow**

**IMPORTANT**: Test files in `scm/*/tests/` are **ALSO auto-generated** from templates in the `openapi-integration-creator` repository. Any changes made directly to test files in `scm-python` will be **LOST** when running `make clean-python && make generate-python`.

#### The Correct Workflow for Updating Tests

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Fix/Update Test in scm-python                                │
│    Location: scm-python/scm/*/tests/api_*_test.py              │
│    - Write the test fix                                          │
│    - Verify it works: pytest scm/*/tests/api_*_test.py -v      │
│    - Document workarounds needed for auto-generated model bugs  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2. Update Template in openapi-integration-creator               │
│    Location: openapi-integration-creator/cmd/generate/python/   │
│              test_templates/api_*_test_template.go              │
│    - Copy working test from scm-python                           │
│    - Wrap in Go template constant                               │
│    - Add getter function                                         │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ 3. Register Template in generator.go                            │
│    Location: openapi-integration-creator/cmd/generate/python/   │
│              generator.go                                        │
│    - Add entry in packageTestTemplates map                       │
│    - Specify FileName and GetContent function                   │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ 4. Regenerate Python SDK with Tests                             │
│    From openapi-integration-creator directory:                   │
│    $ make clean-python                                           │
│    $ make generate-python                                        │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ 5. Verify Regenerated Tests Pass                                │
│    From scm-python directory:                                   │
│    $ source setup_scm_env.sh                                     │
│    $ source venv/bin/activate                                    │
│    $ pytest scm/*/tests/api_*_test.py -v                        │
└─────────────────────────────────────────────────────────────────┘
```

#### Template File Structure

Every test template file follows this structure:

```go
// File: cmd/generate/python/test_templates/api_<resource>_test_template.go
package test_templates

const <resource>TestTemplate = `
<COMPLETE PYTHON TEST FILE CONTENT>
`

// Get<Resource>TestTemplate returns the test template
func Get<Resource>TestTemplate() string {
    return <resource>TestTemplate
}
```

#### Common Test Helper (scm/test_helpers.py)

**IMPORTANT**: All test files import a common `perform()` function from `scm.test_helpers`:

```python
from scm.test_helpers import perform
```

This helper function:
- Logs API requests and responses for debugging
- Handles ApiResponse unwrapping from `_with_http_info` methods
- Supports manual deserialization for 201 Created responses
- Provides consistent logging format across all tests

**Template**: `test_helpers_template.go` generates `scm/test_helpers.py`
**Generator**: Automatically created in `scm/` directory (not in `scm/*/tests/`)

#### Example: Adding a New Test Template

**Step 1**: Write and verify test in scm-python
```bash
# Edit scm-python/scm/identity_services/tests/api_authentication_profiles_test.py
# Run test to verify it works
cd scm-python
source setup_scm_env.sh && source venv/bin/activate
pytest scm/identity_services/tests/api_authentication_profiles_test.py -v
```

**Step 2**: Create template in openapi-integration-creator
```bash
cd /Users/vnarayanan/Documents/github/openapi-integration-creator
# Create cmd/generate/python/test_templates/api_authentication_profiles_test_template.go
```

```go
package test_templates

const authenticationProfilesTestTemplate = `
import logging
import uuid
import json
import pytest
from scm import Scm
from scm.identity_services.models.authentication_profiles import AuthenticationProfiles
# ... rest of Python test file ...
`

func GetAuthenticationProfilesTestTemplate() string {
    return authenticationProfilesTestTemplate
}
```

**Step 3**: Register in generator.go
```go
// In cmd/generate/python/generator.go
"identity_services": {
    // ... other templates ...
    {
        FileName:   "api_authentication_profiles_test.py",
        GetContent: test_templates.GetAuthenticationProfilesTestTemplate,
    },
},
```

**Step 4**: Regenerate
```bash
cd openapi-integration-creator
make clean-python
make generate-python
```

**Step 5**: Verify
```bash
cd scm-python
source setup_scm_env.sh && source venv/bin/activate
pytest scm/identity_services/tests/api_authentication_profiles_test.py -v
```

#### Current Test Templates (2026-01-13)

**Identity Services** (8 templates):
- ✅ `api_authentication_portals_test_template.go` - Authentication portals
- ✅ `api_authentication_profiles_test_template.go` - Authentication profiles with local database
- ✅ `api_authentication_rules_test_template.go` - Authentication rules with prerequisite profile
- ✅ `api_authentication_sequences_test_template.go` - Authentication sequences with prerequisite profile
- ✅ `api_certificate_profiles_test_template.go` - Certificate profiles with CA certificates
- ✅ `api_radius_server_profiles_test_template.go` - RADIUS server profiles
- ✅ `api_saml_server_profiles_test_template.go` - SAML server profiles
- ✅ `api_tls_service_profiles_test_template.go` - TLS service profiles with protocol settings

**Objects** (12 templates):
- ✅ `api_addresses_test_template.go` - Address objects
- ✅ `api_address_groups_test_template.go` - Address groups
- ✅ `api_application_filters_test_template.go` - Application filters
- ✅ `api_application_groups_test_template.go` - Application groups
- ✅ `api_applications_test_template.go` - Applications
- ✅ `api_dynamic_user_groups_test_template.go` - Dynamic user groups
- ✅ `api_external_dynamic_lists_test_template.go` - External dynamic lists
- ✅ `api_hip_objects_test_template.go` - HIP objects
- ✅ `api_hip_profiles_test_template.go` - HIP profiles
- ✅ `api_services_test_template.go` - Service objects
- ✅ `api_service_groups_test_template.go` - Service groups
- ✅ `api_tags_test_template.go` - Tags

**Network Services** (14 templates):
- ✅ Various interface and routing templates

---

## General Rules for Working with Auto-Generated SDK Code

### **CRITICAL RULE: Never Modify Auto-Generated Files**

Files generated by `openapi-integration-creator` must **NEVER** be manually edited.

#### How to Identify Auto-Generated Files
Look for these indicators at the top of files:
```python
"""
Generated by OpenAPI Generator (https://openapi-generator.tech)
Do not edit the class manually.
"""
```

#### Common Auto-Generated Paths
- `scm/*/models/*.py` - Pydantic model classes
- `scm/*/api/*.py` - API client classes
- `scm/*/api_client.py` - Core API client

---

## When You Find Issues in Auto-Generated Code

### Step 1: Document the Issue
Create or update a section in this README with:
- **File path** of the auto-generated file
- **Issue description** (validation errors, incorrect types, etc.)
- **Root cause** (what in the OpenAPI spec caused this)
- **Impact** (which operations fail)
- **Evidence** (error logs, test failures)

### Step 2: Determine the Fix Location
Issues in auto-generated code must be fixed at the **source**:

```
OpenAPI Spec → openapi-integration-creator → Generated SDK Code
     ↑                                              ↓
   FIX HERE                              NEVER FIX HERE
```

### Step 3: Workaround in Tests (If Needed)
While waiting for spec fixes, you may:
- ✅ Modify **test files** to work around issues
- ✅ Adjust test data to avoid triggering constraints
- ✅ Skip failing tests with clear documentation
- ❌ Modify auto-generated model/API files

---

## Current Known Issues

### Issue #1: RADIUS Server Profiles - Secret Field Length Constraint

**Date Identified**: 2026-01-13

#### Problem
**File**: `scm/identity_services/models/radius_server_profiles_server_inner.py:34`

```python
secret: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(...)
```

The `max_length=64` constraint applies to both request AND response validation. The API encrypts secrets server-side, returning values >64 characters, which causes Pydantic validation errors during deserialization.

#### Evidence
```
ValidationError: 1 validation error for RadiusServerProfilesServerInner
secret
  String should have at most 64 characters [type=string_too_long,
  input_value='-AQ==8L8LdGuTt86vbzGba4J...+TVJRRKB+A2dD+tdRq6eQ==']
```

Example encrypted secrets from API:
- Short input `"secret123"` → `"-AQ==8rF...Rg=="` (63 chars) ✓
- Long input → `"-AQ==8L8...eQ=="` (128 chars) ✗ FAILS VALIDATION

#### Root Cause in OpenAPI Spec
```yaml
# Current (incorrect)
secret:
  type: string
  maxLength: 64  # ← Applied to both request AND response
  description: The RADIUS secret
```

#### Required Fix
In the **openapi-integration-creator** repository, modify the OpenAPI spec:

**Option 1 - Simple** (Remove constraint):
```yaml
secret:
  type: string
  description: The RADIUS secret
```

**Option 2 - Accurate** (Separate schemas):
```yaml
# In request schemas
RadiusServerProfilesServerInnerRequest:
  secret:
    type: string
    maxLength: 64

# In response schemas
RadiusServerProfilesServerInnerResponse:
  secret:
    type: string
    # No maxLength - can be encrypted
```

#### Comparison with Go SDK
Go SDK has NO max_length constraint and works correctly:
```go
// scm-go/generated/identity_services/model_radius_server_profiles_server_inner.go:30
Secret *string `json:"secret,omitempty"`
```

#### Test Workarounds Applied
**File**: `scm/identity_services/tests/api_radius_server_profiles_test.py`

1. Fixed `perform()` helper to properly unwrap `ApiResponse` objects (lines 21-68)
2. Shortened test secret from `"fixtureSecret123"` to `"secret123"` (line 97)

#### Test Results
- ✅ `test_create_radius_profile` - PASSED
- ✅ `test_get_radius_profile_by_id` - PASSED
- ✅ `test_update_radius_profile` - PASSED
- ❌ `test_list_radius_profiles` - **FAILS** (encounters existing profiles with long secrets)
- ✅ `test_delete_radius_profile_by_id` - PASSED

#### Impact
- Cannot reliably use `list_radius_server_profiles()`
- Cannot deserialize profiles with long encrypted secrets
- Breaks in production environments with existing data

#### Files Affected
**Auto-Generated (DO NOT EDIT)**:
- `scm/identity_services/models/radius_server_profiles_server_inner.py`
- `scm/identity_services/models/radius_server_profiles.py`
- `scm/identity_services/models/radius_server_profiles_list_response.py`
- `scm/identity_services/api/radius_server_profiles_api.py`

**Test Files (Modified)**:
- `scm/identity_services/tests/api_radius_server_profiles_test.py`

#### References
- Test logs: `radius_logs.txt` (lines 382-453)
- Working comparison: `scm/objects/tests/api_addresses_test.py`
- Pydantic error docs: https://errors.pydantic.dev/2.12/v/string_too_long

---

## How to Add New Issues to This Document

When you discover new issues in auto-generated code:

### Template

```markdown
### Issue #N: [Brief Description]

**Date Identified**: YYYY-MM-DD

#### Problem
**File**: `path/to/auto-generated/file.py:line`

[Code snippet showing the issue]

[Explanation of what's wrong]

#### Evidence
[Error messages, logs, test output]

#### Root Cause in OpenAPI Spec
[What in the spec caused this]

#### Required Fix
[Changes needed in openapi-integration-creator]

#### Comparison with Go SDK
[How Go SDK handles this, if applicable]

#### Test Workarounds Applied
[What was changed in tests to work around this]

#### Test Results
[Which tests pass/fail]

#### Impact
[What functionality is broken]

#### Files Affected
[List of auto-generated and test files]

#### References
[Links, logs, documentation]
```

---

## Testing Best Practices

### 0. Setup Environment Before Running Tests

**CRITICAL**: Before executing tests, you MUST run the setup script to configure environment variables:

```bash
# From the scm-python directory
source setup_scm_env.sh
```

This script sets up required environment variables:
- `SCM_CLIENT_ID` - OAuth client ID for authentication
- `SCM_CLIENT_SECRET` - OAuth client secret
- `SCM_TSG_ID` - Tenant Service Group ID
- Other SCM configuration variables

Without these credentials, all tests will be skipped with:
```
SKIPPED [100%] - Skipping tests due to client initialization failure
```

### 1. Compare with Go SDK Tests
When Python tests fail but Go tests pass, compare implementations:
```bash
# Find Go test file
find ../scm-go -name "*_test.go" | grep <feature>

# Check Go model
find ../scm-go -name "model_*.go" | grep <feature>
```

### 2. Check Response Handling
Common pattern in working tests (e.g., `api_addresses_test.py`):

```python
def perform(func, response_type=None, **kwargs):
    response = func(**kwargs)

    # Unwrap ApiResponse objects
    if hasattr(response, 'data') and hasattr(response, 'raw_data'):
        if response.data is not None:
            return response.data
        # Handle 201 Created with manual deserialization if needed

    return response
```

### 3. Keep Test Data Simple
- Use short strings to avoid length constraints
- Use simple values to avoid validation issues
- Create minimal objects that satisfy required fields

### 4. Document Workarounds
When applying test workarounds:
```python
# Workaround for issue #1: Secret field max_length constraint
# See CLAUDE_README.md for details
# TODO: Remove this workaround once OpenAPI spec is fixed
secret="secret123"  # Keep short to avoid encrypted length >64 chars
```

---

## Workflow Summary

```
Issue Found in Auto-Generated Code
         ↓
1. Document in CLAUDE_README.md
         ↓
2. Identify OpenAPI spec problem
         ↓
3. Create issue for openapi-integration-creator team
         ↓
4. Apply test workarounds (if possible)
         ↓
5. Wait for spec fix & regeneration
         ↓
6. Remove workarounds after fix deployed
```

---

## Contact & Resources

- **OpenAPI Integration Creator**: [Repository link needed]
- **SCM Go SDK**: `/Users/vnarayanan/Documents/github/scm-go`
- **SCM Python SDK**: `/Users/vnarayanan/Documents/github/scm-python`

---

## Update History

- **2026-01-13**: Initial document created
  - Added Issue #1: RADIUS Server Profiles secret field constraint
  - Established auto-generated file modification rules
  - Added Testing Best Practices section with environment setup requirements
  - Created all identity services tests (40 tests across 8 test files)

---

### Issue #2: TLS Service Profiles - Invalid Default Values for min_version/max_version

**Date Identified**: 2026-01-13

#### Problem
**File**: `scm/identity_services/models/tls_service_profiles_protocol_settings.py:40-41`

```python
max_version: Optional[StrictStr] = Field(default='3', description="Maximum TLS version")
min_version: Optional[StrictStr] = Field(default='2', description="Minimum TLS version")
```

The auto-generated model has invalid default values `'3'` and `'2'` when the field validators (lines 44-62) only allow enum values: `['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3']`.

#### Evidence
```
ValidationError: 2 validation errors for TlsServiceProfilesProtocolSettings
max_version
  Value error, must be one of enum values ('tls1-0', 'tls1-1', 'tls1-2', 'tls1-3') [type=value_error, input_value='3', input_type=str]
min_version
  Value error, must be one of enum values ('tls1-0', 'tls1-1', 'tls1-2', 'tls1-3') [type=value_error, input_value='2', input_type=str]
```

When creating TLS profiles with minimal settings (only specifying `keyxchg_algo_rsa=True`), the defaults cause validation failures on deserialization.

#### Root Cause in OpenAPI Spec
The OpenAPI spec incorrectly defines default values for these enum fields:
```yaml
min_version:
  type: string
  enum: ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3']
  default: '2'  # ← Invalid! Should be 'tls1-2' or no default

max_version:
  type: string
  enum: ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3']
  default: '3'  # ← Invalid! Should be 'tls1-3' or no default
```

#### Required Fix
In the **openapi-integration-creator** repository:

**Option 1 - Remove Defaults** (simplest):
```yaml
min_version:
  type: string
  enum: ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3']
  # No default

max_version:
  type: string
  enum: ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3']
  # No default
```

**Option 2 - Fix to Valid Enum Values**:
```yaml
min_version:
  type: string
  enum: ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3']
  default: 'tls1-2'  # Valid enum value

max_version:
  type: string
  enum: ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3']
  default: 'tls1-3'  # Valid enum value
```

#### Comparison with Go SDK
Go SDK has no default values and works correctly:
```go
// scm-go/generated/identity_services/model_tls_service_profiles_protocol_settings.go
MinVersion *string `json:"min_version,omitempty"`
MaxVersion *string `json:"max_version,omitempty"`
```

#### Test Workarounds Applied
**File**: `scm/identity_services/tests/api_tls_service_profiles_test.py`

For simple create tests (lines 192, 211):
```python
protocol_settings = TlsServiceProfilesProtocolSettings(
    keyxchg_algo_rsa=True,
    min_version=None,  # Workaround: override invalid defaults
    max_version=None   # See CLAUDE_README.md for details
)
```

For complex create tests (lines 78-87):
```python
protocol_settings = TlsServiceProfilesProtocolSettings(
    min_version="tls1-1",  # Explicitly set to valid enum value
    max_version="tls1-3",  # Explicitly set to valid enum value
    keyxchg_algo_rsa=True,
    # ... other settings
)
```

#### Test Results
- ✅ `test_get_tls_profile_by_id` - PASSED
- ✅ `test_update_tls_profile` - PASSED
- ❌ `test_create_tls_profile` - **FAILS** (simple create with invalid defaults)
- ❌ `test_list_tls_profiles` - **FAILS** (encounters existing profiles with invalid defaults)
- ❌ `test_delete_tls_profile_by_id` - **FAILS** (simple create with invalid defaults)

#### Impact
- Cannot create TLS profiles without explicitly setting min/max versions
- Cannot reliably use `list_tls_service_profiles()` if existing profiles have invalid defaults
- Breaks in environments with pre-existing TLS profiles created with invalid defaults

#### Files Affected
**Auto-Generated (DO NOT EDIT)**:
- `scm/identity_services/models/tls_service_profiles_protocol_settings.py`
- `scm/identity_services/models/tls_service_profiles.py`
- `scm/identity_services/models/tls_service_profiles_list_response.py`
- `scm/identity_services/api/tls_service_profiles_api.py`

**Test Files (Modified)**:
- `scm/identity_services/tests/api_tls_service_profiles_test.py`

#### References
- Pydantic error docs: https://errors.pydantic.dev/2.12/v/value_error

---

### Issue #3: SAML and TLS Service Profiles - ID Field Incorrectly Required

**Date Identified**: 2026-01-13

#### Problem
**Files**:
- `scm/identity_services/models/saml_server_profiles.py`
- `scm/identity_services/models/tls_service_profiles.py`

The `id` field is incorrectly marked as required (`id: StrictStr`) instead of optional (`id: Optional[StrictStr]`). This causes validation errors when creating new objects (where id should not be provided).

#### Evidence
```
ValidationError: 1 validation error for SamlServerProfiles
id
  Field required [type=missing, input_value={...}, input_type=dict]
```

#### Comparison with Working Models
Certificate Profiles (working) has:
```python
id: Optional[StrictStr] = Field(default=None, description="UUID of the resource")
```

SAML/TLS (broken) has:
```python
id: StrictStr = Field(description="UUID of the resource")
```

#### Root Cause in OpenAPI Spec
The OpenAPI spec incorrectly marks `id` as required in request schemas:
```yaml
# Current (incorrect)
SamlServerProfiles:
  required:
    - id  # ← Should not be required for create requests
    - name
    - ...
```

#### Required Fix
In the **openapi-integration-creator** repository:

**Option 1** - Separate request/response schemas:
```yaml
SamlServerProfilesRequest:
  required: [name, folder, ...]  # No id
  properties:
    name: ...
    folder: ...
    # id not included in request

SamlServerProfilesResponse:
  required: [id, name, folder, ...]  # id required
  allOf:
    - $ref: '#/components/schemas/SamlServerProfilesRequest'
    - properties:
        id:
          type: string
```

**Option 2** - Make id optional:
```yaml
SamlServerProfiles:
  required: [name, folder, ...]  # Remove id from required
  properties:
    id:
      type: string
      readOnly: true  # Indicate it's only in responses
```

#### Test Workarounds Applied
**Files**:
- `scm/identity_services/tests/api_saml_server_profiles_test.py`
- `scm/identity_services/tests/api_tls_service_profiles_test.py`

Provide empty string for id field (lines 97, 129, 200 in SAML; lines 91, 124, 197 in TLS):
```python
payload = SamlServerProfiles(
    id="",  # Workaround: id incorrectly marked as required in model
    name=profile_name,
    folder=TARGET_FOLDER,
    ...
)
```

#### Test Results
With workaround applied:
- ✅ Tests can create objects by passing `id=""`
- ✅ API correctly ignores the empty id and generates a proper UUID
- ⚠️ Workaround required in all create operations

#### Impact
- Cannot create SAML or TLS profiles without providing dummy `id=""` workaround
- Violates API design principles (id should be server-generated, not client-provided)
- Every test and SDK user must apply this workaround

#### Files Affected
**Auto-Generated (DO NOT EDIT)**:
- `scm/identity_services/models/saml_server_profiles.py`
- `scm/identity_services/models/tls_service_profiles.py`

**Test Files (Modified)**:
- `scm/identity_services/tests/api_saml_server_profiles_test.py`
- `scm/identity_services/tests/api_tls_service_profiles_test.py`

---

## Update History

- **2026-01-13**: Initial document created
  - Added Issue #1: RADIUS Server Profiles secret field constraint
  - Added Issue #2: TLS Service Profiles invalid default values for min_version/max_version
  - Added Issue #3: SAML and TLS Service Profiles id field incorrectly required
  - Established auto-generated file modification rules
  - Added Testing Best Practices section with environment setup requirements
  - Created all identity services tests (40 tests across 8 test files)
  - **Test Results**: 32/40 passing (80%) - blocked by auto-generated code bugs
