
  create or replace   view FINANCIAL_RISK_INTELLIGENCE.ANALYTICS.dim_channel
  
  
  
  
  as (
    ({config (
    materialized='table',
    schema='GOLD'
)})

WITH singh AS (
    SELECT DISTINCT 
      SUBMITTED_VIA
    FROM FINANCIAL_RISK_INTELLIGENCE.ANALYTICS_SILVER.stg_complaints
    WHERE SUBMITTED_VIA IS NOT NULL 
)   
SELECT
    ROW_NUMBER() OVER (ORDER BY SUBMITTED_VIA) AS channel_id,
    SUBMITTED_VIA AS channel_name
FROM singh
  );

