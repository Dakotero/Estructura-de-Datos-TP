#aca lo q agregue yo (belu) esta en proceso: 

#########################################
#                                       #
# CARGA DE DATOS                        #
#                                       #
#########################################

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
#    print(f"Origen: {c.origen}, Destino: {c.destino}, Modo: {c.modo}")


#########################################
#                                       #
# EJECUTO SOLICITUD                     #
#                                       #
#########################################

def convertir_a_objetos_ruta(resultados_optimizador, solicitud):
    rutas = []
    for transporte, lista_conexiones in resultados_optimizador:
        nueva_ruta = Ruta(transporte, solicitud, lista_conexiones)
        rutas.append(nueva_ruta)
    return rutas
    
for solicitud in Solicitud.solicitudes.values():
    inicio = Nodo.nodos[solicitud.origen]
    fin = Nodo.nodos[solicitud.destino]

    print(f"\n=== Solución para solicitud {solicitud.id_carga}: {solicitud.origen} -> {solicitud.destino} ===")
#    super_optimizador(vehiculos, inicio, fin)
    rutas = super_optimizador(vehiculos, inicio, fin)
    for modo, camino in rutas:
        print(f"[DEBUG] Ruta generada para {modo.modo}: {len(camino)} tramos.")

#    break  # probár con una sola solicitud

    rutas = convertir_a_objetos_ruta(rutas, solicitud)

    for ruta in rutas:
        tiempo_total = ruta.calcular_tiempo_ruta()
        costo_total = ruta.calcular_costo_ruta(solicitud)
        print(F'El camino {ruta} tarda {tiempo_total} horas, y cuesta {costo_total} pesos')
    #    rutas_chequeadas = super_chequeador()

