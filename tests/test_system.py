from system_monitor.collectors.system import collect_system_stats


def test_system_statistics():
    """Verify that system information is available."""

    stats = collect_system_stats()

    assert stats.operating_system
    assert stats.os_version
    assert stats.architecture
    assert stats.hostname
    assert stats.python_version
