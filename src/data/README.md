# Data Sources Layer

## Overview

The Data Sources layer provides the foundation for the AI-Powered Financial Risk Intelligence Platform.

The platform combines structured financial complaint data with unstructured regulatory, compliance, and risk management documents to support analytics, reporting, and AI-powered risk intelligence.

Data is collected, validated, enriched, transformed, and ultimately delivered to Power BI dashboards and Generative AI applications.

---

# Data Architecture

```text
CFPB Complaint Data
          │
          ▼
AWS S3
          │
          ▼
Snowflake
          │
          ▼
dbt Transformations
          │
          ▼
AI Risk Enrichment
          │
          ▼
Power BI
```

```text
Compliance Documents
          │
          ▼
Document Processing
          │
          ▼
Embeddings
          │
          ▼
ChromaDB
          │
          ▼
RAG Question Answering
```

---

# Directory Structure

```text
src/
└── data/
    │
    ├── consumer_complaints_processed.csv
    │
    ├── ai_documents/
    │   ├── compliance/
    │   ├── regulations/
    │   └── risk_reports/
    │
    └── ingestion/
```

---

# CFPB Consumer Complaint Dataset

## Overview

The Consumer Financial Protection Bureau (CFPB) publishes consumer complaints submitted against financial institutions and financial products.

This dataset serves as the primary structured data source for the platform.

---

## Dataset Usage

The complaint dataset is used for:

```text
Risk Analytics

Complaint Trend Analysis

Product Risk Analysis

Company Performance Analysis

AI Risk Classification

Power BI Dashboards
```

---

## Key Fields

```text
Complaint ID

Date Received

Product

Sub Product

Issue

Sub Issue

Company

State

ZIP Code

Submitted Via

Consumer Complaint Narrative
```

---

## Ingestion Process

Workflow:

```text
CFPB API
      │
      ▼
Download
      │
      ▼
Validation
      │
      ▼
AWS S3
      │
      ▼
Snowflake
```

---

# Processed Complaint Data

File:

```text
consumer_complaints_processed.csv
```

Purpose:

Stores processed complaint records used during development, testing, and validation.

---

# AI Documents

Location:

```text
src/data/ai_documents/
```

These documents support the Retrieval-Augmented Generation (RAG) system.

---

# Compliance Documents

Location:

```text
src/data/ai_documents/compliance/
```

Files:

```text
compliance_01_third_party_risk_management_guide.pdf

compliance_02_bsa_aml_procedures.pdf

compliance_03_third_party_relationships_guidance.pdf
```

Purpose:

Provide guidance related to:

```text
Vendor Risk

AML Compliance

Third-Party Risk Management

Financial Controls

Governance
```

---

# Regulatory Documents

Location:

```text
src/data/ai_documents/regulations/
```

Files:

```text
regulations_01_compliance_management_systems.pdf

regulations_02_regulatory_reporting.pdf

regulations_03_review_of_regulatory_reports.pdf
```

Purpose:

Provide regulatory requirements and supervisory guidance used during AI-assisted compliance analysis.

---

# Risk Reports

Location:

```text
src/data/ai_documents/risk_reports/
```

Files:

```text
risk_reports_01_fdic_2024_risk_review.pdf

risk_reports_02_fdic_2025_risk_review.pdf

risk_reports_03_fdic_2026_risk_review.pdf
```

Purpose:

Provide information regarding:

```text
Emerging Risks

Industry Trends

Banking Sector Risks

Regulatory Concerns

Financial Stability
```

---

# Structured vs Unstructured Data

## Structured Data

Source:

```text
CFPB Complaints
```

Characteristics:

```text
Rows and Columns

SQL Queryable

Used for Reporting

Stored in Snowflake
```

Examples:

```text
Complaint ID

Company

Product

State

Issue
```

---

## Unstructured Data

Sources:

```text
Compliance PDFs

Regulations

Risk Reports
```

Characteristics:

```text
Free Text

Requires NLP Processing

Used by RAG

Stored in ChromaDB
```

---

# Data Flow Across the Platform

## Structured Data Flow

```text
CFPB API
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
Power BI
```

---

## Unstructured Data Flow

```text
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
ChromaDB
      │
      ▼
RAG System
```

---

# Business Value

Combining structured complaint data with unstructured compliance documentation enables a more complete view of financial risk.

Benefits include:

* Complaint trend analysis
* Regulatory research
* Risk intelligence generation
* Compliance monitoring
* AI-assisted decision making
* Natural language querying of financial documents

---

# Skills Demonstrated

```text
Data Engineering

Data Collection

Data Validation

API Integration

AWS S3

Snowflake

dbt

Document Processing

Generative AI

RAG

Vector Databases

Financial Risk Analytics

Regulatory Compliance Analytics

Power BI
```

-
