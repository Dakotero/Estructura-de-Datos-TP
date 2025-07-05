
import math
from Conexion import Conexion
from Solicitud import Solicitud
from medios_transporte import transportes
from Graficador import *

class Ruta():
    contadorID = 1
    def __init__(self, transporte, solicitud, conexiones, nodos):
        self.id = Ruta.contadorID
        Ruta.contadorID += 1

        self.transporte = transporte
        self.solicitud = solicitud
        self.conexiones = conexiones
        self.costo_total = 0
        self.tiempo_total = 0
        self.nodos = nodos
        self.cantidad_a_utilizar = 0
        self.cantidad_conexiones = len(conexiones)+1

    def __str__(self):

        if not self.conexiones:
            return f"No hay conexiones para transporte ({self.transporte})"
        nodos = [self.conexiones[0].origen]
        for c in self.conexiones:
            if c.origen == nodos[-1]:
                nodos.append(c.destino)
            else:
                nodos.append(c.origen)
        nombres_nodos = [n.nombre for n in nodos]

        tiempo_total = self.calcular_tiempo_ruta()
        costo_total = self.calcular_costo_ruta(self.solicitud)

        texto = f"\nTransporte: {self.transporte}"
        texto += f"\nRecorrido: {' → '.join(nombres_nodos)}"
        texto += f"\nDuración: {int(tiempo_total)}h {int((tiempo_total % 1) * 60)}m {int((((tiempo_total % 1) * 60) % 1) * 60)}s"
        texto += f"\nCosto total: ${costo_total:,.2f}"
        texto += f"\nCantidad de transportes: {self.cantidad_a_utilizar}"
        texto +=f"\nCantidad de ciudades: {int(self.cantidad_conexiones)}"


        return texto

    def __repr__(self):
        return self.__str__()
    
    def calcular_cantidad(self):
        try:
            for conexion in self.conexiones:
                cantidad=conexion.calcular_cantidad(self.solicitud)
                if cantidad>self.cantidad_a_utilizar:
                    self.cantidad_a_utilizar=cantidad    
        except (ValueError, TypeError) as e:
            raise ValueError(f"Hubo un problema calculando la cantidad de transportes necesarios. \nMas detalles: {e}")
        
    def calcular_tiempo_ruta(self):
        tiempo_total = 0
        for conexion in self.conexiones:
            tiempo_total += conexion.calcular_tiempo_conexion()
        return tiempo_total
                
    def calcular_costo_ruta(self, solicitud):
        costo_total = 0
        for conexion in self.conexiones:
            costo_total += conexion.calcular_costo_conexion(solicitud, self.cantidad_a_utilizar)

        transporte = transportes[self.transporte]
        carga_total = solicitud.peso_kg

        if transporte.modo == "automotor":
            capacidad = transporte.capacidad_kg
            cantidad_completa = carga_total // capacidad
            carga_restante = carga_total % capacidad

            for _ in range(cantidad_completa):
                costo_total += transporte.costokg(capacidad) * capacidad

            if carga_restante > 0:
                costo_total += transporte.costokg(carga_restante) * carga_restante

        else:
            costo_total += transporte.costo_kg * carga_total

        return costo_total

    @staticmethod
    def convertir_a_objetos_ruta(tupla_modo_conexiones, solicitud, tupla_modo_nodos):
        rutas = []
        try:
            for i in range(len(tupla_modo_conexiones)):
                transporte = tupla_modo_conexiones[i][0]
                lista_conexiones = tupla_modo_conexiones[i][1]
                lista_nodos = tupla_modo_nodos[i][1]

                nueva_ruta = Ruta(transporte, solicitud, lista_conexiones, lista_nodos)
                rutas.append(nueva_ruta)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Hubo un problema transformando los resultados del optimizador en Rutas. \nMas detalles: {e}")

        return rutas

    @staticmethod
    def mostrar_ruta_mas_rapida(rutas):
        if not rutas:
            print("No hay rutas disponibles.")
            return

        ruta_mas_rapida = rutas[0]
        tiempo_minimo = ruta_mas_rapida.calcular_tiempo_ruta()

        for ruta in rutas[1:]:
            tiempo = ruta.calcular_tiempo_ruta()
            if tiempo < tiempo_minimo:
                tiempo_minimo = tiempo
                ruta_mas_rapida = ruta

        print(f"{ruta_mas_rapida}")  
        
        graficar_tiempo_vs_distancia(ruta_mas_rapida, tipo_ruta="Ruta más rápida")
        graficador_conexion_vs_tiempo(ruta_mas_rapida, tipo_ruta="Ruta más rápida")
        graficar_distancia_vs_costo(ruta_mas_rapida, tipo_ruta="Ruta más rápida")

    @staticmethod
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

        print(f"{ruta_mas_economica}")
        
        graficar_tiempo_vs_distancia(ruta_mas_economica, tipo_ruta="Ruta más económica")
        graficador_conexion_vs_tiempo(ruta_mas_economica, tipo_ruta="Ruta más económica")
        graficar_distancia_vs_costo(ruta_mas_economica, tipo_ruta="Ruta más económica")

    @staticmethod
    def mostrar_ruta_mas_ciudades(rutas):
        if not rutas:
            print("No hay rutas disponibles.")
            return

        ruta_mas_ciuadades = rutas[0]
        mas_ciudades = ruta_mas_ciuadades.cantidad_conexiones

        for ruta in rutas[1:]:
            cantidad = ruta.cantidad_conexiones
            if cantidad > mas_ciudades:
                mas_ciudades = cantidad
                ruta_mas_ciuadades = ruta

        print(f"{ruta_mas_ciuadades}")
        print(f"Cantidad de nodos intermedios: {int(ruta_mas_ciuadades.cantidad_conexiones)-2}")