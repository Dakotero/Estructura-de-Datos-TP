
from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from Ruta import *
from medios_transporte import *
from optimizador import *
from correr_rutas import *
from Graficador import *

archivo_solicitud = 'solicitudes.csv'
archivo_nodos = 'nodos.csv'
archivo = 'conexiones.csv'

class Verificacion:

    def runVerificacion(self):

        try:
            Nodo.nodos = {}
            Conexion.conexiones = []
            Solicitud.solicitudes = {}
            
            Nodo.asignar_nodos(archivo_nodos)
            Conexion.asignar_conexion(archivo)
            Solicitud.asignar_solicitudes(archivo_solicitud)     
                
            vehiculos = list(transportes.values())

            #########################################
            #                                       #
            # EJECUTO SOLICITUD                     #
            #                                       #
            #########################################

            for solicitud in Solicitud.solicitudes.values():
                inicio = Nodo.nodos[solicitud.origen]
                fin = Nodo.nodos[solicitud.destino]

                print(f"\n=== Solución para solicitud {solicitud.id_carga}: {solicitud.origen} -> {solicitud.destino} ===")
                tupla_modo_conexiones, tupla_modo_nodos = super_optimizador(vehiculos, inicio, fin)

            #########################################################

                rutas = convertir_a_objetos_ruta(tupla_modo_conexiones, solicitud, tupla_modo_nodos)
                for ruta in rutas:
                    ruta.calcular_cantidad()

                print(F'\n === Rutas encontradas para la solicitud {solicitud.id_carga} ===\n')

                if not rutas:
                    print("No se encontraron rutas para esta solicitud.")
                    continue
                for ruta in rutas:
                    print(ruta)

            ###################################

                print(F'\n === Mejores rutas para la solicitud {solicitud.id_carga} ===\n')

                mostrar_ruta_mas_rapida(rutas)

                mostrar_ruta_mas_economica(rutas, solicitud)

        except ValueError as e:
            print(f"[Cd Automatico] ValueError: {e}.")
        except Exception as e:
            print(f"[Cd Automatico] Exception Error: {e}.")