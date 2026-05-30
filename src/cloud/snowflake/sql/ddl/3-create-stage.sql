-- Create External Stage
CREATE STAGE risk_complaints_stage
URL='s3://financial-risk-intelligence-platform-dev-guru/raw/'
STORAGE_INTEGRATION = risk_s3_int;

-- Check File Visibility
LIST @risk_complaints_stage;

--show stages 
show satges;
