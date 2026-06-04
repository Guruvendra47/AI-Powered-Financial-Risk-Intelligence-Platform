import io
import requests
import pandas as pd
import time

from src.utils.logger import get_logger
from src.utils.exceptions import CFPBDownloadError

# Initialize centralized logging
logger = get_logger(__name__)

MAX_RETRIES = 3
REQUEST_TIMEOUT = 120


def download_complaints(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download CFPB complaints for a given date range using the high-performance
    CSV streaming API capability.

    Args:
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)

    Returns:
        pd.DataFrame: Structured complaint records
    """

    logger.info(
        f"Starting CFPB download from {start_date} to {end_date}"
    )

    url = (
        "https://www.consumerfinance.gov/data-research/"
        "consumer-complaints/search/api/v1/"
    )

    # Use format=csv to bypass the 10,000 JSON record pagination ceiling
    # Use no_aggs=true to disable analytical aggregate summaries for massive speed gains
    params = {
        "date_received_min": start_date,
        "date_received_max": end_date,
        "format": "csv",
        "no_aggs": "true"
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(
                f"Sending request to CFPB API (Attempt {attempt})"
            )

            # Request data stream with an explicit timeout safeguard
            response = requests.get(
                url,
                params=params,
                timeout=REQUEST_TIMEOUT
            )

            # Instantly trip the alarm if a HTTP 503 or 400 error occurs
            response.raise_for_status()

            logger.info("API stream received successfully. Parsing content...")

            # Use io.StringIO to parse the incoming string data into Pandas cleanly
            # without writing a temporary messy text file to disk
            df = pd.read_csv(io.StringIO(response.text), low_memory=False)

            logger.info(
                f"Retrieved {len(df)} complaint records"
            )

            logger.info("CFPB download completed successfully")
            return df

        except Exception as error:
            logger.error(
                f"Attempt {attempt} failed: {error}"
            )

            if attempt < MAX_RETRIES:
                logger.info("Waiting 5 seconds before retrying...")
                time.sleep(5)
            else:
                raise CFPBDownloadError(
                    f"Failed to download CFPB data after "
                    f"{MAX_RETRIES} attempts due to structural or network failure."
                )

    return pd.DataFrame()
