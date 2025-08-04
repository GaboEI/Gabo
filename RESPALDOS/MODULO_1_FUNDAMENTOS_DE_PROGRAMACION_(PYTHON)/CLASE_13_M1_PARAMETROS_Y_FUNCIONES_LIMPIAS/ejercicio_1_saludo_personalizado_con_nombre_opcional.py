"""====================================================================================
# #!🧪 Ejercicio 1  Clase 13

#?📌 Nombre: Saludo personalizado con nombre opcional
#?🔑 Conceptos: Parámetro opcional + docstring + return limpio

🎯 ¿Qué debe hacer la función?
1️⃣ Recibir un nombre de usuario como parámetro (opcional).
2️⃣ Si no se proporciona ningún nombre, debe saludar como "invitado".
3️⃣ Devolver un saludo como cadena, no imprimirlo directamente.
4️⃣ Tener un docstring claro explicando su comportamiento.

#?💼 ¿Dónde sirve esto profesionalmente?
⏺️ En sistemas que muestran mensajes de bienvenida a usuarios con login opcional.
⏺️ Interfaces donde no todos los datos están disponibles.
⏺️ Funciones reusables en bibliotecas propias de automatización o apps.
===================================================================================="""
def saludar(nombre="invitado"):
    """
    Retorna un saludo personalizado.
    Parámetros:
    nombre (str): nombre del usuario. Por defecto es "invitado".
    Retorna:
    str: saludo personalizado.
    """
    return(f"Hola, {nombre}! Bienbenido el sistema")
print(saludar("Gabo"))
print(saludar())
