from Nodo import Nodo
import csv

class Solicitud:
    solicitudes = {}
    def __init__(self, id_carga, peso_kg, origen, destino):
        self.id_carga = id_carga
        self.peso_kg = peso_kg
        self.origen = origen
        self.destino = destino
        Solicitud.solicitudes[self.id_carga] = self
        
        
    @classmethod
    def asignar_solicitudes(cls, archivo_solicitud):
        with open(archivo_solicitud, 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            header = next(lector, None)

            header_esperado = [ "id_carga","peso_kg","origen","destino" ]
            if header is None:
                raise ValueError("El archivo esta vachio o no tiene header")
            header = [h.strip().lower() for h in header]
            if header != header_esperado:
                raise ValueError(f"El header tiene que ser exactamente:\n {','.join(header_esperado)}")

            for fila in lector:
                if len(fila) < 4:
                    raise ValueError("Falta información en la fila del archivo de pedidos.")
                id_carga = fila[0].strip()
                try:
                    peso_kg = int(fila[1].strip())
                except (ValueError, TypeError):
                    raise ValueError(f"Uno de los pesos_kg no se pudo transformar a entero.")
                if peso_kg <= 0:
                    raise ValueError(f"El peso_kg no puede ser negativo o cero (ID: {id_carga}).")
                origen = fila[2].strip()
                destino = fila[3].strip()
                
                if id_carga in cls.solicitudes:
                    raise ValueError(f"ID de carga duplicado: {id_carga}")

                if origen not in Nodo.nodos or destino not in Nodo.nodos:
                    raise ValueError(f"Origen o destino inválido: {origen}, {destino}")

                Solicitud(id_carga, peso_kg, origen, destino)

