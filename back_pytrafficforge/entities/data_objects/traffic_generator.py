"""Интерфейс генератора трафика"""


from dataclasses import dataclass
from datetime import datetime

from entities.data_objects.elementary import GeneratorType, NetProtocols, TrafficProfile


@dataclass
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


@dataclass
class GeneratorCapabilities:
    """Возможности генератора"""

    max_throughput: int  # Mbps
    max_pps: int  # packets per second
    supported_protocols: list[NetProtocols]
    hardware_accelerated: bool = False
    can_generate_malformed: bool = False
    supports_timing_analysis: bool = False


@dataclass
class TrafficGeneratorData:
    """Данные генератора нагрузки - чистая DTO"""

    id: str
    name: str
    type: GeneratorType
    capabilities: GeneratorCapabilities
    interface_bindings: list[]  # ID интерфейсов, к которым привязан

    is_running: bool = False
    current_load: float = 0.0  # процент от максимальной
    last_start_time: datetime | None = None
    total_packets_sent: int = 0

    current_config: TrafficConfig | None = None
    active_profile: TrafficProfile | None = None
