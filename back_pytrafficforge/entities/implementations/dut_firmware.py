"""Интерфейсы реализаций софтовой части"""


from typing import Protocol

from back_pytrafficforge.entities.data_objects.dut_firmware import (
    DUTSoftwareData,
    NetworkEndpoint,
    SoftwareComponentData,
    SoftwareService,
)
from back_pytrafficforge.entities.data_objects.elementary import SoftType


class IDUTSoftwareImplementation(Protocol):
    """Интерфейс реализации DUT Software - объединяет данные и поведение"""


    @property
    def data(self) -> DUTSoftwareData: ...
    def get_component_by_type(self, component_type: SoftType) -> SoftwareComponentData | None: ...
    def get_all_endpoints(self) -> list[NetworkEndpoint]: ...
    def find_service_by_port(self, port: int) -> SoftwareService | None: ...
    def update_environment_var(self, key: str, value: str) -> None: ...
    def get_running_services_count(self) -> int: ...
    def get_system_health_report(self) -> dict: ...
    def validate_system(self) -> bool: ...
