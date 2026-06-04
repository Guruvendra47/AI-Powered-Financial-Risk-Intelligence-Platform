# AI Risk Intelligence Layer

## Overview

The AI layer enriches financial complaint data using Large Language Models (LLMs) and generates actionable risk intelligence.

The objective is to automate complaint analysis, risk classification, compliance review, and summarization activities that would normally require significant manual effort.

The platform uses OpenAI models to analyze complaint narratives and generate structured risk insights that can be stored in Snowflake and visualized in Power BI.

---

# Architecture

```text
CFPB Complaints
        │
        ▼
Snowflake
(STG_COMPLAINTS)
        │
        ▼
process_complaints.py
        │
        ▼
complaint_analyzer.py
        │
        ▼
OpenAI API
        │
        ▼
AI Risk Analysis
        │
        ├── Risk Category
        ├── Severity Score
        ├── Sentiment
        ├── Summary
        └── Compliance Insight
        │
        ▼
Snowflake
        │
        ▼
Power BI
```

---

# Project Structure

```text
src/
└── ai/
    │
    ├── complaint_analyzer.py
    ├── process_complaints.py
    ├── main.py
    │
    └── tests/
        ├── 1_test_complaint_analyzer.py
        └── 2_test_process_complaints.py
```

---

# Components

## complaint_analyzer.py

Purpose:

Responsible for interacting with OpenAI models.

Main functions:

```text
Send complaint narratives to OpenAI

Generate risk classifications

Generate summaries

Generate compliance insights

Generate sentiment assessments
```

---

## process_complaints.py

Purpose:

Processes complaints from Snowflake and performs AI enrichment.

Workflow:

```text
Read complaints

Call OpenAI

Generate AI outputs

Store results

Log processing status
```

---

## main.py

Purpose:

Provides an entry point for running AI enrichment processes.

Used during local testing and development.

---

# AI Processing Workflow

## Step 1

Read complaint data.

Source:

```text
Snowflake
```

Example:

```text
Consumer reports unauthorized charges
on credit card account.
```

---

## Step 2

Send complaint narrative to OpenAI.

Example Prompt:

```text
Analyze this financial complaint and provide:

1. Risk Category
2. Severity Level
3. Complaint Summary
4. Compliance Concerns
5. Sentiment
```

---

## Step 3

Generate AI Insights.

Example Output:

```text
Risk Category:
Fraud Risk

Severity:
High

Sentiment:
Negative

Summary:
Customer reported unauthorized
transactions on a credit card account.

Compliance Insight:
Potential fraud investigation required.
```

---

## Step 4

Store Results.

Outputs may be stored in:

```text
Snowflake Risk Analysis Tables

AI Query Logs

Future Reporting Tables
```

---

# AI Risk Categories

Examples:

```text
Fraud Risk

Compliance Risk

Operational Risk

Credit Risk

Customer Service Risk

Regulatory Risk

Cybersecurity Risk
```

---

# Sentiment Analysis

Possible classifications:

```text
Positive

Neutral

Negative
```

Purpose:

Measure customer dissatisfaction trends and emerging complaint patterns.

---

# OpenAI Integration

The platform uses:

```text
OpenAI API
```

For:

```text
Risk Classification

Complaint Summarization

Compliance Analysis

Insight Generation

Sentiment Analysis
```

---

# Environment Variables

Required configuration:

```text
OPENAI_API_KEY
```

Stored securely using:

```text
.env
```

---

# Airflow Integration

AI processing is executed as part of the Airflow pipeline.

Workflow:

```text
Download CFPB Data
        │
        ▼
Validate Data
        │
        ▼
Upload To AWS S3
        │
        ▼
Snowflake Load
        │
        ▼
dbt Transformations
        │
        ▼
AI Enrichment
        │
        ▼
Power BI
```

---

# Example End-to-End Flow

Input Complaint:

```text
Customer reported unauthorized
transactions on their credit card.
```

AI Output:

```text
Risk Category:
Fraud Risk

Severity:
High

Sentiment:
Negative

Summary:
Unauthorized transactions reported
on consumer credit card account.

Compliance Concern:
Potential fraud investigation required.
```

---

# Business Value

The AI layer reduces manual review effort by automatically analyzing complaint narratives and generating structured risk intelligence.

Benefits include:

* Faster complaint analysis
* Consistent risk classification
* Automated summarization
* Improved compliance monitoring
* Better risk visibility
* Enhanced decision making

---

# Testing

Test files:

```text
tests/

1_test_complaint_analyzer.py

2_test_process_complaints.py
```

Testing validates:

```text
OpenAI Integration

Response Processing

Complaint Classification

Pipeline Execution
```

---

# Skills Demonstrated

```text
Generative AI

OpenAI API

Prompt Engineering

LLMs

Financial Risk Analytics

Sentiment Analysis

Risk Classification

Python

Snowflake

Apache Airflow

Data Engineering

AI Enrichment Pipelines
```

---

## Folder Location

```text
src/
└── ai/
    └── README.md
```
