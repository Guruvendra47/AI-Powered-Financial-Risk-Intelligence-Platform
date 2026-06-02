

WITH singh AS (
    -- Point to the exact table dbt just successfully built
    SELECT DISTINCT product
    FROM FINANCIAL_RISK_INTELLIGENCE.ANALYTICS_SILVER.stg_complaints
    WHERE product IS NOT NULL
)

SELECT
    ROW_NUMBER() OVER (ORDER BY product) AS product_key,
    product
FROM singh