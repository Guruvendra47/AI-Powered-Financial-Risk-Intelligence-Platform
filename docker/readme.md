# Docker Setup — AI-Powered Financial Risk Intelligence Platform

## Architecture Overview

```text
CFPB Data API → S3 (Landing) → Snowflake → dbt → OpenAI (Analysis)
                     ↑
          Airflow (API Server + Scheduler)
                     ↑
              Postgres (MetaDB)
                     ↑
                  Docker

```

This platform is containerized using Docker to ensure a production-grade, decoupled architecture suitable for scalable financial risk modeling.

---

# Step 1 — Install Docker

Download and install Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop/).

### Verify Installation

```bash
docker --version

```

### Purpose

Docker encapsulates the entire infrastructure, ensuring that the environment matches production settings regardless of your host operating system.

---

# Step 2 — Navigate to Project Folder

```bash
cd AI-Powered-Financial-Risk-Intelligence-Platform/docker

```

### Purpose

Ensures `docker compose` has direct access to your configuration files and the local volume mappings.

---

# Step 3 — Start Services Using Docker Compose

Run the following command:

```bash
docker compose up -d

```

### What Is Started

* **Postgres:** Metadata database for Airflow.
* **Airflow Init:** Prepares the database schema.
* **Airflow API Server:** The UI and API management layer.
* **Airflow Scheduler:** The engine responsible for triggering your risk intelligence workflows.

### Purpose

Launches a multi-service, production-ready environment where the Webserver and Scheduler scale independently.

---

# Step 4 — Verify Running Containers

```bash
docker ps

```

### Purpose

Confirms that all core components (`postgres`, `airflow-api-server`, `airflow-scheduler`) are running successfully.

---

# Step 5 — Access Airflow UI & Authentication

Open your browser and navigate to: `http://localhost:8080`

### Authentication

Your authentication is handled by the Simple Auth Manager.

**Option A (Recommended for Dev):** To bypass login, add this to the `environment` section of **both** `airflow-api-server` and `airflow-scheduler` in your `docker-compose.yaml`:

```yaml
AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_ALL_ADMINS: "True"

```

**Option B (Retrieve Password):**
If not using the bypass, retrieve your auto-generated password:

```bash
docker exec -it airflow-api-server cat /opt/airflow/simple_auth_manager_passwords.json.generated

```

---

# Step 6 — Ingest Financial Risk Data

Place your Python DAG files in `./airflow/dags/`. Airflow will automatically detect them.

### What Happens

1. Airflow Scheduler detects new DAGs.
2. Data is fetched from the Financial API.
3. Data is processed and stored in S3/Snowflake.

---

# Step 7 — Stop All Services

```bash
docker compose down --volumes

```

### Purpose

Safely stops the containers and clears the local database state if needed.

---

# `docker-compose.yaml`

```yaml
services:
  postgres:
    image: postgres:16
    container_name: postgres
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    ports:
      - "5432:5432"

  airflow-init:
    image: apache/airflow:3.0.2
    depends_on:
      - postgres
    environment:
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    command: >
      airflow db migrate

  airflow-api-server:
    image: apache/airflow:3.0.2
    depends_on:
      airflow-init:
        condition: service_completed_successfully
    ports:
      - "8080:8080"
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - ./airflow/logs:/opt/airflow/logs
      - ./airflow/plugins:/opt/airflow/plugins
    environment:
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__LOAD_EXAMPLES: "false"
      AIRFLOW__API_AUTH__JWT_SECRET: "my-secret-key"
      AIRFLOW_SIMPLE_AUTH_MANAGER_USERS: "admin:admin"
    command: >
      airflow api-server

  airflow-scheduler:
    image: apache/airflow:3.0.2
    depends_on:
      airflow-init:
        condition: service_completed_successfully
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - ./airflow/logs:/opt/airflow/logs
      - ./airflow/plugins:/opt/airflow/plugins
    environment:
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__LOAD_EXAMPLES: "false"
      AIRFLOW__API_AUTH__JWT_SECRET: "my-secret-key"
      AIRFLOW_SIMPLE_AUTH_MANAGER_USERS: "admin:admin"
    command: >
      airflow scheduler

```

---

# Summary

This platform leverages modern data engineering tools to provide AI-driven financial risk insights:

* **Airflow 3.0 (Distributed):** Orchestrates workflows using separate API and Scheduler services.
* **Snowflake & dbt:** Handles data modeling and warehousing.
* **OpenAI API:** Provides the intelligence layer for risk assessment.
* **S3:** Serves as the robust cloud storage foundation.
