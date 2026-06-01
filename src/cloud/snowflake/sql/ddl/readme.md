# ❄️ Snowflake Infrastructure & Data Warehouse DDL

This directory houses the foundational SQL scripts required to establish the platform's core compute resources, storage layers, and automated ingestion infrastructure within Snowflake. The scripts are intentionally ordered with numeric prefixes (`1-` through `7.1-`) to establish a clean dependency chain for deployment.

---

## 📈 Database Deployment Sequence

To configure the database infrastructure correctly, run these scripts sequentially within your Snowflake Worksheet (or CI/CD deployment pipeline) using an account with administrative privileges (e.g., `ACCOUNTADMIN` or `SYSADMIN` where appropriate):

```text
1-create-database-schema-warehouse.sql       ➔ Set up RBAC, computing warehouses, and databases
2-create-storage-integration.sql             ➔ Establish secure IAM trust connection to AWS S3
3-create-stage.sql                           ➔ Map external stage location pointing to S3 landing path
4-create-file-format.sql                     ➔ Declare optimized binary Parquet formatting engine
5-create-raw-complaints_table.sql            ➔ Deploy the immutable Bronze table structural schema
6-test-the-file.sql                          ➔ Run validation checks on stage file availability
7-copy-into-manual.sql                       ➔ Execute historical backfill copy scripts
7.1-copy-into-snowpipe-automation.sql        ➔ Activate Snowpipe serverless automated ingestion micro-service

```

---

## 🔍 Script Architecture & Operational Breakdown

### `1-create-database-schema-warehouse.sql`

* **Objective:** Spins up the dedicated virtual warehouses (`X-Small` optimized to limit cost overhead), separates databases into analytical environments (`RAW` and `ANALYTICS`), and enforces Role-Based Access Control (RBAC).

### `2-create-storage-integration.sql`

* **Objective:** Generates a secure, native cloud communication link using a Snowflake `STORAGE INTEGRATION`. This establishes a trust relationship with your AWS IAM role **without hardcoding secret access keys** in plain text.
* **Interview Context:** *Proves adherence to strict enterprise cloud security guidelines by utilizing IAM identity provider policies over long-lived, unsafe security access keys.*

### `3-create-stage.sql` & `4-create-file-format.sql`

* **Objective:** `3-create-stage.sql` references the storage integration to establish an entry point to the S3 bucket path. `4-create-file-format.sql` defines the structural parser configuration needed to handle binary compressed Parquet records (`TYPE = PARQUET COMPRESSION = SNAPPY`).

### `5-create-raw-complaints_table.sql`

* **Objective:** Builds the **Bronze Layer** of your Medallion architecture inside Snowflake. This table holds an exact, unmutated representation of the incoming data, storing columns directly alongside high-performance semi-structured Variant parameters if needed.

### `6-test-the-file.sql` & `7-copy-into-manual.sql`

* **Objective:** `6-test-the-file.sql` runs discovery checks (`LIST @my_stage`) to ensure data exists. `7-copy-into-manual.sql` runs a manual bulk `COPY INTO` operation to clear out your initial 5-year historical backfill records from S3.

### `7.1-copy-into-snowpipe-automation.sql`

* **Objective:** Declares the automated serverless micro-service engine via `CREATE PIPE`. It hooks directly into AWS S3 event notifications (SQS queues) to automatically ingest daily incremental data into the Bronze table the absolute second a new `.parquet` file lands in your S3 bucket.

---
