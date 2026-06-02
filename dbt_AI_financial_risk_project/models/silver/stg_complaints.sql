--table, view, incremental, ephemeral 
{{ config(
    materialized='incremental', 
    schema='SILVER'
) }}

WITH singh AS (
    SELECT *
    -- Pointing directly to the database.schema.table where the raw complaints data lives
    FROM FINANCIAL_RISK_INTELLIGENCE.RAW.RAW_COMPLAINTS
),

-- cleaning steps to filter out records with missing critical fields and standardize text formatting
cleaned_data AS (
    SELECT *
    FROM singh
    WHERE COMPLAINT_ID IS NOT NULL
      AND DATE_RECEIVED IS NOT NULL
),

-- deduplication step to retain only the most recent record for each unique complaint based on COMPLAINT_ID and DATE_RECEIVED
deduplicated AS (
    SELECT *
    FROM cleaned_data
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY COMPLAINT_ID
        ORDER BY DATE_RECEIVED DESC
    ) = 1
)

-- final selection and transformation to conform to the desired schema for the stg_complaints table
SELECT
    CAST(COMPLAINT_ID AS NUMBER)                          AS complaint_id,
    TO_DATE(DATE_RECEIVED)                                AS date_received,
    TRIM(PRODUCT)                                         AS product,
    TRIM(SUB_PRODUCT)                                     AS sub_product,
    TRIM(ISSUE)                                           AS issue,
    TRIM(SUB_ISSUE)                                       AS sub_issue,
    CONSUMER_COMPLAINT_NARRATIVE                          AS consumer_complaint_narrative,
    TRIM(COMPANY_PUBLIC_RESPONSE)                         AS company_public_response,
    UPPER(TRIM(COMPANY))                                  AS company,
    UPPER(TRIM(STATE))                                    AS state,
    TRIM(ZIP_CODE)                                        AS zip_code,
    TRIM(TAGS)                                            AS tags,
    TRIM(CONSUMER_CONSENT_PROVIDED)                       AS consumer_consent_provided,
    TRIM(SUBMITTED_VIA)                                   AS submitted_via,
    TO_DATE(DATE_SENT_TO_COMPANY)                         AS date_sent_to_company,
    TRIM(COMPANY_RESPONSE_TO_CONSUMER)                    AS company_response_to_consumer,
    TRIM(TIMELY_RESPONSE)                                 AS timely_response,
    TRIM(CONSUMER_DISPUTED)                               AS consumer_disputed
FROM deduplicated