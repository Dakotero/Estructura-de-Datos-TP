import csv
from Nodo import Nodo 
from medios_transporte import MedioTransporte

'''
for ruta in rutas:
    for conexion in ruta:
        if conexion[0] == 'ferroviario'
        
                if modo == "ferroviario":
                    transporte = MedioTransporte.ferroviario
                elif modo == "automotor":
                    transporte = MedioTransporte.automotor
                elif modo == "aereo":
                    transporte = MedioTransporte.aereo
                elif modo == "fluvial":
                    transporte = MedioTransporte.fluvial
                else:

for conexion in Conexion.conexiones:
if conexion.modo 
    
'''

class Conexion():
    conexiones = []
    def __init__(self, origen, destino, modo, distancia, restriccion, valor_restriccion=None):
        self.origen = origen
        self.destino = destino
        self.modo = modo
        self.distancia=distancia 
        self.restriccion = restriccion   
        self.valor_restriccion= valor_restriccion
        
        self.conexiones.append(self)

    @classmethod
    def asignar_conexion(cls,archivo):
        # Leer el archivo CSV
        with open(archivo, 'r') as f:
            lector = csv.reader(f)
            next(lector)

            for fila in lector:
                if fila[0] not in Nodo.nodos.keys() or fila[1] not in Nodo.nodos.keys():
                    raise ValueError("El origen o el destino no estan entre los nodos")
                if  fila[2].lower() not in MedioTransporte.tipo_conexion:
                    raise ValueError("El modo no esta entre los modos posibles")
                if fila[0]==fila[1]:
                    raise ValueError("El origen y el destino no pueden ser el mismo")
                #validar que no exista ya ese camino
                origen = Nodo.nodos[fila[0]]
                destino = Nodo.nodos[fila[1]]
                modo= fila[2].lower()
                restriccion = fila[3]
                valor_restriccion = fila[4]
                Conexion(origen, destino, modo, restriccion, valor_restriccion)

'''                
archivo = 'conexiones.csv'
Conexion.asignar_conexion(archivo)

for c in Conexion.conexiones:
lista_
    print(f"{c.origen} -> {c.destino} ({c.modo}), distancia: {c.distancia}, restricción: {c.restriccion}, valor: {c.valor_restriccion}")

'''