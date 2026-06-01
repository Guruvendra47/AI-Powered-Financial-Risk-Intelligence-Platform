# 🛠️ Utilities Layer (`src/utils/`)

The utilities layer contains global framework components used across the entire application ecosystem. By decoupling logging and error classification from specific business logic, the platform ensures standardized tracking and predictable failure recovery.

---

## 📝 Centralized Logging (`logger.py`)

Rather than initializing basic logging setups across multiple individual files, components import a pre-configured utility logger. This ensures a consistent log format, standardized timestamps, and multi-handler routing (console and local files).

### ⚙️ Production Configurations
* **Log Level:** Inherits setting state (Defaults to `INFO`, changes to `DEBUG` via environment).
* **Format:** `[YYYY-MM-DD HH:MM:SS] | LEVEL | [module:line] | Message`
* **File Rotation:** Configured to automatically split and archive logs daily to prevent storage bottlenecks.

### 💻 Code Integration

Always import and instantiate the logger through the `get_logger` factory method:

```python
from src.utils.logger import get_logger

# Initialize contextual logger for the module
logger = get_logger(__name__)

def download_data():
    logger.info("Initializing connection to CFPB endpoint...")
    try:
        # Code execution logic here
        logger.debug("Parsing data payload chunks in-memory.")
    except Exception as e:
        logger.error(f"Fatal network exception encountered: {str(e)}")
```
## ⚠️ Custom Platform Exceptions (`exceptions.py`)

Standard Python exceptions (like `ValueError` or `RuntimeError`) are often too vague for complex data pipelines. This platform implements a robust, domain-specific exception hierarchy inheriting from a base `PlatformException` class. 

Using specific custom exceptions isolates issues instantly, helping engineers identify whether a pipeline failure stems from network drops, schema validation mismatches, or cloud permission errors.

### 📂 Custom Exception Hierarchy

| Custom Exception Class | Base Class | Trigger Context |
| :--- | :--- | :--- |
| `PlatformException` | `Exception` | Base exception for all internal platform issues. |
| `CFPBDownloadError` | `PlatformException` | Triggered when API connections, file streaming, or data downloads fail. |
| `S3UploadError` | `PlatformException` | Triggered when bucket connections or programmatic object uploads fail. |
| `ValidationError` | `PlatformException` | Triggered when row counts, headers, or schema data types fail structural checks. |

### 💻 Code Integration

Utilize these custom exceptions inside your `try/except` blocks to raise explicit system alerts:

```python
import requests
from src.utils.exceptions import CFPBDownloadError
from src.utils.logger import get_logger

logger = get_logger(__name__)

def fetch_cfpb_payload(url: str):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Wrap the generic network exception inside our domain exception
        raise CFPBDownloadError(f"Failed to pull historical records from CFPB: {str(e)}")
