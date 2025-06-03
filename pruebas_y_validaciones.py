'''ID de carga no vacío

El identificador debe ser un string no vacío y único (si se gestiona en una lista/conjunto de pedidos).

Peso positivo y no nulo

El peso debe ser mayor a 0 kg. No se aceptan pedidos vacíos ni con carga negativa.

Peso numérico

Debe ser un número (int o float), no una cadena de texto tipo "70000kg".

Origen y destino distintos

No debe permitirse un pedido donde el origen y el destino sean la misma ciudad.

Origen y destino válidos

Deben existir dentro del conjunto de nodos (ciudades) cargados en la red. Si la red no está inicializada, marcar como "pendiente de validación".

Distancia disponible entre origen y destino

Debe existir al menos un camino posible entre ambos (esto se puede validar después en el planificador, pero es clave advertirlo en el pedido si es detectable).

Formato correcto del nombre de ciudad

Idealmente, evitar nombres con caracteres inválidos o vacíos.

'''

