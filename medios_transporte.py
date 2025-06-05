class MedioTransporte:
    tipo_conexion=['aerea','ferroviaria', 'automotor', 'fluvial']
    modos=["aereo","fluvial","ferroviario","automotor"]
    def __init__(self,modo, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg):
        self.modo = modo
        self.velocidad_nom_kmh = velocidad_nom_kmh
        self.capacidad_kg = capacidad_kg
        self.costo_fijo = costo_fijo
        self.costo_km = costo_km
        self.costo_kg = costo_kg
        
        if self.modo not in self.modos:
            raise ValueError('Modo no permitido')
        
        
class Aereo(MedioTransporte):
    def __init__(self, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg, vel_mal_clima_kmh):
        super().__init__("aereo", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        self.vel_mal_clima_kmh=vel_mal_clima_kmh


class Fluvial(MedioTransporte):
    def __init__(self, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg, tasa_maritima):
        super().__init__("fluvial", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        self.tasa_maritima=tasa_maritima
        
    def costofijo(self, tasa_maritima=False): #para afectar el costo_fijo por tramo. depende de conexion
        if tasa_maritima:
            return self.tasa_maritima
        return self.costo_fijo


class Ferroviario(MedioTransporte):
    def __init__(self, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg, costo_tramo_largo):
        super().__init__( "ferroviario", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        self.costo_tramo_largo=costo_tramo_largo
        
    def costokm(self, tramo_largo=False): #para afectar el costo_km. depende de conexion
        if tramo_largo:
            return self.costo_tramo_largo
        return self.costo_km

class Automotor(MedioTransporte):
    def __init__(self, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg):
        super().__init__( "automotor", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        
    def costokg(self, carga_kg): #afecta el costo por kilogramo (costo_kg). depende de solicitud 
        if carga_kg>= 15000:
            return 2
        return 1


aereo = Aereo(600, 5000, 750, 40, 10, 400)
maritimo = Fluvial(40, 100000, 500, 15, 2, 1500)
ferroviario = Ferroviario(100, 150000, 100, 20, 3, 15)
automotor = Automotor(80, 30000, 30, 5, None)


#esto lo puse x las dudas pero sirve xq lo vamos a validar en la Redes de transporte. ignorar
'''for transporte in [aereo, maritimo, ferroviario, automotor]:
    if solicitud.peso_kg <= transporte.capacidad_kg:
        print(f"El transporte {transporte.modo} puede transportar esta solicitud")
'''