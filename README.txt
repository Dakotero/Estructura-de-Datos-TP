

ACLARACIONES / SUPOSICIONES

1) En el cálculo del tiempo para cada ruta, en el caso de aéreo, la velocidad se ve afectada por el clima.
Para la velocidad nominal del aereo hicimos la esperanza.
Velocidad_nominal = (probabilidad de mal clima) x (velocidad si hay mal clima) + (1 - probabilidad de mal clima) x (velocidad si hay buen clima)
por ejemplo, si la probabilidad de mal clima es 0,2, se calcula:   vel_nom = 0,2 x 400 + 0,8 x 600

2) 






z) CHECKS:
[GENERALES]
# 1. Pongan una opcion valida de los menus del CLI, o vuelven a intentar
[NODOS]
# 1. El nombre del csv no este vacio
# 2. No pongan el nombre con .csv
# 3. Exista un header no nulo que sea en lower.strip "nombre"
# 4. No haya un Nodo nulo o vacio
# En cambio, nodos duplicados, se arreglan solos "ignorando" el segundo
[CONEXIONES]
# 1. El nombre del csv no este vacio
# 2. No pongan el nombre con .csv
# 3. El modo ded transporte sea valido
# 4. Los nodos origen y destino entren entre los nodos cargados
# 5. Los nodos origen y destino no sean el mismo
# 6. Exista el header, no sea nulo, y sea lo que esperamos
[SOLICITUDES]
# 1. El nombre del csv no este vacio
# 2. No pongan el nombre con .csv
# 3. No falte informacion en alguna de las solicitudes
# 4. No esten duplicados los ID de solicitud
# 5. Origen y Destino existan como nodo
# 6. Exista el header, no sea nulo, y sea lo que esperamos