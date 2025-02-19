import logging
from datetime import datetime

import pytz
from config import settings


def initial_logger():
    # Create a logger instance
    logger = logging.getLogger("app")

    # Set the logging level
    logger.setLevel(logging.DEBUG)

    # Set the timezone to Berlin
    Berlin_timezone = pytz.timezone("Europe/Berlin")

    # Configure logging with the Berlin timezone
    logging.Formatter.converter = (
        lambda *args: pytz.utc.localize(datetime.utcnow())
        .astimezone(Berlin_timezone)
        .timetuple()
    )

    # Define the log format
    console_log_format = "%(asctime)s - %(levelname)s - %(message)s"
    file_log_format = (
        "%(asctime)s - %(levelname)s - %(message)s - (%(filename)s:%(lineno)d)"
    )

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(
        logging.Formatter(console_log_format, datefmt=settings.DATE_FMT)
    )
    logger.addHandler(console_handler)

    # Create a file handler
    file_handler = logging.FileHandler(filename=settings.LOG_DIR, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(file_log_format, datefmt=settings.DATE_FMT)
    )
    logger.addHandler(file_handler)

    return logger


LOGGER = initial_logger()
