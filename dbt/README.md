# dbt Analytics Engineering Layer

## Overview

This folder contains the dbt project responsible for transforming raw financial complaint data stored in Snowflake into analytics-ready datasets used by Power BI dashboards and AI-driven risk intelligence workflows.

The dbt layer follows a modern Medallion Architecture approach by implementing Silver and Gold transformation layers.

---

# Architecture

```text
RAW Layer
RAW.RAW_COMPLAINTS
        │
        ▼
Silver Layer
ANALYTICS_SILVER.STG_COMPLAINTS
        │
        ▼
Gold Layer
DIM_COMPANY
DIM_LOCATION
DIM_PRODUCT
DIM_CHANNEL
FACT_COMPLAINTS
```

---

# Project Structure

```text
dbt
│
├── models
│   ├── silver
│   │   └── stg_complaints.sql
│   │
│   └── gold
│       ├── dim_company.sql
│       ├── dim_location.sql
│       ├── dim_product.sql
│       ├── dim_channel.sql
│       └── fact_complaints.sql
│
├── dbt_project.yml
├── profiles.yml
└── README.md
```

---

# Silver Layer

## stg_complaints

Materialization:

```sql
incremental
```

Source Table:

```text
FINANCIAL_RISK_INTELLIGENCE.RAW.RAW_COMPLAINTS
```

Target Table:

```text
FINANCIAL_RISK_INTELLIGENCE.ANALYTICS_SILVER.STG_COMPLAINTS
```

Responsibilities:

* Data cleaning
* Data standardization
* Duplicate removal
* Null handling
* Data type conversion
* Incremental processing

Transformations:

* Convert complaint identifiers to numeric format
* Standardize date fields
* Trim unnecessary whitespace
* Normalize company names
* Remove duplicate complaints
* Validate required business fields

---

# Gold Layer

The Gold Layer contains dimensional models optimized for reporting and analytics.

---

## DIM_COMPANY

Purpose:

Stores unique company information.

Example:

```text
Bank of America
Capital One
Wells Fargo
Citibank
```

Business Value:

Supports complaint analysis by company.

---

## DIM_LOCATION

Purpose:

Stores geographical attributes.

Example:

```text
State
Zip Code
```

Business Value:

Supports regional complaint trend analysis.

---

## DIM_PRODUCT

Purpose:

Stores financial product categories.

Example:

```text
Credit Card
Mortgage
Student Loan
Checking Account
```

Business Value:

Identifies products generating the highest complaint volumes.

---

## DIM_CHANNEL

Purpose:

Stores complaint submission channels.

Example:

```text
Web
Phone
Email
Referral
```

Business Value:

Analyzes customer engagement and complaint submission behavior.

---

## FACT_COMPLAINTS

Purpose:

Central analytical fact table.

Contains:

* Complaint records
* Company relationships
* Product relationships
* Geographic relationships
* Submission channel relationships

Business Value:

Provides the primary reporting table used by Power BI.

---

# Star Schema

```text
                DIM_COMPANY
                      |
                      |
DIM_PRODUCT ---- FACT_COMPLAINTS ---- DIM_LOCATION
                      |
                      |
                DIM_CHANNEL
```

Benefits:

* Simplified analytics
* Improved reporting performance
* Optimized Power BI queries
* Enterprise reporting standards

---

# Running dbt

## Validate Configuration

```bash
dbt debug --profiles-dir .
```

---

## Execute Models

```bash
dbt run --profiles-dir .
```

---

## Run Tests

```bash
dbt test --profiles-dir .
```

---

## Generate Documentation

```bash
dbt docs generate
```

---

# Snowflake Integration

dbt connects to Snowflake using environment variables configured in:

```text
profiles.yml
```

Key Variables:

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

# Business Impact

The dbt layer transforms raw complaint data into analytics-ready datasets that support:

* Financial risk monitoring
* Complaint trend analysis
* Product performance analysis
* Company benchmarking
* Geographic complaint insights
* Power BI dashboards
* AI-powered risk intelligence workflows

---

# Key Skills Demonstrated

* dbt
* Snowflake
* SQL
* Data Modeling
* Incremental Models
* Dimensional Modeling
* Star Schema Design
* Analytics Engineering
* ELT Pipelines
* Business Intelligence

```
```
