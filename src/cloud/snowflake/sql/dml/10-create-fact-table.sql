
---------------------------------------------------------------------------
 -- Create Fact Table
--------------------------------------------------------------------------

CREATE OR REPLACE TABLE FACT_COMPLAINTS AS
SELECT
    c.COMPLAINT_ID,
    p.PRODUCT_ID,
    co.COMPANY_ID,
    l.LOCATION_ID,
    ch.CHANNEL_ID,
    c.DATE_RECEIVED,
    c.ISSUE,
    c.TIMELY_RESPONSE,
    c.CONSUMER_DISPUTED
FROM COMPLAINTS c
LEFT JOIN DIM_PRODUCT p
    ON c.PRODUCT = p.PRODUCT_NAME
LEFT JOIN DIM_COMPANY co
    ON c.COMPANY = co.COMPANY_NAME
LEFT JOIN DIM_LOCATION l
    ON c.STATE = l.STATE_CODE
LEFT JOIN DIM_CHANNEL ch
    ON c.SUBMITTED_VIA = ch.CHANNEL_NAME;


---verify
SELECT COUNT(*) FROM FACT_COMPLAINTS;
