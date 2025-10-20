"""Интерфейс аппаратной части"""

from dataclasses import dataclass

from .elementary import CPU, NetworkInterface, RAM, Storage


@dataclass
class DUTHardware:
    """Поля сущности аппаратной части DUT"""

    id: str
    name: str | None = None
    model: str | None = None
    version: str | None = None

    cpu: CPU
    ram: RAM
    stor: Storage
    network_interfaces: list[NetworkInterface]