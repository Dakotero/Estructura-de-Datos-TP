#aca lo q agregue yo (belu) esta en proceso: 

#########################################
#                                       #
# CARGA DE DATOS                        #
#                                       #
#########################################

from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from Ruta import *
from medios_transporte import *
from optimizador import *
from correr_rutas import *

archivo_solicitud = 'solicitudes.csv'
archivo_nodos = 'nodos.csv'
archivo = 'conexiones.csv'

Nodo.asignar_nodos(archivo_nodos)
Conexion.asignar_conexion(archivo)
Solicitud.asignar_solicitudes(archivo_solicitud)          

transportes = {"ferroviario": ferroviario, "automotor": automotor, "aereo": aereo,"fluvial": fluvial}    
vehiculos = list(transportes.values())

# print("\n--- SOLICITUDES CARGADAS ---")
# for s in Solicitud.solicitudes.values():
#    print(f"ID: {s.id_carga}, Origen: {s.origen}, Destino: {s.destino}, Peso: {s.peso_kg} kg")

# print("\n--- NODOS CARGADOS ---")
# for nombre, nodo in Nodo.nodos.items():
#    print(f"Nombre: {nombre}, Objeto: {nodo}")

# print("\n--- CONEXIONES CARGADAS ---")
# for c in Conexion.conexiones:
#    print(f"Origen: {c.origen}, Destino: {c.destino}, Modo: {c.modo}")


#########################################
#                                       #
# EJECUTO SOLICITUD                     #
#                                       #
#########################################

for solicitud in Solicitud.solicitudes.values():
    inicio = Nodo.nodos[solicitud.origen]
    fin = Nodo.nodos[solicitud.destino]

    print(f"\n=== Solución para solicitud {solicitud.id_carga}: {solicitud.origen} -> {solicitud.destino} ===")
#    super_optimizador(vehiculos, inicio, fin)
    tupla_modo_conexiones, tupla_modo_nodos = super_optimizador(vehiculos, inicio, fin)

########## PRUEBA DE RESULTADOS DEL OPTIMIZADOR ##########

    # print("\n-------- Caminos (modo y conexiones) ---")
    # for modo, conexiones in tupla_modo_conexiones:
    #     for conexion in conexiones:
    #         print(f"[INFO]  {conexion.origen.nombre} -> {conexion.destino.nombre} ({conexion.modo.modo})")

    # print("\n--------   Caminos  (modo y nodos)   ---")
    # for modo, nodos in tupla_modo_nodos:
    #     nombres = [nodo.nombre for nodo in nodos]
    #     print(f"[INFO] Modo: {modo} | Nodos: {' -> '.join(nombres)}")

# #    break  # probár con una sola solicitud

#########################################################

    rutas = convertir_a_objetos_ruta(tupla_modo_conexiones, solicitud, tupla_modo_nodos)

########## MOSTRAR RUTAS ##########

#    for ruta in rutas:
#        print(ruta)

###################################

    print(F'\n === Rutas encontradas para la solicitud {solicitud.id_carga} ===\n')

    if not rutas:
        print("No se encontraron rutas para esta solicitud.")
        continue
    for ruta in rutas:
        print(ruta)

###################################

    print(F'\n === Mejores rutas para la solicitud {solicitud.id_carga} ===\n')

    mostrar_ruta_mas_rapida(rutas, solicitud)

    mostrar_ruta_mas_economica(rutas)

#     # Luego de mostrar la ruta mas rapida y la mas economica, es necesario borrar las rutas actuales para iniciar de 0 en la proxima solicitud
#     rutas.clear()
