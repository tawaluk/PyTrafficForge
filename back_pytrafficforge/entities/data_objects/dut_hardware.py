"""Интерфейс аппаратной части"""

from dataclasses import dataclass

from .elementary import (
    CPU,
    GPU,
    RAM,
    NetworkInterface,
    NetworkRole,
    PowerSupply,
    StatusNI,
    Storage,
    TemperatureSensor,
)


@dataclass
class DUTHardware:
    """Поля сущности аппаратной части DUT"""

    id: str
    name: str | None = None
    model: str | None = None
    meta_infp: dict | None = None
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

    def _get_interfaces_by_role(self, role: NetworkRole) -> list[NetworkInterface]:
        """Получить интерфейсы по роли"""
        if not self.network_interfaces:
            return []
        return [ni for ni in self.network_interfaces if role in ni.role]

    def get_traffic_generator_interfaces(self) -> list[NetworkInterface]:
        """Получить интерфейсы для генерации трафика"""
        return self._get_interfaces_by_role(NetworkRole.TRAFFIC_GENERATOR)

    def get_traffic_consumer_interfaces(self) -> list[NetworkInterface]:
        """Получить интерфейсы для приема трафика"""
        return self._get_interfaces_by_role(NetworkRole.TRAFFIC_CONSUMER)

    def get_management_interfaces(self) -> list[NetworkInterface]:
        """Получить интерфейсы управления"""
        return self._get_interfaces_by_role(NetworkRole.MANAGEMENT)

    def get_monitoring_interfaces(self) -> list[NetworkInterface]:
        """Получить интерфейсы мониторинга"""
        return self._get_interfaces_by_role(NetworkRole.MONITORING)

    def _get_interfaces_by_status(self, status: StatusNI) -> list[NetworkInterface]:
        """Получить все интерфейсы в статусе"""
        if not self.network_interfaces:
            return []
        return [ni for ni in self.network_interfaces if getattr(ni, 'status', None) == status]

    def get_free_interfaces(self) -> list[NetworkInterface]:
        """Получить свободные интерфейсы"""
        return self._get_interfaces_by_status(StatusNI.FREE)

    def get_busy_interfaces(self) -> list[NetworkInterface]:
        """Получить занятые интерфейсы"""
        return self._get_interfaces_by_status(StatusNI.BUSY)

    def get_working_interfaces(self) -> list[NetworkInterface]:
        """Получить работающие интерфейсы"""
        return self._get_interfaces_by_status(StatusNI.WORK)

    def set_interface_status(self, interface_id: str, status: StatusNI) -> bool:
        """Установить статус интерфейса"""
        for ni in self.network_interfaces:
            if ni.id == interface_id:
                ni.status = status
                return True
        return False

    def mark_interface_as_busy(self, interface_id: str) -> bool:
        """Пометить интерфейс как занятый"""
        return self.set_interface_status(interface_id, StatusNI.BUSY)

    def mark_interface_as_free(self, interface_id: str) -> bool:
        """Пометить интерфейс как свободный"""
        return self.set_interface_status(interface_id, StatusNI.FREE)

    def mark_interface_as_working(self, interface_id: str) -> bool:
        """Пометить интерфейс как работающий"""
        return self.set_interface_status(interface_id, StatusNI.WORK)

    def get_interface_status(self, interface_id: str) -> StatusNI | None:
        """Получить статус интерфейса"""
        for ni in self.network_interfaces:
            if ni.id == interface_id:
                return getattr(ni, 'status', StatusNI.FREE)
        return None
