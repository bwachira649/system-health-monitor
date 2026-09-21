from system_monitor.services.monitor import collect_system_snapshot


def test_system_snapshot():
    """Verify that a complete system snapshot can be collected."""

    snapshot = collect_system_snapshot()

    assert snapshot.cpu.usage_percent >= 0
    assert snapshot.memory.total_gb > 0
    assert snapshot.disk.total_gb > 0
    assert snapshot.network.bytes_sent >= 0
    assert snapshot.system.operating_system
