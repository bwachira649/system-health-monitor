from system_monitor.collectors.cpu import CPUStats
from system_monitor.collectors.disk import DiskStats
from system_monitor.collectors.memory import MemoryStats
from system_monitor.collectors.network import NetworkStats
from system_monitor.collectors.system import SystemStats
from system_monitor.services.alerts import generate_alerts
from system_monitor.services.monitor import SystemSnapshot


def create_snapshot() -> SystemSnapshot:
    """Create a predictable system snapshot for testing."""

    return SystemSnapshot(
        cpu=CPUStats(
            usage_percent=95.0,
            physical_cores=4,
            logical_cores=8,
            frequency_mhz=2500.0,
        ),
        memory=MemoryStats(
            total_gb=16.0,
            available_gb=1.0,
            used_gb=15.0,
            usage_percent=94.0,
        ),
        disk=DiskStats(
            total_gb=500.0,
            used_gb=460.0,
            free_gb=40.0,
            usage_percent=92.0,
        ),
        network=NetworkStats(
            bytes_sent=1000,
            bytes_received=2000,
            packets_sent=10,
            packets_received=20,
            errors_in=0,
            errors_out=0,
            dropped_in=0,
            dropped_out=0,
        ),
        system=SystemStats(
            operating_system="Linux",
            os_version="Test",
            architecture="x86_64",
            hostname="test-machine",
            python_version="3.14.4",
        ),
    )


def test_generate_alerts():
    """Verify that high resource usage generates alerts."""

    snapshot = create_snapshot()

    alerts = generate_alerts(snapshot)

    assert len(alerts) == 3
    assert alerts[0].component == "CPU"
    assert alerts[1].component == "Memory"
    assert alerts[2].component == "Disk"

    assert all(alert.severity == "WARNING" for alert in alerts)
