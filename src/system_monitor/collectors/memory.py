"""Memory monitoring functionality."""

from dataclasses import dataclass

import psutil


@dataclass(frozen=True)
class MemoryStats:
    """Represents a snapshot of memory statistics."""

    total_gb: float
    available_gb: float
    used_gb: float
    usage_percent: float


def collect_memory_stats() -> MemoryStats:
    """Collect and return the current memory statistics."""

    memory = psutil.virtual_memory()

    return MemoryStats(
        total_gb=round(memory.total / (1024 ** 3), 2),
        available_gb=round(memory.available / (1024 ** 3), 2),
        used_gb=round(memory.used / (1024 ** 3), 2),
        usage_percent=memory.percent,
    )
