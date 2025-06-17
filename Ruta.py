
import math
from Conexion import Conexion
from Solicitud import Solicitud
from medios_transporte import transportes

class Ruta():
    contadorID = 1
    def __init__(self, transporte, solicitud, conexiones, nodos): #solicitud tiene que ser el objeto (instancia) de solicitud, conexiones es una lista de objetos conexion

        self.id = Ruta.contadorID
        Ruta.contadorID += 1

        self.transporte = transporte
        self.solicitud = solicitud
        self.conexiones = conexiones
        self.costo_total = 0
        self.tiempo_total = 0
        self.nodos = nodos
        self.cantidad_a_utilizar = 0

    def __str__(self):

        if not self.conexiones:
            return f"No hay conexiones para transporte ({self.transporte})"

        nodos = [self.conexiones[0].origen] + [c.destino for c in self.conexiones]
        nombres_nodos = [n.nombre for n in nodos]

        tiempo_total = self.calcular_tiempo_ruta()
        costo_total = self.calcular_costo_ruta(self.solicitud)

        texto = f"\nTransporte: {self.transporte}"
        texto += f"\nRecorrido: {' → '.join(nombres_nodos)}"
        #si queremos el tiempo en horas, minutos y segundos:
        texto += f"\nDuración: {int(tiempo_total)}h {int((tiempo_total % 1) * 60)}m {int((((tiempo_total % 1) * 60) % 1) * 60)}s"
        #si queremos el tiempo en horas decimales:
        #texto += f"\nDuración: {tiempo_total:.2f} horas" 
        texto += f"\nCosto total: ${costo_total:,.2f}"
        texto += f"\nCantidad de transportes: {self.cantidad_a_utilizar}"


        return texto

    def __repr__(self):
        return self.__str__()
    
    def calcular_cantidad(self):
        for conexion in self.conexiones:
            cantidad=conexion.calcular_cantidad(self.solicitud)
            if cantidad>self.cantidad_a_utilizar:
                self.cantidad_a_utilizar=cantidad    
        
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


def convertir_a_objetos_ruta(tupla_modo_conexiones, solicitud, tupla_modo_nodos):
    rutas = []

    for i in range(len(tupla_modo_conexiones)):
        transporte = tupla_modo_conexiones[i][0]
        lista_conexiones = tupla_modo_conexiones[i][1]
        lista_nodos = tupla_modo_nodos[i][1]

        nueva_ruta = Ruta(transporte, solicitud, lista_conexiones, lista_nodos)
        rutas.append(nueva_ruta)

    return rutas
