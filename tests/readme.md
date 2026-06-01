# 🧪 Automated Test Pipeline & Quality Assurance

This directory contains the serialized testing framework for the platform's data ingestion and validation layers. The test suite is intentionally ordered with numeric prefixes (`1_` through `5_`) to create a **progressive execution pipeline**. This design isolates failures early in the ingestion lifecycle before interacting with remote cloud infrastructure.

---

## 📈 Test Execution Sequence

To execute the test suite completely and accurately, run the modules sequentially from the project's root directory using your active virtual environment:

```powershell
# Step 1: Verify Core Platform Logging
python -m tests.1_test_logger

# Step 2: Validate Error Framework Bound-Checking
python -m tests.2_test_exceptions

# Step 3: Test Live API Streaming & Response Parsing
python -m tests.3_test_download_cfpb

# Step 4: Enforce Data Quality & Schema Contracts
python -m tests.4_test_validate_file

# Step 5: Test In-Memory Parquet Compression & S3 Stream Upload
python -m tests.5_test_upload_to_s3

```

---

## 🔍 Detailed Module Breakdown

### `1_test_logger.py` — Infrastructure Logging Agent

* **Objective:** Validates that the centralized logging framework (`src/utils/logger.py`) properly instantiates, formats string outputs, and writes logs to standard output streams.
* **Interview Context:** *Ensures complete observability and system traceability across distributed workers before data pipelines fire.*

### `2_test_exceptions.py` — Custom Error Bounds

* **Objective:** Tests the platform's ability to cleanly raise and trap domain-specific exceptions (e.g., `CFPBDownloadError`, `ValidationError`, `S3UploadError`).
* **Interview Context:** *Demonstrates defensive software engineering principles by preventing generic, unhandled runtime crashes from obscuring root-cause pipeline issues.*

### `3_test_download_cfpb.py` — API Extraction Engine

* **Objective:** Hits the live CFPB consumer complaints endpoint using streaming parameters (`format=csv`), testing connection limits, network timeouts, and raw chunk-based byte conversions into a Pandas DataFrame.
* **Interview Context:** *Validates efficient utilization of raw data sources and network connection stability.*

### `4_test_validate_file.py` — Schema Gatekeeper & Data Quality Layer

* **Objective:** Validates the pulled dataset against the pipeline's strict structural contract. It checks for completely empty states, tests for critical required columns (`Complaint ID`, `Date received`, `Product`, `Company`, `Consumer complaint narrative`), evaluates duplicate records using the primary business key (`Complaint ID`), and prints a missing value null analysis profile.
* **Interview Context:** *This is the critical gatekeeper. It keeps corrupt data, structural shifts, or missing AI text features from breaking Snowflake loads or wasting OpenAI tokens.*

### `5_test_upload_to_s3.py` — Cloud Storage Ingestion

* **Objective:** Runs the complete end-to-end ingestion thread. It downloads sample records, runs validation checks, converts the data to a memory-efficient Parquet format using the `pyarrow` engine, builds a partitioned destination path (`raw/complaints/year=YYYY/month=MM/day=DD/`), appends an audit timestamp, and streams the binary payload directly into AWS S3 via `boto3`.
* **Interview Context:** *Proves storage-only optimization for S3 (Landing Zone) before handover to Snowflake/dbt for Medallion layer modeling.*

---

## ⚙️ Requirements & Environment State

To prevent execution failures during test runs, ensure the following core libraries are installed and verified in your local environment (`myenv`):

* `pandas` — Matrix structure and internal dataframe parsing.
* `pyarrow` — High-performance backend engine required for `.to_parquet()` transformations.
* `boto3` — AWS SDK for Python to open connection pipes and land files in S3.
* `requests` — HTTP library for stream communication with the CFPB API endpoints.

```powershell
pip install pandas pyarrow boto3 requests

```

> ⚠️ **AWS Authentication Note:** Prior to running `5_test_upload_to_s3.py`, make sure your terminal is securely authenticated with AWS IAM user credentials that possess `s3:PutObject` access on your designated landing bucket.
