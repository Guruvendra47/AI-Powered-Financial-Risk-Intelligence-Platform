## ⚙️ Configuration Management (`settings.py`)

The platform utilizes a centralized configuration management pattern located in `src/config/settings.py`. This design ensures that all ingestion, transformation, AI, and database components share a unified configuration standard, preventing hardcoded values and reducing security risks.

### 🔒 Environment Variable Isolation
The framework uses `python-dotenv` to decouple application logic from infrastructure credentials. All sensitive secrets are stored in a local `.env` file (which is explicitly ignored by `.gitignore`) and loaded into immutable upper-case variables at runtime.

### 📋 Required Configuration Variables

| Variable Name | Description | Target Component |
| :--- | :--- | :--- |
| `AWS_ACCESS_KEY_ID` | IAM User Access Key for S3 programmatic access. | `upload_to_s3.py` |
| `AWS_SECRET_ACCESS_KEY`| IAM User Secret Key for S3 programmatic access. | `upload_to_s3.py` |
| `AWS_REGION` | The AWS region where the data lake is deployed. | S3 Clients |
| `AWS_BUCKET_NAME` | Name of the target S3 Landing Zone bucket. | S3 Clients |
| `SNOWFLAKE_ACCOUNT` | Snowflake account identifier (org-account format). | Snowflake Stage / Pipe |
| `SNOWFLAKE_USER` | Service account user for pipeline execution. | Snowflake Connectors |
| `SNOWFLAKE_PASSWORD` | Password credentials for the service user. | Snowflake Connectors |
| `SNOWFLAKE_WAREHOUSE` | Dedicated compute warehouse for data processing. | Snowflake Transformations |
| `SNOWFLAKE_DATABASE` | Target database for the raw and analytical layers. | Snowflake Storage |
| `SNOWFLAKE_SCHEMA` | Active schema context for raw table landing. | Snowflake Storage |
| `OPENAI_API_KEY` | Developer API key for compliance RAG & enrichment. | AI Services Layer |

---

### 🚀 Setup and Initialization

1. **Create your Local Environment File:**
   In the root directory of the project, duplicate the template file to create your active environment variables:
   ```bash
   cp .env.example .env
