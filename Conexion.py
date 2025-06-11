import csv
import math
from Nodo import Nodo 
from medios_transporte import transportes, MedioTransporte, tipo_conexion

class Conexion():
    conexiones = []
    def __init__(self, origen:Nodo, destino:Nodo, modo, distancia, restriccion, valor_restriccion=None):
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
                #if fila[0] not in Nodo.nodos.keys() or fila[1] not in Nodo.nodos.keys():
                #    raise ValueError("El origen o el destino no estan entre los nodos")
                origen_nombre = fila[0].strip()
                destino_nombre = fila[1].strip()
                if origen_nombre not in Nodo.nodos or destino_nombre not in Nodo.nodos:
                    raise ValueError("El origen o el destino no están entre los nodos")
                
                
                if  fila[2].lower() not in tipo_conexion:
                    raise ValueError("El modo no esta entre los modos posibles")
                
                
                #if fila[0]==fila[1]:
                #    raise ValueError("El origen y el destino no pueden ser el mismo")
                if origen_nombre == destino_nombre:
                    raise ValueError("El origen y el destino no pueden ser el mismo")
                
                
                #validar que no exista ya ese camino
                origen = Nodo.nodos[origen_nombre]
                destino = Nodo.nodos[destino_nombre]
                assert isinstance(origen, Nodo) #tratando de encontrar el error. 
                assert isinstance(destino, Nodo)

                
                modo= fila[2].strip().lower()
                
                if modo == "ferroviaria": #dejar ferroviariA xq en el archivo de conexiones es femenino
                    modo = transportes['ferroviario']
                elif modo == "automotor":
                    modo = transportes['automotor']
                elif modo == "aerea": #dejar aereA xq en el csv de conexiones es femenino
                    modo = transportes['aereo'] 
                elif modo == "fluvial":
                    modo = transportes['fluvial']
                
                distancia = float(fila[3].strip())    
                restriccion = fila[4]
                valor_restriccion = fila[5]

                Conexion(origen, destino, modo, distancia, restriccion, valor_restriccion)
                

    def calcular_tiempo_conexion(self):
        tiempo_conexion = 0
        transporte = self.modo
        velocidad_transporte = transporte.velocidad_nom_kmh

        if transporte.modo == "aereo":
            prob_mal_tiempo = float(self.valor_restriccion or 0)
            velocidad_transporte = (transporte.vel_mal_clima_kmh)*(prob_mal_tiempo) + (transporte.velocidad_nom_kmh)*(1-prob_mal_tiempo)

        if self.restriccion == 'velocidad_max':
            if self.valor_restriccion:
                vel_max=float(self.valor_restriccion)
        else:
            vel_max=transporte.velocidad_nom_kmh
        vel= min(vel_max, velocidad_transporte)
                
        tiempo_conexion += self.distancia / vel
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