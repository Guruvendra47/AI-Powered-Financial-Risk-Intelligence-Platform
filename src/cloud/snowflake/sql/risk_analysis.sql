CREATE OR REPLACE TABLE GOLD.RISK_ANALYSIS (
    complaint_id NUMBER,
    risk_category STRING,
    sentiment STRING,
    complaint_summary STRING,
    analysis_status STRING,
    model_name STRING,
    processed_timestamp TIMESTAMP
);
