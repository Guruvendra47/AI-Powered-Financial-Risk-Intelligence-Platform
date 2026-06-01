from src.ingestion.complaints.download_cfpb import (
    download_complaints
)

from src.ingestion.complaints.validate_file import (
    validate_dataframe
)


def main():

    df = download_complaints(
        start_date="2025-01-01",
        end_date="2025-01-31"
    )

    validate_dataframe(df)

    print(
        "\nValidation Successful"
    )


if __name__ == "__main__":
    main()
