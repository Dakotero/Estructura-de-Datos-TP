import csv
import math
from Nodo import Nodo 
from medios_transporte import transportes, tipo_conexion

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
        with open(archivo, 'r') as f:
            lector = csv.reader(f)
            header = next(lector, None)

            header_esperado = [ "origen", "destino", "tipo", "distancia_km", "restriccion", "valor_restriccion" ]
            if header is None:
                raise ValueError("El archivo esta vachio o no tiene header")
            header = [h.strip().lower() for h in header]
            if header != header_esperado:
                raise ValueError(f"El header tiene que ser exactamente:\n {','.join(header_esperado)}")

            for fila in lector:

                origen_nombre = fila[0].strip()
                destino_nombre = fila[1].strip()
                if origen_nombre not in Nodo.nodos or destino_nombre not in Nodo.nodos:
                    raise ValueError("El origen o el destino de una de las conexiones no esta entre los nodos")
                
                
                if  fila[2].lower() not in tipo_conexion:
                    raise ValueError("El modo de transporte no esta entre los modos posibles")
                

                if origen_nombre == destino_nombre:
                    raise ValueError("El origen y el destino no pueden ser el mismo")
                
                
                origen = Nodo.nodos[origen_nombre]
                destino = Nodo.nodos[destino_nombre]
                assert isinstance(origen, Nodo) 
                assert isinstance(destino, Nodo)

                
                modo= fila[2].strip().lower()
                
                if modo == "ferroviaria": 
                    modo = transportes['ferroviario']
                elif modo == "automotor":
                    modo = transportes['automotor']
                elif modo == "aerea": 
                    modo = transportes['aereo'] 
                elif modo == "fluvial":
                    modo = transportes['fluvial']
                else:
                    raise ValueError(f"El modo de transporte '{modo}' no es válido. Debe ser uno de: {', '.join(tipo_conexion)}.")
                
                distancia = float(fila[3].strip())
                if distancia <= 0:
                    raise ValueError(f"La distancia debe ser mayor a cero (origen: {origen_nombre}, destino: {destino_nombre}).")
                restriccion = fila[4]
                valor_restriccion = fila[5]
                if restriccion == "prob_mal_tiempo":
                    try:
                        prob = float(valor_restriccion)
                    except ValueError:
                        raise ValueError(f"El valor de restricción para 'prob_mal_tiempo' debe ser numérico (origen: {origen_nombre}, destino: {destino_nombre}).")
                    if not (0 <= prob <= 1):
                        raise ValueError(f"La probabilidad de mal tiempo debe estar entre 0 y 1 (origen: {origen_nombre}, destino: {destino_nombre}).")
                elif restriccion == "tipo":
                    es_tipo_valido = valor_restriccion.lower() in ("maritimo", "fluvial")
                    if not es_tipo_valido:
                        raise ValueError(f"El tipo de restricción debe ser 'maritimo' o 'fluvial' (origen: {origen_nombre}, destino: {destino_nombre}).")
                elif valor_restriccion != "":
                    try:
                        numero_restriccion = float(valor_restriccion)
                        if numero_restriccion < 0:
                            raise ValueError(f"El valor de restricción no puede ser negativo (origen: {origen_nombre}, destino: {destino_nombre}).")
                    except ValueError:
                        raise ValueError(f"El valor de restricción debe ser numérico (origen: {origen_nombre}, destino: {destino_nombre}).")






                Conexion(origen, destino, modo, distancia, restriccion, valor_restriccion)
                

    def calcular_tiempo_conexion(self):
        transporte = self.modo
        velocidad_transporte = transporte.velocidad_nom_kmh

        if transporte.modo == "aereo":
            prob_mal_tiempo = float(self.valor_restriccion or 0)
            velocidad_transporte = (
                transporte.vel_mal_clima_kmh * prob_mal_tiempo +
                transporte.velocidad_nom_kmh * (1 - prob_mal_tiempo)
            )
        if self.restriccion == 'velocidad_max' and self.valor_restriccion:
            vel_max = float(self.valor_restriccion)
        else:
            vel_max = transporte.velocidad_nom_kmh
        vel = min(vel_max, velocidad_transporte)

        return self.distancia / vel
    
    def calcular_cantidad(self, solicitud):
        transporte = self.modo
        carga_total = solicitud.peso_kg
        capacidad = transporte.capacidad_kg
        if self.restriccion=='peso_max' and capacidad>int(self.valor_restriccion):
            return(math.ceil(carga_total / int(self.valor_restriccion)))
        else:
            return(math.ceil(carga_total / capacidad))
                
    def calcular_costo_conexion(self, solicitud, cantidad):
        transporte = self.modo
        carga_total = solicitud.peso_kg
        if self.restriccion=='peso_max' and transporte.capacidad_kg>int(self.valor_restriccion):
            capacidad = int(self.valor_restriccion)
        else:
            capacidad = transporte.capacidad_kg
        distancia = self.distancia
        costo_conexion = 0

        if transporte.modo == "automotor":
            cantidad_completa = carga_total // capacidad
            carga_restante = carga_total % capacidad

            for _ in range(cantidad_completa):
                costo_conexion += transporte.costo_fijo
                costo_conexion += transporte.costo_km * distancia

            if carga_restante > 0:
                costo_conexion += transporte.costo_fijo
                costo_conexion += transporte.costo_km * distancia

        elif transporte.modo == "ferroviario":
            tramo_largo = distancia >= 200
            costo_km = transporte.costokm(tramo_largo)
            costo_conexion += transporte.costo_fijo * cantidad
            costo_conexion += costo_km * distancia * cantidad

        elif transporte.modo == "fluvial":
            tipo_tramo = (self.valor_restriccion or "").strip().lower()
            es_maritimo = tipo_tramo == "maritimo"
            costo_fijo_real = transporte.costofijo(tasa_maritima=es_maritimo)

            costo_conexion += costo_fijo_real * cantidad
            costo_conexion += transporte.costo_km * distancia * cantidad

        elif transporte.modo == "aereo":
            costo_conexion += transporte.costo_fijo * cantidad
            costo_conexion += transporte.costo_km * distancia * cantidad

        return costo_conexion

