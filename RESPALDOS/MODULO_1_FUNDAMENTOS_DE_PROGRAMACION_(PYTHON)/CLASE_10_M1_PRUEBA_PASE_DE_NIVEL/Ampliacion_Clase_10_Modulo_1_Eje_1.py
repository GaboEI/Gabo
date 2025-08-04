# Archivo donde se guardarán los datos
archivo_txt = "estudiantes.txt"

# Función para cargar estudiantes desde archivo al iniciar
def cargar_estudiantes(nombre_archivo):
    estudiantes = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()[2:]  # Saltamos encabezado
            for linea in lineas:
                partes = linea.strip().split("|")
                if len(partes) == 4:
                    _, nombre, edad, nota = partes
                    estudiantes.append({
                        "nombre": nombre.strip(),
                        "edad": int(edad.strip()),
                        "nota": float(nota.strip())
                    })
    except FileNotFoundError:
        pass  # Si el archivo no existe, devolvemos lista vacía
    return estudiantes

# Función para imprimir estudiantes en consola
def imprimir_estudiantes(lista):
    print("\nLista de estudiantes")
    print("N° | Nombre      | Edad | Nota")
    print("-" * 32)
    for idx, est in enumerate(lista, 1):
        print(f"{idx:<2} | {est['nombre']:<11} | {est['edad']:<4} | {est['nota']:<5.2f}")

# Función para guardar en archivo txt
def guardar_en_txt(lista, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("Lista de estudiantes\n")
        archivo.write("N° | Nombre      | Edad | Nota\n")
        archivo.write("-" * 32 + "\n")
        for idx, est in enumerate(lista, 1):
            archivo.write(f"{idx:<2} | {est['nombre']:<11} | {est['edad']:<4} | {est['nota']:<5.2f}\n")
    print(f"\nArchivo '{nombre_archivo}' guardado correctamente.")

# ======================
# PROGRAMA PRINCIPAL
# ======================

estudiantes = cargar_estudiantes(archivo_txt)

while True:
    print("\n=== Menú ===")
    print("[1] Agregar estudiante")
    print("[2] Ver lista")
    print("[3] Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ").strip().capitalize()
        edad = int(input("Edad: "))
        nota = float(input("Nota: "))
        estudiantes.append({"nombre": nombre, "edad": edad, "nota": nota})
        guardar_en_txt(estudiantes, archivo_txt)

    elif opcion == "2":
        imprimir_estudiantes(estudiantes)

    elif opcion == "3":
        print(" Programa finalizado.")
        break

    else:
        print(" Opción inválida.")
