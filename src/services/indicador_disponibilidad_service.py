"""Servicio para calcular el estado visual y color distintivo de disponibilidad de un vehículo."""

from typing import Dict, Any
from src.models.indicador_disponibilidad import IndicadorDisponibilidad

_ESTADOS_CONFIG = {
    "DISPONIBLE": {
        "color": "VERDE",
        "mensaje": "Vehículo disponible para reserva inmediata"
    },
    "RESERVADO": {
        "color": "ROJO",
        "mensaje": "Vehículo no disponible (reservado temporalmente)"
    },
    "MANTENIMIENTO": {
        "color": "AMARILLO",
        "mensaje": "Vehículo en revisión técnica"
    }
}

def obtener_indicador_disponibilidad(id_vehiculo: str, estado_actual: str) -> Dict[str, Any]:
    """Determina la representación visual y el distintivo del vehículo según su estado."""
    if not id_vehiculo:
        raise ValueError("El identificador del vehículo es obligatorio.")

    estado_norm = estado_actual.strip().upper() if estado_actual else "DISPONIBLE"
    config = _ESTADOS_CONFIG.get(estado_norm, {
        "color": "GRIS",
        "mensaje": f"Estado desconocido: {estado_norm}"
    })

    indicador = IndicadorDisponibilidad(
        id_vehiculo=id_vehiculo.strip().upper(),
        estado=estado_norm,
        color_distintivo=config["color"],
        mensaje_usuario=config["mensaje"]
    )
    return indicador.to_dict()

if __name__ == "__main__":
    print("Probando indicador de disponibilidad:")
    print(obtener_indicador_disponibilidad("VEH-01", "DISPONIBLE"))