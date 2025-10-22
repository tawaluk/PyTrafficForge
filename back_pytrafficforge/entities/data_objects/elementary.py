"""Самые атомарные сущности"""

import ipaddress
from dataclasses import dataclass
from enum import Enum


class NetworkRole(Enum):
    """Роль сетевого интерфейса в тестировании"""

    TRAFFIC_GENERATOR = "generator"
    TRAFFIC_CONSUMER = "consumer"
    MANAGEMENT = "management"
    MONITORING = "monitoring"
    SPAN_MIRROR = "span_mirror"  # Для зеркалирования трафика


class StatusNI(Enum):
    """Статус по занятости интерфейса"""

    FREE = "free"
    BUSY = "basy"
    WORK = "work"


class Protocol(Enum):
    """Сетевые протоколы"""

    TCP = "tcp"
    UDP = "udp"
    HTTP = "http"
    HTTPS = "https"
    DNS = "dns"
    ICMP = "icmp"


@dataclass(frozen=True)
class MAC:
    """MAC-адрес"""

    address: str

    def __post_init__(self):
        if not self._is_valid_mac(self.address):
            raise ValueError(f"Invalid MAC address: {self.address}")

    @staticmethod
    def _is_valid_mac(mac: str) -> bool:
        """Проверка валидности MAC-адреса"""
        import re
        pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        return bool(re.match(pattern, mac))

    def __str__(self):
        return self.address


@dataclass(frozen=True)
class IPv4:
    """IPv4 адрес"""

    address: str
    netmask: str = "255.255.255.0"
    gateway: str | None = None

    def __post_init__(self):
        try:
            ipaddress.IPv4Address(self.address)
            ipaddress.IPv4Address(self.netmask)
            if self.gateway:
                ipaddress.IPv4Address(self.gateway)
        except ipaddress.AddressValueError as e:
            raise ValueError(f"Invalid IPv4 address: {e}")

    @property
    def network(self) -> ipaddress.IPv4Network:
        return ipaddress.IPv4Network(f"{self.address}/{self.netmask}", strict=False)

    def __str__(self):
        return self.address


@dataclass(frozen=True)
class IPv6:
    """IPv6 адрес"""

    address: str
    prefix_length: int = 64
    gateway: str | None = None

    def __post_init__(self):
        try:
            ipaddress.IPv6Address(self.address)
            if self.gateway:
                ipaddress.IPv6Address(self.gateway)
        except ipaddress.AddressValueError as e:
            raise ValueError(f"Invalid IPv6 address: {e}")

    @property
    def network(self) -> ipaddress.IPv6Network:
        return ipaddress.IPv6Network(f"{self.address}/{self.prefix_length}", strict=False)

    def __str__(self):
        return self.address


# Тип для любого сетевого адреса
NetworkAddress = IPv4 | IPv6 | MAC


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

    # Дополнительные характеристики
    architecture: str = "x86_64"  # x86, ARM, RISC-V
    socket: str | None = None
    thermal_design_power: int | None = None  # TDP в ваттах


@dataclass
class RAM:
    """ОЗУ"""

    id: str
    name: str
    clock_speed: int  # MHz
    ddr_type: str  # DDR3, DDR4, DDR5
    total: int  # Mb

    # Тайминги
    latency: int | None = None  # CL тайминг
    timings: str | None = None  # "16-18-18-36"
    ecc: bool = False  # ECC память

    # Физические характеристики
    modules: int = 1  # Количество модулей
    configuration: str | None = None  # "2x8GB"


@dataclass
class Storage:
    """Накопитель данных"""

    id: str
    name: str
    type: str  # SSD, HDD, NVMe, eMMC
    total: int  # Mb

    # Производительность
    read_speed: int | None = None  # MB/s
    write_speed: int | None = None  # MB/s
    iops_read: int | None = None  # IOPS для чтения
    iops_write: int | None = None  # IOPS для записи

    # Интерфейс
    interface: str | None = None  # SATA, PCIe, USB
    form_factor: str | None = None  # 2.5", M.2, U.2

    # Надежность
    endurance: int | None = None  # TBW для SSD
    smart_status: bool | None = None


@dataclass
class NetworkInterface:
    """Сетевой интерфейс"""

    id: str
    name: str
    mac_address: MAC
    speed: int  # Mbps
    interface_type: str  # Ethernet, WiFi, Cellular
    role: list[NetworkRole]
    address: list[NetworkAddress] | None
    status: StatusNI

    duplex: str | None = None  # full, half
    mtu: int = 1500
    state: str = "up"  # up, down
    driver: str | None = None  # Драйвер интерфейса

    vlan_id: int | None = None
    vlan_native: bool = False

    def get_ip_addresses(self) -> list[IPv4 | IPv6]:
        """Получить все IP адреса интерфейса"""
        return [addr for addr in self.address if isinstance(addr, (IPv4, IPv6))]

    def get_ipv4_addresses(self) -> list[IPv4]:
        """Получить IPv4 адреса"""
        return [addr for addr in self.address if isinstance(addr, IPv4)]

    def get_ipv6_addresses(self) -> list[IPv6]:
        """Получить IPv6 адреса"""
        return [addr for addr in self.address if isinstance(addr, IPv6)]


@dataclass
class GPU:
    """Графический процессор"""

    id: str
    name: str
    model: str
    memory: int  # Mb

    # Производительность
    cores: int | None = None
    clock_speed: int | None = None  # MHz
    memory_clock: int | None = None  # MHz
    memory_type: str | None = None  # GDDR5, GDDR6, HBM2

    # Интерфейс
    bus: str | None = None  # PCIe x16
    tdp: int | None = None  # Thermal Design Power


@dataclass
class PowerSupply:
    """Блок питания. На всякий случай"""

    id: str
    name: str
    wattage: int  # Ватты
    efficiency: str | None = None  # 80 Plus rating
    modular: bool = False  # Модульный кабели


@dataclass
class TemperatureSensor:
    """Датчик температуры. На всякий случай"""

    id: str
    name: str
    current_temp: float  # °C
    max_temp: float | None = None  # °C
    critical_temp: float | None = None  # °C
    location: str | None = None  # CPU, GPU, System
