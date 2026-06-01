import requests
import pandas as pd
from time import sleep

from src.utils.logger import get_logger
from src.utils.exceptions import CFPBDownloadError

# Initialize centralized logging
logger = get_logger(__name__)

MAX_RETRIES = 3


def download_complaints(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download CFPB complaints for a given date range.

    Args:
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)

    Returns:
        pd.DataFrame
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
        "size": 10000
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
                timeout=60
            )
            
            # Instantly trip the alarm if a HTTP 503 or 400 error occurs
            response.raise_for_status()

            data = response.json()

            complaints = data.get("hits", [])

            df = pd.DataFrame(complaints)

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

                sleep(5)

            else:

                raise CFPBDownloadError(
                    f"Failed to download CFPB data after "
                    f"{MAX_RETRIES} attempts"
                )

    return pd.DataFrame()
