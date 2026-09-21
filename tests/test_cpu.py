from system_monitor.collectors.cpu import collect_cpu_stats


def test_cpu_statistics():
    """Verify that CPU statistics contain valid values."""

    stats = collect_cpu_stats()

    assert 0 <= stats.usage_percent <= 100

    assert stats.physical_cores > 0
    assert stats.logical_cores > 0

    if stats.frequency_mhz is not None:
        assert stats.frequency_mhz > 0
