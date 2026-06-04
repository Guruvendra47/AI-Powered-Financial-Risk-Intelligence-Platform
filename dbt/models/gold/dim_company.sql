{{ config(
    materialized='table',
    schema='GOLD'
) }}

WITH singh AS (
    SELECT DISTINCT
        company
    FROM {{ ref('stg_complaints') }}
    WHERE company IS NOT NULL
)

SELECT
    ROW_NUMBER() OVER (ORDER BY company) AS company_key,
    company
FROM singh