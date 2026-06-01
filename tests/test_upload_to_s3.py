from src.ingestion.complaints.download_cfpb import (
    download_complaints
)

from src.ingestion.complaints.validate_file import (
    validate_dataframe
)

from src.ingestion.complaints.upload_to_s3 import (
    upload_dataframe_to_s3
)


def main():

    df = download_complaints(
        start_date="2025-01-01",
        end_date="2025-01-31"
    )

    validate_dataframe(df)

    s3_path = upload_dataframe_to_s3(df)

    print(
        f"\nUpload Successful:\n{s3_path}"
    )


if __name__ == "__main__":
    main()
