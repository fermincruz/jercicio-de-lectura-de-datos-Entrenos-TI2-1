from entrenos import *

datos = lee_entrenos("data/entrenos.csv")
print(f"Se han leído {len(datos)} datos.")

print("\nMostrando los tres primeros registros:")
print(datos[:3])

print("\nMostrando los tres últimos registros:")
print(datos[-3:])



