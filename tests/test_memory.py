from system_monitor.collectors.memory import collect_memory_stats


def test_memory_statistics():
    """Verify that memory statistics contain valid values."""

    stats = collect_memory_stats()

    assert stats.total_gb > 0
    assert stats.available_gb >= 0
    assert stats.used_gb >= 0
    assert 0 <= stats.usage_percent <= 100
