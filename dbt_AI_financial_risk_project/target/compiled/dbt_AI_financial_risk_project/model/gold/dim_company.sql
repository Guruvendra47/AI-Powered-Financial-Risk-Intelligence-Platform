

WITH singh AS (
    SELECT DISTINCT
        company
    FROM FINANCIAL_RISK_INTELLIGENCE.ANALYTICS_SILVER.stg_complaints
    WHERE company IS NOT NULL
)

SELECT
    ROW_NUMBER() OVER (ORDER BY company) AS company_key,
    company
FROM singh