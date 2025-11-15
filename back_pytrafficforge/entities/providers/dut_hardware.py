"""Интерфейсы реализаций аппаратной части"""

from typing import Protocol

from back_pytrafficforge.entities.behavior.dut_hardware import (
    IHardwareManager,
    IHardwareMonitor,
    IHardwareStatusManager,
)
from back_pytrafficforge.entities.data_objects.dut_hardware import DUTHardwareData


class IDUTHardwareProvider(IHardwareManager, IHardwareMonitor, IHardwareStatusManager, Protocol):
    """Интерфейс реализации DUT Hardware - объединяет данные и поведение"""

    @property
    def _data(self) -> DUTHardwareData: ...
