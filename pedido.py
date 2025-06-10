import Nodo
import csv

class Solicitud:
    solicitudes = []
    def __init__(self, id_carga, peso_kg, origen, destino):
        self.id_carga = id_carga
        self.peso_kg = peso_kg
        self.origen = origen
        self.destino = destino
        
    @classmethod
    def asignar_pedido(cls, archivo_solicitud):
        with open(archivo_solicitud, 'r') as f:
            lector = csv.reader(f)
            next(lector)
            for fila in lector:
                if len(fila) < 4:
                    raise ValueError("Falta información en la fila del archivo de pedidos.")
                id_carga = fila[0]
                peso_kg = int(fila[1])
                origen = fila[2]
                destino = fila[3]

                if origen not in Nodo.nodos or destino not in Nodo.nodos:
                    raise ValueError(f"Origen o destino inválido: {origen}, {destino}")

                Solicitud(id_carga, peso_kg, origen, destino)

                    
                    
archivo_solicitud = 'pedidos.csv'
print(Pedido)

'''id_carga,peso_kg,origen,destino
CARGA_001,70000,Zarate,Mar_del_Plata
'''