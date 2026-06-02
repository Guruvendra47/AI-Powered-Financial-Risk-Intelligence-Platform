# Utilities Layer (`src/utils/`)

The utilities layer contains reusable framework components shared across the entire platform. By separating logging, exception handling, and operational utilities from business logic, the application maintains consistency, scalability, and predictable error management across all services.

This layer provides:

* centralized logging
* standardized exception handling
* reusable utility functions
* improved debugging capabilities
* cleaner application architecture

---

# Centralized Logging (`logger.py`)

Instead of configuring logging separately in multiple modules, the platform uses a centralized logging utility through `logger.py`.

All application components import a pre-configured logger instance to maintain a consistent logging structure across the platform.

---

# Logging Configuration

## Default Logging Features

| Configuration   | Description                                                                    |       |               |          |
| --------------- | ------------------------------------------------------------------------------ | ----- | ------------- | -------- |
| Log Level       | Defaults to `INFO` and can be switched to `DEBUG` through environment settings |       |               |          |
| Log Format      | `[YYYY-MM-DD HH:MM:SS]                                                         | LEVEL | [module:line] | Message` |
| Output Handlers | Logs are written to both console and local log files                           |       |               |          |
| Log Rotation    | Daily log rotation prevents excessive file growth                              |       |               |          |

---

# Benefits of Centralized Logging

Using a centralized logging framework provides several operational advantages:

* standardized log formatting
* simplified debugging
* centralized monitoring
* improved observability
* easier production troubleshooting

This approach is commonly used in enterprise-grade data engineering and distributed systems.

---

# Logger Integration Example

Always initialize loggers using the `get_logger()` factory method.

## Recommended Implementation

```python id="v4m2kc"
from src.utils.logger import get_logger

# Initialize module-level logger
logger = get_logger(__name__)

def download_data():
    logger.info("Initializing connection to CFPB endpoint...")

    try:
        # Business logic execution
        logger.debug("Parsing data payload in memory.")

    except Exception as e:
        logger.error(f"Fatal network exception encountered: {str(e)}")
```

---

# Custom Exception Framework (`exceptions.py`)

Standard Python exceptions such as `ValueError` or `RuntimeError` are often insufficient for large-scale data platforms because they do not provide domain-specific context.

To improve reliability and debugging efficiency, the platform implements a structured custom exception hierarchy built on top of a base `PlatformException` class.

This approach enables faster issue identification and cleaner failure management.

---

# Exception Hierarchy

| Exception Class     | Base Class          | Usage Context                                                         |
| ------------------- | ------------------- | --------------------------------------------------------------------- |
| `PlatformException` | `Exception`         | Base exception for internal platform errors                           |
| `CFPBDownloadError` | `PlatformException` | Raised during API failures, network issues, or download interruptions |
| `S3UploadError`     | `PlatformException` | Raised during S3 upload failures or authentication issues             |
| `ValidationError`   | `PlatformException` | Raised when schema, headers, or row validations fail                  |

---

# Benefits of Custom Exceptions

Custom exception handling provides:

* clearer error categorization
* improved debugging workflows
* predictable failure handling
* better monitoring integration
* cleaner retry and recovery logic

This structure is especially important in distributed data pipelines where failures can occur across multiple infrastructure layers.

---

# Exception Integration Example

Use custom exceptions inside `try/except` blocks to create meaningful system-level alerts and error handling.

## Recommended Implementation

```python id="2f3x7m"
import requests

from src.utils.exceptions import CFPBDownloadError
from src.utils.logger import get_logger

logger = get_logger(__name__)

def fetch_cfpb_payload(url: str):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Wrap external exception inside platform-specific exception
        raise CFPBDownloadError(
            f"Failed to retrieve historical CFPB records: {str(e)}"
        )
```

---

# Recommended Best Practices

## Logging Best Practices

* Use contextual log messages
* Avoid logging sensitive credentials
* Use appropriate log levels (`INFO`, `DEBUG`, `ERROR`)
* Enable log rotation for long-running applications

## Exception Handling Best Practices

* Use domain-specific exceptions
* Avoid generic `except:` blocks
* Include meaningful error messages
* Preserve original exception context where possible

---

# Summary

The utilities layer acts as the operational backbone of the platform by providing reusable logging and exception management capabilities.

This architecture ensures:

* consistent operational standards
* improved maintainability
* scalable debugging workflows
* reliable error classification
* enterprise-grade observability

The `src/utils/` framework supports stable and maintainable data engineering workflows across ingestion, transformation, orchestration, and AI service layers.
