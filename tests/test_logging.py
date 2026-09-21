"""Tests for application logging."""

from pathlib import Path

from system_monitor.utils.logging_config import configure_logging


def test_configure_logging_creates_log_file(tmp_path: Path) -> None:
    """The logging configuration should create and write to a log file."""

    log_file = tmp_path / "system_monitor.log"

    logger = configure_logging(log_file)
    logger.info("Test log message.")

    assert log_file.exists()
    assert "Test log message." in log_file.read_text()
