from src.utils.exceptions import (
    CFPBDownloadError
)


def main():

    try:

        raise CFPBDownloadError(
            "Unable to download CFPB data"
        )

    except CFPBDownloadError as error:

        print(error)


if __name__ == "__main__":
    main()
