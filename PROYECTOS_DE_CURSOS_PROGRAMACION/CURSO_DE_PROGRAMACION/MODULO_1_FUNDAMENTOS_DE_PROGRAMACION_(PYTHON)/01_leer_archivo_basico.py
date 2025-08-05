try:
    nombre_archivo = input("Por favor, introduce el nombre del archivo que deseas leer: ")

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

        print("\n--- Contenido del archivo ---")
        print(contenido)
        print("-----------------------------\n")

except FileNotFoundError:
    print(f"\n¡Error! El archivo '{nombre_archivo}' no fue encontrado. Asegúrate de que el nombre sea correcto y el archivo exista en la misma ubicación que el script.")
except Exception as e:
    print(f"\nOcurrió un error inesperado: {e}")
"""
Por favor, introduce el nombre del archivo que deseas leer: mi_documento.txt

--- Contenido del archivo ---
Hola, este es un archivo de prueba.
Contiene algunas líneas de texto.
¡Espero que lo leas bien!
-----------------------------


Por favor, introduce el nombre del archivo que deseas leer: archivo_inexistente.txt

¡Error! El archivo 'archivo_inexistente.txt' no fue encontrado. Asegúrate de que el nombre sea correcto y el archivo exista en la misma ubicación que el script.
"""
