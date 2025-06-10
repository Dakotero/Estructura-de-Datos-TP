class MedioTransporte:
    modos=["aereo","maritimo","ferroviario","automotor"]
    def __init__(self, nombre, modo, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg):
        if modo not in MedioTransporte.modos:
            raise ValueError('Modo no permitido')
        #"""
        #Clase base para medios de transporte.

        #:param nombre: Nombre del vehiculo (ej: "Avion A1", "Barcaza B1", etc.)
        #:param modo: Modo de transporte (aereo, maritimo, ferroviario, automotor)
        ##:param velocidad_nom_kmh: Velocidad nominal en km/h
       #:param capacidad_kg: Capacidad de carga maxima en kg
        #:param costo_fijo: Costo fijo por tramo
       #:param costo_km: Costo por kilometro recorrido
        #:param costo_kg: Costo por kilogramo transportado
        #"""
        self.nombre = nombre
        self.modo = modo
        self.velocidad_nom_kmh = velocidad_nom_kmh
        self.capacidad_kg = capacidad_kg
        self.costo_fijo = costo_fijo
        self.costo_km = costo_km
        self.costo_kg = costo_kg
        
        
class Aereo(MedioTransporte):
    def __init__(self, nombre, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg, vel_mal_clima_kmh):
        super().__init__(nombre, "aereo", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        self.vel_mal_clima_kmh=vel_mal_clima_kmh


class Maritimo(MedioTransporte):
    def __init__(self, nombre, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg, tasa_maritima):
        super().__init__(nombre, "maritimo", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        self.tasa_maritima=tasa_maritima


class Ferroviario(MedioTransporte):
    def __init__(self, nombre, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg, costo_tramo_largo):
        super().__init__(nombre, "ferroviario", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        self.costo_tramo_largo=costo_tramo_largo
        
        

class Automotor(MedioTransporte):
    def __init__(self, nombre, velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg, costo_carga_alta):
        super().__init__(nombre, "automotor", velocidad_nom_kmh, capacidad_kg, costo_fijo, costo_km, costo_kg)
        self.costo_carga_alta=costo_carga_alta
        
        
