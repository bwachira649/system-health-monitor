"""Application entry point for the System Health Monitor."""

import argparse
import time
from pathlib import Path

from system_monitor.config import (
    DEFAULT_CPU_THRESHOLD,
    DEFAULT_DISK_THRESHOLD,
    DEFAULT_INTERVAL_SECONDS,
    DEFAULT_MEMORY_THRESHOLD,
)
from system_monitor.services.alerts import generate_alerts
from system_monitor.services.monitor import collect_system_snapshot
from system_monitor.services.reports import generate_report
from system_monitor.utils.logging_config import configure_logging


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description="Monitor system health and performance."
    )

    parser.add_argument(
        "--watch",
        action="store_true",
        help="Continuously monitor the system.",
    )

    parser.add_argument(
        "--interval",
        type=float,
        default=DEFAULT_INTERVAL_SECONDS,
        help="Refresh interval in seconds (default: 5).",
    )

    parser.add_argument(
        "--cpu-threshold",
        type=float,
        default=DEFAULT_CPU_THRESHOLD,
        help="CPU warning threshold percentage (default: 90).",
    )

    parser.add_argument(
        "--memory-threshold",
        type=float,
        default=DEFAULT_MEMORY_THRESHOLD,
        help="Memory warning threshold percentage (default: 90).",
    )

    parser.add_argument(
        "--disk-threshold",
        type=float,
        default=DEFAULT_DISK_THRESHOLD,
        help="Disk warning threshold percentage (default: 90).",
    )

    parser.add_argument(
        "--log-file",
        type=Path,
        default=Path("system_monitor.log"),
        help="Path to the application log file.",
    )

    return parser


def validate_threshold(name: str, value: float) -> None:
    """Validate a percentage threshold."""

    if not 0 <= value <= 100:
        raise ValueError(
            f"{name} threshold must be between 0 and 100."
        )


def run_once(
    cpu_threshold: float,
    memory_threshold: float,
    disk_threshold: float,
    logger,
) -> None:
    """Collect and display one system health report."""

    logger.info("Collecting system health information.")

    snapshot = collect_system_snapshot()

    alerts = generate_alerts(
        snapshot,
        cpu_threshold=cpu_threshold,
        memory_threshold=memory_threshold,
        disk_threshold=disk_threshold,
    )

    report = generate_report(snapshot, alerts)

    print(report)

    logger.info(
        "System health report generated successfully. "
        "Active alerts: %d.",
        len(alerts),
    )


def run_watch(
    interval: float,
    cpu_threshold: float,
    memory_threshold: float,
    disk_threshold: float,
    logger,
) -> None:
    """Continuously monitor the system."""

    if interval <= 0:
        raise ValueError(
            "Monitoring interval must be greater than zero."
        )

    logger.info(
        "Continuous monitoring started. Interval: %s seconds.",
        interval,
    )

    print("System Health Monitor")
    print("Continuous monitoring mode")
    print("Press Ctrl+C to stop.")
    print()

    try:
        while True:
            run_once(
                cpu_threshold,
                memory_threshold,
                disk_threshold,
                logger,
            )

            print(f"\nRefreshing in {interval:g} seconds...")
            time.sleep(interval)
            print("\n" + "\033[2J\033[H", end="")

    except KeyboardInterrupt:
        logger.info("Continuous monitoring stopped by user.")
        print("\nMonitoring stopped.")
        print("Goodbye.")


def main() -> None:
    """Run the System Health Monitor application."""

    parser = create_parser()
    args = parser.parse_args()

    logger = configure_logging(args.log_file)

    logger.info("System Health Monitor started.")

    try:
        validate_threshold("CPU", args.cpu_threshold)
        validate_threshold("Memory", args.memory_threshold)
        validate_threshold("Disk", args.disk_threshold)

        if args.watch:
            run_watch(
                args.interval,
                args.cpu_threshold,
                args.memory_threshold,
                args.disk_threshold,
                logger,
            )
        else:
            run_once(
                args.cpu_threshold,
                args.memory_threshold,
                args.disk_threshold,
                logger,
            )

    except Exception:
        logger.exception("Application error occurred.")
        raise

    finally:
        logger.info("System Health Monitor finished.")


if __name__ == "__main__":
    main()
