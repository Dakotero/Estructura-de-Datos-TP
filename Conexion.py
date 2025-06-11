import csv
import math
from Nodo import Nodo 
from medios_transporte import MedioTransporte, transportes

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
                
                if modo == "ferroviario":
                    modo = transportes['ferroviario']
                elif modo == "automotor":
                    modo = transportes['automotor']
                elif modo == "aereo":
                    modo = transportes['aereo']
                elif modo == "fluvial":
                    modo = transportes['fluvial']
                    
                restriccion = fila[3]
                valor_restriccion = fila[4]

                Conexion(origen, destino, modo, restriccion, valor_restriccion)
                

    def calcular_tiempo_conexion(self):
        tiempo_conexion = 0
        transporte = self.modo
        velocidad_transporte = transporte.velocidad_nom_kmh

        if transporte == "aereo":
            prob_mal_tiempo = float(self.valor_restriccion or 0)
            velocidad_transporte = (transporte.vel_mal_clima_kmh)*(prob_mal_tiempo) + (transporte.velocidad_nom_kmh)*(1-prob_mal_tiempo)

        if self.restriccion == 'velocidad_max':
            vel_max=float(self.valor_restriccion)
        else:
            vel_max=transporte.velocidad_nom_kmh
            vel= min(vel_max, velocidad_transporte)
                
        tiempo_conexion += self.distancia_km / vel
        return tiempo_conexion 
    
            
    def calcular_costo_conexion(self, solicitud):
        transporte = self.modo
        cantidad = math.ceil(solicitud.peso_kg / transporte.capacidad_kg)
        costo_conexion = 0
        if transporte.modo == "automotor":
            costo_conexion += transporte.costo_fijo*cantidad
            costo_conexion += (transporte.costo_km * self.distancia)*cantidad
            costo_conexion += (transporte.costokg(solicitud.peso_kg) * solicitud.peso_kg)*cantidad

        elif transporte.modo == "ferroviario":
            costo_conexion += transporte.costo_fijo*cantidad
            tramo_largo = self.distancia >= 200*cantidad
            costo_conexion += (transporte.costokm(tramo_largo) * self.distancia)*cantidad
            costo_conexion += (transporte.costo_kg * solicitud.peso_kg)*cantidad
                
        elif transporte.modo == "fluvial":
            tipo_tramo = self.valor_restriccion
            costo_fijo_real = transporte.costofijo(tasa_maritima=(tipo_tramo == "maritimo"))
            costo_conexion += costo_fijo_real*cantidad
            costo_conexion += (transporte.costo_km * self.distancia)*cantidad
            costo_conexion += (transporte.costo_kg * solicitud.peso_kg)*cantidad
            
        elif transporte.modo == "aereo":
            costo_conexion += transporte.costo_fijo*cantidad
            costo_conexion += (transporte.costo_km * self.distancia)*cantidad
            costo_conexion += (transporte.costo_kg * solicitud.peso_kg)*cantidad
        return costo_conexion
        


'''                
archivo = 'conexiones.csv'
Conexion.asignar_conexion(archivo)

for c in Conexion.conexiones:
lista_
    print(f"{c.origen} -> {c.destino} ({c.modo}), distancia: {c.distancia}, restricción: {c.restriccion}, valor: {c.valor_restriccion}")

'''