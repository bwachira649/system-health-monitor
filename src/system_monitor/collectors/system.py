"""System information collection functionality."""

from dataclasses import dataclass
import platform
import socket
import sys


@dataclass(frozen=True)
class SystemStats:
    """Represents information about the current system."""

    operating_system: str
    os_version: str
    architecture: str
    hostname: str
    python_version: str


def collect_system_stats() -> SystemStats:
    """Collect and return information about the current system."""

    return SystemStats(
        operating_system=platform.system(),
        os_version=platform.release(),
        architecture=platform.machine(),
        hostname=socket.gethostname(),
        python_version=sys.version.split()[0],
    )
