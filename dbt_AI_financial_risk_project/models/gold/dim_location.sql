{{ config(
    materialized='table',
    schema='GOLD'
) }}

WITH singh AS (
    -- Get the unique combinations of state and zip
    SELECT DISTINCT 
        state, 
        zip_code
    FROM {{ ref('stg_complaints') }}
    WHERE state IS NOT NULL
)

SELECT
    ROW_NUMBER() OVER (ORDER BY state, zip_code) AS location_key,
    state,
    zip_code
FROM singh