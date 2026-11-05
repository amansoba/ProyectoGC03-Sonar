
import unittest
from datetime import date
from time import perf_counter

from disponibilidad import Vehiculo, Reserva, consultar_vehiculos_disponibles
from fechas import RangoFechas


class TestConsultaDisponibilidadRendimiento(unittest.TestCase):

    def setUp(self):
        self.vehiculo = Vehiculo(
            "VEH-01", "Toyota", "Corolla", "Turismo", "disponible"
        )
        self.rango = RangoFechas(
            date(2026, 11, 10), date(2026, 11, 14)
        )

    def test_busqueda_sin_vehiculos(self):
        resultado = consultar_vehiculos_disponibles(
            [], [], self.rango
        )
        self.assertEqual(resultado, [])

    def test_vehiculo_disponible(self):
        resultado = consultar_vehiculos_disponibles(
            [self.vehiculo], [], self.rango
        )
        self.assertEqual(resultado, [self.vehiculo])

    def test_excluir_reserva_solapada(self):
        reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 12),
                date(2026, 11, 16),
                "activa"
            )
        ]
        resultado = consultar_vehiculos_disponibles(
            [self.vehiculo], reservas, self.rango
        )
        self.assertEqual(resultado, [])

    def test_excluir_vehiculo_no_disponible(self):
        for estado in ("inactivo", "mantenimiento"):
            with self.subTest(estado=estado):
                self.vehiculo.estado = estado
                resultado = consultar_vehiculos_disponibles(
                    [self.vehiculo], [], self.rango
                )
                self.assertEqual(resultado, [])

    def test_reserva_fuera_de_fechas(self):
        reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 20),
                date(2026, 11, 25),
                "activa"
            )
        ]
        resultado = consultar_vehiculos_disponibles(
            [self.vehiculo], reservas, self.rango
        )
        self.assertEqual(resultado, [self.vehiculo])

    def test_reserva_cancelada(self):
        reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 12),
                date(2026, 11, 16),
                "cancelada"
            )
        ]
        resultado = consultar_vehiculos_disponibles(
            [self.vehiculo], reservas, self.rango
        )
        self.assertEqual(resultado, [self.vehiculo])

    def test_reserva_de_otro_vehiculo(self):
        reservas = [
            Reserva(
                "VEH-02",
                date(2026, 11, 12),
                date(2026, 11, 16),
                "activa"
            )
        ]
        resultado = consultar_vehiculos_disponibles(
            [self.vehiculo], reservas, self.rango
        )
        self.assertEqual(resultado, [self.vehiculo])

    def test_rango_fechas_invalido(self):
        rango = RangoFechas(
            date(2026, 11, 15),
            date(2026, 11, 10)
        )
        with self.assertRaises(ValueError):
            consultar_vehiculos_disponibles(
                [self.vehiculo], [], rango
            )

    def test_tiempo_respuesta_inferior_dos_segundos(self):
        vehiculos = [
            Vehiculo(
                f"VEH-{i:03d}",
                "Seat",
                "Ibiza",
                "Turismo",
                "inactivo" if i % 3 == 0 else "disponible"
            )
            for i in range(300)
        ]

        reservas = [
            Reserva(
                f"VEH-{i:03d}",
                date(2026, 11, 11),
                date(2026, 11, 12),
                "activa"
            )
            for i in range(300)
            if i % 3 == 1
        ]

        inicio = perf_counter()

        resultado = consultar_vehiculos_disponibles(
            vehiculos, reservas, self.rango
        )

        tiempo = perf_counter() - inicio

        self.assertEqual(len(resultado), 100)
        self.assertTrue(
            all(int(v.identificador.split("-")[1]) % 3 == 2
                for v in resultado)
        )
        self.assertLess(tiempo, 2.0)


if __name__ == "__main__":
    unittest.main()
