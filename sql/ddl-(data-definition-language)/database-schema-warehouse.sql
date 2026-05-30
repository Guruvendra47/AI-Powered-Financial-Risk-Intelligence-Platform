-------create database---
CREATE DATABASE FINANCIAL_RISK_INTELLIGENCE;

-----verify database-----
SHOW DATABASES;

----use database-----
USE DATABASE FINANCIAL_RISK_INTELLIGENCE;

----create schema-----
CREATE SCHEMA ANALYTICS;

-----verify schema----
SHOW SCHEMAS;

----create warehouse-----
CREATE WAREHOUSE RISK_INTELLIGENCE_WH
WITH
WAREHOUSE_SIZE = 'XSMALL'
AUTO_SUSPEND = 60
AUTO_RESUME = TRUE;

---verify warehouse-----
SHOW WAREHOUSES;
