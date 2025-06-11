from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from Ruta import Ruta
from medios_transporte import *
from optimizador import *




def convertir_a_objetos_ruta(resultados_optimizador, solicitud):
    rutas = []
    for transporte, lista_conexiones in resultados_optimizador:
        nueva_ruta = Ruta(transporte, solicitud, lista_conexiones)
        rutas.append(nueva_ruta)
    return rutas
