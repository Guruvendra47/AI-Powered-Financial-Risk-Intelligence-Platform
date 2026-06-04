# Financial Risk Data Transformation Engine (`dbt`)

This subdirectory contains the core **dbt (Data Build Tool)** project for the **AI-Powered-Financial-Risk-Intelligence-Platform**. It manages the ELT (Extract-Load-Transform) pipeline layers inside **Snowflake**, transforming raw Consumer Financial Protection Bureau (CFPB) complaints into structured, clean analytical data marts optimized for downstream GenAI processing and Power BI dashboards.

---

## 🏗️ Data Architecture Layers

Transformations inside Snowflake are strictly decoupled into modular logical layers within the `models/` directory:

* **`models/staging/`**: Light validation, casting, and standardizing of column naming conventions directly over raw landing tables.
* **`models/marts/`**: Dense business logic, computing risk aggregates, customer sentiment indicators, and combining datasets into final dimensions and facts.
* **`seeds/`**: Static lookup maps (e.g., state codes, company sectors, risk priority thresholds).
* **`tests/`**: Automated schema tests ensuring primary keys are `unique` and non-null (`not_null`), alongside custom relational integrity validation.

---

## ⚙️ Configuration & Prerequisites

Before running this project locally or via orchestration, ensure your environment is properly configured.

### 1. Profile Setup (`profiles.yml`)
Your profile tells dbt how to securely authenticate with your Snowflake Warehouse. Ensure your local `~/.dbt/profiles.yml` or the project-level `profiles.yml` is structured like this:

```yaml
financial_risk_profile:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: <your_snowflake_account_locator>
      user: <your_username>
      password: <your_password>
      role: <your_functional_role>
      database: AIRFLOW_DB
      warehouse: COMPUTE_WH
      schema: TRANSFORMS
      threads: 4

```

---

## 🚀 Step-by-Step Execution Guide

Follow these steps in order to run and test your dbt transformations locally or within your development terminal. Always ensure you are inside the `dbt_AI_financial_risk_project` directory before running these commands.

### Step 1: Install Project Dependencies

Fetch external dbt package dependencies (such as `dbt_utils`) declared in your `packages.yml`:

```bash
dbt deps

```

### Step 2: Load Static Seed Data

Load csv data files located in your `seeds/` folder straight into Snowflake as static lookup tables:

```bash
dbt seed --profiles-dir .

```

### Step 3: Run Transformations (The Entire Project)

Compile all SQL models and materialize tables/views into Snowflake:

```bash
dbt run --profiles-dir .

```

### Step 4: Running Specific SQL Files (Models)

Instead of running the entire project, you can isolate specific SQL files using the `--select` (or `-s`) flag. **Do not include the `.sql` extension when selecting models.**

* **Run a single specific SQL file:**
```bash
dbt run --select stg_complaints --profiles-dir .

```


* **Run a model and everything after it (Downstream):**
If you modified a staging file and want to rebuild it *and* any mart tables that depend on it, add a `+` to the **end**:
```bash
dbt run --select stg_complaints+ --profiles-dir .

```


* **Run a model and everything before it (Upstream):**
If you want to run a final mart table but need to ensure all its underlying staging views are refreshed first, add a `+` to the **beginning**:
```bash
dbt run --select +fct_financial_risk --profiles-dir .

```


* **Run an entire directory of SQL files:**
To execute every single SQL file inside a specific folder (e.g., the staging folder):
```bash
dbt run --select staging --profiles-dir .

```



### Step 5: Execute Data Quality Tests

Run data assertions and semantic constraints to catch schema anomalies:

```bash
dbt test --profiles-dir .

```

### Step 6: Generate Lineage Graph & Documentation

Generate and host a local interactive visualization map of your model dependency graph:

```bash
dbt docs generate && dbt docs serve

```

---

## 🤖 Airflow Orchestration Context

Within the broader platform, this dbt project is triggered automatically via Apache Airflow inside the Docker container layout. Airflow orchestrates the **entire project** as a single task using the `BashOperator`, allowing dbt's internal graph resolver to handle individual file dependencies:

```python
dbt_run_task = BashOperator(
    task_id="dbt_run",
    bash_command="""
    cd /opt/project/dbt_AI_financial_risk_project &&
    dbt run --profiles-dir .
    """
)

```

> ⚠️ **Maintenance Note:** When adding new raw source data tables to your pipeline, remember to declare them in your configuration schemas inside `models/staging/schema.yml` before writing your staging `.sql` files to prevent compilation errors during production runs.

```

```
