import csv

class Nodo():
    nodos = {}
    def __init__(self, nombre):
        self.nombre = nombre
        Nodo.nodos[nombre] = self
        
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
            header = next(lector, None)
            if header is None or len(header) == 0 or header[0].lower().strip() != "nombre":
                raise ValueError("El archivo de nodos debe tener una cabecera con el nombre 'nombre'.")
            for fila in lector:
                if fila[0] == "":
                    raise ValueError("El nombre de uno de los nodos esta vacio.")
                elif fila[0] not in cls.nodos:  # Verifica si el nodo ya existe:
                    Nodo(fila[0])
                
'''                
archivo_nodos = 'nodos.csv'
Nodo.asignar_nodos(archivo_nodos)
print(Nodo.nodos)
'''

