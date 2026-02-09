# Common Patterns and Workflows

This guide covers common patterns, best practices, and workflows when using the SCM Python SDK.

## Table of Contents

- [Initialization Patterns](#initialization-patterns)
- [CRUD Operation Patterns](#crud-operation-patterns)
- [Fetch-Modify-Update Pattern](#fetch-modify-update-pattern)
- [Error Handling Patterns](#error-handling-patterns)
- [Bulk Operation Patterns](#bulk-operation-patterns)
- [Pagination Patterns](#pagination-patterns)
- [Rule Management Patterns](#rule-management-patterns)
- [Tag Management Patterns](#tag-management-patterns)
- [Idempotent Operations](#idempotent-operations)
- [Atomic Operations](#atomic-operations)
- [Validation Patterns](#validation-patterns)
- [Logging and Debugging](#logging-and-debugging)

---

## Initialization Patterns

### Pattern: Singleton Client

Use a single client instance throughout your application for better token management and connection pooling.

```python
from scm import Scm

class SCMClient:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Scm(
                log_level="INFO",
                token_file="/tmp/scm_token.json"
            )
        return cls._instance

# Usage
client = SCMClient.get_instance()
addresses_api = client.objects.AddressesApi(client.objects.api_client)
```

### Pattern: Context Manager for Client

Ensure proper cleanup with context managers.

```python
from contextlib import contextmanager
from scm import Scm

@contextmanager
def scm_client():
    """Context manager for SCM client."""
    client = Scm(log_level="INFO")
    try:
        yield client
    finally:
        # Any cleanup if needed
        pass

# Usage
with scm_client() as client:
    addresses_api = client.objects.AddressesApi(client.objects.api_client)
    # Perform operations
```

### Pattern: Multi-Environment Configuration

Support multiple environments (dev, staging, prod).

```python
import os
from scm import Scm
from typing import Literal

def get_scm_client(
    environment: Literal["dev", "staging", "prod"] = "dev"
) -> Scm:
    """Get SCM client for specific environment."""

    env_configs = {
        "dev": {
            "client_id": os.getenv("SCM_DEV_CLIENT_ID"),
            "client_secret": os.getenv("SCM_DEV_CLIENT_SECRET"),
            "tsg_id": os.getenv("SCM_DEV_TSG_ID"),
            "log_level": "DEBUG",
        },
        "staging": {
            "client_id": os.getenv("SCM_STAGING_CLIENT_ID"),
            "client_secret": os.getenv("SCM_STAGING_CLIENT_SECRET"),
            "tsg_id": os.getenv("SCM_STAGING_TSG_ID"),
            "log_level": "INFO",
        },
        "prod": {
            "client_id": os.getenv("SCM_PROD_CLIENT_ID"),
            "client_secret": os.getenv("SCM_PROD_CLIENT_SECRET"),
            "tsg_id": os.getenv("SCM_PROD_TSG_ID"),
            "log_level": "WARNING",
        },
    }

    config = env_configs.get(environment)
    if not config:
        raise ValueError(f"Invalid environment: {environment}")

    return Scm(**config)

# Usage
prod_client = get_scm_client("prod")
```

---

## CRUD Operation Patterns

### Pattern: Safe Create with Existence Check

Check if object exists before creating to avoid duplicates.

```python
from scm.objects.models.addresses import Addresses
from scm.exceptions import NameNotUniqueError

def safe_create_address(api, name: str, folder: str, **kwargs) -> Addresses:
    """Create address only if it doesn't exist."""

    # Check if exists using fetch
    existing = api.fetch_addresses(name=name, folder=folder)

    if existing:
        print(f"Address '{name}' already exists (ID: {existing.id})")
        return existing

    # Create new address
    try:
        address = Addresses(
            id="",
            name=name,
            folder=folder,
            **kwargs
        )
        created = api.create_addresses(addresses=address)
        print(f"Created address '{name}' (ID: {created.id})")
        return created

    except NameNotUniqueError:
        # Race condition: created between check and create
        # Fetch and return the existing one
        return api.fetch_addresses(name=name, folder=folder)

# Usage
address = safe_create_address(
    addresses_api,
    name="web-server",
    folder="Texas",
    ip_netmask="10.0.0.1/32"
)
```

### Pattern: Get or Create

Return existing object or create if it doesn't exist.

```python
from typing import Optional

def get_or_create_address(
    api,
    name: str,
    folder: str,
    defaults: Optional[dict] = None
) -> tuple[Addresses, bool]:
    """
    Get existing address or create if not found.

    Returns:
        tuple: (address_object, created_flag)
    """
    # Try to fetch existing
    existing = api.fetch_addresses(name=name, folder=folder)

    if existing:
        return existing, False

    # Create with defaults
    create_data = defaults or {}
    address = Addresses(
        id="",
        name=name,
        folder=folder,
        **create_data
    )

    try:
        created = api.create_addresses(addresses=address)
        return created, True
    except NameNotUniqueError:
        # Race condition - fetch again
        existing = api.fetch_addresses(name=name, folder=folder)
        return existing, False

# Usage
address, created = get_or_create_address(
    addresses_api,
    name="web-server",
    folder="Texas",
    defaults={
        "ip_netmask": "10.0.0.1/32",
        "description": "Production web server",
        "tag": ["Production"]
    }
)

if created:
    print(f"Created new address: {address.name}")
else:
    print(f"Using existing address: {address.name}")
```

### Pattern: Update or Create

Update existing object or create if not found.

```python
def update_or_create_address(
    api,
    name: str,
    folder: str,
    **data
) -> tuple[Addresses, bool]:
    """
    Update existing address or create if not found.

    Returns:
        tuple: (address_object, created_flag)
    """
    existing = api.fetch_addresses(name=name, folder=folder)

    if existing:
        # Update existing
        for key, value in data.items():
            setattr(existing, key, value)

        updated = api.update_addresses_by_id(
            id=existing.id,
            addresses=existing
        )
        return updated, False

    # Create new
    address = Addresses(
        id="",
        name=name,
        folder=folder,
        **data
    )
    created = api.create_addresses(addresses=address)
    return created, True

# Usage
address, created = update_or_create_address(
    addresses_api,
    name="web-server",
    folder="Texas",
    ip_netmask="10.0.0.2/32",
    description="Updated web server",
    tag=["Production", "Updated"]
)
```

---

## Fetch-Modify-Update Pattern

### Pattern: Basic Fetch-Modify-Update

Standard pattern for updating existing objects.

```python
def update_address_ip(api, name: str, folder: str, new_ip: str):
    """Update address IP using fetch-modify-update pattern."""

    # 1. Fetch
    address = api.fetch_addresses(name=name, folder=folder)
    if not address:
        raise ValueError(f"Address '{name}' not found")

    # 2. Modify
    old_ip = address.ip_netmask
    address.ip_netmask = new_ip

    # 3. Update
    updated = api.update_addresses_by_id(
        id=address.id,
        addresses=address
    )

    print(f"Updated {name}: {old_ip} -> {new_ip}")
    return updated

# Usage
update_address_ip(
    addresses_api,
    name="web-server",
    folder="Texas",
    new_ip="10.0.0.5/32"
)
```

### Pattern: Conditional Update

Update only if conditions are met.

```python
def conditional_update_address(
    api,
    name: str,
    folder: str,
    condition_func,
    **updates
):
    """Update address only if condition is met."""

    address = api.fetch_addresses(name=name, folder=folder)
    if not address:
        return None

    # Check condition
    if not condition_func(address):
        print(f"Condition not met for {name}, skipping update")
        return address

    # Apply updates
    for key, value in updates.items():
        setattr(address, key, value)

    updated = api.update_addresses_by_id(
        id=address.id,
        addresses=address
    )

    print(f"Updated {name}")
    return updated

# Usage: Update only addresses without tags
conditional_update_address(
    addresses_api,
    name="web-server",
    folder="Texas",
    condition_func=lambda addr: not addr.tag,
    tag=["Untagged-Updated"]
)
```

### Pattern: Batch Modify with Rollback

Modify multiple objects with rollback on failure.

```python
from scm.exceptions import ScmException

def batch_update_addresses(api, updates: list[dict], folder: str):
    """
    Update multiple addresses with rollback on failure.

    Args:
        updates: List of dicts with 'name' and update fields
    """
    original_states = {}
    updated = []

    try:
        for update_info in updates:
            name = update_info.pop('name')

            # Fetch current state
            address = api.fetch_addresses(name=name, folder=folder)
            if not address:
                raise ValueError(f"Address '{name}' not found")

            # Store original
            original_states[address.id] = {
                'ip_netmask': address.ip_netmask,
                'description': address.description,
                'tag': address.tag.copy() if address.tag else []
            }

            # Apply updates
            for key, value in update_info.items():
                setattr(address, key, value)

            # Update
            result = api.update_addresses_by_id(
                id=address.id,
                addresses=address
            )
            updated.append(result)
            print(f"✓ Updated {name}")

        return updated

    except Exception as e:
        print(f"Error during batch update: {e}")
        print("Rolling back changes...")

        # Rollback
        for addr in updated:
            if addr.id in original_states:
                orig = original_states[addr.id]
                addr.ip_netmask = orig['ip_netmask']
                addr.description = orig['description']
                addr.tag = orig['tag']

                try:
                    api.update_addresses_by_id(
                        id=addr.id,
                        addresses=addr
                    )
                    print(f"  Rolled back {addr.name}")
                except Exception as rollback_err:
                    print(f"  Failed to rollback {addr.name}: {rollback_err}")

        raise

# Usage
batch_update_addresses(
    addresses_api,
    updates=[
        {'name': 'web-01', 'ip_netmask': '10.0.0.11/32'},
        {'name': 'web-02', 'ip_netmask': '10.0.0.12/32'},
        {'name': 'web-03', 'ip_netmask': '10.0.0.13/32'},
    ],
    folder="Texas"
)
```

---

## Error Handling Patterns

### Pattern: Comprehensive Error Handler

Handle all common exception types.

```python
from scm.exceptions import (
    ObjectNotPresentError,
    NameNotUniqueError,
    InvalidObjectError,
    ReferenceNotZeroError,
    MissingQueryParameterError,
    ScmException
)
import logging

logger = logging.getLogger(__name__)

def robust_create_address(api, address_data: dict) -> Optional[Addresses]:
    """Create address with comprehensive error handling."""

    try:
        address = Addresses(**address_data)
        created = api.create_addresses(addresses=address)
        logger.info(f"Created address: {created.name}")
        return created

    except NameNotUniqueError as e:
        logger.warning(f"Address already exists: {e.object_name}")
        # Return existing address
        return api.fetch_addresses(
            name=address_data['name'],
            folder=address_data['folder']
        )

    except InvalidObjectError as e:
        logger.error(f"Invalid address configuration: {e.message}")
        logger.error(f"Details: {e.details}")
        return None

    except MissingQueryParameterError as e:
        logger.error(f"Missing required parameter: {e.message}")
        return None

    except ScmException as e:
        logger.error(f"SCM API error: {e.message} (code: {e.error_code})")
        return None

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return None

# Usage
result = robust_create_address(
    addresses_api,
    {
        'id': '',
        'name': 'web-server',
        'folder': 'Texas',
        'ip_netmask': '10.0.0.1/32'
    }
)
```

### Pattern: Retry with Exponential Backoff

Retry failed operations with backoff.

```python
import time
from typing import Callable, TypeVar, Any

T = TypeVar('T')

def retry_with_backoff(
    func: Callable[..., T],
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (ScmException,)
) -> T:
    """Retry function with exponential backoff."""

    delay = initial_delay

    for attempt in range(max_retries):
        try:
            return func()
        except exceptions as e:
            if attempt == max_retries - 1:
                raise

            logger.warning(
                f"Attempt {attempt + 1} failed: {e}. "
                f"Retrying in {delay}s..."
            )
            time.sleep(delay)
            delay *= backoff_factor

# Usage
def create_operation():
    return addresses_api.create_addresses(addresses=address)

result = retry_with_backoff(
    create_operation,
    max_retries=3,
    initial_delay=1.0
)
```

### Pattern: Safe Delete with Reference Checking

Delete with proper reference handling.

```python
from scm.exceptions import ReferenceNotZeroError, ObjectNotPresentError

def safe_delete_address(api, address_id: str, force: bool = False) -> bool:
    """
    Safely delete address with reference checking.

    Args:
        force: If True, attempt to find and remove references
    """
    try:
        api.delete_addresses_by_id(id=address_id)
        logger.info(f"Deleted address: {address_id}")
        return True

    except ReferenceNotZeroError as e:
        logger.warning(f"Address {address_id} is referenced elsewhere")

        if force:
            logger.info("Force flag set, but automatic reference removal not implemented")
            logger.info("Manually remove references before deleting")

        return False

    except ObjectNotPresentError:
        logger.info(f"Address {address_id} already deleted")
        return True

    except Exception as e:
        logger.error(f"Failed to delete address {address_id}: {e}")
        return False

# Usage
deleted = safe_delete_address(address.id, force=False)
```

---

## Bulk Operation Patterns

### Pattern: Parallel Bulk Create

Create multiple objects efficiently.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

def bulk_create_addresses(
    api,
    addresses_data: List[dict],
    max_workers: int = 5
) -> dict:
    """Create multiple addresses in parallel."""

    results = {
        'created': [],
        'failed': [],
        'skipped': []
    }

    def create_single(data):
        try:
            address = Addresses(**data)
            created = api.create_addresses(addresses=address)
            return ('created', created)

        except NameNotUniqueError:
            return ('skipped', data['name'])

        except Exception as e:
            return ('failed', (data['name'], str(e)))

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(create_single, addr_data)
            for addr_data in addresses_data
        ]

        for future in as_completed(futures):
            status, result = future.result()
            results[status].append(result)

    logger.info(f"Created: {len(results['created'])}")
    logger.info(f"Skipped: {len(results['skipped'])}")
    logger.info(f"Failed: {len(results['failed'])}")

    return results

# Usage
addresses_data = [
    {
        'id': '',
        'name': f'server-{i}',
        'folder': 'Texas',
        'ip_netmask': f'10.0.0.{i}/32'
    }
    for i in range(1, 51)
]

results = bulk_create_addresses(addresses_api, addresses_data)
```

### Pattern: Bulk Update with Progress

Update multiple objects with progress tracking.

```python
from tqdm import tqdm

def bulk_update_with_progress(
    api,
    folder: str,
    update_func: Callable,
    filter_func: Callable = None
):
    """Update multiple objects with progress bar."""

    # Get all objects
    all_objects = []
    offset = 0
    limit = 200

    print("Fetching objects...")
    while True:
        response = api.list_addresses(
            folder=folder,
            limit=limit,
            offset=offset
        )
        all_objects.extend(response.data)

        if len(response.data) < limit:
            break
        offset += limit

    # Filter if needed
    if filter_func:
        objects_to_update = [obj for obj in all_objects if filter_func(obj)]
    else:
        objects_to_update = all_objects

    print(f"Updating {len(objects_to_update)} objects...")

    results = {'success': 0, 'failed': 0}

    for obj in tqdm(objects_to_update, desc="Updating"):
        try:
            # Apply update function
            update_func(obj)

            # Update via API
            api.update_addresses_by_id(id=obj.id, addresses=obj)
            results['success'] += 1

        except Exception as e:
            logger.error(f"Failed to update {obj.name}: {e}")
            results['failed'] += 1

    return results

# Usage: Add tag to all addresses
def add_reviewed_tag(address):
    if not address.tag:
        address.tag = []
    if "Reviewed" not in address.tag:
        address.tag.append("Reviewed")

results = bulk_update_with_progress(
    addresses_api,
    folder="Texas",
    update_func=add_reviewed_tag,
    filter_func=lambda addr: not (addr.tag and "Reviewed" in addr.tag)
)
```

---

## Pagination Patterns

### Pattern: Iterator for Large Datasets

Create iterator for memory-efficient processing.

```python
from typing import Iterator

def iterate_all_addresses(api, folder: str, limit: int = 200) -> Iterator[Addresses]:
    """Iterate over all addresses without loading all into memory."""

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

# Usage
for address in iterate_all_addresses(addresses_api, "Texas"):
    if address.tag and "Production" in address.tag:
        print(f"Production address: {address.name}")
```

### Pattern: Batched Processing

Process large datasets in batches.

```python
from typing import List, Callable

def process_in_batches(
    api,
    folder: str,
    batch_size: int,
    process_func: Callable[[List[Addresses]], None]
):
    """Process addresses in batches."""

    batch = []

    for address in iterate_all_addresses(api, folder):
        batch.append(address)

        if len(batch) >= batch_size:
            process_func(batch)
            batch = []

    # Process remaining
    if batch:
        process_func(batch)

# Usage
def print_batch(addresses: List[Addresses]):
    names = [addr.name for addr in addresses]
    print(f"Processing batch of {len(addresses)}: {names}")

process_in_batches(
    addresses_api,
    folder="Texas",
    batch_size=10,
    process_func=print_batch
)
```

---

## Rule Management Patterns

### Pattern: Insert Rule at Specific Position

Insert security rule at top/bottom/specific position.

```python
from scm.security_services.models.security_rules import SecurityRules
from scm.security_services.models.rule_move_post_request import RuleMovePostRequest

def create_rule_at_position(
    api,
    rule_data: dict,
    position: str = "top",  # "top", "bottom", or specific rule ID
    rulebase: str = "pre"
):
    """Create rule and move to specific position."""

    # Create rule
    rule = SecurityRules(**rule_data)
    created = api.create_security_rules(security_rules=rule)

    # Move to position
    if position in ["top", "bottom"]:
        move_request = RuleMovePostRequest(
            destination=position,
            rulebase=rulebase
        )
    else:
        # Position relative to another rule
        move_request = RuleMovePostRequest(
            destination=position,  # ID of target rule
            rulebase=rulebase,
            destination_rule=position
        )

    api.move_security_rules_by_id(
        id=created.id,
        rule_move_post_request=move_request
    )

    return created

# Usage
rule = create_rule_at_position(
    security_rules_api,
    rule_data={
        'id': '',
        'name': 'critical-block-rule',
        'folder': 'Texas',
        'position': 'pre',
        'source': ['any'],
        'destination': ['any'],
        'application': ['malicious-apps'],
        'service': ['any'],
        'action': 'deny'
    },
    position="top"
)
```

### Pattern: Rule Reordering

Reorder multiple rules.

```python
def reorder_rules(api, rule_order: List[str], folder: str):
    """
    Reorder rules to match specified order.

    Args:
        rule_order: List of rule names in desired order
    """
    # Get all rules
    response = api.list_rules(folder=folder)

    # Create name-to-id mapping
    rule_map = {rule.name: rule for rule in response.data}

    # Move rules to match order
    for idx, rule_name in enumerate(rule_order):
        if rule_name not in rule_map:
            logger.warning(f"Rule '{rule_name}' not found")
            continue

        rule = rule_map[rule_name]

        if idx == 0:
            # Move to top
            move_request = RuleMovePostRequest(
                destination="top",
                rulebase="pre"
            )
        else:
            # Move after previous rule
            prev_rule_name = rule_order[idx - 1]
            if prev_rule_name in rule_map:
                prev_rule = rule_map[prev_rule_name]
                move_request = RuleMovePostRequest(
                    destination=prev_rule.id,
                    rulebase="pre",
                    destination_rule=prev_rule.id
                )
            else:
                continue

        api.move_security_rules_by_id(
            id=rule.id,
            rule_move_post_request=move_request
        )
        logger.info(f"Moved rule '{rule_name}' to position {idx}")

# Usage
reorder_rules(
    security_rules_api,
    rule_order=[
        "critical-deny-rule",
        "important-allow-rule",
        "standard-allow-rule",
        "default-deny-rule"
    ],
    folder="Texas"
)
```

---

## Tag Management Patterns

### Pattern: Tag-Based Grouping

Create and manage resources by tags.

```python
def ensure_tag_exists(tags_api, tag_name: str, folder: str, **kwargs) -> Tags:
    """Ensure tag exists, create if not."""
    from scm.objects.models.tags import Tags

    existing = tags_api.fetch_tags(name=tag_name, folder=folder)

    if existing:
        return existing

    tag = Tags(
        id="",
        name=tag_name,
        folder=folder,
        **kwargs
    )

    return tags_api.create_tags(tags=tag)

def tag_resource(resource_api, resource_name: str, folder: str, tag: str):
    """Add tag to a resource."""

    # Fetch resource (works with addresses, services, etc.)
    resource = resource_api.fetch_addresses(name=resource_name, folder=folder)

    if not resource:
        raise ValueError(f"Resource '{resource_name}' not found")

    # Add tag
    if not resource.tag:
        resource.tag = []

    if tag not in resource.tag:
        resource.tag.append(tag)

        # Update
        resource_api.update_addresses_by_id(
            id=resource.id,
            addresses=resource
        )

# Usage
ensure_tag_exists(
    tags_api,
    tag_name="Production",
    folder="Texas",
    color="Red",
    comments="Production resources"
)

tag_resource(
    addresses_api,
    resource_name="web-server",
    folder="Texas",
    tag="Production"
)
```

---

## Idempotent Operations

### Pattern: Idempotent Configuration Deployment

Deploy configuration idempotently.

```python
from typing import Dict, Any

class IdempotentDeployer:
    """Deploy configurations idempotently."""

    def __init__(self, client: Scm):
        self.client = client
        self.addresses_api = client.objects.AddressesApi(client.objects.api_client)
        self.security_rules_api = client.security_services.SecurityRulesApi(
            client.security_services.api_client
        )

    def deploy_addresses(self, addresses_config: List[Dict[str, Any]], folder: str):
        """Deploy addresses idempotently."""
        for addr_config in addresses_config:
            name = addr_config['name']

            existing = self.addresses_api.fetch_addresses(name=name, folder=folder)

            if existing:
                # Check if update needed
                needs_update = False
                for key, value in addr_config.items():
                    if key != 'name' and getattr(existing, key, None) != value:
                        needs_update = True
                        setattr(existing, key, value)

                if needs_update:
                    self.addresses_api.update_addresses_by_id(
                        id=existing.id,
                        addresses=existing
                    )
                    logger.info(f"Updated address: {name}")
                else:
                    logger.info(f"Address unchanged: {name}")
            else:
                # Create new
                address = Addresses(id="", folder=folder, **addr_config)
                self.addresses_api.create_addresses(addresses=address)
                logger.info(f"Created address: {name}")

    def deploy_security_rules(self, rules_config: List[Dict[str, Any]], folder: str):
        """Deploy security rules idempotently."""
        # Implementation similar to addresses
        pass

# Usage
deployer = IdempotentDeployer(client)

addresses_config = [
    {
        'name': 'web-server',
        'ip_netmask': '10.0.0.1/32',
        'description': 'Production web server',
        'tag': ['Production']
    },
    # ... more addresses
]

deployer.deploy_addresses(addresses_config, folder="Texas")
```

---

## Atomic Operations

### Pattern: Transaction-like Updates

Group related updates with rollback capability.

```python
class Transaction:
    """Transaction-like context for API operations."""

    def __init__(self):
        self.operations = []
        self.rollback_operations = []

    def add_operation(self, forward_op, rollback_op):
        """Add operation with rollback."""
        self.operations.append(forward_op)
        self.rollback_operations.append(rollback_op)

    def execute(self):
        """Execute all operations."""
        executed = []

        try:
            for op in self.operations:
                result = op()
                executed.append(result)

            return executed

        except Exception as e:
            logger.error(f"Transaction failed: {e}")
            logger.info("Rolling back...")

            # Execute rollback operations in reverse
            for rollback_op in reversed(self.rollback_operations[:len(executed)]):
                try:
                    rollback_op()
                except Exception as rollback_err:
                    logger.error(f"Rollback failed: {rollback_err}")

            raise

# Usage
txn = Transaction()

# Create address
def create_addr():
    return addresses_api.create_addresses(addresses=address1)

def rollback_addr(addr_id):
    return lambda: addresses_api.delete_addresses_by_id(id=addr_id)

created_addr = create_addr()
txn.add_operation(
    lambda: created_addr,
    rollback_addr(created_addr.id)
)

# Add more operations...

# Execute transaction
try:
    results = txn.execute()
    logger.info("Transaction successful")
except Exception:
    logger.error("Transaction failed and rolled back")
```

---

## Validation Patterns

### Pattern: Pre-Creation Validation

Validate objects before creating.

```python
from typing import Optional

class AddressValidator:
    """Validate address objects before creation."""

    @staticmethod
    def validate_ip_netmask(ip_netmask: str) -> bool:
        """Validate IP/netmask format."""
        import ipaddress
        try:
            ipaddress.ip_network(ip_netmask, strict=False)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_fqdn(fqdn: str) -> bool:
        """Validate FQDN format."""
        import re
        pattern = r'^(?=.{1,253}$)(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})$'
        return bool(re.match(pattern, fqdn))

    @classmethod
    def validate_address(cls, address_data: dict) -> tuple[bool, Optional[str]]:
        """
        Validate address data.

        Returns:
            tuple: (is_valid, error_message)
        """
        # Check required fields
        if 'name' not in address_data:
            return False, "Name is required"

        if 'folder' not in address_data:
            return False, "Folder is required"

        # Check address type
        has_ip = 'ip_netmask' in address_data
        has_fqdn = 'fqdn' in address_data
        has_range = 'ip_range' in address_data

        if sum([has_ip, has_fqdn, has_range]) != 1:
            return False, "Must specify exactly one of: ip_netmask, fqdn, ip_range"

        # Validate IP if present
        if has_ip and not cls.validate_ip_netmask(address_data['ip_netmask']):
            return False, f"Invalid IP/netmask: {address_data['ip_netmask']}"

        # Validate FQDN if present
        if has_fqdn and not cls.validate_fqdn(address_data['fqdn']):
            return False, f"Invalid FQDN: {address_data['fqdn']}"

        return True, None

# Usage
address_data = {
    'id': '',
    'name': 'web-server',
    'folder': 'Texas',
    'ip_netmask': '10.0.0.1/32'
}

is_valid, error = AddressValidator.validate_address(address_data)

if is_valid:
    address = Addresses(**address_data)
    created = addresses_api.create_addresses(addresses=address)
else:
    logger.error(f"Validation failed: {error}")
```

---

## Logging and Debugging

### Pattern: Detailed Operation Logging

Log all operations for audit trail.

```python
import logging
from functools import wraps
from typing import Callable

def log_operation(operation_type: str):
    """Decorator to log API operations."""

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"[{operation_type}] Starting: {func.__name__}")
            logger.debug(f"  Args: {args}")
            logger.debug(f"  Kwargs: {kwargs}")

            try:
                result = func(*args, **kwargs)
                logger.info(f"[{operation_type}] Success: {func.__name__}")
                return result

            except Exception as e:
                logger.error(f"[{operation_type}] Failed: {func.__name__}")
                logger.error(f"  Error: {e}")
                raise

        return wrapper
    return decorator

# Usage
@log_operation("CREATE")
def create_address_with_logging(api, name, folder, ip):
    address = Addresses(
        id="",
        name=name,
        folder=folder,
        ip_netmask=ip
    )
    return api.create_addresses(addresses=address)

result = create_address_with_logging(
    addresses_api,
    "web-server",
    "Texas",
    "10.0.0.1/32"
)
```

### Pattern: Debug Mode with Request/Response Logging

Enable detailed debugging.

```python
import logging

def enable_debug_mode():
    """Enable detailed debug logging."""

    # Set SCM SDK to DEBUG
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Create client with debug logging
    client = Scm(log_level="DEBUG")

    return client

# Usage
client = enable_debug_mode()
addresses_api = client.objects.AddressesApi(client.objects.api_client)

# All API calls will now log request/response details
```

---

## Additional Resources

- [Examples](EXAMPLES.md) - Practical examples for each service
- [Migration Guide](MIGRATION_GUIDE.md) - Migrating from pan-scm-sdk
- [API Reference](../scm/) - Full API documentation
