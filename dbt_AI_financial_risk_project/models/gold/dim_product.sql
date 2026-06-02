{{ config(
    materialized='table',
    schema='GOLD'
) }}

WITH singh AS (
    -- Point to the exact table dbt just successfully built
    SELECT DISTINCT product
    FROM {{ ref('stg_complaints') }}
    WHERE product IS NOT NULL
)

SELECT
    ROW_NUMBER() OVER (ORDER BY product) AS product_key,
    product
FROM singh