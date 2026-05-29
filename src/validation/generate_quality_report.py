import pandas as pd
import json
from pathlib import Path

from src.utils.logger import get_logger

logger = get_logger()

def main():

    file_path = "data/processed/consumer_complaints_processed.csv"

    df = pd.read_csv(
        file_path,
        low_memory=False
    )

    report = {
        "total_records": int(len(df)),
        "total_columns": int(len(df.columns)),
        "duplicate_records": int(df.duplicated().sum()),
        "null_counts": (
            df.isnull()
            .sum()
            .to_dict()
        )
    }

    output_path = (
        "data/quality/"
        "data_quality_report.json"
    )

    Path("data/quality").mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    logger.info(
        f"Quality report saved to {output_path}"
    )

if __name__ == "__main__":
    main()
