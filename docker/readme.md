# Docker Deployment

## Overview

This project uses Docker and Docker Compose to provide a reproducible environment for running the complete Financial Risk Intelligence Platform.

Containerization ensures that all services run consistently across development, testing, and deployment environments.

The Docker environment includes:

* Apache Airflow
* PostgreSQL
* dbt
* Snowflake Connectivity
* OpenAI Integration
* LangChain Components
* ChromaDB Dependencies

---

# Architecture

```text
                     Docker Compose
                            │
     ┌──────────────────────┼──────────────────────┐
     │                      │                      │
     ▼                      ▼                      ▼

PostgreSQL          Airflow API Server      Airflow Scheduler
     │                      │                      │
     └──────────────────────┼──────────────────────┘
                            │
                            ▼
                     Financial Risk DAG
                            │
                            ▼
                Snowflake + AWS + OpenAI
```

---

# Folder Structure

```text
docker
│
├── Dockerfile
├── docker-compose.yml
└── airflow
    ├── dags
    ├── logs
    └── plugins
```

---

# Dockerfile

Purpose:

Builds a custom image containing all required libraries and dependencies.

Installed Components:

* Apache Airflow
* dbt Core
* dbt Snowflake Adapter
* Snowflake Connector
* OpenAI SDK
* LangChain
* ChromaDB
* boto3
* pandas
* Python Dependencies

---

# Docker Compose Services

## PostgreSQL

Purpose:

Stores Airflow metadata.

Container:

```text
postgres
```

Responsibilities:

* DAG metadata
* Task execution history
* Scheduler state
* User management

---

## Airflow Init

Purpose:

Initializes and migrates the Airflow metadata database.

Command:

```bash
airflow db migrate
```

Responsibilities:

* Create Airflow tables
* Apply schema upgrades
* Prepare Airflow environment

---

## Airflow API Server

Purpose:

Provides the Airflow user interface and API.

Port:

```text
8080
```

Access:

```text
http://localhost:8080
```

Responsibilities:

* DAG management
* Task monitoring
* Workflow execution
* Log inspection

---

## Airflow Scheduler

Purpose:

Monitors DAGs and schedules task execution.

Responsibilities:

* DAG scheduling
* Dependency management
* Task orchestration
* Workflow execution

---

# Environment Variables

Sensitive credentials are stored in:

```text
.env
```

Examples:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_BUCKET_NAME

SNOWFLAKE_ACCOUNT
SNOWFLAKE_USER
SNOWFLAKE_PASSWORD
SNOWFLAKE_ROLE
SNOWFLAKE_WAREHOUSE
SNOWFLAKE_DATABASE
SNOWFLAKE_SCHEMA

OPENAI_API_KEY
```

---

# Building Containers

## Build Images

```bash
docker compose build
```

Purpose:

Build all project containers.

---

# Starting Services

## Start Containers

```bash
docker compose up -d
```

Purpose:

Start all services in detached mode.

---

# Checking Container Status

```bash
docker compose ps
```

Purpose:

Verify service health and availability.

---

# Viewing Logs

## All Services

```bash
docker compose logs
```

---

## Scheduler Logs

```bash
docker compose logs airflow-scheduler
```

---

## API Server Logs

```bash
docker compose logs airflow-api-server
```

---

# Accessing Containers

## Scheduler Container

```bash
docker compose exec airflow-scheduler bash
```

---

## PostgreSQL Container

```bash
docker compose exec postgres bash
```

---

# Stopping Services

```bash
docker compose down
```

Purpose:

Stop and remove containers.

---

# Mounted Volumes

The following directories are mounted into containers:

```text
Project Root
        │
        ▼
/opt/project
```

```text
docker/airflow/dags
        │
        ▼
/opt/airflow/dags
```

```text
docker/airflow/logs
        │
        ▼
/opt/airflow/logs
```

Benefits:

* Instant code updates
* Persistent logs
* Simplified development workflow

---

# Business Value

Docker enables:

* Environment consistency
* Faster onboarding
* Simplified deployment
* Reproducible builds
* Reduced configuration issues
* Scalable workflow execution

---

# Skills Demonstrated

* Docker
* Docker Compose
* Containerization
* Environment Management
* Airflow Deployment
* PostgreSQL
* Infrastructure Automation
* DevOps Fundamentals

```
```
