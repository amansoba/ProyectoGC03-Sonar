
from datetime import date

from disponibilidad import Vehiculo, Reserva, consultar_vehiculos_disponibles
from fechas import RangoFechas


vehiculos = [
    Vehiculo("VEH-01", "Toyota", "Corolla", "Turismo", "disponible"),
    Vehiculo("VEH-02", "Seat", "Ibiza", "Turismo", "disponible"),
    Vehiculo("VEH-03", "Renault", "Clio", "Turismo", "mantenimiento"),
    Vehiculo("VEH-04", "Ford", "Focus", "Turismo", "disponible"),
]

reservas = [
    Reserva("VEH-02", date(2026, 11, 12), date(2026, 11, 16), "activa"),
    Reserva("VEH-04", date(2026, 11, 20), date(2026, 11, 25), "activa"),
]

rango = RangoFechas(date(2026, 11, 10), date(2026, 11, 14))


if __name__ == "__main__":
    resultado = consultar_vehiculos_disponibles(vehiculos, reservas, rango)

    identificadores = [vehiculo.identificador for vehiculo in resultado]
    assert identificadores == ["VEH-01", "VEH-04"]

    print("Vehículos disponibles:")
    for vehiculo in resultado:
        print(f"{vehiculo.identificador} - {vehiculo.marca} {vehiculo.modelo}")

    print("Caso de prueba superado.")
