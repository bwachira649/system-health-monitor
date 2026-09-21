"""Disk monitoring functionality."""

from dataclasses import dataclass

import psutil


@dataclass(frozen=True)
class DiskStats:
    """Represents a snapshot of disk statistics."""

    total_gb: float
    used_gb: float
    free_gb: float
    usage_percent: float


def collect_disk_stats(path: str = "/") -> DiskStats:
    """Collect and return disk statistics for the specified path."""

    disk = psutil.disk_usage(path)

    return DiskStats(
        total_gb=round(disk.total / (1024 ** 3), 2),
        used_gb=round(disk.used / (1024 ** 3), 2),
        free_gb=round(disk.free / (1024 ** 3), 2),
        usage_percent=disk.percent,
    )
