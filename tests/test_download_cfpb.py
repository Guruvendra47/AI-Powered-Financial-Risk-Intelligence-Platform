from src.ingestion.complaints.download_cfpb import (
    download_complaints
)


def main():

    df = download_complaints(
        start_date="2025-01-01",
        end_date="2025-01-31"
    )

    print(df.head())

    print(f"\nRecords Retrieved: {len(df)}")


if __name__ == "__main__":
    main()
