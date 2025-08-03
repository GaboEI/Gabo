# Clase 9 – Proyecto Integrador Módulo 1
archivo_tareas = "tareas_gabo.txt"

# === AGREGAR TAREA ===
def agregar_tareas():
    tarea = input("Ingrese la tarea, ")                                     
    with open(archivo_tareas, "a", encoding="utf-8") as archivo:  
        archivo.write(f"P|{tarea}\n")                                         
    print("Tarea Agregada")

# === VER TAREAS ===
def ver_tarea():
    try:
        with open(archivo_tareas, "r", encoding="utf-8") as archivo:           
            tareas = archivo.readlines()
            if tareas:
                for idx, linea in enumerate(tareas, 1):
                    estado, tarea = linea.strip().split("|")
                    estado_legible = "Pendiente" if estado == "P" else "Completada"
                    print(f"{idx}. {estado_legible} {tarea}")
            else:
                print("No hay tareas registradas")               
    except FileNotFoundError:
        print("No existe el archivo aun. Agregue una tarea primero")

# === ELIMINAR TAREA ===
def eliminar_tarea():
    try:
        with open(archivo_tareas, "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()    
        if tareas:
            print("\nTareas actuales")
            for idx, linea in enumerate(tareas, 1):
                estado, tarea = linea.strip().split("|")
                estado_legible = "Pendiente" if estado == "P" else "Completada"
                print(f"{idx}. [{estado_legible}] {tarea}")
            numero = int(input("Ingrese el numero de la tarea a eliminar "))
            if 1 <= numero <= len(tareas):
                tarea_eliminada = tareas.pop(numero - 1)
                with open(archivo_tareas, "w", encoding="utf-8") as archivo:
                    archivo.writelines(tareas)  
                print(f"Tarea eliminada correctamente: {tarea_eliminada.strip()}")
            else:
                print("Numero de tarea invalido")
        else:
            print("No hay tareas a eliminar")
    except FileNotFoundError:
        print("No existe el archivo aun, agregue una tarea primero")

# === MARCAR COMPLETADA ===              
def marcar_completadas():
    with open("tareas_gabo.txt", "r", encoding="utf-8") as archivo:
        tareas_completadas = archivo.readlines()
    for idx, linea in enumerate(tareas_completadas, 1):
        estado, tarea = linea.strip().split("|")
        estado_legible = "Pendiente" if estado == "P" else "Completada"
        print(f"{idx}, [{estado_legible}] {tarea}")
    numero = int(input("Ingrese el numero de la tarea: "))
    if 1 <= numero <= len(tareas_completadas):
        estado, tarea = tareas_completadas[numero - 1].strip().split("|")
        if estado == "P":
            tareas_completadas[numero - 1] = f"C|{tarea}\n"
            print(f"Marcada como completada: {tarea}")        
        else:
            print(f"La tarea '{tarea}', ya estaba marcada como Completada.")
        with open("tareas_gabo.txt", "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas_completadas)

# === ESTADISTICAS ===        
def ver_estadisticas():
    try:
        with open("tareas_gabo.txt", "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()
        total = len(tareas)
        completadas = sum(1 for linea in tareas if linea.startswith("C|"))
        pendientes = sum(1 for linea in tareas if linea.startswith("P|"))
        print("\n=== Estadisticas de Tareas ===")
        print(f"Totas de tareas: {total}")
        print(f"Tarreas comppletadas: {completadas}")
        print(f"Tareas pendientes: {pendientes}")   
    except FileNotFoundError:
        print("El fichero no existe todavía, añada tareas para ver las estadísticas")

# === Menú Principal ===

while True:
    print("""
=== Gestor de Tareas de Gabo ===
[1] Agregar tarea
[2] Ver tareas
[3] Eliminar tarea
[4] Marcar tarea como completada
[5] Ver estadísticas
[0] Salir
""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tareas()
    elif opcion == "2":
        ver_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        marcar_completadas()
    elif opcion == "5":
        ver_estadisticas()
    elif opcion == "0":
        print("✅ Saliendo del gestor de tareas. ¡Buen trabajo, Gabo!")
        break
    else:
        print("⚠️ Opción inválida. Intente de nuevo.")