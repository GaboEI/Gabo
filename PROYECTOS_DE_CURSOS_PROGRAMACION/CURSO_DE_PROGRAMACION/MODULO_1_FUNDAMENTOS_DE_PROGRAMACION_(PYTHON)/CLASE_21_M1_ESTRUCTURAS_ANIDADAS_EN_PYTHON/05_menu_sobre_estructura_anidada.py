# 05_menu_sobre_estructura_anidada.py

# Base de datos
personas = [
    {"nombre": "Carlos López", "edad": 17, "pais": "México"},
    {"nombre": "Sofía Rodríguez", "edad": 20, "pais": "Argentina"},
    {"nombre": "Juan Martínez", "edad": 16, "pais": "México"},
    {"nombre": "Lucía Gómez", "edad": 22, "pais": "España"},
    {"nombre": "Miguel Sánchez", "edad": 19, "pais": "México"},
    {"nombre": "Ana García", "edad": 24, "pais": "Chile"},
    {"nombre": "Valeria Torres", "edad": 15, "pais": "Perú"},
    {"nombre": "Diego Fernández", "edad": 21, "pais": "Colombia"},
    {"nombre": "María Pérez", "edad": 18, "pais": "Brasil"},
    {"nombre": "Andrés Díaz", "edad": 23, "pais": "USA"}
]

def recorrer_lista():
    for p in personas:
        for clave, valor in p.items():
            print(clave, ":", valor)
    print()  # Salto de línea adicional

def mayor_18():
    mayores = [p for p in personas if p["edad"] >= 18]
    if mayores:
        for p in mayores:
            print(p)
    else:
        print("😔 No hay personas mayores de edad en la lista.")
    print()  # Salto de línea adicional

def buscador_pais():
    pais_buscado = input("🌍 ¡Hola! ¿Qué país te gustaría buscar? ")
    if not pais_buscado:
        print("⚠️ Por favor, ingresa un país válido. 😊")
        return
    contador_pais = 0
    for p in personas:
        if "pais" in p and p["pais"].lower() == pais_buscado.lower():
            print(f"🎉 {p['nombre']} - {p['edad']} años - {p['pais']}")
            contador_pais += 1
    if contador_pais == 0:
        print("😕 No se encontraron coincidencias para ese país.")
    else:
        print(f"🌟 ¡Coincidencias totales encontradas: {contador_pais}!")
    print()  # Salto de línea adicional

def personas_por_pais():
    nuevo_dic = {}
    for p in personas:
        if "pais" in p:
            pais = p["pais"]
            nuevo_dic[pais] = nuevo_dic.get(pais, 0) + 1
    if nuevo_dic:
        print("🌎 Países y cantidades:")
        print("-" * 20)
        for pais, cantidad in sorted(nuevo_dic.items(), key=lambda x: x[1], reverse=True):
            print(f"{pais:<10} | {cantidad} persona(s) 🌐")
    else:
        print("😔 No hay datos de países disponibles.")
    print()  # Salto de línea adicional

opciones = {
    1: recorrer_lista,
    2: mayor_18,
    3: buscador_pais,
    4: personas_por_pais
}

print("🎉 ¡Bienvenido al Menú de Personas! 🌟\nExplora la base de datos con estas opciones divertidas:")
while True:
    print("\n=== MENÚ PRINCIPAL === 🌈")
    print("1. 📋 Ver todos los registros")
    print("2. 🎂 Mostrar mayores de edad")
    print("3. 🌍 Buscar por país")
    print("4. 📊 Ver conteo por país")
    print("Escribe 'salir' para terminar 😊")
    
    entrada = input("Selecciona una opción: ")
    
    if entrada.lower() == "salir":
        print("\n🙋‍♂️ ¡Gracias por usar el programa! ¡Hasta luego! 🌟")
        break
    
    try:
        numero = int(entrada)
        if numero in opciones:
            opciones[numero]()   # Llamar a la función correspondiente
        else:
            print("\n⚠️ Oops! Esa opción no existe, elige otra. 😄")
    except ValueError:
        print("\n⚠️ Uy! Ingresa un número o 'salir', por favor. 😊")


"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
🎉 ¡Bienvenido al Menú de Personas! 🌟
Explora la base de datos con estas opciones divertidas:

=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 1
nombre : Carlos López
edad : 17
pais : México
nombre : Sofía Rodríguez
edad : 20
pais : Argentina
nombre : Juan Martínez
edad : 16
pais : México
nombre : Lucía Gómez
edad : 22
pais : España
nombre : Miguel Sánchez
edad : 19
pais : México
nombre : Ana García
edad : 24
pais : Chile
nombre : Valeria Torres
edad : 15
pais : Perú
nombre : Diego Fernández
edad : 21
pais : Colombia
nombre : María Pérez
edad : 18
pais : Brasil
nombre : Andrés Díaz
edad : 23
pais : USA


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 2
{'nombre': 'Sofía Rodríguez', 'edad': 20, 'pais': 'Argentina'}
{'nombre': 'Lucía Gómez', 'edad': 22, 'pais': 'España'}
{'nombre': 'Miguel Sánchez', 'edad': 19, 'pais': 'México'}
{'nombre': 'Ana García', 'edad': 24, 'pais': 'Chile'}
{'nombre': 'Diego Fernández', 'edad': 21, 'pais': 'Colombia'}
{'nombre': 'María Pérez', 'edad': 18, 'pais': 'Brasil'}
{'nombre': 'Andrés Díaz', 'edad': 23, 'pais': 'USA'}


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 3
🌍 ¡Hola! ¿Qué país te gustaría buscar? usa
🎉 Andrés Díaz - 23 años - USA
🌟 ¡Coincidencias totales encontradas: 1!


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 4
🌎 Países y cantidades:
--------------------
México     | 3 persona(s) 🌐
Argentina  | 1 persona(s) 🌐
España     | 1 persona(s) 🌐
Chile      | 1 persona(s) 🌐
Perú       | 1 persona(s) 🌐
Colombia   | 1 persona(s) 🌐
Brasil     | 1 persona(s) 🌐
USA        | 1 persona(s) 🌐


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: salir

🙋‍♂️ ¡Gracias por usar el programa! ¡Hasta luego! 🌟
====================================================================
"""