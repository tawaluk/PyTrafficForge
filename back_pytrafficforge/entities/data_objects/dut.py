"""Абстракция обьекта тестирования"""

from enum import Enum


class DUTState(Enum):
    """Статусы обьекта тестирования"""

    UNKNOWN = "unknown"
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    READY = "ready"
    TESTING = "testing"
    ERROR = "error"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"


class DUTType(Enum):
    """Тип обьекта тестирования"""

    NETWORK_DEVICE = "network_device"
    SERVER = "server"
    APPLICATION = "application"
    DATABASE = "database"
    API = "api"
    CUSTOM = "custom"
