#=======================================================================================================================
"""
!🧪 EJERCICIO 1  CLASE 20
?📌 Nombre: Leer el contenido completo de un archivo .txt desde una función y devolverlo como texto plano

!🎯 OBJETIVO DEL EJERCICIO
* Crear una función que abra un archivo externo
* Leer su contenido completo
* Retornar el contenido como cadena de texto
* Mostrar el resultado en consola

!🧠 CONCEPTOS Y DEFINICIONES APLICADOS

| Concepto | Definición breve                            |
| -------- | ------------------------------------------- |
| `open()` | Abre un archivo externo                     |
| `"r"`    | Modo de lectura                             |
| `read()` | Devuelve el contenido completo del archivo  |
| `with`   | Maneja el archivo de forma segura           |
| `return` | Devuelve el contenido al programa principal |
| Tipado   | Se usará `-> str` como tipo de retorno      |

!✍️ ESQUELETO GUÍA (sin resolver)

?1️⃣ Definir función que lee el archivo
def leer_archivo() -> str:

    Lee el contenido completo del archivo 'registro.txt' y lo retorna como cadena de texto.
    Retorna:
    - str: contenido del archivo completo.

    #2️⃣ Usar with open en modo lectura
    with open(..., "r", encoding="utf-8") as archivo:
        #3️⃣ Leer contenido con .read()
        ...
        #4️⃣ Retornar el contenido leído
        ...

?5️⃣ Llamar a la función y mostrar el resultado
!🧪 Archivos esperados:

Crea un archivo llamado `registro.txt` (puede contener 3_5 líneas de texto de ejemplo, como nombres, mensajes, etc.).
Luego, tu función debe **leer ese archivo y retornar su contenido completo.
"""
#=======================================================================================================================
def crear_y_escribir_archivo():
    contenido_a_escribir = "Este es el contenido de prueba para mi archivo de registro.\n" \
                        "Esta es una segunda línea de texto."
    with open("registro.txt", "w", encoding="utf-8") as archivo:
        archivo.write(contenido_a_escribir)
    print("El archivo 'registro.txt' ha sido creado y escrito exitosamente.")

def leer_archivo() -> str:
    with open("registro.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        return contenido

crear_y_escribir_archivo()
print(leer_archivo())

def anadir_contenido_a_archivo():
    contenido_a_anadir = "\nEsta es una nueva línea añadida al final."
    with open("registro.txt", "a", encoding="utf-8") as archivo:
        archivo.write(contenido_a_anadir)
    print("Contenido añadido a 'registro.txt' exitosamente.")

anadir_contenido_a_archivo()
print(leer_archivo())
#=======================================================================================================================
#! ===  respuesta de consola embebida ===
"""
El archivo 'registro.txt' ha sido creado y escrito exitosamente.
Este es el contenido de prueba para mi archivo de registro.
Esta es una segunda línea de texto.
Contenido añadido a 'registro.txt' exitosamente.
Este es el contenido de prueba para mi archivo de registro.
Esta es una segunda línea de texto.
Esta es una nueva línea añadida al final.
"""
#=======================================================================================================================
#! ===  contenido del archivo generado "registro.txt" ===
"""
Este es el contenido de prueba para mi archivo de registro.
Esta es una segunda línea de texto.
Esta es una nueva línea añadida al final.
"""
#=======================================================================================================================