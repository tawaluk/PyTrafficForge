"""Абстракция поведения софтовой части обьекта тестирования"""

from typing import Protocol

from domain.data_objects.dut_firmware import (
    NetworkEndpoint,
    SoftwareService,
)
from domain.data_objects.elementary import NetProtocols, SoftType


class IServiceManager(Protocol):
    """Управление сервисами"""

    def get_running_services(self) -> list[SoftwareService]: ...
    def restart_failed_services(self) -> list[str]: ...
    def start_service(self, service_id: str) -> bool: ...
    def stop_service(self, service_id: str) -> bool: ...


class INetworkEndpointProvider(Protocol):
    """Предоставление сетевых endpoints"""

    def get_service_endpoints(self, service_id: str) -> list[NetworkEndpoint]: ...
    def get_endpoints_by_protocol(self, protocol: NetProtocols) -> list[NetworkEndpoint]: ...


class IComponentMetadata(Protocol):
    """Мета-информация компонента"""

    @property
    def component_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def component_type(self) -> SoftType: ...


class ISoftwareComponent(
    IComponentMetadata,
    IServiceManager,
    INetworkEndpointProvider,
    Protocol
):
    """Композитный протокол программного компонента"""

    def validate_dependencies(self) -> bool: ...


class IDUTSoftware(Protocol):
    """Программная часть DUT"""

    def get_component_by_type(self, component_type: SoftType) -> ISoftwareComponent | None: ...
    def get_all_endpoints(self) -> list[NetworkEndpoint]: ...
    def find_service_by_port(self, port: int) -> SoftwareService | None: ...
    def update_environment_var(self, key: str, value: str) -> None: ...
