from src.utils.logger import get_logger


logger = get_logger(__name__)


def main():

    logger.info("Logger test started")

    logger.warning("This is a warning")

    logger.error("This is an error")

    logger.info("Logger test completed")


if __name__ == "__main__":
    main()
