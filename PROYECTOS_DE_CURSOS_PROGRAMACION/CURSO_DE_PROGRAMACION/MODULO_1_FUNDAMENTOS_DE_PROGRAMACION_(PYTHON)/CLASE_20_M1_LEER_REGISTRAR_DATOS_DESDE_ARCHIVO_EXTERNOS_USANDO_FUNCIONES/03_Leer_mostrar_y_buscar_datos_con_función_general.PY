#==========================================================================================================================================
"""
!🧪 EJERCICIO 3  CLASE 20
todo||📂 Nombre: Leer, mostrar y buscar datos en un archivo con función general

?🎯 OBJETIVO
*Crear una función que:
1. Abra un archivo .txt existente
2. Lea todo su contenido línea por línea
3. Lo almacene en una lista limpia
4. Permita buscar un dato ingresado por el usuario dentro de esa lista
5. Devuelva un mensaje según si fue encontrado o no

!🧠 CONCEPTOS Y DEFINICIONES

| Concepto     | Definición breve                                      |
| ------------ | ----------------------------------------------------- |
| .readlines() | Lee todas las líneas del archivo como una lista       |
| .strip()     | Limpia saltos de línea y espacios en cada línea       |
| for + in     | Se usa para recorrer las líneas y compararlas         |
| input()      | Captura el dato a buscar por el usuario               |
| lower()      | Se puede usar para búsqueda sin distinguir mayúsculas |
| return       | Devuelve mensaje de éxito o fallo                     |
| Tipado       | def buscar_en_archivo(dato: str) -> str               |

!🧱 ESTRUCTURA DEL PROGRAMA

Tendrás que usar funciones como:
* leer_datos(): devuelve una lista limpia desde el archivo
* buscar_dato(lista, dato): busca y devuelve un mensaje

O puedes hacerlo todo dentro de una sola función como:

    def buscar_en_archivo(dato: str) -> str:
    ..

!🧪 RESULTADO ESPERADO EN CONSOLA (ejemplo)

Ingrese un dato a buscar: Gabo
✅ 'Gabo' fue encontrado en el archivo.

Ingrese un dato a buscar: María
❌ 'María' NO se encuentra en el archivo.

📚 OPCIONAL (pero recomendado)

* Puedes imprimir toda la lista antes de buscar, como un pequeño “registro visual”
* Puedes hacer que la búsqueda sea insensible a mayúsculas (`.lower()` en ambas partes)
* Recuerda embebido: consola, archivo, y teoría arriba si deseas mantener tu estructura
"""
#==========================================================================================================================================
def buscar_en_archivo(dato: str) -> str:

    lineas_limpias = []
    encontrado = False


    try:
        with open("registro.txt", "r", encoding="UTF-8") as archivo:
            lineas = archivo.readlines()
        lista_limpia = [linea.strip().lower() for linea in lineas]
        lineas_limpias = lista_limpia 

        print("\nContenido del archivo (limpio y en minúsculas):")
        for linea_individual in lineas_limpias:
            print(linea_individual)
        print("-" * 40)

        dato_a_buscar_lower = dato.strip().lower()

        for linea_en_lista in lineas_limpias:
            if dato_a_buscar_lower in linea_en_lista: 
                encontrado = True
                break 

        if encontrado: 
            return f"❇️ [{dato}] fue encontrado en el archivo."
        else:
            return f"💥 [{dato}] no se encontro en el archivo."

    except FileNotFoundError:
        return f"⚠️ El archivo 'registro.txt' no existe todavia."
    except Exception as e:
        return f"❌ Ocurrió un error inesperado al leer el archivo: {e}"
    finally:
        print("\n✅ Operación de búsqueda finalizada.")

dato_a_buscar = input("🆎 Ingrese un dato a buscar: ")
resultado = buscar_en_archivo(dato_a_buscar)
print(resultado)

#==========================================================================================================================================

#! === CONTENIDO DEL ARCHIVO EN EL QUE SE BUSCAN LOS DATODS === #!
"""
Este es el contenido de prueba para mi archivo de registro.
Esta es una segunda línea de texto.
Esta es una nueva línea añadida al final.
Albert Einstein dijo:

La imaginación es más importante que el conocimiento. El conocimiento es limitado, mientras que la imaginación abarca todo el mundo

"""
#==========================================================================================================================================
#! === RESULTADO DE DIFERENTES PRUEVAS DEL PROGRAMA "RESPUESTA DE CONSOLA" === #!
#*_RESPUESTA 1
"""
🆎 Ingrese un dato a buscar: Albert Einstein dijo:

Contenido del archivo (limpio y en minúsculas):
este es el contenido de prueba para mi archivo de registro.
esta es una segunda línea de texto.
esta es una nueva línea añadida al final.
albert einstein dijo:

la imaginación es más importante que el conocimiento. el conocimiento es limitado, mientras que la imaginación abarca todo el mundo
----------------------------------------

✅ Operación de búsqueda finalizada.
❇️ [Albert Einstein dijo:] fue encontrado en el archivo.
"""

#*_RESPUESTA 2
"""
🆎 Ingrese un dato a buscar: MUNDO

Contenido del archivo (limpio y en minúsculas):
este es el contenido de prueba para mi archivo de registro.
esta es una segunda línea de texto.
esta es una nueva línea añadida al final.
albert einstein dijo:

la imaginación es más importante que el conocimiento. el conocimiento es limitado, mientras que la imaginación abarca todo el mundo
----------------------------------------

✅ Operación de búsqueda finalizada.
❇️ [MUNDO] fue encontrado en el archivo.
"""

#*_RESPUESTA 3
"""
🆎 Ingrese un dato a buscar: CUBA

Contenido del archivo (limpio y en minúsculas):
este es el contenido de prueba para mi archivo de registro.
esta es una segunda línea de texto.
esta es una nueva línea añadida al final.
albert einstein dijo:

la imaginación es más importante que el conocimiento. el conocimiento es limitado, mientras que la imaginación abarca todo el mundo
----------------------------------------

✅ Operación de búsqueda finalizada.
💥 [CUBA] no se encontro en el archivo.
"""

#*_RESPUESTA 4
"""
🆎 Ingrese un dato a buscar: R

Contenido del archivo (limpio y en minúsculas):
este es el contenido de prueba para mi archivo de registro.
esta es una segunda línea de texto.
esta es una nueva línea añadida al final.
albert einstein dijo:

la imaginación es más importante que el conocimiento. el conocimiento es limitado, mientras que la imaginación abarca todo el mundo
----------------------------------------

✅ Operación de búsqueda finalizada.
❇️ [R] fue encontrado en el archivo.
"""
#==========================================================================================================================================
#fin
