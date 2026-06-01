from src.utils.logger import get_logger
from src.utils.exceptions import ValidationError

logger = get_logger(__name__)


REQUIRED_COLUMNS = [
    "Complaint ID",
    "Date received",
    "Product",
    "Company"
]


def validate_dataframe(df):
    """
    Validate CFPB complaint data before
    uploading to AWS S3.

    Args:
        df (pd.DataFrame)

    Returns:
        bool
    """

    logger.info("Starting dataframe validation")

    # ----------------------------
    # Empty DataFrame Check
    # ----------------------------

    if df.empty:

        logger.error(
            "Validation failed: DataFrame is empty"
        )

        raise ValidationError(
            "Downloaded DataFrame is empty"
        )

    logger.info(
        f"Row Count: {len(df):,}"
    )

    logger.info(
        f"Column Count: {len(df.columns)}"
    )

    # ----------------------------
    # Required Columns Check
    # ----------------------------

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:

        logger.error(
            f"Missing columns: {missing_columns}"
        )

        raise ValidationError(
            f"Missing required columns: "
            f"{missing_columns}"
        )

    logger.info(
        "Required columns validation passed"
    )

    # ----------------------------
    # Duplicate Check
    # ----------------------------

    duplicate_count = df.duplicated().sum()

    logger.info(
        f"Duplicate Records Found: "
        f"{duplicate_count:,}"
    )

    # ----------------------------
    # Null Analysis
    # ----------------------------

    logger.info(
        "Null value analysis started"
    )

    for column in REQUIRED_COLUMNS:

        null_count = df[column].isnull().sum()

        logger.info(
            f"{column} Null Count: "
            f"{null_count:,}"
        )

    logger.info(
        "Validation completed successfully"
    )

    return True
