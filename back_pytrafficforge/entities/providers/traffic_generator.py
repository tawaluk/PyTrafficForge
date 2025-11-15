from typing import Protocol

from back_pytrafficforge.entities.behavior.traffic_generator import (
    IAdvancedTrafficFeatures,
    IGeneratorMonitor,
    ITrafficConfigurator,
    ITrafficController,
)
from entities.data_objects.traffic_generator import TrafficGeneratorData


class ITrafficGeneratorProvider(
    ITrafficController,
    ITrafficConfigurator,
    IGeneratorMonitor,
    IAdvancedTrafficFeatures,
    Protocol
):
    """Интерфейс реализации генератора нагрузки - объединяет данные и поведение"""

    @property
    def _data(self) -> TrafficGeneratorData: ...
