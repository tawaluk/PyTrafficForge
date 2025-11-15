"""Интерфейс аппаратной части"""

from dataclasses import dataclass

from entities.data_objects.elementary import (
    CPU,
    GPU,
    RAM,
    NetworkInterface,
    PowerSupply,
    Storage,
    TemperatureSensor,
)


@dataclass
class DUTHardwareData:
    """Данные аппаратной части DUT - чистая DTO"""

    id: str
    name: str | None = None
    model: str | None = None
    meta_info: dict | None = None
    version: str | None = None

    cpu: CPU
    ram: RAM
    storage: list[Storage]
    network_interfaces: list[NetworkInterface]

    gpu: GPU | None = None
    power_supply: PowerSupply | None = None

    temperature_sensors: list[TemperatureSensor] | None = None
    power_consumption: float | None = None  # Ватт
    uptime: int | None = None  # Сек
