"""System monitoring service."""

from dataclasses import dataclass

from system_monitor.collectors.cpu import CPUStats, collect_cpu_stats
from system_monitor.collectors.disk import DiskStats, collect_disk_stats
from system_monitor.collectors.memory import MemoryStats, collect_memory_stats
from system_monitor.collectors.network import (
    NetworkStats,
    collect_network_stats,
)
from system_monitor.collectors.system import SystemStats, collect_system_stats


@dataclass(frozen=True)
class SystemSnapshot:
    """Contains a complete snapshot of system health."""

    cpu: CPUStats
    memory: MemoryStats
    disk: DiskStats
    network: NetworkStats
    system: SystemStats


def collect_system_snapshot() -> SystemSnapshot:
    """Collect all available system health information."""

    return SystemSnapshot(
        cpu=collect_cpu_stats(),
        memory=collect_memory_stats(),
        disk=collect_disk_stats(),
        network=collect_network_stats(),
        system=collect_system_stats(),
    )
