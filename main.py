#aca lo q agregue yo (belu) esta en proceso: 

from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from Ruta import Ruta
from medios_transporte import *
from optimizador import *
from funciones_extras import *

archivo_solicitud = 'solicitudes.csv'
archivo_nodos = 'nodos.csv'
archivo = 'conexiones.csv'

Nodo.asignar_nodos(archivo_nodos)
Conexion.asignar_conexion(archivo)
Solicitud.asignar_solicitudes(archivo_solicitud)          





#LO PUSE COMENTADO XQ LO MOVI A MEDIOS_TRANSPORTE.PY

'''
aereo = Aereo(600, 5000, 750, 40, 10, 400)
fluvial = Fluvial(40, 100000, 500, 15, 2, 1500)
ferroviario = Ferroviario(100, 150000, 100, 20, 3, 15)
automotor = Automotor(80, 30000, 30, 5, 1, 2)
vehiculos = [aereo, fluvial, ferroviario, automotor] #capaz lo saco este
'''
transportes = {"ferroviario": ferroviario, "automotor": automotor, "aereo": aereo,"fluvial": fluvial}    
vehiculos = list(transportes.values())

#print("\n--- SOLICITUDES CARGADAS ---")
#for s in Solicitud.solicitudes.values():
#    print(f"ID: {s.id_carga}, Origen: {s.origen}, Destino: {s.destino}, Peso: {s.peso_kg} kg")

#print("\n--- NODOS CARGADOS ---")
#for nombre, nodo in Nodo.nodos.items():
#    print(f"Nombre: {nombre}, Objeto: {nodo}")

#print("\n--- CONEXIONES CARGADAS ---")
#for c in Conexion.conexiones:
#    print(f"Origen: {c.origen.nombre}, Destino: {c.destino.nombre}, Modo: {c.modo}")



# Paso 2: Ejecutar prueba con primer solicitud
for solicitud in Solicitud.solicitudes.values():
    inicio = Nodo.nodos[solicitud.origen]
    fin = Nodo.nodos[solicitud.destino]

    print(f"\n=== Solución para solicitud {solicitud.id_carga}: {solicitud.origen} -> {solicitud.destino} ===")
    rutas = super_optimizador(vehiculos, inicio, fin)
    break  # probá con una sola solicitud


'''
for s in Solicitud.solicitudes.values():
    print(f"\nSolicitud {s.id_carga}: origen= {s.origen}, destino= {s.destino}, carga= {s.peso_kg} kg")
    inicio = Nodo.nodos[s.origen]
    fin = Nodo.nodos[s.destino]
    super_optimizador(vehiculos, inicio, fin) # LO DEJO COMO DEBUGGING, PERO ELIMINAR

    rutas_optimizador = super_optimizador(vehiculos, inicio, fin)
    rutas = convertir_a_objetos_ruta(rutas_optimizador, s)
    for ruta in rutas:
        tiempo_total = Ruta.calcular_tiempo_ruta(ruta)
        costo_total = Ruta.calcular_costo_ruta(ruta, s)
    


#    rutas_chequeadas = super_chequeador()

'''