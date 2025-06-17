import matplotlib.pyplot as plt

def graficar_itinerario(itinerario):
    distancia_acumulada = []
    tiempo_acumulado = []
    costo_acumulado = []

    suma_distancia = 0
    suma_tiempo = 0
    suma_costo = 0

    for conexion in itinerario.conexiones:
        tiempo = conexion.calcular_tiempo_conexion()
        cantidad = itinerario.cantidad_a_utilizar
        costo = conexion.calcular_costo_conexion(itinerario.solicitud, cantidad)

        suma_distancia += conexion.distancia
        suma_tiempo += tiempo
        suma_costo += costo

        distancia_acumulada.append(suma_distancia)
        tiempo_acumulado.append(suma_tiempo)
        costo_acumulado.append(suma_costo)

    # Gráfico 1: Distancia acumulada vs Tiempo acumulado
    plt.figure(figsize=(10, 5))
    plt.plot(tiempo_acumulado, distancia_acumulada, marker='o')
    plt.xlabel('Tiempo Acumulado (horas)')
    plt.ylabel('Distancia Acumulada (km)')
    plt.title('Distancia Acumulada vs Tiempo Acumulado')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Gráfico 2: Costo acumulado vs Distancia acumulada
    plt.figure(figsize=(10, 5))
    plt.plot(distancia_acumulada, costo_acumulado, marker='o', color='green')
    plt.xlabel('Distancia Acumulada (km)')
    plt.ylabel('Costo Acumulado (USD)')
    plt.title('Costo Acumulado vs Distancia Acumulada')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

