# Project Structure

```text
AI-Powered-Financial-Risk-Intelligence-Platform
│
├── src
│   ├── ai
│   │   ├── complaint_analyzer.py
│   │   ├── process_complaints.py
│   │   └── main.py
│   │
│   ├── cloud
│   │   ├── aws
│   │   └── snowflake
│   │
│   ├── rag
│   │   ├── load_documents.py
│   │   ├── chunk_documents.py
│   │   ├── create_embeddings.py
│   │   ├── retriever.py
│   │   └── rag_chain.py
│   │
│   ├── config
│   └── data
│
├── dbt
│   ├── models
│   │   ├── silver
│   │   │   └── stg_complaints.sql
│   │   │
│   │   └── gold
│   │       ├── dim_company.sql
│   │       ├── dim_location.sql
│   │       ├── dim_product.sql
│   │       ├── dim_channel.sql
│   │       └── fact_complaints.sql
│   │
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── docker
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── airflow
│
├── screenshots
│
├── README.md
└── requirements.txt
```

---

# Snowflake Data Architecture

The platform uses a multi-layer architecture within Snowflake to separate raw ingestion, transformed datasets, and analytical reporting layers.

## RAW Layer

Purpose:

Store source complaint data with minimal modification.

Table:

```text
RAW.RAW_COMPLAINTS
```

Responsibilities:

* Landing zone for complaint records
* Historical storage
* Source system preservation

---

## Silver Layer

Purpose:

Clean, validate, standardize, and deduplicate complaint records.

Model:

```text
ANALYTICS_SILVER.STG_COMPLAINTS
```

Transformations:

* Data type standardization
* Null handling
* Deduplication
* Text cleanup
* Date formatting

---

## Gold Layer

Purpose:

Create business-ready datasets optimized for analytics and reporting.

Dimension Tables:

```text
ANALYTICS_GOLD.DIM_COMPANY
ANALYTICS_GOLD.DIM_LOCATION
ANALYTICS_GOLD.DIM_PRODUCT
ANALYTICS_GOLD.DIM_CHANNEL
```

Fact Table:

```text
ANALYTICS_GOLD.FACT_COMPLAINTS
```

Benefits:

* Star schema design
* Improved query performance
* Power BI optimization
* Business-friendly analytics

---

# Apache Airflow Orchestration

The platform uses Apache Airflow to automate the complete workflow.

DAG:

```text
financial_risk_pipeline
```

Workflow:

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

## Task 1: Download and Validate Complaints

Responsibilities:

* Download CFPB complaint data
* Validate schema
* Check required columns
* Analyze null values
* Detect duplicate records
* Upload validated data to AWS S3

Source Files:

```text
download_cfpb.py
validate_file.py
upload_to_s3.py
```

---

## Task 2: dbt Transformations

Responsibilities:

* Execute Silver layer transformations
* Build Gold layer dimensional models
* Generate analytics-ready datasets

Command:

```bash
dbt run --profiles-dir .
```

---

## Task 3: AI Enrichment

Responsibilities:

* Read complaint narratives
* Generate risk classifications
* Perform sentiment analysis
* Produce AI-generated summaries
* Store enriched results

Source Files:

```text
complaint_analyzer.py
process_complaints.py
```

---

# dbt Analytics Engineering Layer

The project uses dbt to implement modern analytics engineering practices.

## Silver Model

### stg_complaints

Materialization:

```sql
incremental
```

Responsibilities:

* Data cleaning
* Data standardization
* Deduplication
* Type conversion

Source:

```text
RAW.RAW_COMPLAINTS
```

Output:

```text
ANALYTICS_SILVER.STG_COMPLAINTS
```

---

## Gold Models

### dim_company

Contains company-level attributes.

Example:

```text
Bank of America
Capital One
Wells Fargo
```

---

### dim_location

Contains geographic information.

Example:

```text
State
Zip Code
```

---

### dim_product

Contains complaint product categories.

Example:

```text
Credit Card
Mortgage
Checking Account
Student Loan
```

---

### dim_channel

Contains submission channel information.

Example:

```text
Web
Phone
Email
Referral
```

---

### fact_complaints

Central analytical fact table.

Contains:

* Complaint measures
* Company keys
* Product keys
* Location keys
* Channel keys

Supports:

* Complaint trend analysis
* Company comparisons
* Risk reporting
* Dashboard visualizations

```
```
