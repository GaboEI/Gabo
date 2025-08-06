try:
    # 1️⃣ Pedir al usuario el nombre del archivo a sobrescribir
    nombre_archivo = input("Introduce el nombre del archivo a sobrescribir (¡Advertencia: el contenido anterior se eliminará!): ")

    # 2️⃣ Pedir varias líneas nuevas de texto
    print("\nIntroduce el nuevo contenido para el archivo (pulsa Enter dos veces para finalizar):")
    lineas_nuevas = []
    while True:
        linea = input()
        if not linea:
            break
        lineas_nuevas.append(linea + "\n") # Añadir salto de línea para cada entrada

    # 3️⃣ Abrir el archivo en modo "w" (escritura)
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # 4️⃣ Escribir el nuevo contenido en el archivo
        archivo.writelines(lineas_nuevas)

    # 5️⃣ Confirmar la sobrescritura
    print(f"\n✅ Archivo '{nombre_archivo}' sobrescrito con éxito.")

    # 6️⃣ Reabrir el archivo en modo lectura ("r")
    print("\n--- Contenido actual del archivo ---")
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        # 7️⃣ Mostrar el nuevo contenido al usuario
        contenido_actualizado = archivo.read()
        print(contenido_actualizado)
    print("------------------------------------\n")

    # 8️⃣ Aclarar que todo lo anterior fue eliminado
    print("Recuerda: Todo el contenido anterior del archivo fue reemplazado por el texto que acabas de introducir.")

except Exception as e:
    print(f"\n❌ Ocurrió un error: {e}")