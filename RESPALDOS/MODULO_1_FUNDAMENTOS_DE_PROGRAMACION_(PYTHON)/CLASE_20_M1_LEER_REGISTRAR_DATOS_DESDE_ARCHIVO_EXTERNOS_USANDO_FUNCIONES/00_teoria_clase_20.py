#====================================================================================================================
"""
#!🧠 CLASE 20  MÓDULO 1 (Ampliado)
📂Nombre: Leer y registrar datos desde archivos externos (.txt) usando funciones

#!📌 ¿Qué vas a dominar aquí?

* Leer archivos de texto línea por línea con funciones
* Crear archivos nuevos desde funciones
* Separar responsabilidades: una función lee, otra escribe
* Devolver datos desde archivos para usarlos en otras partes del programa

?🧠 TEORÍA PROFUNDA
!🔹 1. ¿Qué es open() y cómo se usa en funciones?

open() te permite abrir archivos de texto. Dentro de una función, se usa así:

def leer_archivo():
    with open("archivo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        return contenido

!🔹 2. Modos de apertura comunes:

| Modo| Significado                              |
| ----| ---------------------------------------- |
| "r" | Leer un archivo existente                |
| "w" | Escribir (sobrescribe todo)              |
| "a" | Añadir al final del archivo              |
| "x" | Crear archivo nuevo (error si ya existe) |

!🔹 3. Separación de responsabilidades en funciones

?💡 Una función no debe hacerlo todo.

Ejemplo ideal:
* leer_estudiantes(): lee nombres desde un archivo y los devuelve como lista
* registrar_estudiante(nombre): añade uno nuevo
* mostrar_estudiantes(lista): imprime uno por uno
Eso se llama programación modular y es buena práctica profesional.

!🔹 4. ¿Qué estructura es mejor para guardar múltiples líneas?
Un .txt con un nombre por línea:

Carlos Pérez
Juana Díaz
Miguel Ruiz

Se puede leer con:
for linea in archivo:
    print(linea.strip())
"""
#====================================================================================================================
"""
!✍️ ESTRUCTURA DE LA CLASE

Tendrás 3 ejercicios:

| Ejercicio  Nombre                                           
| ---------  ------------------------------------------------ 
| 1️⃣       | Leer archivo y devolver contenido                |
| 2️⃣       | Agregar dato a archivo con validación            |
| 3️⃣       | Leer, mostrar y buscar datos con función general |

Cada uno se evalúa por separado.
Solo se avanza al siguiente cuando apruebas el anterior ✅

¿Listo para comenzar con el Ejercicio 1?
Si me das luz verde, te entrego:

* Teoría específica
* Esqueleto guía sin resolver
* Retroalimentación línea por línea cuando lo envíes
"""
#====================================================================================================================