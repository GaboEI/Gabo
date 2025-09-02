# 03_agregar_y_modificar.py

# Lista inicial de personas
personas = [
    {"nombre": "Ana", "edad": 25, "pais": "España"},
    {"nombre": "Juan", "edad": 30, "pais": "México"},
    {"nombre": "Sofía", "edad": 22, "pais": "Argentina"}
]

while True:
    # Mostrar menú
    print("\nMenú de opciones:")
    print("1. Agregar nuevo registro")
    print("2. Modificar registro existente")
    print("Escribe 'salir' para terminar")
    
    # Solicitar opción
    opcion = input("Selecciona una opción: ").lower()
    
    # Salir del programa
    if opcion == "salir":
        break
    
    # Opción 1: Agregar nuevo registro
    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        # Comprobar si el nombre ya existe
        existe = False
        for persona in personas:
            if persona["nombre"].lower() == nombre.lower():
                existe = True
                break
        if existe:
            print("Error: El nombre ya existe en la lista.")
        else:
            try:
                edad = int(input("Ingresa la edad: "))
                pais = input("Ingresa el país: ")
                # Crear y agregar nuevo registro
                nuevo_registro = {"nombre": nombre, "edad": edad, "pais": pais}
                personas.append(nuevo_registro)
                print("Registro agregado correctamente.")
            except ValueError:
                print("Error: La edad debe ser un número entero.")
    
    # Opción 2: Modificar registro existente
    elif opcion == "2":
        nombre = input("Ingresa el nombre de la persona a modificar: ")
        encontrado = False
        for persona in personas:
            if persona["nombre"].lower() == nombre.lower():
                encontrado = True
                # Mostrar datos actuales
                print(f"\nDatos actuales: {persona}")
                # Solicitar nuevos datos
                nuevo_nombre = input("Nuevo nombre (presiona Enter para mantener el actual): ")
                nueva_edad = input("Nueva edad (presiona Enter para mantener la actual): ")
                nuevo_pais = input("Nuevo país (presiona Enter para mantener el actual): ")
                
                # Actualizar campos si se proporcionaron nuevos valores
                if nuevo_nombre:
                    persona["nombre"] = nuevo_nombre
                if nueva_edad:
                    try:
                        persona["edad"] = int(nueva_edad)
                    except ValueError:
                        print("Error: La edad debe ser un número entero. No se modificó la edad.")
                if nuevo_pais:
                    persona["pais"] = nuevo_pais
                print("Registro modificado correctamente.")
                break
        if not encontrado:
            print("No se encontró ese registro.")
    
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 'salir'.")

# Mostrar lista final
print("\nLista final de personas:")
for persona in personas:
    print(persona)

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: 1
Ingresa el nombre: Juan
Error: El nombre ya existe en la lista.

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: 1 
Ingresa el nombre: Ramon
Ingresa la edad: 24
Ingresa el país: Mexico
Registro agregado correctamente.

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: 2
Ingresa el nombre de la persona a modificar: Juan

Datos actuales: {'nombre': 'Juan', 'edad': 30, 'pais': 'México'}
Nuevo nombre (presiona Enter para mantener el actual): Juan Alberto
Nueva edad (presiona Enter para mantener la actual): 23
Nuevo país (presiona Enter para mantener el actual): Mexico
Registro modificado correctamente.

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: salir

Lista final de personas:
{'nombre': 'Ana', 'edad': 25, 'pais': 'España'}
{'nombre': 'Juan Alberto', 'edad': 23, 'pais': 'Mexico'}
{'nombre': 'Sofía', 'edad': 22, 'pais': 'Argentina'}
{'nombre': 'Ramon', 'edad': 24, 'pais': 'Mexico'}
====================================================================
"""