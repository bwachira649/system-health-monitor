from system_monitor.collectors.network import collect_network_stats


def test_network_statistics():
    """Verify that network statistics contain valid values."""

    stats = collect_network_stats()

    assert stats.bytes_sent >= 0
    assert stats.bytes_received >= 0
    assert stats.packets_sent >= 0
    assert stats.packets_received >= 0
    assert stats.errors_in >= 0
    assert stats.errors_out >= 0
    assert stats.dropped_in >= 0
    assert stats.dropped_out >= 0
