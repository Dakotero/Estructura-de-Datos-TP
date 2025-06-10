#aca lo q agregue yo (belu) esta en proceso: 

from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from medios_transporte import *
from optimizador import *

archivo_solicitud = 'solicitudes.csv'
archivo_nodos = 'nodos.csv'
archivo = 'conexiones.csv'

Solicitud.asignar_solicitudes(archivo_solicitud)          
Nodo.asignar_nodos(archivo_nodos)
Conexion.asignar_conexion(archivo)

aereo = Aereo(600, 5000, 750, 40, 10, 400)
maritimo = Fluvial(40, 100000, 500, 15, 2, 1500)
ferroviario = Ferroviario(100, 150000, 100, 20, 3, 15)
automotor = Automotor(80, 30000, 30, 5, 1, 2)
vehiculos = [aereo, maritimo, ferroviario, automotor]

#print("\n--- SOLICITUDES CARGADAS ---")
#for s in Solicitud.solicitudes.values():
#    print(f"ID: {s.id_carga}, Origen: {s.origen}, Destino: {s.destino}, Peso: {s.peso_kg} kg")

#print("\n--- NODOS CARGADOS ---")
#for nombre, nodo in Nodo.nodos.items():
#    print(f"Nombre: {nombre}, Objeto: {nodo}")

#print("\n--- CONEXIONES CARGADAS ---")
#for c in Conexion.conexiones:
#    print(f"Origen: {c.origen.nombre}, Destino: {c.destino.nombre}, Modo: {c.modo}")

for s in Solicitud.solicitudes.values():
    print(f"Solicitud {s.id_carga}: origen= {s.origen}, destino= {s.destino}, carga= {s.peso_kg} kg")
    inicio = Nodo.nodos[s.origen]
    fin = Nodo.nodos[s.destino]
    super_optimizador(vehiculos, inicio, fin)