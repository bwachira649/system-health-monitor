"""CPU monitoring functionality."""

from dataclasses import dataclass

import psutil


@dataclass(frozen=True)
class CPUStats:
    """Represents a snapshot of CPU statistics."""

    usage_percent: float
    physical_cores: int
    logical_cores: int
    frequency_mhz: float | None


def collect_cpu_stats() -> CPUStats:
    """Collect and return the current CPU statistics."""

    frequency = psutil.cpu_freq()

    return CPUStats(
        usage_percent=psutil.cpu_percent(interval=1.0),
        physical_cores=psutil.cpu_count(logical=False) or 0,
        logical_cores=psutil.cpu_count(logical=True) or 0,
        frequency_mhz=(
            round(frequency.current, 2)
            if frequency is not None
            else None
        ),
    )
