import csv
from Nodo import Nodo 
from medios_transporte import MedioTransporte


class Conexion():
    conexiones = []
    def __init__(self, origen, destino, modo, distancia,valor_restriccion=None):
        self.origen = origen
        self.destino = destino
        self.modo = modo
        self.distancia=distancia    
        self.valor_restriccion= valor_restriccion
        
        
        self.conexiones.append(self)
        
    # Lista para guardar todas las conexiones

    @classmethod
    def asignar_conexion(cls,archivo):
        # Leer el archivo CSV
        with open(archivo, 'r') as f:
            lector = csv.reader(f)
            next(lector)  # Saltar la cabecera (si la tiene)

            for fila in lector:
                if fila[0] not in Nodo.nodos.keys() or fila[1] not in Nodo.nodos.keys():
                    raise ValueError("El origen o el destino no estan entre los nodos")
                if  fila[2] not in MedioTransporte.modos:
                    raise ValueError("El modo no esta entre los modos posibles")
                if fila[0]==fila[1]:
                    raise ValueError("El origen y el destino no pueden ser el mismo")
                #validar que no exista ya ese camino
                origen = Nodo.nodos[fila[0]]
                destino = Nodo.nodos[fila[1]]
                modo= fila[2]
                valor_restriccion = fila[4]
                Conexion(origen, destino, modo, valor_restriccion)

                
#archivo = 'conexiones.csv'
#Conexion.asignar_conexion(archivo)

#for c in Conexion.conexiones:
#    print(f"{c.origen} -> {c.destino} ({c.modo}), distancia: {c.distancia}, restricción: {c.restriccion}, valor: {c.valor_restriccion}")

