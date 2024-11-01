# utils/helpers.py

import logging
from datetime import datetime
from typing import Dict, Any


def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Sets up a logger with a specific name and log file."""
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def format_for_display(data: Dict[str, Any]) -> str:
    """Formats a dictionary of data as a readable string."""
    return "\n".join(f"{key}: {value}" for key, value in data.items())


def timestamp() -> str:
    """Returns the current timestamp as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
