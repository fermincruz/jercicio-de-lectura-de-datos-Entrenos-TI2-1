from collections import namedtuple
import csv
from datetime import datetime

Entreno = namedtuple('Entreno', 
'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta_fichero):
    '''
    Esta función lee un fichero de datos en formato CSV y devuelve una lista
    de tuplas de tipo Entreno.

    Un ejemplo de las líneas del fichero CSV esperado es:
    Andar,12/11/2021 8:14,Sevilla,48,155,3.49,89,N

    Parámetro de entrada:
        ruta_fichero: la ruta del fichero CSV, de tipo str.
    
    Valor devuelto:
        Lista de tuplas de tipo Entreno.
    '''
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        lista_entrenos = []
        for tipo, fechahora, ubicacion, duracion,\
             calorias, distancia, frecuencia, compartido in lector:
             fechahora = parsea_fechahora(fechahora)
             duracion = int(duracion)
             calorias = int(calorias)
             distancia = float(distancia)
             frecuencia = int(frecuencia)
             compartido = parsea_logico(compartido)
             lista_entrenos.append(
                Entreno(tipo, fechahora, ubicacion, duracion,
                         calorias, distancia, frecuencia, compartido)
             )
        return lista_entrenos

def parsea_fechahora(cadena):
    '''
    Recibe una cadena con el formato "dia/mes/año hora:minutos",
    y devuelve un objeto datetime con esa información
    '''
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M")

def parsea_logico(cadena):
    '''
    Recibe una cadena con 'S' o 'N', y devuelve True
    en el primero caso, y False en el segundo caso.
    '''
    if cadena == 'S':
        return True
    else:
        return False