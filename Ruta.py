import math

        
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

class Ruta():
    lista_rutas = []
    def __init__(self, transporte, solicitud, conexiones): #solicitud tiene que ser el objeto (instancia) de solicitud, conexiones es una lista de objetos conexion
        self.transporte = transporte
        self.solicitud = solicitud
        self.conexiones = conexiones
        self.costo_total = 0
        self.tiempo_total = 0
        
        
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