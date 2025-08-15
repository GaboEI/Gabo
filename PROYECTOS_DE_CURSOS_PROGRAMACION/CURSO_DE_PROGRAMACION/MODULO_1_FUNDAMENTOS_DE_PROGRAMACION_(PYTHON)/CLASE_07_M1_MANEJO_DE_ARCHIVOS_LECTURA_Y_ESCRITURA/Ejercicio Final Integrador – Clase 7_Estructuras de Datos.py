#🟩 Ejercicio Final Integrador – Clase 7: Estructuras de Datos
#🎯 Objetivo:
#✅ Aplicar listas, tuplas, diccionarios y sets en un ejercicio realista y cotidiano como lo hace un programador en el día a día.
#🪐 Escenario:
# Estás creando un Script de Gestión de Tareas Personales que:
#1️⃣ Permita al usuario gestionar una lista de tareas del día (usando listas y .append(), .remove()).
#2️⃣ Muestre los días de la semana (tupla) y permita elegir el día para registrar las tareas.
#3️⃣ Guarde la información del usuario en un diccionario (nombre, edad, país, ciudad) y permita actualizar la ciudad si el usuario viaja.
#4️⃣ Permita gestionar un set con etiquetas de prioridad para las tareas del día, evitando duplicados.
#✅ Requerimientos:
#🔹 1. Listas:
# Crea una lista vacía tareas.
# Permite al usuario agregar 3 tareas usando .append().
# Permite eliminar una tarea indicando el nombre usando .remove().
# Imprime la lista final de tareas de forma clara.
#🔹 2. Tuplas:
# Crea una tupla dias_semana con los días de la semana.
# Permite al usuario seleccionar el día actual para registrar las tareas e imprímelo.
#🔹 3. Diccionarios:
# Crea un diccionario usuario con "nombre", "edad", "pais", "ciudad".
# Permite actualizar "ciudad" si el usuario indica que viajó.
# Imprime el diccionario ordenado con .items().
#🔹 4. Sets:
# Crea un set prioridades con etiquetas: {"alta", "media", "baja"}
# Permite al usuario agregar una nueva etiqueta (se agregará si no existe).
# Permite eliminar una etiqueta si lo desea.
# Imprime el set final de etiquetas de prioridad.
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#✅ Ejercicio Final Integrador – Clase 7


#1️⃣ Listas - Gestión de tareas
tareas = []
print(f"\n{Nombre}, Ingrrese a continuacion las tareas del dia")
for i in range(3):
    tarea = input(f"Tarea {i + 1}: ")
    tareas.append(tarea)
print("\n🟢 Tareas registradas:")
for t in tareas:
    print(f"• {t}") 
tarea_modificacion = input(f"\n{Nombre}, ¿Desea eliminar alguna tarea? (si/no) ").lower()
if tarea_modificacion in ["si", "sí"]:
    tarea_a_eliminar = input("\nIngrese la tarea que desea eliminar: ")
    if tarea_a_eliminar in tareas:
        tareas.remove(tarea_a_eliminar)
        print(f"\n🟢 La tarea '{tarea_a_eliminar}' ha sido eliminada correctamente.") 
    else:
        print(f"\n🔴 La tarea '{tarea_a_eliminar}' no se encuentra en la lista.")
else:
    print(f"\nGracias, {Nombre} por validar el dato")    
print(f"\n🟢 {Nombre},esta es tu lista final de tareas por hacer en el dia")
for final_tareas in tareas:
    print(f"- {final_tareas}")
#2️⃣ Tuplas - Días de la semana
dias_semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
print("\n🟢 Dias de la semana")
for idx, dia in enumerate(dias_semana):
    print(f"{idx +1}. {dia.capitalize()}")
seleccion = int(input("\nIngrese el numero del dia de la semana para de (1-7) para reguistras tus tareas: "))
if 1 <= seleccion <= 7:
    dia_elegido = dias_semana[seleccion - 1]
    print(f"\n🟢 Has seleccionado: {dia_elegido.capitalize()}")
else:
    print("\n🔴 Numero invalido, por favor selecciona un numero del 1 al 7")
#3️⃣ Diccionarios - Información del usuario
usuario = {
    "Nombre": "Gabo",
    "Edad": 26,
    "Pais": "Rusia",
    "Ciudad": "San Petersburgo"
    }
print("\nDatos Usuario")
for clave, valor in usuario.items():
    print(f"- {clave.capitalize()}: {valor}")
modificacion_1 = input("\n¿Has cambiado de Pais (si/no): ")
if modificacion_1 == "si":
    nuevo_pais = input("Ingrese el nombre de el nuevo pais: ")
    usuario["Pais"] = nuevo_pais
    print(f"🟢 Pais '{nuevo_pais}' modificado correctamente.")
else:
    print("Gracias por validar la informacion correcta.")
modificacion_2 = input("\n¿Has cambiado de ciudad (si/no): ").lower()
if modificacion_2 == "si":
    nueva_ciudad = input("Ingrese el nombre de la nueva ciudad: ")
    usuario["Ciudad"] = nueva_ciudad
    print(f"🟢 Ciudad '{nueva_ciudad}' modificada correctamente.")
else:
    print("Gracias por validar la informacion correcta.")
print(f"\n{Nombre} tus datos de an actualisados corectamente \nEstos serian tus datos nuevos")
for clave, valor in usuario.items():
    print(f" - {clave.capitalize()}: {valor}")
#4️⃣ Sets - Etiquetas de prioridad
print("\nEstas son tus prioridades actuales")
prioridades = {"alta", "media","baja"}
for etiquetas in prioridades:
    print(f"→ {etiquetas.capitalize()}")
nueva_etiquetas = input("\nPor favor ingresar el nuevo valor de la etiketa: ").lower()
prioridades.add(nueva_etiquetas)
eliminar = (f"\n¿Deseas eliminar alguna etiketa (si/no): ?")
if eliminar == "si":
    etiqueta_eliminar = input("Ingrese la etiketa qie quieres elominar: ")
    if etiqueta_eliminar in prioridades:
        prioridades.remove(etiqueta_eliminar)
        print(f"🟢Etiketa '{etiqueta_eliminar}' eliminada corectamente.")
    else:
        print(f"\n🔴 La etiketa {etiqueta_eliminar}' no se encuenta en el set.")
print("\n🟢🟢 Set final de etiketas de prioridad:")
for etiqueta in prioridades:
    print(f"• {etiqueta.capitalize()}")
print(f"\n🎉Muchas gracias {Nombre}, por usar el programa.")
