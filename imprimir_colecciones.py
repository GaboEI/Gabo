# ----------- 1. Tuplas (tuple) -----------
# Tupla de ejemplo
tupla = (1, 2, 3, 4, 5)

# Imprimir la tupla completa
print("Tupla completa:", tupla)

# Imprimir cada elemento de la tupla en una nueva l\ínea
print("Elementos de la tupla:")
for elemento in tupla:
    print(f"- {elemento}")

# ----------- 2. Diccionarios (dict) -----------
# Diccionario de ejemplo
diccionario = {"nombre": "Gabo", "edad": 25, "ciudad": "México"}

# Imprimir el diccionario completo
print("\nDiccionario completo:", diccionario)

# Imprimir cada clave y valor del diccionario
print("Elementos del diccionario:")
for clave, valor in diccionario.items():
    print(f"- {clave}: {valor}")

# ----------- 3. Sets (set) -----------
# Set de ejemplo
mi_set = {3, 1, 4, 2, 5}

# Imprimir el set completo
print("\nSet completo (sin orden):", mi_set)

# Imprimir los elementos del set ordenados
print("Set ordenado:")
for elemento in sorted(mi_set):  # sorted() ordena los elementos
    print(f"- {elemento}")

# ----------- 4. Listas (list) -----------
# Lista de ejemplo
lista = ["Estudiar", "Programar", "Dormir"]

# Imprimir la lista completa
print("\nLista completa:", lista)

# Imprimir cada elemento de la lista en una nueva l\ínea
print("Elementos de la lista:")
for elemento in lista:
    print(f"- {elemento}")

# ----------- 5. Pretty Print para estructuras complejas -----------
from pprint import pprint

# Estructura compleja de ejemplo
datos = {
    "usuarios": [
        {"nombre": "Gabo", "edad": 25},
        {"nombre": "Ana", "edad": 30},
    ],
    "ciudades": {"México", "Bogotá", "Lima"},
}

# Imprimir con pprint
print("\nEstructura compleja con pprint:")
pprint(datos)
