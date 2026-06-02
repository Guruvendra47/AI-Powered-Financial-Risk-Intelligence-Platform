# Configuration Management (`settings.py`)

The platform uses a centralized configuration management approach through `src/config/settings.py`. This design ensures all ingestion, transformation, orchestration, AI, and database components follow a consistent configuration standard across the application.

Centralized configuration management provides:

* improved maintainability
* reduced hardcoded values
* better environment portability
* enhanced security practices
* simplified infrastructure management

---

# Environment Variable Management

The project uses `python-dotenv` to securely manage environment variables and sensitive credentials.

All infrastructure secrets and configuration values are stored in a local `.env` file, which is excluded from version control using `.gitignore`.

At runtime, configuration values are loaded into immutable uppercase variables through the centralized settings module.

---

# Required Configuration Variables

| Variable Name           | Description                                                 | Target Component         |
| ----------------------- | ----------------------------------------------------------- | ------------------------ |
| `AWS_ACCESS_KEY_ID`     | IAM access key used for S3 programmatic access              | S3 Upload Services       |
| `AWS_SECRET_ACCESS_KEY` | IAM secret key used for secure S3 authentication            | S3 Upload Services       |
| `AWS_REGION`            | AWS region where the data lake resources are deployed       | AWS Clients              |
| `AWS_BUCKET_NAME`       | Target S3 bucket for raw and processed data storage         | Data Lake Storage        |
| `SNOWFLAKE_ACCOUNT`     | Snowflake account identifier in organization-account format | Snowflake Connectivity   |
| `SNOWFLAKE_USER`        | Service account username for pipeline execution             | Snowflake Connectors     |
| `SNOWFLAKE_PASSWORD`    | Password for the Snowflake service account                  | Snowflake Authentication |
| `SNOWFLAKE_WAREHOUSE`   | Compute warehouse used for data processing workloads        | Snowflake Processing     |
| `SNOWFLAKE_DATABASE`    | Primary database containing raw and analytics layers        | Snowflake Storage        |
| `SNOWFLAKE_SCHEMA`      | Active schema used for staging and transformation           | Snowflake Storage        |
| `OPENAI_API_KEY`        | API key used for AI enrichment and compliance services      | AI Services Layer        |

---

# Setup and Initialization

## Step 1 — Create the Environment File

In the root directory of the project, create a local environment file from the provided template:

```bash id="s4m7u1"
cp .env.example .env
```

### Purpose

Creates a dedicated local configuration file for managing environment-specific credentials and settings.

---

# Step 2 — Configure Credentials

Open the `.env` file and replace all placeholder values with valid infrastructure credentials and service configurations.

### Example

```env id="3pt48z"
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
AWS_BUCKET_NAME=financial-data-lake

SNOWFLAKE_ACCOUNT=org-account
SNOWFLAKE_USER=service_user
SNOWFLAKE_PASSWORD=secure_password
```

### Purpose

Allows the application to securely connect with cloud infrastructure and external services.

---

# Step 3 — Import Configuration in Application Code

Instead of using `os.getenv()` repeatedly across modules, import configuration values directly from the centralized settings module.

## Recommended Approach

```python id="ieaq11"
from src.config import settings

# Example usage inside the S3 upload module
print(f"Target S3 Bucket: {settings.AWS_BUCKET_NAME}")
```

---

# Benefits of Centralized Configuration

Using a centralized settings module provides several operational advantages:

* eliminates duplicate configuration logic
* improves code consistency
* reduces runtime configuration errors
* simplifies debugging and maintenance
* improves application scalability

This approach also ensures that all services across the platform use standardized environment variables and configuration handling practices.

---

# Security Best Practices

## Recommended Practices

* Never commit `.env` files to version control
* Store production secrets in secure secret management systems
* Rotate credentials regularly
* Use IAM roles and least-privilege access policies
* Separate development and production configurations

## `.gitignore` Recommendation

```bash id="hfz2sd"
.env
*.pem
*.key
```

This prevents sensitive credentials from being pushed into source control repositories.

---

# Summary

The centralized configuration framework ensures secure, scalable, and maintainable infrastructure management across the platform.

The `settings.py` module acts as a single source of truth for:

* cloud credentials
* database configurations
* AI service integrations
* storage settings
* infrastructure variables

This design pattern is commonly used in enterprise-grade data engineering and cloud-native platforms to maintain consistency, reliability, and operational security.
