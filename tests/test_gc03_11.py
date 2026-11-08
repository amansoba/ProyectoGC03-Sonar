
import io
import unittest
from contextlib import redirect_stdout
from datetime import date
from unittest.mock import patch

from fechas import RangoFechas
from campos_fecha import introducir_fechas


class TestGC0311(unittest.TestCase):

    def test_rango_correcto(self):
        rango = RangoFechas(date(2026, 11, 10), date(2026, 11, 15))
        valido, mensaje = rango.validar()

        self.assertTrue(valido)
        self.assertEqual(mensaje, "El rango de fechas es válido.")

    def test_fechas_iguales(self):
        rango = RangoFechas(date(2026, 11, 10), date(2026, 11, 10))
        valido, _ = rango.validar()

        self.assertTrue(valido)

    def test_fecha_inicio_ausente(self):
        rango = RangoFechas(None, date(2026, 11, 15))
        valido, mensaje = rango.validar()

        self.assertFalse(valido)
        self.assertIn("fecha de inicio", mensaje)

    def test_fecha_fin_ausente(self):
        rango = RangoFechas(date(2026, 11, 10), None)
        valido, mensaje = rango.validar()

        self.assertFalse(valido)
        self.assertIn("fecha de fin", mensaje)

    def test_fecha_inicio_invalida(self):
        rango = RangoFechas("fecha incorrecta", date(2026, 11, 15))
        valido, mensaje = rango.validar()

        self.assertFalse(valido)
        self.assertIn("no es válida", mensaje)

    def test_fecha_fin_invalida(self):
        rango = RangoFechas(date(2026, 11, 10), "fecha incorrecta")
        valido, mensaje = rango.validar()

        self.assertFalse(valido)
        self.assertIn("no es válida", mensaje)

    def test_fecha_fin_anterior_a_inicio(self):
        rango = RangoFechas(date(2026, 11, 15), date(2026, 11, 10))
        valido, mensaje = rango.validar()

        self.assertFalse(valido)
        self.assertIn("no puede ser anterior", mensaje)

    def test_interfaz_muestra_error_de_formato(self):
        entradas = [
            "fecha incorrecta", "2026-11-15",
            "2026-11-10", "2026-11-15"
        ]

        salida = io.StringIO()

        with patch("builtins.input", side_effect=entradas):
            with redirect_stdout(salida):
                rango = introducir_fechas()

        self.assertIn("Error: la fecha de inicio", salida.getvalue())
        self.assertEqual(rango.fecha_inicio, date(2026, 11, 10))

    def test_interfaz_muestra_error_de_fecha_fin(self):
        entradas = [
            "2026-11-10", "fecha incorrecta",
            "2026-11-10", "2026-11-15"
        ]

        salida = io.StringIO()

        with patch("builtins.input", side_effect=entradas):
            with redirect_stdout(salida):
                rango = introducir_fechas()

        self.assertIn("Error: la fecha de fin", salida.getvalue())
        self.assertEqual(rango.fecha_fin, date(2026, 11, 15))

    def test_interfaz_corrige_rango_invertido(self):
        entradas = [
            "2026-11-15", "2026-11-10",
            "2026-11-10", "2026-11-15"
        ]

        salida = io.StringIO()

        with patch("builtins.input", side_effect=entradas):
            with redirect_stdout(salida):
                rango = introducir_fechas()

        self.assertIn("no puede ser anterior", salida.getvalue())
        self.assertIn("Vuelve a introducir las fechas", salida.getvalue())
        self.assertEqual(rango.fecha_inicio, date(2026, 11, 10))
        self.assertEqual(rango.fecha_fin, date(2026, 11, 15))


if __name__ == "__main__":
    unittest.main()
