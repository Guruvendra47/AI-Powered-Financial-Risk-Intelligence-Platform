# Airflow Orchestration Architecture

## Overview

Apache Airflow orchestrates all ingestion, transformation, enrichment, warehouse loading, and AI processing workflows within the Financial Risk Intelligence Platform.

---

## DAG 1 – Complaint Ingestion Pipeline

Schedule:

Daily

Workflow:

1. Read complaint dataset
2. Validate source files
3. Load raw data
4. Log execution status

Output:

Raw complaint records

---

## DAG 2 – Regulatory Document Pipeline

Schedule:

Daily

Workflow:

1. Read regulatory documents
2. Extract metadata
3. Store raw documents
4. Log execution status

Output:

Regulatory document repository

---

## DAG 3 – ETL Processing Pipeline

Schedule:

Daily

Workflow:

1. Data validation
2. Data cleaning
3. Data transformation
4. Curated dataset creation

Output:

Analytics-ready datasets

---

## DAG 4 – AI Enrichment Pipeline

Schedule:

Daily

Workflow:

1. Generate embeddings
2. Risk classification
3. Sentiment analysis
4. AI summarization

Output:

AI-enriched complaint records

---

## DAG 5 – Snowflake Load Pipeline

Schedule:

Daily

Workflow:

1. Load complaint data
2. Load risk analysis data
3. Load document metadata
4. Verify load success

Output:

Snowflake reporting tables

---

## Monitoring

Airflow tracks:

* Task success rate
* Task failures
* Pipeline duration
* Retry attempts
* Execution history
