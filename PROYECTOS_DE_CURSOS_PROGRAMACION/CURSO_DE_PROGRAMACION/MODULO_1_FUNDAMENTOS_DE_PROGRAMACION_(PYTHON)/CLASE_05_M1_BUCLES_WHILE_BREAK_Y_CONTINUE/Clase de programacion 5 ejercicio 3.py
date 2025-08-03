"""Ejercicio 3: Tabla de multiplicar
Pide al usuario un número y usa un for para mostrar su tabla de multiplicar del 1 al 10."""
numero = 7
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

