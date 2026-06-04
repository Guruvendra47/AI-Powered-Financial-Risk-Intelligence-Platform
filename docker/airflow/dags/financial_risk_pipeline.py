from datetime import datetime

from airflow import DAG

from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator

from src.ingestion.complaints.download_cfpb import download_complaints
from src.ingestion.complaints.validate_file import validate_dataframe
from src.ingestion.complaints.upload_to_s3 import upload_dataframe_to_s3


def download_validate_upload():
    """
    Download CFPB complaints,
    validate data,
    upload to S3.
    """

    df = download_complaints(
        start_date="2025-01-01",
        end_date="2025-01-31"
    )

    validate_dataframe(df)

    upload_dataframe_to_s3(df)


def run_ai_enrichment():
    """
    Import AI code only when task runs.
    Prevents Airflow DAG parser from
    requiring OpenAI during startup.
    """

    from src.ai.process_complaints import process_complaints

    process_complaints()


with DAG(
    dag_id="financial_risk_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=[
        "financial-risk",
        "snowflake",
        "dbt",
        "genai"
    ]
) as dag:

    ingestion_task = PythonOperator(
        task_id="download_validate_upload",
        python_callable=download_validate_upload
    )

    dbt_run_task = BashOperator(
        task_id="dbt_run",
        bash_command="""
        cd /opt/project/dbt_AI_financial_risk_project &&
        dbt run --profiles-dir .
        """
    )

    ai_enrichment_task = PythonOperator(
        task_id="process_complaints",
        python_callable=run_ai_enrichment
    )

    ingestion_task >> dbt_run_task >> ai_enrichment_task
