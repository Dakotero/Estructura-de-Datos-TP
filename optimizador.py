from Conexion import Conexion
from Nodo import Nodo
from medios_transporte import *
from itertools import groupby

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
                        nuevo_camino = camino + [conexion]
                        if len(set(nuevo_camino)) == len(nuevo_camino):  # todos los nodos son únicos
                            pila.append((conexion, nuevo_camino))

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

    todos_los_caminos = []
    set_rutas_unicas = set()

    for v in vehiculos:
        red = Red_de_Conexiones(v)

        if inicio not in red.caminos or fin not in red.caminos:
            print(f"\n[INFO] No hay conexion entre {inicio} y {fin} en red de transporte: ({v.modo})")
            continue

        print(f"\n[INFO] Buscando caminos para el medio: ({v.modo})")
        caminos = red.buscar_caminos(inicio, fin)

        if not caminos:
            print(f"[INFO] No se encontraron caminos entre {inicio.nombre} y {fin.nombre} para el medio: {v.modo}")
            continue

        for c in caminos:
            nombres_caminos = [n.nombre for n in c]
            print(f"[RESULTADO - {v.modo}] : {nombres_caminos}")

            conexiones_del_camino = []
            for i in range(len(c) - 1):
                origen = c[i]
                destino = c[i + 1]
                conexion = next(
                    (con for con in Conexion.conexiones if
                     ((con.origen == origen and con.destino == destino) or
                      (con.origen == destino and con.destino == origen)) and
                     con.modo.modo == v.modo),
                    None
                )
                if conexion:
                    conexiones_del_camino.append(conexion)
                else:
                    print(f"[ADVERTENCIA] No se encontró conexión entre {origen} y {destino} para {v.modo}")

            # Verificación final de unicidad (por secuencia de nodos)
            secuencia_nodos = tuple(n.nombre for n in c)
            if secuencia_nodos not in set_rutas_unicas:
                set_rutas_unicas.add(secuencia_nodos)
                todos_los_caminos.append((v, conexiones_del_camino))
            else:
                print(f"[DEBUG] Ruta duplicada detectada: {secuencia_nodos}")

    return todos_los_caminos

# [
#     ('automotor', [Conexion(A→B), Conexion(B→C)]),
#     ('ferroviario', [Conexion(A→C)]),
#     ...
# ]


'''
def super_optimizador(vehiculos, inicio, fin):
    if inicio not in Nodo.nodos.values() or fin not in Nodo.nodos.values():
        print(f"[ERROR] El nodo de inicio o fin no existe.")
        return []

    todos_los_caminos = []
    set_rutas_unicas = set()

    for v in vehiculos:
        red = Red_de_Conexiones(v)

        if inicio not in red.caminos or fin not in red.caminos:
            print(f"\n[INFO] No hay conexión entre {inicio} y {fin} en red de transporte: ({v.modo})")
            continue

        print(f"\n[INFO] Buscando caminos para el medio: ({v.modo})")
        caminos = red.buscar_caminos(inicio, fin)

        for c in caminos:
            # Eliminar nodos consecutivos duplicados (como Buenos_Aires → Buenos_Aires)
            camino_sin_repetidos = [n for n, _ in groupby(c)]

            # Verificar si el camino es único (por secuencia de nodos)
            secuencia_nodos = tuple(n.nombre for n in camino_sin_repetidos)
            if secuencia_nodos in set_rutas_unicas:
                print(f"[DEBUG] Ruta duplicada detectada: {secuencia_nodos}")
                continue
            set_rutas_unicas.add(secuencia_nodos)

            print(f"[OK - {v.modo}] Ruta encontrada: {' → '.join(secuencia_nodos)}")

            conexiones_del_camino = []
            for i in range(len(camino_sin_repetidos) - 1):
                origen = camino_sin_repetidos[i]
                destino = camino_sin_repetidos[i + 1]
                conexion = next(
                    (con for con in Conexion.conexiones if
                     ((con.origen == origen and con.destino == destino) or
                      (con.origen == destino and con.destino == origen)) and
                     con.modo.modo == v.modo),
                    None
                )
                if conexion:
                    conexiones_del_camino.append(conexion)
                else:
                    print(f"[ADVERTENCIA] No se encontró conexión entre {origen} y {destino} para {v.modo}")

            todos_los_caminos.append((v, conexiones_del_camino))
            print(f"[DEBUG] Ruta generada para {v.modo}: {len(conexiones_del_camino)} tramos.")

    return todos_los_caminos
'''