"""Modelo de datos para el indicador visual de disponibilidad en detalle de vehículo."""

class IndicadorDisponibilidad:
    def __init__(self, id_vehiculo: str, estado: str, color_distintivo: str, mensaje_usuario: str):
        self.id_vehiculo = id_vehiculo
        self.estado = estado
        self.color_distintivo = color_distintivo
        self.mensaje_usuario = mensaje_usuario

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "estado": self.estado,
            "color_distintivo": self.color_distintivo,
            "mensaje_usuario": self.mensaje_usuario
        }