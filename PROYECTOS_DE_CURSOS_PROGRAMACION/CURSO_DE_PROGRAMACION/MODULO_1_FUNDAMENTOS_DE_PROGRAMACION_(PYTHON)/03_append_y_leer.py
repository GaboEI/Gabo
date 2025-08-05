try:
    # 1️⃣ Solicitar al usuario el nombre del archivo
    nombre_archivo = input("Por favor, introduce el nombre del archivo al que deseas añadir una línea (se creará si no existe): ")

    # 2️⃣ Pedir al usuario la línea de texto a agregar
    linea_a_agregar = input("Introduce la línea de texto que deseas añadir: ")

    # Añadir un salto de línea al final para que siempre se escriba en una nueva línea
    linea_a_agregar += "\n"

    # 3️⃣ Abrir el archivo en modo append ("a") con codificación UTF-8
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(linea_a_agregar)

    # 4️⃣ Confirmar al usuario que el contenido fue agregado correctamente
    print(f"\n✅ Línea añadida con éxito al archivo '{nombre_archivo}'.")

    # 5️⃣ Reabrir el mismo archivo en modo lectura ("r") para mostrar el contenido actualizado
    print("\n--- Contenido actual del archivo ---")
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido_actualizado = archivo.read()
        # 6️⃣ Mostrar el contenido completo del archivo en consola
        print(contenido_actualizado)
    print("------------------------------------\n")

except Exception as e:
    print(f"\n❌ Ocurrió un error: {e}")

"""
Por favor, introduce el nombre del archivo al que deseas añadir una línea (se creará si no existe): mis_notas.txt
Introduce la línea de texto que deseas añadir: Esta es una nueva línea que quiero agregar.

✅ Línea añadida con éxito al archivo 'mis_notas.txt'.

--- Contenido actual del archivo ---
Este es un texto de prueba que estoy escribiendo en mi archivo. ¡Hola mundo!
Esta es una nueva línea que quiero agregar.

------------------------------------


Por favor, introduce el nombre del archivo al que deseas añadir una línea (se creará si no existe): mi_log.txt
Introduce la línea de texto que deseas añadir: Registro de inicio de sesión: Usuario 'admin'

✅ Línea añadida con éxito al archivo 'mi_log.txt'.

--- Contenido actual del archivo ---
Registro de inicio de sesión: Usuario 'admin'

------------------------------------
"""
