from pathlib import Path

from src.cloud.aws.s3_client import get_s3_client
from src.config.settings import AWS_BUCKET_NAME
from src.utils.logger import get_logger

logger = get_logger()

def main():

    local_file = (
        "data/processed/"
        "consumer_complaints_processed.csv"
    )

    s3_key = (
        "raw/"
        "consumer_complaints_processed.csv"
    )

    if not Path(local_file).exists():
        raise FileNotFoundError(
            f"{local_file} not found"
        )

    s3_client = get_s3_client()

    logger.info(
        "Uploading file to S3"
    )

    s3_client.upload_file(
        local_file,
        AWS_BUCKET_NAME,
        s3_key
    )

    logger.info(
        f"Upload completed: {s3_key}"
    )

if __name__ == "__main__":
    main()
