try:
    # 1️⃣ Pedir al usuario el nombre del archivo
    nombre_archivo = input("Por favor, introduce el nombre del archivo que deseas crear o sobrescribir: ")

    # 2️⃣ Pedir al usuario el contenido a escribir
    contenido_a_escribir = input("Ahora, introduce el contenido que deseas guardar en el archivo: ")

    # 3️⃣ Abrir el archivo en modo escritura ("w") con codificación UTF-8 usando 'with'
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # 4️⃣ Escribir el contenido en el archivo
        archivo.write(contenido_a_escribir)

    # 5️⃣ Confirmar al usuario que la escritura fue exitosa
    print(f"\n✅ Archivo guardado correctamente como '{nombre_archivo}'")

except Exception as e:
    print(f"\n❌ Ocurrió un error al intentar escribir el archivo: {e}")
"""
Por favor, introduce el nombre del archivo que deseas crear o sobrescribir: mis_notas.txt
Ahora, introduce el contenido que deseas guardar en el archivo: Este es un texto de prueba que estoy escribiendo en mi archivo. ¡Hola mundo!

✅ Archivo guardado correctamente como 'mis_notas.txt'
"""
