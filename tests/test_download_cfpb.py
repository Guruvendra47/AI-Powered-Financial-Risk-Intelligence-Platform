from src.ingestion.complaints.download_cfpb import (
    download_complaints
)


def main():

    df = download_complaints(
        start_date="2025-01-01",
        end_date="2025-01-31"
    )

    print("\nColumns Returned:\n")

    print(df.columns.tolist())

    print("\nFirst 5 Records:\n")

    print(df.head())

    print(
        f"\nTotal Records Retrieved: {len(df):,}"
    )

    print(
        f"Total Columns: {len(df.columns)}"
    )


if __name__ == "__main__":
    main()
