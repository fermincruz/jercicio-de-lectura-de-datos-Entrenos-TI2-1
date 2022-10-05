from collections import namedtuple
import csv
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta_fichero):
    '''
    Esta función lee un fichero CSV con datos de entrenamiento, y devuelve
    una lista de tuplas de tipo Entreno.

    Parámetros:
     - ruta_fichero: la ruta del fichero CSV, de tipo str.

    Valor de devolución:
     - lista de tuplas de tipo Entreno.
    '''
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        lista_entrenos = []
        for tipo, fechahora, ubicacion\
            ,duracion, calorias, distancia\
            ,frecuencia, compartido in lector:
                fechahora = parsea_fechahora(fechahora)
                duracion = int(duracion)
                calorias = int(calorias)
                distancia = float(distancia)
                frecuencia = int(frecuencia)
                compartido = parsea_logico(compartido)
                lista_entrenos.append(
                    Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
                )
        return lista_entrenos

def parsea_fechahora(cadena):
    '''
    Recibe una cadena de texto con una fecha y hora con el formato:
        dia/mes/año hora:minutos

    , y devuelve un objeto de tipo datetime con esa información.
    '''
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M")

def parsea_logico(cadena):
    '''
    Recibe una cadena de texto que puede ser 'S' o 'N', devolviendo
    True en el primer caso y False en el segundo.
    '''
    if cadena == 'S':
        return True
    else:
        return False