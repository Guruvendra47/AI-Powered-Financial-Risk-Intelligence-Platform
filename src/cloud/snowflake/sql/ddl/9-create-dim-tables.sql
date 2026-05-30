---------------------------------------------------------------------------
 -- Creating Dimension Tables
--------------------------------------------------------------------------

-- Use Database and Schema if not used before

-----------------------------------------------------------------------------
-- Product dimension
-----------------------------------------------------------------------------
CREATE OR REPLACE TABLE dim_product AS
SELECT
    ROW_NUMBER() OVER (ORDER BY PRODUCT) AS product_id,
    PRODUCT AS product_name
FROM (
    SELECT DISTINCT PRODUCT
    FROM COMPLAINTS
    WHERE PRODUCT IS NOT NULL
);

----------------------------------------------------------------------------
-- Company dimension
----------------------------------------------------------------------------
CREATE OR REPLACE TABLE dim_company AS
SELECT
    ROW_NUMBER() OVER (ORDER BY COMPANY) AS company_id,
    COMPANY AS company_name
FROM (
    SELECT DISTINCT COMPANY
    FROM COMPLAINTS
    WHERE COMPANY IS NOT NULL
);

------------------------------------------------------------------------------
-- Location dimension
------------------------------------------------------------------------------
CREATE OR REPLACE TABLE dim_location AS
SELECT
    ROW_NUMBER() OVER (ORDER BY STATE) AS location_id,
    STATE AS state_code
FROM (
    SELECT DISTINCT STATE
    FROM COMPLAINTS
    WHERE STATE IS NOT NULL
);

-------------------------------------------------------------------------------
-- Channel dimension
-------------------------------------------------------------------------------
CREATE OR REPLACE TABLE dim_channel AS
SELECT
    ROW_NUMBER() OVER (ORDER BY SUBMITTED_VIA) AS channel_id,
    SUBMITTED_VIA AS channel_name
FROM (
    SELECT DISTINCT SUBMITTED_VIA
    FROM COMPLAINTS
    WHERE SUBMITTED_VIA IS NOT NULL
);


-- Verify Dimensions
SELECT COUNT(*) FROM dim_product;
SELECT COUNT(*) FROM dim_company;
SELECT COUNT(*) FROM dim_location;
SELECT COUNT(*) FROM dim_channel;
