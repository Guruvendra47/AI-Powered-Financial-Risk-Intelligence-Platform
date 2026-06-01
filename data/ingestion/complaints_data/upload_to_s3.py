import io
from datetime import datetime

import boto3
import pandas as pd

from src.config.settings import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    AWS_BUCKET_NAME
)

from src.utils.logger import get_logger
from src.utils.exceptions import S3UploadError

logger = get_logger(__name__)


def upload_dataframe_to_s3(
    df: pd.DataFrame
) -> str:
    """
    Convert DataFrame to Parquet
    and upload to AWS S3.

    Returns:
        S3 object path
    """

    try:

        logger.info(
            "Starting S3 upload process"
        )

        today = datetime.utcnow()

        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")

        s3_key = (
            f"raw/complaints/"
            f"year={year}/"
            f"month={month}/"
            f"day={day}/"
            f"complaints.parquet"
        )

        parquet_buffer = io.BytesIO()

        df.to_parquet(
            parquet_buffer,
            index=False,
            engine="pyarrow"
        )

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        s3_client.put_object(
            Bucket=AWS_BUCKET_NAME,
            Key=s3_key,
            Body=parquet_buffer.getvalue()
        )

        logger.info(
            f"Upload successful: {s3_key}"
        )

        return s3_key

    except Exception as error:

        logger.error(
            f"S3 upload failed: {error}"
        )

        raise S3UploadError(
            f"Failed to upload file to S3. "
            f"Error: {error}"
        )
