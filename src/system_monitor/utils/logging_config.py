"""Logging configuration for the System Health Monitor."""

import logging
from pathlib import Path

DEFAULT_LOG_FILE = Path("system_monitor.log")


def configure_logging(
    log_file: Path = DEFAULT_LOG_FILE,
) -> logging.Logger:
    """Configure application logging and return the application logger."""

    logger = logging.getLogger("system_monitor")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Remove existing handlers so the function can safely be reused.
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()

    log_file.parent.mkdir(parents=True, exist_ok=True)

    handler = logging.FileHandler(log_file)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
