from entrenos import *

registros = lee_entrenos("data/entrenos.csv")

print(f"Leídos {len(registros)} registros.")

print("\nMostrando los tres primeros registros:")
print(registros[:3])

print("\nMostrando los tres últimos registros:")
print(registros[-3:])
