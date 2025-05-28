###########################################

# OPTIMIZADOR DE CAMINOS EJEMPLO

###########################################

# Ejemplo de datos que ingresan

nodos = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
trayectos = ["ABY", "BCY", "DBX", "DAY", "ACY", "DFZ", "BFZ", "DBZ"]
inicio = "D"
fin = "B"

###########################################

class Red_de_Transporte:
    def __init__(self, transporte): # No uso nodos, porque los nodos son implícitos en los trayectos,
                                    # Y sino estan, tampoco me importaria
        self.transporte = transporte
        self.vecinos = {}  # Diccionario: nodo -> lista de vecinos


# Osea, la clase Red_de_Transporte es para CADA TIPO DE TRANSPORTE
# Entonces, tengo uno para X, Y, Z (osea, maritimo, aereo, terrestre, etc.)
# Y lo que voy a intentar hacer, es que cada tipo de transporte tenga su propia red de transporte
# Entonces despues corro la busqueda de caminos en cada red de transporte


###########################################

    # Empiezo con una funcion simple, que agrega una conexión entre dos nodos, generico
    # Agrego una conexión bidireccional entre dos nodos

    def agregar_conexion(self, nodo1, nodo2):
        if nodo1 not in self.vecinos: # Si el nodo no existe, lo creo
            self.vecinos[nodo1] = []
        if nodo2 not in self.vecinos:
            self.vecinos[nodo2] = []
        self.vecinos[nodo1].append(nodo2) 
        self.vecinos[nodo2].append(nodo1)  # bidireccional

        # Osea, si tengo A y B, y los conecto, entonces A tiene a B como vecino, y B tiene a A como vecino
        # En el diccionario queda:
        # {A: [B], B: [A]}

###########################################

    # Busco caminos entre dos nodos, de forma generica
    def buscar_caminos(self, inicio, fin):
        pila = [(inicio, [inicio])] # Pila con (nodo_actual, camino_actual)
                                    # Hago con Pila, asi es LIFO, y puedo ir buscando caminos de forma iterativa
        caminos_finales = [] # Lista donde pongo los caminos que ya encontre y "valide"

        while pila: # Mientras haya nodos en la pila
            nodo_actual, camino = pila.pop() # Agarro el nodo actual y el camino actual

            if nodo_actual == fin:             # Me fijo si llegue al nodo final
                caminos_finales.append(camino) # Si llegue al nodo final, agrego el camino a la lista de caminos
            else: 
                for vecino in self.vecinos.get(nodo_actual, []): # Recorro los vecinos del nodo actual,
                                                                 # que los tengo que haber agregado con agregar_conexion
                # mas exacto, busco en el diccionario de vecinos (el self.vecinos.get) la lista (el []) del nodo_actual
                
                    if vecino not in camino:                     # No quiero repetir nodos en el camino
                        pila.append((vecino, camino + [vecino])) # Agrego POR vecino (osea, posibles caminos a recorrer)
                                                                 # a la pila tanto el vecino como nodo actual, 
                                                                 # y el camino actual sumandole que ahora llegue al vecino

        return caminos_finales

# Ejemplo de que esta sucediendo:

# Arranco con D, y el camino es [D]
# Pila: [(D, [D])]

# Agarro D, y veo que tiene como vecinos A y B
# Agrego A y B a la pila, con el camino [D, A] y [D, B]
# Pila: [(A, [D, A]), (B, [D, B])] 
# SE FUE [(D, [D])] PORQUE EN EL WHILE HAGO UN POP, Y EL POP SACA EL ULTIMO ELEMENTO, ADEMAS DE AGARRAR EL NODO Y CAMINO

# Despues, agarro (B, [D, B]) por ser el ultimo elemento de la pila
# Y veo que B tiene como vecinos A y C, A NO ESTA EN EL CAMINO DE B
# Entonces, elimino (B, [D, B]) de la pila y sumo los otros dos
# Pila: [(A, [D, A]), (A, [D, B, A]), (C, [D, B, C])]

# Y asi sigo hasta que la pila se vacia
# Con la excepcion de si encuentra un vecino, que ya esta en el camino, entonces no lo agrega a la pila
# Y, si antes de buscar vecinos, se da cuenta que el es el nodo final, se agrega a caminos_finales despues de eliminarse de la pila

###########################################

# Ahora que tengo la clase de red de transporte, y tengo las dos funciones esenciales,
# que son 1. Entender y agregar conexiones entre nodos, y 2. Buscar caminos entre dos nodos, a partir de estas conexiones,
# hago la funcion principal que va a usar estas dos funciones y la clase para encontrar el camino mas corto entre dos nodos
# a partir de los datos que me den

# Este en verdad va a cambiar segun como procesemos los datos, pero bueno yo para probar

def principal_encontrar_caminos(nodos, trayectos, inicio, fin):
    # Creo una instancia de clase por tipo de transporte
    redes = {}

    for trayecto in trayectos:

        if len(trayecto) != 3: # Si el trayecto no tiene 3 caracteres, lo ignoro
            print(f"[ERROR] Trayecto inválido: {trayecto}. Debe tener 3 caracteres.")
            continue
        if trayecto[0] not in nodos or trayecto[1] not in nodos:
            print(f"[ERROR] Trayecto inválido: {trayecto}. Los nodos deben estar en la lista de nodos.")
            continue

        a, b, transporte = trayecto[0], trayecto[1], trayecto[2] # Agarro los nodos y el transporte del trayecto

        if transporte not in redes: # Si el transporte no esta en las redes, lo creo
            redes[transporte] = Red_de_Transporte(transporte)

        redes[transporte].agregar_conexion(a, b) # Agrego la conexion

    # Aca ya procese redes y conexiones, ahora busco los caminos
    if inicio not in nodos or fin not in nodos:
        print(f"[ERROR] Inicio o fin inválido: {inicio}, {fin}. Deben estar en la lista de nodos.")
        return []
    
    todos_los_caminos = []

    for transporte, red in redes.items(): # Recorro cada red de transporte
        print(f"\n[INFO] Buscando caminos en la red de transporte: {transporte}") # (? para molestar

    # redes es un diccionario donde la clave es el tipo de transporte y el valor es la instancia de Red_de_Transporte
    # {
    #     'Y': <Red_de_Transporte objeto para 'Y'>,
    #     'X': <Red_de_Transporte objeto para 'X'>,
    #     'Z': <Red_de_Transporte objeto para 'Z'>
    # }
    # Entonces, el for recorre cada tipo de transporte (Y, X, Z) y su respectiva red de transporte
    # Ejemplo, si estoy en transporte 'Y' es la instancia de objeto, puedo hacer:
    # red.transporte = 'Y'
    # red.vecinos = {'A': ['B', 'C', 'D'], 'B': ['A', 'C'], ...}

        if inicio not in red.vecinos or fin not in red.vecinos: # Si no estan en la red de vecinos, ni son parte de la red de transporte
            print(f"\n[ERROR] Inicio o fin no conectados en la red de transporte {transporte}: {inicio}, {fin}.\n")
            continue

        caminos_crudos = red.buscar_caminos(inicio, fin)

        for camino in caminos_crudos:
            print(f"[INFO] Camino encontrado {transporte}: {camino}")
    return todos_los_caminos


###########################################

# PRUEBO
caminos = principal_encontrar_caminos(nodos, trayectos, inicio, fin)

