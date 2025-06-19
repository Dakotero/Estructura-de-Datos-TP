import time
import subprocess

def main():
    print("\nBienvenido al TP del Grupo 5!")
    time.sleep(0.5)
    print("\nCargando opciones...")
    time.sleep(0.5)
    print("\n[#          ]   10%")
    print("[##         ]   20%")
    time.sleep(1.5)
    print("[####       ]   40%")
    time.sleep(0.5)
    print("[#######    ]   70%")
    time.sleep(2)
    print("[########## ]   90%")
    time.sleep(1.5)
    print("[###########]   100%")
    time.sleep(0.5)
    print("Opciones cargadas con exito!")
    time.sleep(0.5)

    while True:
        print("\n~~~ Menú Principal ~~~")
        print("1. Ejecutar CLI                    (verificaciones especificas)")
        print("2. Ejecutar código automático      (verificaciones genericas)")
        print("3. Salir")
        opcion = input("[Menu] Ingrese 1, 2 o 3: ").strip()

        if opcion == "1":
            print("Ejecutando CLI...")
            time.sleep(0.2)
            subprocess.run(["python", "CLI.py"])

        elif opcion == "2":
            print("Ejecutando código automático...")
            time.sleep(0.5)
            subprocess.run(["python", "verificaciones.py"])

        elif opcion == "3":
            print("Saliendo del programa...")
            time.sleep(0.5)
            break
        else:
            print("\n[Menu] Opción no válida. Intente nuevamente.")

main()