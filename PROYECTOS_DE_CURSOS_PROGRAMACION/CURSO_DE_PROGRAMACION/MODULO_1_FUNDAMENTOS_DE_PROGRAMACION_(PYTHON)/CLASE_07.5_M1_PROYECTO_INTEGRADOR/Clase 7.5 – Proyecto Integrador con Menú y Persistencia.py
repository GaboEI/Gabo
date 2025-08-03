# Clase 7.5 – Proyecto Integrador con Menú y Persistencia
#----------------------------------------------------------------------------------------
#-Datos iniciale
tareas = []
dias_semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
usuario = {"nombre": "Grabiel", "edad": 27, "pais": "Rusia", "siudad": "San Petersburgo"}
prioridades = {"Alta", "Baja", "Baja"}
#----------------------------------------------------------------------------------------
def gestionar_tareas():
    print("\nGestion de tareas")
    for i in range(3):
        tarea = input(f"Ingese la tare {i+1}: ")
        tareas.append(tarea)
    cambiar = input("¿Deseas eliminar una tarea? (si/no) ").lower()
    if cambiar in ["si", "sí"]:
        tarea_eliminar = input("Ingrrese la tarea a eliminar ")
        if tarea_eliminar in tareas:
            tareas.remove(tarea_eliminar)
            print(f"- '{tarea_eliminar}' eliminada con exito")
        else:
            print("Tare no encontrana")
    print("\n- Lista final de tareas")
    for t in tareas:
        print(f"- {t}")
#----------------------------------------------------------------------------------------
def seleccionar_dia():
    print("\n📌 Selección del Día")
    for idx, dia in enumerate(dias_semana):
        print(f"{idx+1}. {dia.capitalize()}")
    seleccion = int(input("Seleccione el número del día: "))
    if 1 <= seleccion <= 7:
        print(f"✅ Día seleccionado: {dias_semana[seleccion - 1].capitalize()}")
    else:
        print("⚠️ Selección inválida.")
def actualizar_usuario():
    print("\n📌 Datos del Usuario")
    for k, v in usuario.items():
        print(f"- {k.capitalize()}: {v}")
    modificacion_1 = input("\n¿Has cambiado de País (si/no): ").lower()
    if modificacion_1 in ["si", "sí"]:
        nuevo_pais = input("Ingrese el nombre del nuevo país: ")
        usuario["pais"] = nuevo_pais
        print(f"✅ País '{nuevo_pais}' modificado correctamente.")
    else:
        print("Gracias por validar la información correcta.")
    cambiar = input("¿Desea cambiar la ciudad? (si/no): ").lower()
    if cambiar in ["si", "sí"]:
        nueva_ciudad = input("Ingrese la nueva ciudad: ")
        usuario["ciudad"] = nueva_ciudad
        print(f"✅ Ciudad actualizada a {nueva_ciudad}.")
    print("\n✅ Datos actualizados:")
    for k, v in usuario.items():
        print(f"- {k.capitalize()}: {v}")

def gestionar_prioridades():
    print("\n📌 Gestión de Prioridades")
    print("Prioridades actuales:")
    for p in prioridades:
        print(f"- {p.capitalize()}")
    nueva = input("Ingrese una nueva prioridad: ").lower()
    prioridades.add(nueva)
    eliminar = input("¿Desea eliminar una prioridad? (si/no): ").lower()
    if eliminar in ["si", "sí"]:
        eliminar_p = input("Ingrese la prioridad a eliminar: ").lower()
        if eliminar_p in prioridades:
            prioridades.remove(eliminar_p)
            print(f"✅ '{eliminar_p}' eliminada correctamente.")
        else:
            print("⚠️ Prioridad no encontrada.")
    print("\n✅ Prioridades finales:")
    for p in prioridades:
        print(f"- {p.capitalize()}")

def ver_resumen():
    print("\n📌 Resumen Completo")
    print("Tareas:")
    for t in tareas:
        print(f"- {t}")
    print("\nUsuario:")
    for k, v in usuario.items():
        print(f"- {k.capitalize()}: {v}")
    print("\nPrioridades:")
    for p in prioridades:
        print(f"- {p.capitalize()}")

# Menú principal
while True:
    print("""
    === Menú Principal ===
    [1] Gestionar lista de tareas
    [2] Seleccionar día de la semana
    [3] Ver o actualizar datos de usuario
    [4] Gestionar etiquetas de prioridad
    [5] Ver resumen de todo
    [0] Salir
    """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        gestionar_tareas()
    elif opcion == "2":
        seleccionar_dia()
    elif opcion == "3":
        actualizar_usuario()
    elif opcion == "4":
        gestionar_prioridades()
    elif opcion == "5":
        ver_resumen()
    elif opcion == "0":
        print("✅ Gracias por usar el gestor de tareas, Gabo. ¡Hasta pronto!")
        break
    else:
        print("⚠️ Opción inválida. Intente nuevamente.")   

