
  
    

create or replace transient table FINANCIAL_RISK_INTELLIGENCE.ANALYTICS_GOLD.dim_location
    
    
    
    as (

WITH singh AS (
    -- Get the unique combinations of state and zip
    SELECT DISTINCT 
        state, 
        zip_code
    FROM FINANCIAL_RISK_INTELLIGENCE.ANALYTICS_SILVER.stg_complaints
    WHERE state IS NOT NULL
)

SELECT
    ROW_NUMBER() OVER (ORDER BY state, zip_code) AS location_key,
    state,
    zip_code
FROM singh
    )
;


  