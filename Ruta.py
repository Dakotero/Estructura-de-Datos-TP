
import math
from Conexion import Conexion
from Solicitud import Solicitud

class Ruta():
    rutas = [] #no se para que guardamos esta lista todavia, vemos si la sacamos a futuro
    def __init__(self, transporte, solicitud, conexiones): #solicitud tiene que ser el objeto (instancia) de solicitud, conexiones es una lista de objetos conexion
        self.transporte = transporte
        self.solicitud = solicitud
        self.conexiones = conexiones
        self.costo_total = 0
        self.tiempo_total = 0
        
    def __str__(self):

        if not self.conexiones:
            return f"por {self.transporte.modo} no existe"

        nodos = [self.conexiones[0].origen.nombre]  # arranco con el primer origen
        for conexion in self.conexiones:
            nodos.append(conexion.destino.nombre)  # agrego cada destino en orden

        texto = f"por {self.transporte.modo}:\n  " + " → ".join(nodos)
        return texto

    def __repr__(self):
        return self.__str__()
        
        
    def calcular_tiempo_ruta(self):
        tiempo_total = 0
        for conexion in self.conexiones:
            tiempo_total += conexion.calcular_tiempo_conexion()
        return tiempo_total
                
    def calcular_costo_ruta(self, solicitud):
        costo_total = 0
        for conexion in self.conexiones:
            costo_total += conexion.calcular_costo_conexion(solicitud)
        return costo_total





'''
        
for conexion in 
                if modo == "ferroviario":
                    transporte = MedioTransporte.ferroviario
                elif modo == "automotor":
                    transporte = MedioTransporte.automotor
                elif modo == "aereo":
                    transporte = MedioTransporte.aereo
                elif modo == "fluvial":
                    transporte = MedioTransporte.fluvial
                else:
                    continue
            
transportes = {"ferroviario": ferroviario, "automotor": automotor, "aereo": aereo,"fluvial": fluvial}    
'''
'''
for solicitud in Solicitud.solicitudes.values():
    for ruta in rutas:
        tiempo_total = 0
        costo_total = 0
        for conexion in ruta[1]:
            tiempo_total += Conexion.calcular_tiempo_conexion(conexion)
            costo_total += Conexion.calcular_costo_conexion(conexion, solicitud)
 '''
'''           
for solicitud in Solicitud.solicitudes.values():
    for ruta in rutas:
        tiempo_total = 0
        for conexion in ruta[1]:
            tiempo_total += Conexion.calcular_tiempo_conexion(conexion)
            

for solicitud in Solicitud.solicitudes.values():
    for ruta in rutas:
        costo_total = 0
        for conexion in ruta[1]:
            costo_total += Conexion.calcular_costo_conexion(conexion, solicitud)

def calcular_tiempo_ruta(self):
    tiempo_total = 0
    for conexion in self.conexiones:
            tiempo_total += Conexion.calcular_tiempo_conexion(conexion)
            
def calcular_costo_ruta(self, solicitud):
    costo_total = 0
    for conexion in self.conexiones:
        costo_total += Conexion.calcular_costo_conexion(conexion, solicitud)


for ruta in rutas:
    if ruta[0] == 'ferroviario':
        transporte = transportes['ferroviario']
    elif ruta[0] == 'automotor':
        transporte = transportes['automotor']
    elif ruta[0] == 'aereo':
        transporte = transportes['aereo']
    elif ruta[0] == 'fluvial':
        transporte = transportes['fluvial']
    
    for conexion in ruta[1]:
        
        

    for conexion in conexion[1]:
if conexion.modo 
    # [
#     ('automotor', [Conexion(A→B), Conexion(B→C)]),
#     ('ferroviario', [Conexion(A→C)]),



#     


    '''   
'''
    def calcular_tiempo_ruta(self): #transporte tiene que ser una de las 4 instancias de transporte
                                            #ruta tiene que ser una lista de objetos
        tiempo_total = 0

        for conexion in self.conexiones:
            velocidad_transporte = self.transporte.velocidad_nom_kmh

            if transporte.modo == "aereo":
                prob_mal_tiempo = float(conexion.valor_restriccion or 0)
                velocidad_transporte = (transporte.vel_mal_clima_kmh)*(prob_mal_tiempo) + (transporte.velocidad_nom_kmh)*(1-prob_mal_tiempo)

            if conexion.restriccion == 'velocidad_max':
                vel_max=float(conexion.valor_restriccion)
            else:
                vel_max=transporte.velocidad_nom_kmh
            vel= min(vel_max, velocidad_transporte)
                
            tiempo_total += conexion.distancia_km / vel
        return tiempo_total  
        
    def calcular_costo_ruta(self):
        for conexion in self.conexiones:
            cantidad = math.ceil(self.solicitud.peso_kg / transporte.capacidad_kg)
            if transporte.modo == "automotor":
                costo_total += transporte.costo_fijo*cantidad
                costo_total += (transporte.costo_km * conexion.distancia)*cantidad
                costo_total += (transporte.costokg(self.solicitud.peso_kg) * self.solicitud.peso_kg)*cantidad

            elif transporte.modo == "ferroviario":
                costo_total += transporte.costo_fijo*cantidad
                tramo_largo = conexion.distancia >= 200*cantidad
                costo_total += (transporte.costokm(tramo_largo) * conexion.distancia)*cantidad
                costo_total += (transporte.costo_kg * self.solicitud.peso_kg)*cantidad
                
            elif transporte.modo == "fluvial":
                tipo_tramo = conexion.valor_restriccion
                costo_fijo_real = transporte.costofijo(tasa_maritima=(tipo_tramo == "maritimo"))
                costo_total += costo_fijo_real*cantidad
                costo_total += (transporte.costo_km * conexion.distancia)*cantidad
                costo_total += (transporte.costo_kg * self.solicitud.peso_kg)*cantidad
            
            elif transporte.modo == "aereo":
                costo_total += transporte.costo_fijo*cantidad
                costo_total += (transporte.costo_km * conexion.distancia)*cantidad
                costo_total += (transporte.costo_kg * self.solicitud.peso_kg)*cantidad
        return costo_total
        
        '''
        
