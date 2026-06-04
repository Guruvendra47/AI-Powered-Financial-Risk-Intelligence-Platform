# Snowflake Data Warehouse Layer

## Overview

The Snowflake Data Warehouse serves as the centralized analytics platform for the AI-Powered Financial Risk Intelligence Platform. It stores raw financial complaint data, cleansed analytical datasets, AI-enriched risk intelligence outputs, and reporting-ready dimensional models used by Power BI dashboards.

The platform follows a modern Medallion Architecture consisting of RAW, SILVER, and GOLD layers to ensure scalability, maintainability, and high-quality analytics.

---

# Snowflake Architecture

```text
CFPB API
    │
    ▼
AWS S3
    │
    ▼
RAW.RAW_COMPLAINTS
    │
    ▼
SILVER.STG_COMPLAINTS
    │
    ▼
GOLD DIMENSIONS
    │
    ├── DIM_COMPANY
    ├── DIM_LOCATION
    ├── DIM_PRODUCT
    └── DIM_CHANNEL
    │
    ▼
FACT_COMPLAINTS
    │
    ▼
AI RISK INTELLIGENCE
    │
    ▼
POWER BI
```

---

# Database Structure

Database:

```text
FINANCIAL_RISK_INTELLIGENCE
```

Schemas:

```text
RAW
ANALYTICS_SILVER
ANALYTICS_GOLD
```

---

# RAW Layer

## Purpose

The RAW layer serves as the landing zone for complaint data ingested from external sources.

No transformations are performed in this layer.

The objective is to preserve source-system fidelity for auditing, lineage tracking, and reprocessing.

---

## Tables

### RAW_COMPLAINTS

Stores complaint records downloaded from the CFPB Consumer Complaint Database and loaded from AWS S3 into Snowflake.

Key fields include:

```text
COMPLAINT_ID
DATE_RECEIVED
PRODUCT
SUB_PRODUCT
ISSUE
SUB_ISSUE
COMPANY
STATE
ZIP_CODE
SUBMITTED_VIA
CONSUMER_COMPLAINT_NARRATIVE
```

---

# SILVER Layer (dbt)

Schema:

```text
ANALYTICS_SILVER
```

---

## Purpose

The SILVER layer contains cleansed and standardized complaint data.

Data quality rules are applied before making the dataset available for analytics.

---

## Transformations Performed

### Data Validation

* Removes records with missing Complaint IDs
* Removes records with missing dates
* Ensures required fields exist

### Data Standardization

* Trims whitespace
* Standardizes text formatting
* Converts dates into Snowflake date format

### Deduplication

Duplicate complaints are removed using:

```sql
ROW_NUMBER()
```

partitioned by:

```text
COMPLAINT_ID
```

keeping only the most recent record.

---

## Tables

### STG_COMPLAINTS

Contains validated and standardized complaint records used by downstream models.

---

# GOLD Layer (dbt)

Schema:

```text
ANALYTICS_GOLD
```

---

## Purpose

The GOLD layer contains business-ready dimensional models optimized for reporting and analytics.

These models support Power BI dashboards and AI-generated risk intelligence reporting.

---

# Dimension Tables

## DIM_COMPANY

Contains unique companies involved in consumer complaints.

Example:

```text
JPMORGAN CHASE
BANK OF AMERICA
WELLS FARGO
CAPITAL ONE
```

---

## DIM_LOCATION

Contains geographic information.

Example:

```text
State
Zip Code
```

Used for geographic analysis and complaint heat maps.

---

## DIM_PRODUCT

Contains complaint product categories.

Example:

```text
Credit Card
Mortgage
Checking Account
Auto Loan
```

---

## DIM_CHANNEL

Contains complaint submission channels.

Example:

```text
Web
Phone
Referral
Postal Mail
```

---

# Fact Table

## FACT_COMPLAINTS

Central analytical table containing complaint events.

Links all dimensions together.

Measures include:

```text
Complaint Count
Complaint Volume
Risk Trends
Complaint Distribution
```

---

# Snowflake Connection

The platform connects to Snowflake using a reusable Python connection module.

Location:

```text
src/cloud/snowflake/snowflake_connection.py
```

---

## Environment Variables

Snowflake credentials are securely managed through environment variables.

```text
SNOWFLAKE_ACCOUNT

SNOWFLAKE_USER

SNOWFLAKE_PASSWORD

SNOWFLAKE_ROLE

SNOWFLAKE_WAREHOUSE

SNOWFLAKE_DATABASE

SNOWFLAKE_SCHEMA
```

---

# Data Loading Process

The platform follows the workflow below:

### Step 1

Download complaint data from CFPB.

```text
CFPB API
```

---

### Step 2

Validate complaint records.

Validation checks:

```text
Missing Values

Required Columns

Duplicate Records

Schema Validation
```

---

### Step 3

Upload validated files to AWS S3.

```text
AWS S3 Landing Zone
```

---

### Step 4

Load complaint data into Snowflake RAW layer.

```text
RAW.RAW_COMPLAINTS
```

---

### Step 5

Execute dbt transformations.

```text
RAW
  →
SILVER
  →
GOLD
```

---

### Step 6

Provide analytical datasets to:

```text
Power BI

AI Risk Intelligence Layer

Future APIs
```

---

# AI Enrichment Storage

The platform includes Snowflake tables designed to support AI and Retrieval-Augmented Generation (RAG) workflows.

---

## AI Query Log

Tracks AI interactions and user questions.

File:

```text
create_ai_query_log.sql
```

---

## Risk Analysis

Stores AI-generated risk assessments.

File:

```text
create_risk_analysis.sql
```

---

## Regulatory Documents

Stores compliance and regulatory documents.

File:

```text
create_regulatory_documents.sql
```

---

## Document Embeddings

Stores vector embeddings generated from regulatory and compliance documents.

File:

```text
create_document_embeddings.sql
```

---

# SQL Objects Created

## DDL Scripts

Location:

```text
src/cloud/snowflake/sql/ddl
```

Files:

```text
create_complaints.sql

create_document_embeddings.sql

create_risk_analysis.sql

create_regulatory_documents.sql

create_ai_query_log.sql
```

---

## DML Scripts

Location:

```text
src/cloud/snowflake/sql/dml
```

Files:

```text
8-transform-raw-complaint-table-to-complaints.sql

9-create-dim-tables.sql

10-create-fact-table.sql
```

---

# Power BI Consumption Layer

Power BI connects directly to Snowflake GOLD models.

Primary reporting tables:

```text
FACT_COMPLAINTS

DIM_COMPANY

DIM_LOCATION

DIM_PRODUCT

DIM_CHANNEL
```

---

## Dashboard Capabilities

### Complaint Trend Analysis

Tracks complaint volumes over time.

### Product Risk Analysis

Identifies products generating the highest complaint volume.

### Geographic Analysis

Analyzes complaint distribution across states.

### Company Performance Analysis

Compares complaint volumes by financial institution.

### AI Risk Intelligence Dashboard

Visualizes AI-generated complaint risk classifications and trends.

---

# Business Value

The Snowflake platform serves as the centralized analytical repository for financial complaint data, AI-generated risk insights, and reporting datasets.

It enables scalable storage, fast analytical queries, dimensional modeling, and integration with Power BI dashboards for financial risk intelligence reporting.

The architecture supports future expansion into real-time risk monitoring, advanced analytics, and enterprise-scale AI applications.

---

# Skills Demonstrated

```text
Snowflake

SQL

Data Warehousing

Data Modeling

Dimensional Modeling

Fact Tables

Dimension Tables

ETL Pipelines

dbt

AWS S3

Data Transformation

Cloud Analytics

Power BI Integration

Financial Risk Analytics

Generative AI Data Platforms

RAG Architecture Support
```
