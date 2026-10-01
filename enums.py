from enum import Enum

class EstadoOrden (Enum):
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    EN_ALQUILER = "En alquiler"
    FUERA_DE_SERVICIO = "Fuera de servicio"

class EstadoVehiculo (Enum):
    SOLICITADA = "Solicitada"
    CONFIRMADA = "Confirmada"
    EN_CURSO = "En curso"
    FINALIZADA = "Finalizada"
    CANCELADA = "Cancelada"