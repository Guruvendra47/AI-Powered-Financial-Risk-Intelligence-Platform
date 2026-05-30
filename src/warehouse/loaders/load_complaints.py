import pandas as pd

from src.cloud.snowflake.connection import get_connection
from src.utils.logger import get_logger

logger = get_logger()

def main():

    file_path = (
        "data/processed/"
        "consumer_complaints_processed.csv"
    )

    df = pd.read_csv(
        file_path,
        nrows=5000,
        low_memory=False
    )

    logger.info(
        f"Loaded {len(df)} records from file"
    )

    df = df[
        [
            "Complaint ID",
            "Date received",
            "Product",
            "Issue",
            "Company",
            "State",
            "Consumer complaint narrative"
        ]
    ]
    df = df.fillna("")

    conn = get_connection()

    cursor = conn.cursor()

    records_loaded = 0

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO COMPLAINTS
            (
                COMPLAINT_ID,
                DATE_RECEIVED,
                PRODUCT,
                ISSUE,
                COMPANY,
                STATE,
                COMPLAINT_NARRATIVE
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                row["Complaint ID"],
                row["Date received"],
                row["Product"],
                row["Issue"],
                row["Company"],
                row["State"],
                row["Consumer complaint narrative"]
            )
        )

        records_loaded += 1

    conn.commit()

    logger.info(
        f"Loaded {records_loaded} records into Snowflake"
    )

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
