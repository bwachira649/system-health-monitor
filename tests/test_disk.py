from system_monitor.collectors.disk import collect_disk_stats


def test_disk_statistics():
    """Verify that disk statistics contain valid values."""

    stats = collect_disk_stats()

    assert stats.total_gb > 0
    assert stats.used_gb >= 0
    assert stats.free_gb >= 0
    assert 0 <= stats.usage_percent <= 100
