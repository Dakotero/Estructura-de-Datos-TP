from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from Ruta import *
from medios_transporte import *
from optimizador import *
from correr_rutas import *
from graficador_belu import *
from Graficador import *
import time

class CLI:

    def runCLI(self):

        try:

###################################################################################

            print("\n~~~ Bienvenido al CLI del Grupo 5 ~~~")
            time.sleep(0.2)

###################################################################################

            while True:
                # Verifico POR
                # 1. Pongan una opcion valida de los menus, o vuelven a intentar
                try:
                    print("\n~~~ Carga de datos ~~~")
                    print("Empezamos cargando los datos necesarios")

                    print("\n~~~ NODOS ~~~")
                    print("Como se llama el csv de los nodos?")
                    print("a. nodos.csv")
                    print("b. distinto")
                    opcion = input("\n[Menu] Seleccione una opción: ").strip().lower()

                    if opcion == "a":
                        print("\n[Menu] Cargando nodos desde nodos.csv...")
                        time.sleep(0.5)
                        
                        archivo_nodos = 'nodos.csv'
                        Nodo.asignar_nodos(archivo_nodos)
                        if not Nodo.nodos:
                            raise ValueError("No se encontraron nodos en el archivo")
                        print("[Menu] Nodos cargados correctamente.")

                        break

                    elif opcion == "b":
                        print("\n[Menu] Como se llama el csv de los nodos?")
                        print("[Menu] No incluir la extension .csv")
                        nombre_nodoscsv = input("[Menu] Ingrese el nombre del archivo: ").strip()


                        if nombre_nodoscsv.strip() == "":
                            raise ValueError("El nombre del archivo de nodos no puede estar vacío.")
                        if nombre_nodoscsv.endswith(".csv"):
                            raise ValueError("El nombre del archivo de nodos no debe contener la extensión '.csv'.")
                        
                        print(f"\n[Menu] Cargando nodos desde {nombre_nodoscsv}.csv...")
                        time.sleep(0.5)

                        archivo_nodos = f"{nombre_nodoscsv}.csv"
                        Nodo.asignar_nodos(archivo_nodos)
                        if not Nodo.nodos:
                            raise ValueError("No se encontraron nodos en el archivo")
                        print("[Menu] Nodos cargados correctamente.")

                        break

                    else:
                        print("[Menu] Opción no válida. Intenta nuevamente.")
                
                # Verifico POR:
                # 1. El nombre del csv no este vacio
                # 2. No pongan el nombre con .csv
                # 3. Exista un header no nulo que sea en lower.strip "nombre"
                # 4. No haya un Nodo nulo o vacio
                # En cambio, nodos duplicados, se arreglan solos "ignorando" el segundo
                # 5. Que no hayan 0 nodos
                except ValueError as e:
                    print(f"[CLI] ValueError: {e}")
                    time.sleep(1)
                except Exception as e:
                    print(f"[CLI] Error al cargar los nodos: {e}")
                    print("[CLI] Asegúrate de que el archivo CSV esté en el formato correcto.")
                    time.sleep(1)

            time.sleep(1)

###################################################################################

            while True:
                try:
                    print("\n~~~ CONEXIONES ~~~")
                    print("Como se llama el csv de las conexiones?")
                    print("a. conexiones.csv")
                    print("b. distinto")
                    opcion = input("\n[Menu] Seleccione una opción: ").strip().lower()

                    if opcion == "a":
                        print("\n[Menu] Cargando conexiones desde conexiones.csv...")
                        time.sleep(0.5)

                        archivo_conexiones = 'conexiones.csv'
                        Conexion.asignar_conexion(archivo_conexiones)
                        if not Conexion.conexiones:
                            raise ValueError("No se encontraron conexiones en el archivo")
                        print("[Menu] Conexiones cargadas correctamente.")

                        break

                    elif opcion == "b":
                        print("\n[Menu] Como se llama el csv de las conexiones?")
                        print("[Menu] No incluir la extension .csv")
                        nombre_conexionescsv = input("[Menu] Ingrese el nombre del archivo: ").strip()

                        if nombre_conexionescsv.strip() == "":
                            raise ValueError("El nombre del archivo de conexiones no puede estar vacío.")
                        if nombre_conexionescsv.endswith(".csv"):
                            raise ValueError("El nombre del archivo de conexiones no debe contener la extensión '.csv'.")
                        
                        print(f"\n[Menu] Cargando conexiones desde {nombre_conexionescsv}.csv...")
                        time.sleep(0.5)

                        archivo_conexiones = f"{nombre_conexionescsv}.csv"
                        Conexion.asignar_conexion(archivo_conexiones)
                        if not Conexion.conexiones:
                            raise ValueError("No se encontraron conexiones en el archivo")
                        print("[Menu] Conexiones cargadas correctamente.")
                        break

                    else:
                        print("[Menu] Opción no válida. Intenta nuevamente.")

                # Verifico POR:
                # 1. El nombre del csv no este vacio
                # 2. No pongan el nombre con .csv
                # 3. El modo ded transporte sea valido
                # 4. Los nodos origen y destino entren entre los nodos cargados
                # 5. Los nodos origen y destino no sean el mismo
                # 6. Exista el header, no sea nulo, y sea lo que esperamos
                # 7. Que no hayan 0 conexiones
                except ValueError as e:
                    print(f"[CLI] ValueError: {e}")
                    time.sleep(1)
                except Exception as e:
                    print(f"[CLI] Error al cargar las conexiones: {e}")
                    print("[CLI] Asegúrate de que el archivo CSV esté en el formato correcto.")
                    time.sleep(1)

            time.sleep(1)

###################################################################################

            while True:
                try:
                    print("\n~~~ SOLICITUD ~~~")
                    print("Como se llama el csv de las solicitudes?")
                    print("a. solicitudes.csv")
                    print("b. distinto")
                    opcion = input("\n[Menu] Seleccione una opción: ").strip().lower()

                    if opcion == "a":
                        print("\n[Menu] Cargando solicitudes desde solicitudes.csv...")
                        time.sleep(0.5)

                        archivo_solicitudes = 'solicitudes.csv'
                        Solicitud.asignar_solicitudes(archivo_solicitudes)
                        if len(Solicitud.solicitudes) == 0:
                            raise ValueError("No se encontraron solicitudes en el archivo")
                        print("[Menu] Solicitudes cargadas correctamente.")
                        break

                    elif opcion == "b":
                        print("\n[Menu] Como se llama el csv de las solicitudes?")
                        print("[Menu] No incluir la extension .csv")
                        nombre_solicitudescsv = input("[Menu] Ingrese el nombre del archivo: ").strip()

                        if nombre_solicitudescsv.strip() == "":
                            raise ValueError("El nombre del archivo de solicitudes no puede estar vacío.")
                        if nombre_solicitudescsv.endswith(".csv"):
                            raise ValueError("El nombre del archivo de solicitudes no debe contener la extensión '.csv'.")
                        
                        print(f"\n[Menu] Cargando solicitudes desde {nombre_solicitudescsv}.csv...")
                        time.sleep(0.5)

                        archivo_solicitudes = f"{nombre_solicitudescsv}.csv"
                        Solicitud.asignar_solicitudes(archivo_solicitudes)
                        if len(Solicitud.solicitudes) == 0:
                            raise ValueError("No se encontraron solicitudes en el archivo")
                        print("[Menu] Solicitudes cargadas correctamente.")
                        break

                    else:
                        print("[Menu] Opción no válida. Intenta nuevamente.")

                # Verifico POR:
                # 1. El nombre del csv no este vacio
                # 2. No pongan el nombre con .csv
                # 3. No falte informacion en alguna de las solicitudes
                # 4. No esten duplicados los ID de solicitud
                # 5. Origen y Destino existan como nodo
                # 6. Exista el header, no sea nulo, y sea lo que esperamos
                # 7. Peso_kg pueda convertirse a entero
                # 8. No haya 0 solicitudes
                except ValueError as e:
                    print(f"[CLI] ValueError: {e}")
                    time.sleep(1)
                except Exception as e:
                    print(f"[CLI] Error al cargar las solicitudes: {e}")
                    print("[CLI] Asegúrate de que el archivo CSV esté en el formato correcto.")
                    time.sleep(1)

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
                        
                        id_solicitud = input("[Menu] Ingrese el ID de la solicitud (ex. CARGA_011): ").strip()

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
                                    time.sleep(1)

                                elif opcion == "c":
                                    print(f"\n[Resultado] Ruta más económica y sus Gráficos para la solicitud {id_solicitud}:")
                                    mostrar_ruta_mas_economica(rutas, solicitud)
                                    time.sleep(1)

                                elif opcion == "z":
                                    break

                                else:
                                    print("\n[Menu] Opción no válida. Intenta nuevamente.")
                
                elif opcion == "z":
                    print("\n[Menu] Volviendo a cargar los datos...")
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

cli = CLI()
cli.runCLI()