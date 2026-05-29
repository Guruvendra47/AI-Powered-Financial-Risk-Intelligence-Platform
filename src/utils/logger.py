from loguru import logger

logger.add(
    "logs/application.log",
    rotation="10 MB",
    retention="10 days"
)

def get_logger():
    return logger
