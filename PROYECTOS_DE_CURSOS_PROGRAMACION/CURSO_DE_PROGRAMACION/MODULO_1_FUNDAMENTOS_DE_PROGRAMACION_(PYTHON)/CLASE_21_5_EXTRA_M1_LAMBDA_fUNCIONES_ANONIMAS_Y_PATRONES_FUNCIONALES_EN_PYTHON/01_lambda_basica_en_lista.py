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

mayusculas = list(map(lambda persona: {
    "nombre": persona["nombre"].upper(),
    "edad": persona["edad"],
    "pais": persona["pais"].upper()
}, personas))
print(mayusculas)
