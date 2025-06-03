import csv

archivo_nodos = 'nodos.csv'

class Nodo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []
        self.nodos = set()

    def asignar_nodos(self, archivo_nodos):
        with open(archivo_nodos, 'r') as f:
            lector = csv.reader(f)
            for fila in lector:
                nodo = Nodo(fila[0]).nombre
                self.nodos.add(nodo)
                
print(Nodo().asignar_nodos(archivo_nodos))
        