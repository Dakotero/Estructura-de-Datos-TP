from optimizador import *

nodo_a = Nodo("A")
nodo_b = Nodo("B")
nodo_c = Nodo("C")
nodo_d = Nodo("D")
nodo_e = Nodo("E")
nodo_f = Nodo("F")

vehiculo1 = MedioTransporte("Camion 1", "automotor", 80, 10000, 500, 10, 0.5)
vehiculo2 = MedioTransporte("Tren 1", "ferroviario", 100, 50000, 1000, 5, 0.2)
vehiculo3 = MedioTransporte("Barco 1", "maritimo", 40, 200000, 2000, 2, 0.1)
vehiculo4 = MedioTransporte("Avion 1", "aereo", 600, 20000, 5000, 20, 1.5)
vehiculos = [vehiculo1, vehiculo2, vehiculo3, vehiculo4]

Conexion(nodo_a, nodo_b, "automotor", 100)
Conexion(nodo_b, nodo_c, "automotor", 150)
Conexion(nodo_c, nodo_f, "automotor", 120)
Conexion(nodo_a, nodo_d, "automotor", 90)
Conexion(nodo_d, nodo_e, "automotor", 110)
Conexion(nodo_e, nodo_f, "automotor", 130)
Conexion(nodo_b, nodo_d, "automotor", 80)
Conexion(nodo_c, nodo_e, "automotor", 70)

Conexion(nodo_a, nodo_c, "ferroviario", 200)
Conexion(nodo_c, nodo_e, "ferroviario", 250)
Conexion(nodo_b, nodo_d, "ferroviario", 180)

Conexion(nodo_a, nodo_f, "maritimo", 800)
Conexion(nodo_b, nodo_e, "maritimo", 700)

Conexion(nodo_a, nodo_d, "aereo", 500)
Conexion(nodo_c, nodo_f, "aereo", 600)

super_optimizador(vehiculos, nodo_a, nodo_c)