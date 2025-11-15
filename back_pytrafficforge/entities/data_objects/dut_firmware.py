"""Интерфейс программной части"""

from dataclasses import dataclass
from datetime import datetime

from entities.data_objects.elementary import NetProtocols, ServiceStatus, SoftType, StatusNI


@dataclass
class SoftwareService:
    """Служба/процесс"""

    id: str
    name: str
    version: str
    status: ServiceStatus
    port: int | None = None
    protocol: NetProtocols | None = None
    pid: int | None = None
    start_time: datetime | None = None
    config_path: str | None = None


@dataclass
class NetworkEndpoint:
    """Сетевой endpoint"""

    id: str
    address: str
    port: int
    protocol: NetProtocols
    service: str | None = None
    status: StatusNI


@dataclass
class SoftwareComponentData:
    """Программный компонент"""

    id: str
    name: str
    version: str
    type: SoftType
    services: list[SoftwareService]
    endpoints: list[NetworkEndpoint]
    dependencies: list[str]


@dataclass
class OperatingSystem:
    """Операционная система"""

    name: str
    version: str
    kernel: str
    architecture: str
    install_date: datetime | None = None


@dataclass
class DUTSoftwareData:
    """Данные программной части DUT - чистая DTO"""

    id: str
    operating_system: OperatingSystem
    components: list[SoftwareComponentData]
    firmware_version: str | None = None
    environment_vars: dict[str, str] = None
    config_files: dict[str, str] = None
    boot_time: datetime | None = None
    last_update: datetime | None = None

    def __post_init__(self):
        if self.environment_vars is None:
            self.environment_vars = {}
        if self.config_files is None:
            self.config_files = {}
