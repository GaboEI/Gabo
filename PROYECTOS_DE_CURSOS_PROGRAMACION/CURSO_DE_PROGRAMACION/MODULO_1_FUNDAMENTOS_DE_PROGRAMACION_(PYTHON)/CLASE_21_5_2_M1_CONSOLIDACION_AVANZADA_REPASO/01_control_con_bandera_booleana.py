# 1. Definición de la Matriz de Ejemplo (Array 2D)
matriz = [
    [10, 20, 30],
    [40, -5, 60], # ¡Aquí está el negativo!
    [70, 80, 90]
]

# 2. Inicialización de Variables (INICIO del diagrama de flujo)
bandera_negativo = False  # Bandera = False
pos_i = -1                # Pos_i = -1 (Fila)
pos_j = -1                # Pos_j = -1 (Columna)

# 3. Recorrido de la Matriz
# El 'enumerate' nos da el índice (i, j) y el valor en cada iteración.

# Recorrer filas (Bucle externo con índice i)
for i, fila in enumerate(matriz):
    # Recorrer números en la fila (Bucle interno con índice j)
    for j, numero in enumerate(fila):
        
        # ¿Número < 0?
        if numero < 0:
            # Sí -> Se encontró un negativo
            bandera_negativo = True
            
            # 🟥 Guardar posición [i, j] del valor negativo (MEJORA)
            pos_i = i 
            pos_j = j
            
            # Romper bucle interno
            break
            
    # ¿Bandera == True?
    if bandera_negativo:
        # Sí -> Romper bucle externo
        break
        
# 4. Resultado Final
print("-" * 52)

# ¿Bandera == True?
if bandera_negativo:
    # Sí -> Mostrar mensaje de número negativo y su posición
    print("¡ERROR: Se detectó un número negativo!")
    # 🟥 Mostrar posición al final del programa (MEJORA)
    print(f"El valor negativo se encontró en la posición: [{pos_i}, {pos_j}]")
else:
    # No -> Mostrar mensaje de éxito
    print("ÉXITO: La matriz no contiene números negativos.")

"""
RESPUETA CONSOLA:
----------------------------------------------------
¡ERROR: Se detectó un número negativo!
El valor negativo se encontró en la posición: [1, 1] 
"""