import matplotlib.pyplot as plt
from medios_transporte import transportes


def graficar_tiempo_vs_distancia(ruta):
    tiempo_acumulado = 0
    distancia_acumulada = 0

    tiempos = [0]
    distancias = [0]
    
    fig, ax = plt.subplots(figsize=(10, 5))

    for i, conexion in enumerate(ruta.conexiones):
        tiempo_tramo = conexion.calcular_tiempo_conexion()
        distancia_tramo = conexion.distancia

        t0 = tiempo_acumulado
        t1 = tiempo_acumulado + tiempo_tramo

        d0 = distancia_acumulada
        d1 = distancia_acumulada + distancia_tramo

        # Graficar cada tramo individual
        ax.plot([t0, t1], [d0, d1], marker='o', label=f'Tramo {i+1}: {conexion.origen.nombre} → {conexion.destino.nombre}')

        tiempo_acumulado = t1
        distancia_acumulada = d1

    ax.set_xlabel("Tiempo acumulado (horas)")
    ax.set_ylabel("Distancia acumulada (km)")
    ax.set_title(f"Distancia vs Tiempo - Transporte: {ruta.transporte}")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()



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



def graficar_distancia_vs_costo(ruta):
    ruta.calcular_cantidad()
    cantidad = ruta.cantidad_a_utilizar
    solicitud = ruta.solicitud
    transporte = ruta.transporte

    distancia_acumulada = 0
    costo_acumulado = 0

    fig, ax = plt.subplots(figsize=(12, 6))

    # Costo por kg total, se suma al principio
    medio = transportes[transporte]
    if medio.modo == "automotor":
        capacidad = medio.capacidad_kg
        carga_total = solicitud.peso_kg
        cantidad_completa = carga_total // capacidad
        carga_restante = carga_total % capacidad

        for _ in range(cantidad_completa):
            costo_acumulado += medio.costokg(capacidad) * capacidad
        if carga_restante > 0:
            costo_acumulado += medio.costokg(carga_restante) * carga_restante
    else:
        costo_acumulado += medio.costo_kg * solicitud.peso_kg

    # Primer punto con costo por kg incluido
    puntos_x = [0]
    puntos_y = [costo_acumulado]

    for i, conexion in enumerate(ruta.conexiones):
        distancia_tramo = conexion.distancia
        costo_variable = conexion.modo.costo_km * distancia_tramo * cantidad

        # Costo fijo de esta conexión
        costo_fijo = 0
        if conexion.modo.modo == "ferroviario":
            costo_fijo = conexion.modo.costo_fijo * cantidad
        elif conexion.modo.modo == "fluvial":
            es_maritimo = (conexion.valor_restriccion or "").strip().lower() == "maritimo"
            costo_fijo = conexion.modo.costofijo(tasa_maritima=es_maritimo) * cantidad
        else:
            costo_fijo = conexion.modo.costo_fijo * cantidad

        # Salto vertical por costo fijo
        puntos_x.append(distancia_acumulada)
        puntos_y.append(puntos_y[-1] + costo_fijo)

        # Línea por costo variable a lo largo del tramo
        distancia_acumulada += distancia_tramo
        puntos_x.append(distancia_acumulada)
        puntos_y.append(puntos_y[-1] + costo_variable)

        # Etiqueta
        ax.plot(puntos_x[-2:], puntos_y[-2:], marker='o', label=f'Tramo {i+1}: {conexion.origen.nombre} → {conexion.destino.nombre}')

    ax.set_xlabel("Distancia acumulada (km)")
    ax.set_ylabel("Costo acumulado ($)")
    ax.set_title(f"Costo Total vs Distancia - Transporte: {transporte}")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()

'''

    # Gráfico 2: Costo acumulado vs Distancia acumulada
    plt.figure(figsize=(10, 5))
    plt.plot(distancia_acumulada, costo_acumulado, marker='o', color='green')
    plt.xlabel('Distancia Acumulada (km)')
    plt.ylabel('Costo Acumulado (USD)')
    plt.title('Costo Acumulado vs Distancia Acumulada')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

'''