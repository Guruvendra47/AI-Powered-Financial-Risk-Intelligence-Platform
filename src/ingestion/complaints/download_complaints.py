import kagglehub
from pathlib import Path
from src.utils.logger import get_logger

logger = get_logger()

def main():
    logger.info("Starting CFPB dataset download")

    dataset_path = kagglehub.dataset_download(
        "shashwatwork/consume-complaints-dataset-fo-nlp"
    )

    logger.info(f"Dataset downloaded to: {dataset_path}")

    raw_path = Path("data/raw")
    raw_path.mkdir(parents=True, exist_ok=True)

    logger.info("Download completed successfully")

if __name__ == "__main__":
    main()
