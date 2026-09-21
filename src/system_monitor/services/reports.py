"""System health report generation."""

from system_monitor.services.alerts import Alert
from system_monitor.services.monitor import SystemSnapshot


def generate_report(
    snapshot: SystemSnapshot,
    alerts: list[Alert],
) -> str:
    """Generate a human-readable system health report."""

    lines = [
        "=" * 60,
        "SYSTEM HEALTH REPORT",
        "=" * 60,
        "",
        "SYSTEM INFORMATION",
        "-" * 60,
        f"Operating System : {snapshot.system.operating_system}",
        f"OS Version       : {snapshot.system.os_version}",
        f"Architecture     : {snapshot.system.architecture}",
        f"Hostname         : {snapshot.system.hostname}",
        f"Python Version   : {snapshot.system.python_version}",
        "",
        "CPU",
        "-" * 60,
        f"Usage            : {snapshot.cpu.usage_percent:.1f}%",
        f"Physical Cores   : {snapshot.cpu.physical_cores}",
        f"Logical Cores    : {snapshot.cpu.logical_cores}",
        (
            "Frequency        : "
            f"{snapshot.cpu.frequency_mhz:.2f} MHz"
            if snapshot.cpu.frequency_mhz is not None
            else "Frequency        : N/A"
        ),
        "",
        "MEMORY",
        "-" * 60,
        f"Total            : {snapshot.memory.total_gb:.2f} GB",
        f"Used             : {snapshot.memory.used_gb:.2f} GB",
        f"Available        : {snapshot.memory.available_gb:.2f} GB",
        f"Usage            : {snapshot.memory.usage_percent:.1f}%",
        "",
        "DISK",
        "-" * 60,
        f"Total            : {snapshot.disk.total_gb:.2f} GB",
        f"Used             : {snapshot.disk.used_gb:.2f} GB",
        f"Free             : {snapshot.disk.free_gb:.2f} GB",
        f"Usage            : {snapshot.disk.usage_percent:.1f}%",
        "",
        "NETWORK",
        "-" * 60,
        f"Data Sent        : {snapshot.network.bytes_sent:,} bytes",
        f"Data Received    : {snapshot.network.bytes_received:,} bytes",
        f"Packets Sent     : {snapshot.network.packets_sent:,}",
        f"Packets Received : {snapshot.network.packets_received:,}",
        f"Errors In        : {snapshot.network.errors_in:,}",
        f"Errors Out       : {snapshot.network.errors_out:,}",
        f"Dropped In       : {snapshot.network.dropped_in:,}",
        f"Dropped Out      : {snapshot.network.dropped_out:,}",
        "",
        "ALERTS",
        "-" * 60,
    ]

    if alerts:
        for alert in alerts:
            lines.append(
                f"[{alert.severity}] {alert.component}: {alert.message}"
            )
    else:
        lines.append("No active alerts.")

    lines.extend(
        [
            "",
            "=" * 60,
        ]
    )

    return "\n".join(lines)
