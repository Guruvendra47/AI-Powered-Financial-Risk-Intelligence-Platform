# Apache Airflow Orchestration

## Overview

This folder contains the Apache Airflow DAG responsible for orchestrating the end-to-end Financial Risk Intelligence Platform.

The workflow automates:

* CFPB complaint ingestion
* Data validation
* AWS S3 uploads
* dbt transformations
* AI-powered risk classification

The DAG ensures that all pipeline stages execute in the correct sequence while maintaining dependency management and workflow monitoring.

---

# DAG Structure

DAG Name:

```text
financial_risk_pipeline
```

Location:

```text
docker/airflow/dags/financial_risk_pipeline.py
```

---

# End-to-End Workflow

```text
CFPB Complaint API
          │
          ▼
download_validate_upload
          │
          ▼
       dbt_run
          │
          ▼
 process_complaints
          │
          ▼
Risk Intelligence Dataset
```

---

# Task 1: download_validate_upload

Operator:

```python
PythonOperator
```

Purpose:

Responsible for ingesting and validating CFPB complaint data.

Workflow:

```text
Download Complaint Data
            │
            ▼
Validate Dataset
            │
            ▼
Upload to AWS S3
```

Source Files:

```text
src/data/ingestion/complaints/download_cfpb.py

src/data/ingestion/complaints/validate_file.py

src/data/ingestion/complaints/upload_to_s3.py
```

Responsibilities:

* Connect to CFPB API
* Retrieve complaint records
* Validate required fields
* Check duplicate records
* Analyze null values
* Upload validated data to AWS S3

Output:

```text
Validated complaint dataset stored in AWS S3
```

---

# Task 2: dbt_run

Operator:

```python
BashOperator
```

Purpose:

Executes dbt transformations inside the Docker environment.

Command:

```bash
dbt run --profiles-dir .
```

Workflow:

```text
Snowflake RAW Layer
          │
          ▼
stg_complaints
          │
          ▼
Gold Layer Models
```

Models Built:

```text
stg_complaints

dim_company
dim_location
dim_product
dim_channel

fact_complaints
```

Responsibilities:

* Execute Silver layer transformations
* Build Gold layer models
* Create analytics-ready datasets
* Prepare reporting tables for Power BI

Output:

```text
ANALYTICS_SILVER
ANALYTICS_GOLD
```

---

# Task 3: process_complaints

Operator:

```python
PythonOperator
```

Purpose:

Performs AI-powered complaint analysis using OpenAI models.

Source Files:

```text
src/ai/complaint_analyzer.py

src/ai/process_complaints.py
```

Workflow:

```text
Complaint Narrative
         │
         ▼
OpenAI Analysis
         │
         ├── Risk Classification
         ├── Sentiment Analysis
         └── Summary Generation
         │
         ▼
Enriched Dataset
```

Responsibilities:

* Read complaint narratives
* Generate AI risk categories
* Perform sentiment analysis
* Create complaint summaries
* Store AI-generated insights

Output:

```text
Risk Intelligence Dataset
```

---

# DAG Configuration

Schedule:

```python
@daily
```

Start Date:

```python
datetime(2025, 1, 1)
```

Catchup:

```python
False
```

Tags:

```text
financial-risk
snowflake
dbt
genai
```

---

# Dependency Management

The DAG uses sequential task dependencies.

```python
ingestion_task >> dbt_run_task >> ai_enrichment_task
```

Execution Order:

```text
1. download_validate_upload

2. dbt_run

3. process_complaints
```

Benefits:

* Prevents downstream failures
* Maintains data consistency
* Ensures transformation occurs after ingestion
* Ensures AI enrichment occurs after modeling

---

# Monitoring

Airflow provides:

* DAG execution tracking
* Task-level monitoring
* Retry management
* Failure notifications
* Log management

Examples:

```text
Task Duration

Task Success Rate

Task Failure Tracking

Execution History
```

---

# Business Value

Apache Airflow enables:

* Automated workflow orchestration
* Reliable data processing
* Scheduled pipeline execution
* Dependency management
* Operational visibility
* Scalable enterprise workflows

---

# Skills Demonstrated

* Apache Airflow
* DAG Development
* Workflow Orchestration
* Python Operators
* Bash Operators
* ETL Automation
* Dependency Management
* Data Pipeline Monitoring
* Snowflake Integration
* dbt Integration
* OpenAI Integration

```
```
