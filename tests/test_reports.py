from system_monitor.collectors.cpu import CPUStats
from system_monitor.collectors.disk import DiskStats
from system_monitor.collectors.memory import MemoryStats
from system_monitor.collectors.network import NetworkStats
from system_monitor.collectors.system import SystemStats
from system_monitor.services.monitor import SystemSnapshot
from system_monitor.services.reports import generate_report


def test_generate_report():
    """Verify that a readable system report is generated."""

    snapshot = SystemSnapshot(
        cpu=CPUStats(usage_percent=25.0, physical_cores=4, logical_cores=8, frequency_mhz=2400.0),
        memory=MemoryStats(total_gb=16.0, available_gb=8.0, used_gb=8.0, usage_percent=50.0),
        disk=DiskStats(total_gb=500.0, used_gb=200.0, free_gb=300.0, usage_percent=40.0),
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

    report = generate_report(snapshot, [])

    assert "SYSTEM HEALTH REPORT" in report
    assert "CPU" in report
    assert "MEMORY" in report
    assert "DISK" in report
    assert "NETWORK" in report
    assert "No active alerts." in report
