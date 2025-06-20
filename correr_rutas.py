from Graficador import *

def mostrar_ruta_mas_rapida(rutas):
    if not rutas:
        print("No hay rutas disponibles.")
        return

    # Buscar la ruta de menor tiempo
    ruta_mas_rapida = rutas[0]
    tiempo_minimo = ruta_mas_rapida.calcular_tiempo_ruta()

    for ruta in rutas[1:]:
        tiempo = ruta.calcular_tiempo_ruta()
        if tiempo < tiempo_minimo:
            tiempo_minimo = tiempo
            ruta_mas_rapida = ruta

    # Mostrar detalles
    print("\n[RESULTADO] Ruta más rápida")
    print(f"{ruta_mas_rapida}")  
    
    graficar_tiempo_vs_distancia(ruta_mas_rapida, tipo_ruta="Ruta más rápida")
    graficador_conexion_vs_tiempo(ruta_mas_rapida, tipo_ruta="Ruta más rápida")
    graficar_distancia_vs_costo(ruta_mas_rapida, tipo_ruta="Ruta más rápida")

def mostrar_ruta_mas_economica(rutas, solicitud):
    if not rutas:
        print("No hay rutas disponibles.")
        return

    ruta_mas_economica = rutas[0]
    costo_minimo = ruta_mas_economica.calcular_costo_ruta(solicitud)

    for ruta in rutas[1:]:
        costo = ruta.calcular_costo_ruta(solicitud)
        if costo < costo_minimo:
            costo_minimo = costo
            ruta_mas_economica = ruta

    print("\n[RESULTADO] Ruta más económica")
    print(f"{ruta_mas_economica}")
    
    graficar_tiempo_vs_distancia(ruta_mas_economica, tipo_ruta="Ruta más económica")
    graficador_conexion_vs_tiempo(ruta_mas_economica, tipo_ruta="Ruta más económica")
    graficar_distancia_vs_costo(ruta_mas_economica, tipo_ruta="Ruta más económica")