--Create Custom IAM Policy
-- Go to AWS Console → IAM → Policies → Create policy

--Create IAM Role in AWS
-- Go to AWS Console → IAM → Roles → Create Role 
--copy role arn after created then paste role arn to STORAGE_AWS_ROLE_ARN

--Create Storage Integration in Snowflake
USE DATABASE FINANCIAL_RISK_INTELLIGENCE;
USE SCHEMA ANALYTICS;

CREATE STORAGE INTEGRATION risk_s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::058862856404:role/role-financial-risk'
STORAGE_ALLOWED_LOCATIONS = ('s3://financial-risk-intelligence-platform-dev/');

-- Get Snowflake IAM User ARN
DESC INTEGRATION risk_s3_int;
-- Copy STORAGE_AWS_IAM_USER_ARN
-- Copy STORAGE_AWS_EXTERNAL_ID

-- Update AWS Role Trust Policy
-- Go back to IAM Role → snowflake-s3-access-role(role name your created)
-- Edit Trust Relationship.
