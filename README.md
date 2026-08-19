# QRadar SDK

A Python SDK for the IBM QRadar REST API (version 26.0).

## Installation

### Install from source

```bash
pip install -e .
```

### Install from a private GitHub repository

The package can be installed directly from a private repository. Use an
authenticated GitHub SSH remote (recommended):

```bash
pip install "git+ssh://git@github.com/binhnguyen143/PyRadar.git@master"
```

Or use HTTPS with a GitHub credential helper or a short-lived token:

```bash
pip install "git+https://github.com/binhnguyen143/PyRadar.git@master"
```

Pin a release tag or commit in production instead of `main`, for example:

```bash
pip install "git+ssh://git@github.com/binhnguyen143/PyRadar.git@v26.0.0"
```

The repository must contain `pyproject.toml` at its root. No package build or
publish step is required for direct Git installation; pip builds the wheel
locally and installs its declared dependencies.

### Install with development dependencies

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from qradar_sdk import QRadarClient

# Initialize the client
client = QRadarClient(
    host="qradar.example.com",
    sec_token="<your-service-token>",
    verify_ssl=False,
)

# Get open offenses
offenses = client.siem.offenses.list(filter="status=OPEN")
print(f"Found {len(offenses)} open offenses")

# Execute an AQL search
result = client.ariel.searches.create(
    query_expression="SELECT * FROM events LAST 5 MINUTES"
)
search_id = result["search_id"]
print(f"Search started: {search_id}")

# Close the client when done
client.close()
```

### Using Context Manager

```python
with QRadarClient(host="qradar.example.com", sec_token="token") as client:
    offenses = client.siem.offenses.list()
```

### Async Usage (for async microservices)

```python
import asyncio
from qradar_sdk import AsyncQRadarClient


async def main() -> None:
    async with AsyncQRadarClient(host="qradar.example.com", sec_token="token") as client:
        offenses = await client.siem.offenses.list()
        print(f"Found {len(offenses)} open offenses")


asyncio.run(main())
```

## Resource API

Endpoints are organized by their QRadar URL hierarchy. Collection and item
operations use short, predictable names:

```python
# GET /siem/offenses
offenses = client.siem.offenses.list(filter="status=OPEN")

# GET /siem/offenses/{offense_id}
offense = client.siem.offenses.get(offense_id)

# POST /siem/offenses/{offense_id}
updated = client.siem.offenses.update(offense_id, follow_up=True)

# POST /siem/offenses/{offense_id}/notes
note = client.siem.offenses.notes.create(offense_id, note_text="Investigating")
```

The available operation names are `list`, `get`, `create`, `update`, `delete`,
`replace`, and `update_many`, depending on the methods supported by QRadar.

## Authentication

The SDK supports two authentication methods:

### SEC Token (Recommended)

```python
client = QRadarClient(
    host="qradar.example.com",
    sec_token="your-sec-token-here",
    verify_ssl=True
)
```

### Basic Authentication

```python
client = QRadarClient(
    host="qradar.example.com",
    username="admin",
    password="your-password",
    verify_ssl=True
)
```

## Available API Tags

The SDK provides access to all major QRadar API endpoints organized by tags:

- `access` - Access management
- `analytics` - Analytics rules
- `ariel` - AQL searches
- `asset_model` - Asset management
- `auth` - Authentication
- `backup_and_restore` - Backup operations
- `bandwidth_manager` - Bandwidth management
- `config` - Configuration
- `data_classification` - Data classification
- `disaster_recovery` - Disaster recovery
- `dynamic_search` - Dynamic searches
- `forensics` - Forensics
- `gui_app_framework` - GUI applications
- `health` - System health
- `health_data` - Health data
- `help` - API help
- `qni` - QRadar Network Insights
- `qrm` - QRadar Risk Manager
- `qvm` - QRadar Vulnerability Manager
- `reference_data` - Reference data
- `reference_data_collections` - Reference data collections
- `scanner` - Scanner management
- `services` - Services
- `siem` - SIEM offenses and events
- `staged_config` - Staged configuration
- `system` - System information

## Features

- Resource-oriented access to 729 methods covering the complete QRadar API
- Discoverable operations such as `list`, `get`, `create`, `update`, and `delete`
- Type hints with `py.typed` marker
- Automatic pagination support
- Custom exceptions for different error types
- SSL verification control
- API version specification
- Context manager support

## Development

### Running Tests

```bash
pytest
```

### Running Tests with Coverage

```bash
pytest --cov=qradar_sdk --cov-report=html
```

### Code Formatting

```bash
black qradar_sdk tests
```

### Type Checking

```bash
mypy qradar_sdk
```

## Error Handling

The SDK provides specific exception types:

```python
from qradar_sdk import (
    QRadarError,           # Base exception
    QRadarAPIError,        # General API errors
    QRadarAuthError,       # Authentication failures (401)
    QRadarNotFoundError,   # Resource not found (404)
    QRadarRateLimitError,  # Rate limit exceeded (429)
)

try:
    offense = client.siem.offenses.get(offense_id=9999)
except QRadarNotFoundError:
    print("Offense not found")
except QRadarAuthError:
    print("Authentication failed")
except QRadarAPIError as e:
    print(f"API error: {e.status_code} - {e.message}")
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on GitHub.
