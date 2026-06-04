-- This model creates the fact_complaints table in the GOLD schema by joining the staging complaints data with the dimension tables for products, companies, and locations. It selects relevant fields and keys to form a comprehensive fact table for analysis.
-- table, view, incremental, ephemeral 
{{ config(
    materialized='table', 
    schema='GOLD'
) }}

SELECT
    s.complaint_id,
    p.product_key,
    c.company_key,
    l.location_key,
    s.date_received,
    s.product,
    s.company,
    s.state,
    s.zip_code,
    s.issue,
    s.sub_issue,
    s.consumer_complaint_narrative,
    s.timely_response,
    s.consumer_disputed
FROM {{ ref('stg_complaints') }} s
LEFT JOIN {{ ref('dim_product') }} p
    ON s.product = p.product
LEFT JOIN {{ ref('dim_company') }} c
    ON s.company = c.company
LEFT JOIN {{ ref('dim_location') }} l
    ON s.state = l.state
   AND s.zip_code = l.zip_code
