# ETL Architecture

## Overview

The ETL layer is responsible for ingesting, validating, transforming, enriching, and loading financial complaint and regulatory data into the analytics platform.

---

## Data Flow

Data Sources
↓
Raw Layer
↓
Validation Layer
↓
Transformation Layer
↓
Enrichment Layer
↓
Curated Layer
↓
Snowflake

---

## Raw Layer

Purpose:

Store source data exactly as received.

Examples:

* Complaint CSV files
* Regulatory PDFs
* Compliance documents

Location:

AWS S3 Raw Zone

Folder:

data/raw/

---

## Validation Layer

Purpose:

Verify data quality before processing.

Checks:

* Missing values
* Duplicate records
* Invalid dates
* Invalid document formats

Output:

Validation reports and clean datasets.

---

## Transformation Layer

Purpose:

Standardize and prepare data.

Transformations:

* Column standardization
* Date normalization
* Null handling
* Duplicate removal

Output:

Processed datasets.

Location:

data/processed/

---

## Enrichment Layer

Purpose:

Generate AI-powered insights.

Generated Fields:

* Risk Category
* Sentiment
* Risk Score
* AI Summary

Output:

Enriched datasets.

---

## Curated Layer

Purpose:

Provide analytics-ready datasets.

Consumers:

* Snowflake
* Power BI
* RAG Engine

Location:

data/curated/

---

## Warehouse Load

Destination:

Snowflake

Target Tables:

* complaints
* risk_analysis
* regulatory_documents
* ai_summaries
