"""Network monitoring functionality."""

from dataclasses import dataclass

import psutil


@dataclass(frozen=True)
class NetworkStats:
    """Represents a snapshot of network statistics."""

    bytes_sent: int
    bytes_received: int
    packets_sent: int
    packets_received: int
    errors_in: int
    errors_out: int
    dropped_in: int
    dropped_out: int


def collect_network_stats() -> NetworkStats:
    """Collect and return network statistics."""

    network = psutil.net_io_counters()

    return NetworkStats(
        bytes_sent=network.bytes_sent,
        bytes_received=network.bytes_recv,
        packets_sent=network.packets_sent,
        packets_received=network.packets_recv,
        errors_in=network.errin,
        errors_out=network.errout,
        dropped_in=network.dropin,
        dropped_out=network.dropout,
    )
