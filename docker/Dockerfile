FROM apache/airflow:3.0.2

USER root

# Install system dependencies needed for compiling Snowflake/PyArrow wheels
RUN apt-get update && \
    apt-get install -y gcc g++ build-essential && \
    apt-get clean

USER airflow

# Install your complete data pipeline, DBT, and GenAI stack
RUN pip install --no-cache-dir \
    dbt-core \
    dbt-snowflake \
    snowflake-connector-python \
    openai \
    langchain \
    langchain-openai \
    langchain-chroma \
    chromadb \
    pandas \
    pyarrow \
    boto3 \
    python-dotenv \
    requests