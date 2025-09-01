# 01_lista_de_diccionarios.py

personas = [
    {"nombre": "Gabriel", "edad": 27, "pais": "Cuba"},
    {"nombre": "Eduardo", "edad": 32, "pais": "USA"},
    {"nombre": "Roberto", "edad": 21, "pais": "Brasil"}
]

for persona in personas:
    
    if "nombre" in persona:
        print("nombre:", persona["nombre"].title())
    else:
        print("nombre: No Disponoble")
    
    
    if "edad" in persona:
        print("edad:", persona["edad"])
    else:
        print("edad: No Disponoble")
    
    
    if "pais" in persona:
        print("pais:", persona["pais"].capitalize())
    else:
        print("pais: No Disponoble")
    print("=" * 30)

"""
==============================
===   RESPUESTA DE CONSOLA ===
==============================
nombre: Gabriel
edad: 27
pais: Cuba
==============================
nombre: Eduardo
edad: 32
pais: Usa
==============================
nombre: Roberto
edad: 21
pais: Brasil
==============================
"""

