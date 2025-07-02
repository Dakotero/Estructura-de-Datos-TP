from Conexion import Conexion
from Nodo import Nodo
from medios_transporte import *

class Red_de_Conexiones:
    def __init__(self, vehiculo):

        self.vehiculo = vehiculo 
        self.caminos = {}

        for conexion in Conexion.conexiones:

            if conexion.modo.modo == self.vehiculo.modo:
                self.agregar_conexion(conexion.origen, conexion.destino)

    @staticmethod
    def modo_str(modo): 
        return modo.modo if hasattr(modo, "modo") else str(modo).lower().strip()

    def agregar_conexion(self, nodo1, nodo2):
        try:
            if nodo1 not in self.caminos:
                self.caminos[nodo1] = []
            if nodo2 not in self.caminos:
                self.caminos[nodo2] = []
            if nodo2 not in self.caminos[nodo1]:
                self.caminos[nodo1].append(nodo2)
            if nodo1 not in self.caminos[nodo2]:
                self.caminos[nodo2].append(nodo1)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Hubo un problema en el optimizador, creando las tuplas de nodos y sus vecinos. \nMas detalles: {e}")

###########################################

    def buscar_caminos(self, inicio, fin):
        try:
            pila = [(inicio, [inicio])]
            caminos_finales = []

            while pila:
                nodo_actual, camino = pila.pop()

                if nodo_actual == fin:
                    caminos_finales.append(camino)
                else:
                    for conexion in self.caminos.get(nodo_actual, []): 
                        if conexion not in camino:
                            pila.append((conexion, camino + [conexion]))
        except (ValueError, TypeError) as e:
            raise ValueError(f"Hubo un problema en el optimizador, buscando todos los caminos posibles. \nMas detalles: {e}")

        return caminos_finales

###########################################

def crear_redes_de_conexiones(vehiculos):
    redes = []
    for v in vehiculos:
        red = Red_de_Conexiones(v)
        redes.append(red)
    return redes

###########################################

def super_optimizador(vehiculos, inicio, fin):

    try:

        if inicio not in Nodo.nodos.values() or fin not in Nodo.nodos.values():
            print(f"[ERROR] El nodo de inicio o fin no existe.")
            return []

        tupla_modo_conexiones = []
        tupla_modo_nodos = []

        for v in vehiculos:
            red = Red_de_Conexiones(v) 
            if inicio not in red.caminos or fin not in red.caminos:
                continue

            caminos = red.buscar_caminos(inicio, fin)
            if not caminos:
                print(f"[INFO] No se encontraron caminos entre {inicio.nombre} y {fin.nombre} para el medio: {v.modo}")
            else:
                for c in caminos:
                    conexiones_del_camino = []
                    for i in range(len(c) - 1):
                        origen = c[i]
                        destino = c[i + 1]
                        conexion = next(
                            (con for con in Conexion.conexiones if
                            ((con.origen == origen and con.destino == destino) or
                            (con.origen == destino and con.destino == origen)) and
                            Red_de_Conexiones.modo_str(con.modo) == Red_de_Conexiones.modo_str(v.modo)),
                            None
                        )

                        if conexion:
                            conexiones_del_camino.append(conexion)
                        else:
                            print(f"[ADVERTENCIA] No se encontró conexión entre {origen} y {destino} para {v.modo}")

                    tupla_modo_conexiones.append((v.modo, conexiones_del_camino))
                    tupla_modo_nodos.append((v.modo, c))
    except (ValueError, TypeError) as e:
        raise ValueError(f"Hubo un problema corriendo el super_optimizador. Revisar datos \nMas detalles: {e}")

    return tupla_modo_conexiones, tupla_modo_nodos
