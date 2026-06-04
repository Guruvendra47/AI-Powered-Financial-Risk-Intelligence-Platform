# Data Ingestion Layer

## Overview

The Data Ingestion Layer is responsible for collecting financial complaint data from external sources, validating data quality, and loading datasets into cloud storage for downstream processing.

The ingestion pipeline automates the collection of CFPB consumer complaints and prepares the data for Snowflake loading, dbt transformations, AI enrichment, and Power BI reporting.

---

# Architecture

```text
CFPB API
    │
    ▼
download_cfpb.py
    │
    ▼
validate_file.py
    │
    ▼
upload_to_s3.py
    │
    ▼
AWS S3
    │
    ▼
Snowflake
    │
    ▼
dbt
    │
    ▼
AI Risk Intelligence
    │
    ▼
Power BI
```

---

# Directory Structure

```text
src/
└── data/
    └── ingestion/
        │
        ├── complaints/
        │   ├── download_cfpb.py
        │   ├── validate_file.py
        │   └── upload_to_s3.py
        │
        ├── documents/
        │   └── document_ingestion.py
        │
        ├── utils/
        │   ├── logger.py
        │   └── exceptions.py
        │
        └── tests/
```

---

# CFPB Complaint Ingestion

## Overview

The CFPB complaint ingestion process automatically retrieves complaint data from the Consumer Financial Protection Bureau API.

The downloaded data is validated and uploaded to AWS S3 before being loaded into Snowflake.

---

# Step 1: Download Data

File:

```text
complaints/download_cfpb.py
```

Purpose:

Downloads complaint records from the CFPB API.

---

## Responsibilities

```text
API Connectivity

Date Filtering

Response Validation

Retry Handling

Data Extraction

Pandas DataFrame Creation
```

---

## Workflow

```text
CFPB API
      │
      ▼
HTTP Request
      │
      ▼
JSON Response
      │
      ▼
Pandas DataFrame
```

---

## Example Processing Window

```python
start_date="2025-01-01"
end_date="2025-01-31"
```

---

# Step 2: Validate Data

File:

```text
complaints/validate_file.py
```

Purpose:

Ensures complaint data meets quality requirements before loading.

---

## Validation Checks

### Row Count Validation

Confirms records exist.

Example:

```text
475,783 Records
```

---

### Required Columns Validation

Checks critical fields.

Example:

```text
COMPLAINT_ID

DATE_RECEIVED

PRODUCT

COMPANY
```

---

### Duplicate Detection

Identifies duplicate complaints.

Example:

```text
Duplicate Records Found: 0
```

---

### Null Value Analysis

Validates critical columns.

Example:

```text
COMPLAINT_ID Null Count

DATE_RECEIVED Null Count
```

---

# Step 3: Upload to AWS S3

File:

```text
complaints/upload_to_s3.py
```

Purpose:

Uploads validated complaint data to AWS S3.

---

## Responsibilities

```text
CSV Generation

S3 Upload

Bucket Management

Cloud Storage Integration
```

---

## Workflow

```text
Validated DataFrame
        │
        ▼
CSV Export
        │
        ▼
AWS S3
```

---

# AWS S3 Landing Zone

Purpose:

Stores validated complaint datasets before Snowflake ingestion.

Benefits:

```text
Scalable Storage

Durability

Centralized Data Lake

Cloud-Native Architecture
```

---

# Document Ingestion

File:

```text
documents/document_ingestion.py
```

Purpose:

Loads compliance, regulatory, and risk management documents used by the RAG system.

---

## Supported Sources

```text
Compliance Documents

Regulatory Documents

Risk Reports
```

---

## Output

Documents become available for:

```text
Chunking

Embedding Generation

Vector Search

RAG Question Answering
```

---

# Logging Framework

File:

```text
utils/logger.py
```

Purpose:

Provides centralized application logging.

---

## Logged Events

```text
API Requests

Download Status

Validation Results

Upload Status

Errors

Warnings
```

---

# Exception Handling

File:

```text
utils/exceptions.py
```

Purpose:

Provides custom exception handling across ingestion workflows.

Benefits:

```text
Cleaner Error Messages

Improved Debugging

Pipeline Stability
```

---

# Airflow Integration

The ingestion layer is orchestrated using Apache Airflow.

DAG:

```text
financial_risk_pipeline
```

---

## Airflow Workflow

```text
download_validate_upload
        │
        ▼
dbt_run
        │
        ▼
process_complaints
```

---

## Ingestion Task

```text
download_validate_upload
```

Performs:

```text
Download CFPB Data

Validate Data

Upload to AWS S3
```

---

# Testing

Location:

```text
src/data/ingestion/tests
```

Files:

```text
test_download_cfpb.py

test_validate_file.py

5_test_upload_to_s3.py

test_logger.py

test_exceptions.py
```

---

# End-to-End Data Flow

```text
CFPB API
      │
      ▼
Download Data
      │
      ▼
Validation
      │
      ▼
AWS S3
      │
      ▼
Snowflake RAW
      │
      ▼
dbt SILVER
      │
      ▼
dbt GOLD
      │
      ▼
AI Enrichment
      │
      ▼
Power BI
```

---

# Business Value

The ingestion layer automates the collection and preparation of financial complaint data, eliminating manual data gathering processes.

Benefits:

* Automated data collection
* Improved data quality
* Scalable cloud ingestion
* Faster analytics delivery
* Reliable reporting datasets
* Foundation for AI-driven risk analysis

---

# Skills Demonstrated

```text
Python

REST APIs

Data Ingestion

Data Validation

AWS S3

Pandas

ETL Pipelines

Apache Airflow

Logging

Exception Handling

Cloud Data Engineering

Financial Data Processing
```
