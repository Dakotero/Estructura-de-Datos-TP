from Conexion import Conexion
from Nodo import Nodo
from medios_transporte import *

###########################################

# OPTIMIZADOR

# Recibo una LISTA DE OBJETOS CON LOS VEHICULOS (subclases de MetodoTransporte) llamado 'vehiculos'

###########################################

class Red_de_Conexiones:
    def __init__(self, vehiculo):

        self.vehiculo = vehiculo # ACA ESTOY GUARDANDO EL OBJETO ENTERO DE LA SUBCLASE DEL VEHICULO
        # print(red.vehiculo.nombre)  >> "Avion A1"
        self.caminos = {}

# Mas adelante, uso una funcion para
# crear una Red de Conexiones por instancia de clase de vehiculos que existan

###########################################

# Ahora, voy a crear una funcion para agregarle a mi red de conexion, todas las conexiones que son de ese tipo de vehiculo
# Esto lo hago al inicializar la clase Red_de_Conexiones

        for conexion in Conexion.conexiones:
            if conexion.modo == self.vehiculo.modo:                         # Que el vehiculo en la conexion es igual al vehiculo de mi Red
                self.agregar_conexion(conexion.origen, conexion.destino)    # No existe todavia, es la siguiente funcion

###########################################

# Hago la funcion agregar conexion, donde confirmo nada se duplique, y que sea BIDIRECCIONAL

    def agregar_conexion(self, nodo1, nodo2):
        if nodo1 not in self.caminos:
            self.caminos[nodo1] = []
        if nodo2 not in self.caminos:
            self.caminos[nodo2] = []
        if nodo2 not in self.caminos[nodo1]:
            self.caminos[nodo1].append(nodo2)
        if nodo1 not in self.caminos[nodo2]:
            self.caminos[nodo2].append(nodo1)

###########################################

# Ahora, una lista de todos los posibles caminos SIN VALIDAR RESTRICCIONES DE NINGUN TIPO, SOLO POR CAMINO

    def buscar_caminos(self, inicio, fin):
        pila = [(inicio, [inicio])]  # Pila con (nodo_actual, camino_actual)
        caminos_finales = []

        while pila:
            nodo_actual, camino = pila.pop() # Elimino y agarro el ultimo

            if nodo_actual == fin:
                caminos_finales.append(camino)
            else:
                for conexion in self.caminos.get(nodo_actual, []): 
                    if conexion not in camino:
                        pila.append((conexion, camino + [conexion]))

        return caminos_finales

###########################################

def crear_redes_de_conexiones(vehiculos):
    redes = []
    for v in vehiculos:
        red = Red_de_Conexiones(v)
        redes.append(red)
    return redes

# Forma de uso:
# redes = crear_redes_de_conexiones(vehiculos)
# y me devuelve una LISTA DE OBJETOS por CADA RED QUE HICE
# tengo 1 red por vehiculo existente

###########################################

# Y ahora funcion para correr el Optimizador

def super_optimizador(vehiculos, inicio, fin):

    # vehiculos: lista de objetos de subclases de MedioTransporte (cada uno con .modo)
    # inicio, fin: objetos Nodo

    if inicio not in Nodo.nodos.values() or fin not in Nodo.nodos.values():
        print(f"[ERROR] El nodo de inicio o fin no existe.")
        return {}

    todos_los_caminos = {}

    for v in vehiculos: # Lo corro una vez por vehiculo existente
        red = Red_de_Conexiones(v) # Creo la red, al hacer esto, AUTOMATICAMENTE ya completo el diccionario de caminos

        if inicio not in red.caminos or fin not in red.caminos:
            print(f"\n[INFO] No hay conexion entre {inicio} y {fin} en red de transporte: ({v.modo})")
#            print(f"[DEBUG] Caminos para el medio: {v.modo}")
#            for nodo, vecinos in red.caminos.items():
#                print(f"[DEBUG] {nodo.nombre}: {[n.nombre for n in vecinos]}")
            continue

        print(f"\n[INFO] Buscando caminos para el medio: ({v.modo})")
        caminos = red.buscar_caminos(inicio, fin)                      # Tengo en caminos la lista de todas las posiblidades

        if not caminos:
            print(f"[INFO] No se encontraron caminos entre {inicio.nombre} y {fin.nombre} para el medio: ({v.modo})")
        else:
            for c in caminos: # c ES UNA LISTA DE NODOS
                # ENTONCES para conseguir el NOMBRE tengo que recorrer c y sacar el nombre de cada nodo
                nombres_caminos = [nodo.nombre for nodo in c]
                print(f"[RESULTADO] : {nombres_caminos}")

    return todos_los_caminos