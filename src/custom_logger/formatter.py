import logging

from .color import colour_text
from .config import DATE_FORMAT, LOG_FORMAT  # type: ignore


class ColourFormatter(logging.Formatter):
    def format(self, record):
        original_msg = super().format(record)
        return colour_text(record.levelname, original_msg)


def get_formatter():
    return ColourFormatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)


def get_plain_formatter():
    return logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
