"""Интерфейс генератора трафика"""


from dataclasses import dataclass, replace
from datetime import datetime

from entities.data_objects.elementary import GeneratorType, NetProtocols, TrafficProfile


@dataclass(frozen=True)
class TrafficConfig:
    """Конфигурация трафика"""

    packet_size: int  # bytes
    packets_per_second: int
    duration: int  # seconds
    protocol: NetProtocols
    source_ports: list[int] | None = None
    destination_ports: list[int] | None = None

    payload_pattern: str | None = None
    ttl: int | None = None
    dscp: int | None = None

    def update(self, **kwargs) -> "TrafficConfig":
        """Для осознанного изменения DTO."""
        return replace(self, **kwargs)


@dataclass(frozen=True)
class GeneratorCapabilities:
    """Возможности генератора"""

    max_throughput: int  # Mbps
    max_pps: int  # packets per second
    supported_protocols: list[NetProtocols]
    hardware_accelerated: bool = False
    can_generate_malformed: bool = False
    supports_timing_analysis: bool = False

    def update(self, **kwargs) -> "GeneratorCapabilities":
        """Для осознанного изменения DTO."""
        return replace(self, **kwargs)


@dataclass(frozen=True)
class TrafficGeneratorData:
    """Данные генератора нагрузки - чистая DTO"""

    id: str
    name: str
    type: GeneratorType
    capabilities: GeneratorCapabilities
    interface_bindings: list[str]  # ID интерфейсов, к которым привязан

    is_running: bool = False
    current_load: float = 0.0  # процент от максимальной
    last_start_time: datetime | None = None
    total_packets_sent: int = 0

    current_config: TrafficConfig | None = None
    active_profile: TrafficProfile | None = None

    def update(self, **kwargs) -> "TrafficGeneratorData":
        """Для осознанного изменения DTO."""
        return replace(self, **kwargs)
