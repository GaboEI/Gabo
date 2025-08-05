#==========================================================================================================================================
"""
!🧪 EJERCICIO 2  CLASE 20
?📂 Nombre: Escribir datos en un archivo solo si el contenido es válido

*🎯 OBJETIVO
Crear una función que:
1. Reciba un texto (nombre, mensaje, etc.)
2. Valide que el texto **no esté vacío**
3. Si es válido, lo **escriba en un archivo .txt**
4. Si no es válido, devuelva un mensaje indicando que no se guardó

!🧠 CONCEPTOS Y DEFINICIONES

| Concepto               | Definición                                             |
| ---------------------- | ------------------------------------------------------ |
| `open(..., "a")`       | Abre archivo en modo **append** (añadir sin borrar)    |
| `archivo.write(...)`   | Escribe texto al final del archivo                     |
| `.strip()`             | Elimina espacios en blanco a los lados                 |
| `if not texto.strip()` | Evalúa si el texto está vacío o solo contiene espacios |
| `return`               | Devuelve un mensaje de éxito o fallo                   |
| Tipado de función      | Se aplicará: `def funcion(dato: str) -> str:`          |

!✅ ENFOQUE PEDAGÓGICO

* Aprenderás a **validar datos antes de guardarlos**
* Practicarás **funciones con entrada, validación y salida textual**
* Simularás un mini formulario de registro
"""
#==========================================================================================================================================
def guardar_texto(texto: str) -> str:
    if not texto.strip():
        return "⚠️ El texto está vacío. No se guardó nada."

    with open("registro.txt", "a", encoding="utf-8") as archivo:
        archivo.write("\n" + texto + "\n")

    return "✅ Texto guardado correctamente."

entrada_usuario = input("Introduce el texto que deseas guardar: ")
print(guardar_texto(entrada_usuario))

#==========================================================================================================================================
#! Respuesta consola 2 ejemplos realizados
"""
ejemplo 1:
Introduce el texto que deseas guardar: Albert Einstein dijo:
✅ Texto guardado correctamente.
ejemplo 2:
Introduce el texto que deseas guardar: La imaginación es más importante que el conocimiento. El conocimiento es limitado, mientras 
que la imaginación abarca todo el mundo
✅ Texto guardado correctamente.

"""
#==========================================================================================================================================
#! ejemmplo de la actualizacion del archivo txt "registro.txt"
"""
Este es el contenido de prueba para mi archivo de registro.
Esta es una segunda línea de texto.
Esta es una nueva línea añadida al final.
Albert Einstein dijo:

La imaginación es más importante que el conocimiento. El conocimiento es limitado, mientras que la imaginación abarca todo el mundo
"""
#==========================================================================================================================================
#FIN