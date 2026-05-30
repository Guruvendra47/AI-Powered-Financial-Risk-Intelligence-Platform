import pandas as pd

from src.utils.logger import get_logger
from src.validation.rules.null_check import check_nulls
from src.validation.rules.duplicate_check import check_duplicates
from src.validation.rules.schema_check import validate_schema

logger = get_logger()


def main():

    logger.info("Starting complaint processing pipeline")

    file_path = "data/raw/consumer_complaints.csv"

    df = pd.read_csv(
        file_path,
        nrows=10000,
        low_memory=False
    )

    logger.info(f"Loaded {len(df)} records")

    missing_columns = validate_schema(df)

    if missing_columns:
        logger.error(
            f"Missing columns: {missing_columns}"
        )
        raise Exception("Schema validation failed")

    logger.info("Schema validation passed")

    check_nulls(df)

    check_duplicates(df)

    processed_file = (
        "data/processed/"
        "consumer_complaints_processed.csv"
    )

    df.to_csv(
        processed_file,
        index=False
    )

    logger.info(
        f"Processed file saved to: {processed_file}"
    )


if __name__ == "__main__":
    main()
