from src.utils.logger import get_logger

logger = get_logger()

def check_duplicates(df):

    duplicate_count = df.duplicated().sum()

    logger.info(
        f"Duplicate Records Found: {duplicate_count}"
    )

    return duplicate_count
