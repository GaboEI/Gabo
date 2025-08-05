# Mostrar un triángulo de asteriscos
# 🔹 Pide al usuario un número entero.
# 🔹 Muestra un triángulo de asteriscos con esa cantidad de filas.
#! Pedir al usuario un número entero
try:
    filas = int(input("Ingresa el número de filas: "))
    
    # Generar el triángulo de asteriscos
    for i in range(1, filas + 1):
        print("*" * i)
except ValueError:


