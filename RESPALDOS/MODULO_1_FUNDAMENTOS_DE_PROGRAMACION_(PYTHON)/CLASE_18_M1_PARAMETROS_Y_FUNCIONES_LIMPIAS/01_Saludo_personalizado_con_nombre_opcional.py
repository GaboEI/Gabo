"""
=================================================================
🧪 EJERCICIO 1  CLASE 18
📌 Nombre: Saludo personalizado con nombre opcional
🔑 Enfoque: parámetro opcional + docstring + return limpio
=================================================================
"""
def saludar(nombre="invitado"):
    """
    Retorna un saludo personalizado.
    Parámetros:
    nombre (str): nombre del usuario. Por defecto es "invitado".
    Retorna:
    str: saludo personalizado.
    """
    return f"Hola, {nombre}!"

nombre = input("Ingresa tu nombre: ")
print(saludar(nombre))
print(saludar())
#*===============================================================
