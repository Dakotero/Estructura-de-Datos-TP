import csv

class Nodo():
    nodos = {}
    def __init__(self, nombre):
        self.nombre = nombre
        self.nodos[nombre] = self
        
    def __str__(self):
        return f"Nodo({self.nombre})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return isinstance(other, Nodo) and self.nombre == other.nombre

    def __hash__(self):
        return hash(self.nombre)

    @classmethod
    def asignar_nodos(cls, archivo_nodos):
        with open(archivo_nodos, 'r') as f:
            lector = csv.reader(f)
            next(lector)
            for fila in lector:
                if fila[0] not in cls.nodos:  # Verifica si el nodo ya existe:
                    Nodo(fila[0])
                
'''                
archivo_nodos = 'nodos.csv'
Nodo.asignar_nodos(archivo_nodos)
print(Nodo.nodos)
'''