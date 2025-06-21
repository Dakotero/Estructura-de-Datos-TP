from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from Ruta import *
from medios_transporte import *
from optimizador import *
from correr_rutas import *
from Graficador import *
import time

class CLI:

    def runCLI(self):

        try:
            Nodo.nodos = {}
            Conexion.conexiones = []
            Solicitud.solicitudes = {}

###################################################################################

            print("\n~~~ Bienvenido al CLI del Grupo 5 ~~~")
            time.sleep(0.5)

###################################################################################
            
            archivo_nodos = 'nodos.csv'
            archivo_conexiones = 'conexiones.csv'
            archivo_solicitudes = 'solicitudes.csv'
            nombre_nodoscsv = 'nodos'
            nombre_conexionescsv = 'conexiones'
            nombre_solicitudescsv = 'solicitudes'
            
            while True:
                try:
                    print("\n~~~ Carga de datos ~~~")
                    print("Empezamos cargando los datos necesarios")
                    time.sleep(0.5)
                    print("Los nombres de archivos a cargar son:\n")    
                    print(f"[NODOS] \t\t{archivo_nodos}")
                    print(f"[CONEXIONES] \t\t{archivo_conexiones}")
                    print(f"[SOLICITUDES] \t\t{archivo_solicitudes}")
                    print("\n[Menu] Queres cambiar alguno?")
                    print("[Menu] [NO: 'no' (continuar)] [SI: 'nodos', 'conexiones', 'solicitudes']")
                    opcion = input("\n[Menu] Seleccione una opción: ").strip().lower()
                    
                    if opcion == "nodos":
                        print("\n[Menu] Como se llama el csv de los nodos?")
                        print("[Menu] No incluir la extension .csv")
                        nombre_nodoscsv = input("[Menu] Ingrese el nombre del archivo: ").strip()
                        archivo_nodos = f"{nombre_nodoscsv}.csv"

                    elif opcion == "conexiones":
                        print("\n[Menu] Como se llama el csv de las conexiones?")
                        print("[Menu] No incluir la extension .csv")
                        nombre_conexionescsv = input("[Menu] Ingrese el nombre del archivo: ").strip()
                        archivo_conexiones = f"{nombre_conexionescsv}.csv"

                    elif opcion == "solicitudes":
                        print("\n[Menu] Como se llama el csv de las solicitudes?")
                        print("[Menu] No incluir la extension .csv")
                        nombre_solicitudescsv = input("[Menu] Ingrese el nombre del archivo: ").strip()
                        archivo_solicitudes = f"{nombre_solicitudescsv}.csv"

                    elif opcion == "no" or opcion == "continuar":

                        # NODOS
                        if nombre_nodoscsv.strip() == "":
                            raise ValueError("[NODOS] El nombre del archivo de nodos no puede estar vacío.")
                        if nombre_nodoscsv.endswith(".csv"):
                            raise ValueError("[NODOS] El nombre del archivo de nodos no debe contener la extensión '.csv'.")
                        Nodo.asignar_nodos(archivo_nodos)
                        if not Nodo.nodos:
                            raise ValueError("[NODOS] No se encontraron nodos en el archivo")

                        # CONEXIONES
                        if nombre_conexionescsv.strip() == "":
                            raise ValueError("[CONEXIONES] El nombre del archivo de conexiones no puede estar vacío.")
                        if nombre_conexionescsv.endswith(".csv"):
                            raise ValueError("[CONEXIONES] El nombre del archivo de conexiones no debe contener la extensión '.csv'.")
                        Conexion.asignar_conexion(archivo_conexiones)
                        if not Conexion.conexiones:
                            raise ValueError("[CONEXIONES] No se encontraron conexiones en el archivo")

                        # SOLICITUDES
                        if nombre_solicitudescsv.strip() == "":
                            raise ValueError("[SOLICITUDES] El nombre del archivo de solicitudes no puede estar vacío.")
                        if nombre_solicitudescsv.endswith(".csv"):
                            raise ValueError("[SOLICITUDES] El nombre del archivo de solicitudes no debe contener la extensión '.csv'.")
                        Solicitud.asignar_solicitudes(archivo_solicitudes)
                        if len(Solicitud.solicitudes) == 0:
                            raise ValueError("[SOLICITUDES] No se encontraron solicitudes en el archivo")

                        break

                    else:
                        print("[Menu] Opción no válida. Intenta nuevamente.")
                        time.sleep(0.5)
                        print("[Menu] Tiene que escribir exactamente ['no', 'nodos', 'conexiones', 'solicitudes'].")
                        time.sleep(1)


                except ValueError as e:
                    print(f"[CLI] ValueError: {e}")
                    time.sleep(1)
                except Exception as e:
                    print(f"[CLI] Error al cargar los archivos: {e}")
                    print("[CLI] Asegúrate de que el archivo CSV esté en el formato correcto y exista dentro de la direccion.")
                    time.sleep(1)

            time.sleep(1)
            print("\n[CLI] Archivos cargados exitosamente.")
            time.sleep(1)

###################################################################################

            while True:
                print("\n~~~ MENU ~~~")

                solicitudes = list(Solicitud.solicitudes.values())

                print("a. Ver total Nodos")
                print("b. Ver total Conexiones")
                print("c. Ver Vehiculos")
                print("d. Ver Solicitudes")
                print("~")
                print("z. Cerrar programa")

                opcion = input("\n[Menu] Seleccione una opción: ").strip().lower()
                time.sleep(0.5)

                if opcion == "a":
                    print(f"\n[Resultado] Total de Nodos: {len(Nodo.nodos)}")
                    for nombre, nodo in Nodo.nodos.items():
                        print(f"Nombre: {nombre},\t\t\tObjeto: {nodo}")
                    time.sleep(1)

                elif opcion == "b":
                    print(f"\n[Resultado] Total de Conexiones: {len(Conexion.conexiones)}")
                    for c in Conexion.conexiones:
                        print(f"Origen: {c.origen.nombre},\t\t\tDestino: {c.destino.nombre},\t\t\tModo: {c.modo.modo}")
                    time.sleep(1)

                elif opcion == "c":
                    print(f"\n[Resultado] Total de Vehiculos: {len(vehiculos)}")
                    for v in transportes.values():
                        print(f"{v.modo} - Capacidad: {v.capacidad_kg} kg, Velocidad: {v.velocidad_nom_kmh} km/h")
                    time.sleep(1)

                elif opcion == "d":
                    while True:
                        print("~~~ SOLICITUDES ~~~")
                        print(f"\n[Menu] Seleccione una de las {len(solicitudes)} solicitudes:")
                        for solicitud in solicitudes:
                            print(f"{solicitud.id_carga}: {solicitud.origen} -> {solicitud.destino}")
                        print(f"\n[Menu] Si desea volver al menu, ingresar 'MENU'\n")
                        
                        id_solicitud = input("[Menu] Ingrese el ID de la solicitud (ex. CARGA_0011): ").strip()

                        if id_solicitud.lower() == "menu":
                            print("[CLI] Volviendo al menú de opciones...")
                            time.sleep(1)
                            break

                        if id_solicitud not in Solicitud.solicitudes:
                            print("\n[Menu] ID de solicitud no válido. Intenta nuevamente.")
                            time.sleep(1)
                            continue
                
                        else:
                            print(f"\n[Menu] Correremos la solicitud {id_solicitud}")
                            time.sleep(1)

                            solicitud = Solicitud.solicitudes[id_solicitud]
                            inicio = Nodo.nodos[solicitud.origen]
                            fin = Nodo.nodos[solicitud.destino]
                            tupla_modo_conexiones, tupla_modo_nodos = super_optimizador(vehiculos, inicio, fin)
                            rutas = convertir_a_objetos_ruta(tupla_modo_conexiones, solicitud, tupla_modo_nodos)
                            for ruta in rutas:
                                ruta.calcular_cantidad()

                            while True:
                                print(f"\n~~~ Solicitud {id_solicitud} ~~~")
                                print("\n~~~ Menú de opciones ~~~")
                                print("a. Ver Rutas")
                                print("b. Ver Ruta mas Rapida y sus Graficos")
                                print("c. Ver Ruta mas Economica y sus Graficos")
                                print("d. Ver la Ruta mas Economica y la mas Rapida, con sus Graficos")
                                print("~")
                                print("z. Ver otra solicitud o opciones del menu")

                                opcion = input("\n[Menu] Seleccione una opción: ").strip().lower()
                                if opcion == "a":
                                    print(f"\n[Resultado] Rutas para la solicitud {id_solicitud}:")
                                    if not rutas:
                                        print("No se encontraron rutas para esta solicitud.")
                                        continue
                                    for ruta in rutas:
                                        print(ruta)
                                    time.sleep(1)

                                elif opcion == "b":
                                    print(f"\n[Resultado] Ruta más rápida y sus Gráficos para la solicitud {id_solicitud}:")
                                    mostrar_ruta_mas_rapida(rutas)
                                    print(f"\n[IMPORTANTE] Si no podes continuar, es porque hay todavia graficos abiertos!")
                                    time.sleep(1)

                                elif opcion == "c":
                                    print(f"\n[Resultado] Ruta más económica y sus Gráficos para la solicitud {id_solicitud}:")
                                    mostrar_ruta_mas_economica(rutas, solicitud)
                                    print(f"\n[IMPORTANTE] Si no podes continuar, es porque hay todavia graficos abiertos!")
                                    time.sleep(1)

                                elif opcion == "d":
                                    print(f"\n[Resultado] Ver la Ruta mas Economica y la mas Rapida, con sus Graficos para la solicitud {id_solicitud}:")
                                    mostrar_ruta_mas_economica(rutas, solicitud)
                                    print(f"\n[IMPORTANTE] Si no podes continuar, es porque hay todavia graficos abiertos!")
                                    time.sleep(1)

                                elif opcion == "z":
                                    print("\n[Menu] Volviendo a cargar los datos...")
                                    break

                                else:
                                    print("\n[Menu] Opción no válida. Intenta nuevamente.")
                
                elif opcion == "z":
                    break
                
                else:
                    print("\n[Menu] Opción no válida. Intenta nuevamente.")

###################################################################################

            print("\n[CLI] Cerrando el CLI...")
            time.sleep(1)

###################################################################################

        except ValueError as e:
            print(f"[CLI] ValueError: {e}.")
        except Exception as e:
            print(f"[CLI] Exception Error: {e}.")

###################################################################################

vehiculos = list(transportes.values())

# cli = CLI()
# cli.runCLI()