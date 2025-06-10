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
            next(lector)
            for fila in lector:
                if len(fila) < 4:
                    raise ValueError("Falta información en la fila del archivo de pedidos.")
                id_carga = fila[0].strip()
                peso_kg = int(fila[1].strip())
                origen = fila[2].strip()
                destino = fila[3].strip()
                
                if id_carga in cls.solicitudes:
                    raise ValueError(f"ID de carga duplicado: {id_carga}")

                if origen not in Nodo.nodos or destino not in Nodo.nodos:
                    raise ValueError(f"Origen o destino inválido: {origen}, {destino}")

                Solicitud(id_carga, peso_kg, origen, destino)

'''
archivo_solicitud = 'solicitudes.csv'
Solicitud.asignar_solicitudes(archivo_solicitud)          

for s in Solicitud.solicitudes.values():
    print(f"Solicitud {s.id_carga}: origen= {s.origen}, destino= {s.destino}, carga= {s.peso_kg} kg")
'''


'''id_carga,peso_kg,origen,destino
CARGA_001,70000,Zarate,Mar_del_Plata
'''