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
#            print(f"[DEBUG] Revisando conexion: {conexion.origen.nombre} -> {conexion.destino.nombre} con modo {type(conexion.modo)}, {conexion.modo}")
#            print(f"Modo {conexion.modo.modo} =?= {self.vehiculo.modo}")
            if conexion.modo.modo == self.vehiculo.modo:
#                print(f"[DEBUG] El vehiculo en la conexion es igual al vehiculo de mi Red")
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
        return []

    tupla_modo_conexiones = []
    tupla_modo_nodos = []

    for v in vehiculos: # Lo corro una vez por vehiculo existente
        red = Red_de_Conexiones(v) # Creo la red, al hacer esto, AUTOMATICAMENTE ya completo el diccionario de caminos

        if inicio not in red.caminos or fin not in red.caminos:
#            print(f"\n[INFO] No hay conexion entre {inicio} y {fin} en red de transporte: ({v.modo})")
#            print(f"[DEBUG] Caminos para el medio: {v.modo}")
#            for nodo, vecinos in red.caminos.items():
#                print(f"[DEBUG] {nodo.nombre}: {[n.nombre for n in vecinos]}")
            continue

#        print(f"\n[INFO] Buscando caminos para el medio: ({v.modo})")
        caminos = red.buscar_caminos(inicio, fin)                      # Tengo en caminos la lista de todas las posiblidades

        if not caminos:
            print(f"[INFO] No se encontraron caminos entre {inicio.nombre} y {fin.nombre} para el medio: {v.modo}")
        else:
            for c in caminos:
                nombres_caminos = [nodo.nombre for nodo in c]
#                print(f"[RESULTADO - {v.modo}] : {nombres_caminos}")

                # Convertir la lista de nodos a lista de conexiones
                conexiones_del_camino = []
                for i in range(len(c) - 1):
                    origen = c[i]
                    destino = c[i + 1]

                    # Buscar la conexión correspondiente
                    conexion = next(
                        (con for con in Conexion.conexiones if
                         ((con.origen == origen and con.destino == destino) or
                          (con.origen == destino and con.destino == origen)) and
                         modo_str(con.modo) == modo_str(v.modo)),
                        None
                    )

                    if conexion:
                        conexiones_del_camino.append(conexion)
                    else:
                        print(f"[ADVERTENCIA] No se encontró conexión entre {origen} y {destino} para {v.modo}")

                tupla_modo_conexiones.append((v.modo, conexiones_del_camino))
                tupla_modo_nodos.append((v.modo, c))

    return tupla_modo_conexiones, tupla_modo_nodos

# [
#     ('automotor', [Conexion(A→B), Conexion(B→C)]),
#     ('ferroviario', [Conexion(A→C)]),
#     ...
# ]

def modo_str(modo): # Pasaba que a veces el modo era un objeto de la clase MedioTransporte y otras veces era un string
    # Y lo estaban cambiando seguido, hago esto para que pare de romperse
    return modo.modo if hasattr(modo, "modo") else str(modo).lower().strip()
