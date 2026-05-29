# Snowflake Data Warehouse Design

## Overview

The Snowflake Data Warehouse serves as the centralized analytics repository for complaint data, regulatory documents, AI-generated insights, and reporting datasets.

---

## Schema

FINANCIAL_RISK_INTELLIGENCE

---

## Table: COMPLAINTS

Purpose:

Store standardized financial complaint records.

Columns:

* complaint_id
* complaint_date
* company
* product
* issue
* state
* complaint_text

Primary Key:

complaint_id

---

## Table: REGULATORY_DOCUMENTS

Purpose:

Store metadata related to regulatory and compliance documents.

Columns:

* document_id
* document_name
* document_type
* upload_date
* source

Primary Key:

document_id

---

## Table: RISK_ANALYSIS

Purpose:

Store AI-generated risk intelligence.

Columns:

* complaint_id
* risk_category
* risk_score
* sentiment
* ai_summary
* processed_date

Primary Key:

complaint_id

---

## Table: DOCUMENT_EMBEDDINGS

Purpose:

Track document embedding metadata.

Columns:

* embedding_id
* document_id
* chunk_id
* embedding_model
* created_date

Primary Key:

embedding_id

---

## Table: AI_QUERY_LOG

Purpose:

Store user interaction history.

Columns:

* query_id
* query_text
* response_time
* timestamp

Primary Key:

query_id
