"""Самые атомарные сущности"""

from dataclasses import dataclass
from enum import Enum


class NetworkRole(Enum):
    """Роль сетевого интерфейса в тестировании"""
    TRAFFIC_GENERATOR = "generator"
    TRAFFIC_CONSUMER = "consumer"
    MANAGEMENT = "management"
    MONITORING = "monitoring"


@dataclass
class CPU:
    """ЦП"""

    id: str
    name: str
    model: str
    cores: int
    v_cores: int
    clock_speed: int  # MHz
    l_1: int  # Mb
    l_2: int  # Mb
    l_3: int | None = None  # Mb


@dataclass
class RAM:
    """ОЗУ"""

    id: str
    name: str
    clock_speed: int  # MHz
    ddr_type: str
    total: int  # Mb

    latency: int | None = None # Sec


@dataclass
class Storage:
    """Накопитель данных"""

    id: str
    name: str
    type: str  # SSD, HDD, NVMe, eMMC
    total: int  # Mb
    read_speed: int | None = None  # MB/s
    write_speed: int | None = None  # MB/s
    interface: int | None = None  # SATA, PCIe, USB


@dataclass
class NetworkInterface:
    """Сетевой интерфейс"""

    id: str
    name: str
    mac_address: str
    speed: int  # Mbps
    interface_type: str  # Ethernet, WiFi, Cellular

    ip_address: str | None = None
    duplex: str | None = None  # full, half


@dataclass
class GPU:
    """Графический процессор"""

    id: str
    name: str
    model: str
    memory: int  # Mb
    cores: int | None = None
    clock_speed: int | None = None  # MHz
