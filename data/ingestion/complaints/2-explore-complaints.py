import pandas as pd
from src.utils.logger import get_logger

logger = get_logger()

def main():

    file_path = "data/raw/consumer_complaints.csv"

    logger.info("Loading sample records")

    df = pd.read_csv(
        file_path,
        nrows=1000,
        low_memory=False
    )

    logger.info(f"Rows Loaded: {len(df)}")
    logger.info(f"Columns: {len(df.columns)}")

    print("\nColumns:\n")
    print(df.columns.tolist())

    print("\nSample Data:\n")
    print(df.head())

if __name__ == "__main__":
    main()
