import logging
import os
from datetime import datetime

from .config import LOG_DIR, LOG_LEVEL  # type: ignore
from .formatter import get_formatter, get_plain_formatter


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Ensure the logs folder exists
        os.makedirs(LOG_DIR, exist_ok=True)

        # Create a timestamped log filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = os.path.join(LOG_DIR, f"{timestamp}.log")

        # Console handler with colour
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(get_formatter())
        logger.addHandler(stream_handler)

        # File handler without colour
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(get_plain_formatter())
        logger.addHandler(file_handler)

        logger.setLevel(LOG_LEVEL)
        logger.propagate = False
    return logger
