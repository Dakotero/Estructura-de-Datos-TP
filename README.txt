1) Calculo de tiempo
En el cálculo del tiempo para cada ruta, en el caso de aéreo, la velocidad se ve afectada por el clima.
Para la velocidad nominal del aereo hicimos la esperanza.
Velocidad_nominal = (probabilidad de mal clima) x (velocidad si hay mal clima) + (1 - probabilidad de mal clima) x (velocidad si hay buen clima)
por ejemplo, si la probabilidad de mal clima es 0,2, se calcula:   vel_nom = 0,2 x 400 + 0,8 x 600

2) Clases creadas
Conexion
Medios de transporte
Cada medio de transporte (clases hijas de medio de transporte) que hereda sus caracteristicas principales de medio de transporte 
Nodo
Ruta
Solicitud 
Red de conexiones
Verificacion 
CLI

3) Principales desafios
Se tomo como una base clave del trabajo la generacion de rutas. Que son creadas en el archivo optimizador.
A partir de ese punto se fueron creando las diferentes clases y adaptando el optimizador segun lo necesario de la caracteristicas de las clases.
Luego se crearon las funciones de la busqueda de rutas mas econimica y de menor tiempo. Al igual que la creacion de graficos.
Finalmente se crearon las debidas restricciones de cada clase, para que el codigo responda a un posibles errores.

4) Decisiones de diseño
Creamos un archivo por cada clase, tambien existe el archivo correr_rutas que esta formado con diferentes funciones.
Creamos un main que ejecuta todo de forma automatica
Tambien un CLI que ejecuta el codigo de forma interactiva con el usuario

5) Optimizador
El optimizador crea una clase (Red de Conexiones) por cada modo de vehiculo, y arma la red para cada uno
La red, es basicamente un diccionario que tiene de clave CADA nodo que exista (accesible por una conexion del vehiculo de la red)
Y una lista de todos sus vecinos.
Entonces termino con la informacion de todos los nodos de la red y sus vecinos.
La busqueda entonces es por sistema de pila de tuplas:
Empezando por el origen, la lista empieza como: [(inicio, [inicio])], siendo (nodo_actual, camino_actual)
Entonces, por sistema LIFO, 
1. agarra el siguiente valor (en este caso hay solo uno)
2. verifica no se haya ya llegado a destino (en caso de que si, lo guarda en caminos posibles)
3. lo elimina
4. suma a la pila TODOS sus vecinos posibles desde el nodo_actual, POR LOS QUE NO PASE YA (no esten en camino_actual) [(vecino, camino + [vecino])]
5. Repito
De esta forma, reviso todos los posibles caminos uno a uno, guardando todos los posibles caminos que partiendo de origen, terminan en destino.
Posteriormente, se aplican restricciones por peso u otras razones

6) CLI
En el uso del CLI, UNA VEZ EMPEZADO, no hay una forma comoda de resetear su memoria.
En caso de por alguna razon (querer cambiar archivos cargados, cambio codigo),
Recomendamos o salir del CLI al menu principial, y volver a correr el CLI, o eliminar la terminal
y volver a correr el codigo

7) CHECKS: (cuando se usa el CLI)

[GENERALES]
# 1. Pongan una opcion valida de los menus del CLI, o vuelven a intentar
# 2. Problemas con el optimizador, creando las tuplas
# 3. Problemas con el optimizador, creando los caminos
# 4. Corriendo el super optimizador, por problema de datos
# 5. Problema usando los resultados del super optimizador para crear las Rutas
# 6. Problema calculando transportes necesarios

[NODOS]
# 1. El nombre del csv no este vacio
# 2. No pongan el nombre con .csv
# 3. Exista un header no nulo que sea en lower.strip "nombre"
# 4. No haya un Nodo nulo o vacio
# En cambio, nodos duplicados, se arreglan solos "ignorando" el segundo
# 5. Que no hayan 0 nodos

[CONEXIONES]
# 1. El nombre del csv no este vacio
# 2. No pongan el nombre con .csv
# 3. El modo ded transporte sea valido
# 4. Los nodos origen y destino entren entre los nodos cargados
# 5. Los nodos origen y destino no sean el mismo
# 6. Exista el header, no sea nulo, y sea lo que esperamos
# 7. Que no hayan 0 conexiones

[SOLICITUDES]
# 1. El nombre del csv no este vacio
# 2. No pongan el nombre con .csv
# 3. No falte informacion en alguna de las solicitudes
# 4. No esten duplicados los ID de solicitud
# 5. Origen y Destino existan como nodo
# 6. Exista el header, no sea nulo, y sea lo que esperamos
# 7. Peso_kg pueda convertirse a entero
# 8. No haya 0 solicitudes