from collections import namedtuple
import csv
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta_fichero):
    '''
    Lee un fichero de datos CSV con información sobre entrenamientos.

    Parámetros:
        - ruta_fichero: la ruta del fichero CSV, de tipo str.
    
    Valor devolución:
        - Una lista de tuplas de tipo Entreno, con la información del fichero.
    '''
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) # Lo hacemos cuando el CSV tiene cabecera
        lista_entrenos = []
        for tipo, fechahora, ubicacion, duracion, calorias, distancia\
            , frecuencia, compartido in lector:
            # Conversión de tipos
            fechahora = parsea_fechahora(fechahora)
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = parsea_logico(compartido)
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            lista_entrenos.append(tupla)
        return lista_entrenos

def parsea_fechahora(cadena):
    '''
    Recibe una cadena con una fecha con el siguiente formato:
        dia/mes/año hora:minutos
    
    Y devuelve un objeto datetime con la fecha y hora indicadas en la cadena.
    '''
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M")


def parsea_logico(cadena):
    '''
    Recibe una cadena que puede ser "S" o "N", y devuelve
    True en el primer caso y False en el segundo.
    '''
    if cadena == "S":
        return True
    else:
        return False