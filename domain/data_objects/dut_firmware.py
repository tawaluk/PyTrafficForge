"""Интерфейс программной части"""

from dataclasses import dataclass, replace
from datetime import datetime

from domain.data_objects.elementary import NetProtocols, ServiceStatus, SoftType, StatusNI


@dataclass(frozen=True)
class SoftwareService:
    """Служба/процесс. DTO"""

    id: str
    name: str
    version: str
    status: ServiceStatus
    port: int | None = None
    protocol: NetProtocols | None = None
    pid: int | None = None
    start_time: datetime | None = None
    config_path: str | None = None

    def update(self, **kwargs) -> "SoftwareService":
        """Для восознанного изменения DTO."""
        return replace(self, **kwargs)


@dataclass(frozen=True)
class NetworkEndpoint:
    """Сетевой endpoint"""

    id: str
    address: str
    port: int
    protocol: NetProtocols
    status: StatusNI
    service: str | None = None

    def update(self, **kwargs) -> "NetworkEndpoint":
        """Для восознанного изменения DTO."""
        return replace(self, **kwargs)


@dataclass(frozen=True)
class SoftwareComponentData:
    """Программный компонент"""

    id: str
    name: str
    version: str
    type: SoftType
    services: list[SoftwareService]
    endpoints: list[NetworkEndpoint]
    dependencies: list[str]

    def update(self, **kwargs) -> "SoftwareComponentData":
        """Для восознанного изменения DTO."""
        return replace(self, **kwargs)


@dataclass(frozen=True)
class OperatingSystem:
    """Операционная система"""

    name: str
    version: str
    kernel: str
    architecture: str
    install_date: datetime | None = None

    def update(self, **kwargs) -> "OperatingSystem":
        """Для восознанного изменения DTO."""
        return replace(self, **kwargs)


@dataclass(frozen=True)
class DUTSoftwareData:
    """Данные программной части DUT - чистая DTO"""

    id: str
    operating_system: OperatingSystem
    components: list[SoftwareComponentData]
    firmware_version: str | None = None
    environment_vars: dict[str, str] | None = None
    config_files: dict[str, str] | None = None
    boot_time: datetime | None = None
    last_update: datetime | None = None

    def update(self, **kwargs) -> "DUTSoftwareData":
        """Для осознанного изменения DTO."""
        return replace(self, **kwargs)
