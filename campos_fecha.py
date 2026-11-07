
from datetime import date
from fechas import RangoFechas


def introducir_fechas():
    print("Búsqueda de vehículos - AutoRent")
    print("Introduce las fechas en formato AAAA-MM-DD")

    while True:
        inicio = input("Fecha de inicio: ")
        fin = input("Fecha de fin: ")

        try:
            fecha_inicio = date.fromisoformat(inicio)
        except ValueError:
            print("Error: la fecha de inicio debe tener un formato válido (AAAA-MM-DD).")
            continue

        try:
            fecha_fin = date.fromisoformat(fin)
        except ValueError:
            print("Error: la fecha de fin debe tener un formato válido (AAAA-MM-DD).")
            continue

        rango = RangoFechas(fecha_inicio, fecha_fin)
        valido, mensaje = rango.validar()

        if valido:
            print(mensaje)
            print("Puedes continuar con la búsqueda de vehículos.")
            return rango

        print(f"Error: {mensaje}")
        print("Vuelve a introducir las fechas para corregirlas.")


if __name__ == "__main__":
    introducir_fechas()
