# QRadar SDK

A Python SDK for the IBM QRadar REST API (version 26.0).

## Installation

### Install from source

```bash
pip install -e .
```

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
offenses = client.siem.get_siem_offenses(filter="status=OPEN")
print(f"Found {len(offenses)} open offenses")

# Execute an AQL search
result = client.ariel.post_ariel_searches(
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
    offenses = client.siem.get_siem_offenses()
```

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

- 729 methods covering the complete QRadar API
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
    offense = client.siem.get_siem_offenses_offense_id(offense_id=9999)
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
