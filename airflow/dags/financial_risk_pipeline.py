from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "guruvendra",
    "depends_on_past": False,
    "retries": 1
}


with DAG(
    dag_id="financial_risk_pipeline",
    description="AI Powered Financial Risk Intelligence Platform",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["finance", "snowflake", "dbt", "genai"]
) as dag:

    download_cfpb = BashOperator(
        task_id="download_cfpb_data",
        bash_command="python /opt/project/data/ingestion/download_cfpb.py"
    )

    validate_file = BashOperator(
        task_id="validate_complaint_file",
        bash_command="python /opt/project/data/ingestion/validate_file.py"
    )

    upload_to_s3 = BashOperator(
        task_id="upload_to_s3",
        bash_command="python /opt/project/data/ingestion/upload_to_s3.py"
    )

    dbt_run = BashOperator(
        task_id="run_dbt_models",
        bash_command="""
        cd /opt/project/dbt_AI_financial_risk_project &&
        dbt run --profiles-dir .
        """
    )

    ai_enrichment = BashOperator(
        task_id="process_complaints",
        bash_command="python /opt/project/src/ai/process_complaints.py"
    )

    (
        download_cfpb
        >> validate_file
        >> upload_to_s3
        >> dbt_run
        >> ai_enrichment
    )