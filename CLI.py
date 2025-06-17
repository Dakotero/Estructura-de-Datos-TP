from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from Ruta import *
from medios_transporte import *
from optimizador import *
from correr_rutas import *
import time

class CLI:

    def runCLI():
        try:
            print("\n~~~ Bienvenido al CLI del Grupo 5 ~~~")
            print("\nCargando opciones...")
            time.sleep(0.5)
            print("\n[#          ]")
            print("\n[##         ]")
            time.sleep(1.5)
            print("\n[####       ]")
            print("\n[#######    ]")
            time.sleep(2)
            print("\n[########## ]")
            time.sleep(1.5)
            print("\n[###########]")
            time.sleep(0.5)



            while True:
                print("\n~~~ Menú de opciones ~~~")
                print("a. AAA")
                print("b. BBB")
                print("c. CCC")
                print("d. DDD")
                print("~~~")
                print("z. Salir")
                opcion = input("\n[Menu] Seleccione una opción: ").strip().lower()

                if opcion == "a":
                    test = int(input("[Menu] Ingrese valor genericooo"))
                    print("\n[Menu] Valor ingresadoooo")

                elif opcion == "b":
                    print("\n[Menu] Valor ingresadoooo")

                elif opcion == "c":
                    print("\n[Menu] Valor ingresadoooo")

                elif opcion == "d":
                    print("\n[Menu] Valor ingresadoooo")

                elif opcion == "z":
                    print("[Ejercicio 1] Saliendo del programa...")
                    break

                else:
                    print("[Menu] Opción no válida. Intenta nuevamente.")

        except ValueError as e:
            print(f"[CLI] ValueError: {e}.")
        except Exception as e:
            print(f"[CLI] Exception Error: {e}.")

CLI.runCLI()