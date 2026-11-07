
from datetime import date


def introducir_fechas():
    print("Búsqueda de vehículos - AutoRent")
    print("Introduce las fechas en formato AAAA-MM-DD")

    fecha_inicio = input("Fecha de inicio: ")
    fecha_fin = input("Fecha de fin: ")

    return fecha_inicio, fecha_fin


if __name__ == "__main__":
    inicio, fin = introducir_fechas()
    print(f"Fecha de inicio: {inicio}")
    print(f"Fecha de fin: {fin}")
