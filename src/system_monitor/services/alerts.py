"""System health alert functionality."""

from dataclasses import dataclass

from system_monitor.services.monitor import SystemSnapshot


@dataclass(frozen=True)
class Alert:
    """Represents a system health alert."""

    component: str
    message: str
    severity: str


def generate_alerts(
    snapshot: SystemSnapshot,
    cpu_threshold: float = 90.0,
    memory_threshold: float = 90.0,
    disk_threshold: float = 90.0,
) -> list[Alert]:
    """Generate alerts based on system health thresholds."""

    alerts: list[Alert] = []

    if snapshot.cpu.usage_percent >= cpu_threshold:
        alerts.append(
            Alert(
                component="CPU",
                message=(
                    f"CPU usage is {snapshot.cpu.usage_percent:.1f}%."
                ),
                severity="WARNING",
            )
        )

    if snapshot.memory.usage_percent >= memory_threshold:
        alerts.append(
            Alert(
                component="Memory",
                message=(
                    f"Memory usage is {snapshot.memory.usage_percent:.1f}%."
                ),
                severity="WARNING",
            )
        )

    if snapshot.disk.usage_percent >= disk_threshold:
        alerts.append(
            Alert(
                component="Disk",
                message=(
                    f"Disk usage is {snapshot.disk.usage_percent:.1f}%."
                ),
                severity="WARNING",
            )
        )

    return alerts
