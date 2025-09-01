# 02_busqueda_en_diccionarios.py

#1️⃣ Crear una lista llamada "personas" con al menos 4 diccionarios
# Cada diccionario debe tener: "nombre", "edad", "pais"
persona = [
    {"nombre": "Gabriel", "edad": 27, "pais": "Cuba"},
    {"nombre": "Eduardo", "edad": 32, "pais": "USA"},
    {"nombre": "Roberto", "edad": 21, "pais": "Brasil"},
    {"nombre": "Juan", "edad": 25, "pais": "Ecuador"}
]

#2️⃣ Solicitar al usuario que ingrese el nombre que desea buscar
print("\n=== BÚSQUEDA DE PERSONAS ===")
busqueda = input("👤 Ingrese el nombre a buscar: ").strip().lower()

#3️⃣ Definir una variable bandera para saber si se encuentra o no el registro
encontrado = False

#4️⃣ Iniciar un bucle for que recorra la lista de diccionarios
for clave in persona:
    #5️⃣ Dentro del bucle:
    # Comparar si el valor de "nombre" coincide con lo ingresado por el usuario
    if busqueda in  clave["nombre"].lower():
        print("\n✅ Registro encontrado:")
        print(f"Nombre: {clave['nombre']}")
        print(f"Edad: {clave['edad']} años")
        print(f"Pais: {clave['pais']}")
        print("-" * 30)
        encontrado = True
        break

#6️⃣ Fuera del bucle:
# Si la bandera sigue siendo False, mostrar mensaje de “No se encontró el registro”
if not encontrado:
    print("\n ❌ No se encontró ningún registro con ese nombre.")

print("\n=== BÚSQUEDA FINALIZADA ===")

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
=== BÚSQUEDA DE PERSONAS ===
👤 Ingrese el nombre a buscar: Roberto

✅ Registro encontrado:
Nombre: Roberto
Edad: 21 años
Pais: Brasil
------------------------------

=== BÚSQUEDA FINALIZADA ===
====================================================================
=== BÚSQUEDA DE PERSONAS ===
👤 Ingrese el nombre a buscar: ardo

✅ Registro encontrado:
Nombre: Eduardo
Edad: 32 años
Pais: USA
------------------------------
=== BÚSQUEDA FINALIZADA ===
====================================================================
=== BÚSQUEDA DE PERSONAS ===
👤 Ingrese el nombre a buscar: python

❌ No se encontró ningún registro con ese nombre.

=== BÚSQUEDA FINALIZADA ===
====================================================================
"""

