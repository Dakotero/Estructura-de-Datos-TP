import matplotlib.pyplot as plt

def graficador_conexion_vs_tiempo(ruta):

    
    nombres_conexiones = []
    tiempos_acumulados = [0]
    tiempos_total = 0

    for conexion in ruta.conexiones:
        nombres_conexiones.append(f"{conexion.origen.nombre} → {conexion.destino.nombre}")
        tiempos_total += conexion.calcular_tiempo_conexion()
        tiempos_acumulados.append(tiempos_total)

    plt.figure(figsize=(8, 5))
    plt.step(["Inicio"] + nombres_conexiones, tiempos_acumulados, where='post', marker='o')
    plt.ylabel("Tiempo acumulado (h)")
    plt.xlabel("Conexión")
    plt.title(f"Tiempo acumulado por conexión - Ruta #{ruta.id}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
