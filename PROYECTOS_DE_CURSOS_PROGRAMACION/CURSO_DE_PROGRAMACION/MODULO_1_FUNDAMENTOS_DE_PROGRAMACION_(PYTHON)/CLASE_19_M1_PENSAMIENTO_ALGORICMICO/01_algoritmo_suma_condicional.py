#=== ALGORITMO SUMA CONDICIONAL ===#
"""
La idea central es sumar dos o más números y aplicar una condición lógica 
para decidir una acción adicional, por ejemplo, verificar si el resultado 
cumple un criterio.
"""
#=== SCRIPT ===#
numero1 = float(input("🔢 Ingrese el primer número: "))
numero2 = float(input("🔢 Ingrese el segundo número: "))

resultado = numero1 + numero2

if resultado > 10:
    print(f"La suma es {resultado}, que es mayor que 10.")
else:
    print(f"La suma es {resultado}, que es 10 o menor.")

#=== RESPUESTA DE LA CONSOLA ===#
"""
EJEMPLO 1:
🔢 Ingrese el primer número: 2
🔢 Ingrese el segundo número: 3
La suma es 5.0, que es 10 o menor.

EJEMPLO 2:
🔢 Ingrese el primer número: 10
🔢 Ingrese el segundo número: 10
La suma es 20.0, que es mayor que 10.
"""


