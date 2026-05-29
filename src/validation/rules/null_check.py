from src.utils.logger import get_logger

logger = get_logger()

def check_nulls(df):

    null_counts = df.isnull().sum()

    null_columns = null_counts[null_counts > 0]

    if len(null_columns) > 0:
        logger.warning(
            f"Columns with null values:\n{null_columns}"
        )

    return null_columns
