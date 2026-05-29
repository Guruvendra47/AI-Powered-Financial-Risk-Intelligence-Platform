# Data Model

## Complaint Records

| Column Name    | Description                 |
| -------------- | --------------------------- |
| complaint_id   | Unique complaint identifier |
| complaint_text | Complaint description       |
| complaint_date | Date received               |
| company        | Financial institution       |
| product        | Product category            |
| issue          | Complaint issue             |
| state          | Customer state              |

## AI Risk Analysis

| Column Name   | Description                    |
| ------------- | ------------------------------ |
| complaint_id  | Complaint identifier           |
| risk_category | Fraud, Compliance, Operational |
| sentiment     | Positive, Neutral, Negative    |
| risk_score    | Low, Medium, High              |
| summary       | AI-generated summary           |

## Regulatory Documents

| Column Name   | Description                    |
| ------------- | ------------------------------ |
| document_id   | Unique document identifier     |
| document_name | File name                      |
| document_type | Regulation, Policy, Compliance |
| upload_date   | Upload date                    |

## Embeddings

| Column Name  | Description       |
| ------------ | ----------------- |
| document_id  | Source document   |
| chunk_id     | Text chunk        |
| embedding_id | Vector identifier |
