# Mini Proyecto: Gestor de Tareas con Persistencia

def agregar_tarea():
    tarea = input("Ingrese la tarea a agregar: ")
    with open("tareas_persistentes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")
    print(f"✅ Tarea '{tarea}' agregada correctamente.")

def ver_tareas():
    print("\n📋 Lista de Tareas:")
    try:
        with open("tareas_persistentes.txt", "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()
            if tareas:
                for idx, tarea in enumerate(tareas, 1):
                    print(f"{idx}. {tarea.strip()}")
            else:
                print("⚠️ No hay tareas registradas.")
    except FileNotFoundError:
        print("⚠️ El archivo aún no existe, agrega una tarea primero.")

def eliminar_tarea():
    ver_tareas()
    numero = int(input("Ingrese el número de la tarea a eliminar: "))
    try:
        with open("tareas_persistentes.txt", "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()
        if 0 < numero <= len(tareas):
            tarea_eliminada = tareas.pop(numero - 1)
            with open("tareas_persistentes.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(tareas)
            print(f"✅ Tarea '{tarea_eliminada.strip()}' eliminada correctamente.")
        else:
            print("⚠️ Número inválido.")
    except FileNotFoundError:
        print("⚠️ No hay archivo aún, agrega tareas primero.")

while True:
    print("""
=== Gestor de Tareas ===
[1] Agregar tarea
[2] Ver tareas
[3] Eliminar tarea
[0] Salir
""")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "0":
        print("✅ Saliendo del gestor de tareas. ¡Buen trabajo, Gabo!")
        break
    else:
        print("⚠️ Opción inválida, intente nuevamente.")