"""Интерфейсы реализаций софтовой части"""


from typing import Protocol

from entities.behavior.dut_firmware import IDUTSoftware
from entities.data_objects.dut_firmware import DUTSoftwareData


class IDUTSoftwareImpProvider(IDUTSoftware, Protocol):
    """Интерфейс реализации DUT Software - объединяет данные и поведение"""

    @property
    def _data(self) -> DUTSoftwareData: ...

    def get_running_services_count(self) -> int: ...
    def get_system_health_report(self) -> dict: ...
    def validate_system(self) -> bool: ...
