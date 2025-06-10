#estuve trabajando en esto q busca rutas y calcula costo y tiempo total (falta corregir xq no imprime. -belu)
#no lo termine, y hay q ver como lo juntamos con lo de Chamon, y si sirve
#por algun motivo no iimprime ,as que la solicitud (algo hice mal). si alguien me ayuda a ver q onda esto joya

from collections import deque
from Conexion import Conexion
from Solicitud import Solicitud
from Nodo import Nodo
from medios_transporte import MedioTransporte
import math



def buscar_rutas(origen, destino, conexiones):
    rutas = []
    cola = deque([([origen], [])])  # ([nodos_visitados], [conexiones_usadas])

    while cola:
        camino_actual, conexiones_actuales = cola.popleft()
        nodo_actual = camino_actual[-1]

        if nodo_actual == destino:
            rutas.append((camino_actual, conexiones_actuales))
            continue

        for conexion in conexiones:
            if conexion.origen == nodo_actual and conexion.destino not in camino_actual:
                nuevo_camino = camino_actual + [conexion.destino]
                nuevas_conexiones = conexiones_actuales + [conexion]
                cola.append((nuevo_camino, nuevas_conexiones))

    return rutas


def calcular_tiempo_ruta(transporte, ruta): #transporte tiene que ser una de las 4 instancias de transporte
                                            #ruta tiene que ser una lista de objetos
    tiempo_total = 0

    for conexion in ruta:
        
        velocidad_transporte = transporte.velocidad_nom_kmh

        if transporte.modo == "aereo":
            prob_mal_tiempo = float(conexion.valor_restriccion or 0)
            velocidad_transporte = (transporte.vel_mal_clima_kmh)*(prob_mal_tiempo) + (transporte.velocidad_nom_kmh)*(1-prob_mal_tiempo)

        if conexion.restriccion == 'velocidad_max':
            vel_max=float(conexion.valor_restriccion)
        else:
            vel_max=transporte.velocidad_nom_kmh
        vel= min(vel_max, velocidad_transporte)
            
        tiempo_total += conexion.distancia_km / vel
    return tiempo_total
    
def calcular_costo_ruta(transporte, ruta, solicitud):
    
    for conexion in ruta:
        cantidad = math.ceil(solicitud.peso_kg / transporte.capacidad_kg)
        if transporte.modo == "automotor":
            costo_total += transporte.costo_fijo*cantidad
            costo_total += (transporte.costo_km * conexion.distancia)*cantidad
            costo_total += (transporte.costokg(solicitud.peso_kg) * solicitud.peso_kg)*cantidad

        elif transporte.modo == "ferroviario":
            costo_total += transporte.costo_fijo*cantidad
            tramo_largo = conexion.distancia >= 200*cantidad
            costo_total += (transporte.costokm(tramo_largo) * conexion.distancia)*cantidad
            costo_total += (transporte.costo_kg * solicitud.peso_kg)*cantidad
            
        elif transporte.modo == "fluvial":
            tipo_tramo = conexion.valor_restriccion
            costo_fijo_real = transporte.costofijo(tasa_maritima=(tipo_tramo == "maritimo"))
            costo_total += costo_fijo_real*cantidad
            costo_total += (transporte.costo_km * conexion.distancia)*cantidad
            costo_total += (transporte.costo_kg * solicitud.peso_kg)*cantidad
        
        elif transporte.modo == "aereo":
            costo_total += transporte.costo_fijo*cantidad
            costo_total += (transporte.costo_km * conexion.distancia)*cantidad
            costo_total += (transporte.costo_kg * solicitud.peso_kg)*cantidad
    return costo_total


def plan():
    for solicitud in Solicitud.solicitudes.values():
        origen = solicitud.origen
        destino = solicitud.destino
        conexiones = Conexion.conexiones
        
        print(f"Conexiones totales cargadas: {len(Conexion.conexiones)}")
        for modo in MedioTransporte.modos:
            conexiones_modo=[]
            for conexion in conexiones:
                if conexion.modo.lower() == modo:
                    conexiones_modo.append(conexion)
                    
            rutas = buscar_rutas(origen, destino, conexiones_modo)        
                  
            print(f"Rutas encontradas: {len(rutas)} para modo {modo}") 
            if not rutas:
                print(f"No se encontraron rutas desde {origen} a {destino} para el modo {modo}.")
                continue
            
            

            
            for trayecto, ruta in rutas:
                if modo == "ferroviario":
                    transporte = MedioTransporte.ferroviario
                elif modo == "automotor":
                    transporte = MedioTransporte.automotor
                elif modo == "aereo":
                    transporte = MedioTransporte.aereo
                elif modo == "fluvial":
                    transporte = MedioTransporte.fluvial
                else:
                    continue
                
                if not solicitud.peso_kg > transporte.capacidad_kg:
                
                    costo = calcular_costo_ruta(transporte, ruta, solicitud)
                    tiempo = calcular_tiempo_ruta(transporte, ruta)
                                        

                    print(f"Solicitud {solicitud.id_carga} puede ser atendida con el modo {modo}.")
                    print(f"  Ruta: {' >>> '.join([c.origen for c in ruta] + [ruta[-1].destino])}")
                    print(f"  Costo total: {costo}")
                    print(f"  Tiempo total: {tiempo:.2f} horas")
                    print("-" * 40)

                            
            
            '''
            
            for ruta in rutas:
                
                if modo == 'ferroviario':
                    transporte = MedioTransporte.ferroviario
                    
                    if solicitud.peso_kg > transporte.capacidad_kg:
                        continue
                    #verificar velocidad. no lo hice tdv
                    
                    for conexion in ruta:
                        if conexion.distancia_km < 200:
                            
                            
                    tiempo = calcular_tiempo(transporte, conexiones)
                            
                            
                            
                            
                        
                            MedioTransporte.Ferroviario.tramo_largo=False
                        else:
                            MedioTransporte.Ferroviario.tramo_largo=True
    
                    if conexion.origen == origen or conexion.destino == origen:
                        if conexion.origen == destino or conexion.destino == destino:
                            print(f"Solicitud {solicitud.id_carga} puede ser atendida con el modo {modo}.")
                            break
            


        if not rutas:
            print(f"No se encontraron rutas desde {origen} a {destino}.")
            continue

        print(f"Rutas desde {origen} a {destino}:")
        for ruta, conexiones_usadas in rutas:
            print(f"Ruta: {' -> '.join(ruta)}")
            print("Conexiones:")
            for conexion in conexiones_usadas:
                print(f"{conexion.origen} -> {conexion.destino} ({conexion.modo}), distancia: {conexion.distancia}, restricción: {conexion.restriccion}, valor: {conexion.valor_restriccion}")
            print()
            
            '''