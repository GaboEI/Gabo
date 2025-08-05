"""
====================================================================================
!🚀 CLASE 18  Módulo 1 Ampliado
?📘 Tema: Parámetros y funciones limpias
todo:🎯 Enfoque: código reutilizable, ordenado y documentado

?📌 Contenido de esta clase:
⏺️ Parámetros obligatorios y opcionales en funciones
⏺️ Buenas prácticas para que tus funciones sean claras, limpias y reutilizables
⏺️ Uso de docstring para documentar bien lo que hace cada función

!📚 Esta clase tendrá 3 ejercicios:

| Nº   Nombre del ejercicio                      Concepto clave                           
| ---  ----------------------------------------  ---------------------------------------- 
| 1️⃣  Saludo personalizado con nombre opcional   Parámetro opcional + return limpio       
| 2️⃣  Calcular precio con o sin descuento        Parámetro opcional + validación de rango 
| 3️⃣  Convertir grados Celsius a Fahrenheit      Función simple + documentación clara 

====================================================================================

"""
#todo|| 🧠 MINI TEORÍA  Funciones limpias y parámetros opcionales

#!🔹 ¿Qué es un parámetro en una función?
#?Un parámetro es una variable que se define en la función para recibir datos de entrada.

def saludar(nombre):
    return f"Hola {nombre}"
# En este caso, nombre es un parámetro obligatorio.

#!🔹 ¿Qué es un parámetro opcional?
#?  Es un parámetro que ya tiene un valor por defecto, por lo tanto no es obligatorio
#?  pasarlo al llamar la función.

def saludar(nombre="invitado"):
    return f"Hola {nombre}"
#Si no pasas nada, usará "invitado" por defecto.

"""
!🔹 ¿Qué es una función limpia?
Una función limpia es:
📦 Modular: hace una sola cosa clara
🚫 No imprime directamente: retorna el resultado
📄 Bien documentada con docstring
🧼 Sin efectos secundarios innecesarios (como variables globales)
"""
#!🔹 ¿Qué es un docstring?
#?Es el bloque de texto que documenta lo que hace la función:

def saludar(nombre="invitado"):
    """
    Retorna un saludo personalizado.
    Parámetros:
    nombre (str): nombre del usuario. Por defecto es "invitado".
    Retorna:
    str: saludo personalizado.
    """
    return f"Hola {nombre}"
# Esto lo hace legible, profesional y útil en documentación o autocompletado.