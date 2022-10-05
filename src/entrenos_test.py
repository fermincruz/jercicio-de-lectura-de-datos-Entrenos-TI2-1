from entrenos import *

datos = lee_entrenos("data/entrenos.csv")

print(f"Leídos {len(datos)} registros.")

print("\nMostrando los primeros 3 registros:")
print(datos[:3])

print("\nMostrando los últimos 3 registros:")
print(datos[-3:])