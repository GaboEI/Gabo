# 04_validar_y_contar_elementos.py

# Base de datos
estudiantes = [ 
    {"nombre": "Carlos López", "edad": 17, "pais": "México"},
    {"nombre": "Sofía Rodríguez", "edad": 20, "pais": "Argentina"},
    {"nombre": "Juan Martínez", "edad": 16, "pais": "México"},
    {"nombre": "Lucía Gómez", "edad": 22, "pais": "España"},
    {"nombre": "Miguel Sánchez", "edad": 19, "pais": "México"},
    {"nombre": "Ana García", "edad": 24, "pais": "Chile"},
    {"nombre": "Valeria Torres", "edad": 15, "pais": "Perú"},
    {"nombre": "Diego Fernández", "edad": 21, "pais": "Colombia"},
    {"nombre": "María Pérez", "edad": 18, "pais": "Brasil"},
    {"nombre": "Andrés Díaz", "edad": 23, "pais": "Estados Unidos"}
]

#contadores:
contador_mayores = 0
contador_menores = 0
contador_mexicanos = 0


for e in estudiantes:

    if "pais"  in e and "edad" in e:
        
        if e["edad"] >= 18:
            contador_mayores += 1

        if e["edad"] < 18:
            contador_menores += 1
        
        if e["pais"].lower() == "méxico":
            contador_mexicanos += 1
            porcentaje_mexicanos = (contador_mexicanos / 10) * 100
        
contadores_pais = {}
for e in estudiantes:
    contadores_pais[e["pais"]] = contadores_pais.get(e["pais"], 0) + 1

mayores_edad = []
for e in estudiantes:
    if "pais" in e and "edad" in e:
        if e["edad"] >= 18:
            mayores_edad.append(e["nombre"])




print(f"""
=== ESTADISTICAS ===
Contadores por país: {contadores_pais}
Nombres de mayores de edad:" {mayores_edad}
Total de mayores de edad: {contador_mayores}
Total de menores de edad: {contador_menores}
Total de personas mexicanas: {contador_mexicanos}
Porcentaje de personas mexicanas: {porcentaje_mexicanos}%
""")

"""
===============================
=== RESPUESTA DE CONSOLA ===
===============================
=== ESTADISTICAS ===
Contadores por país: {'México': 3, 'Argentina': 1, 'España': 1, 'Chile': 1, 'Perú': 1, 'Colombia': 1, 'Brasil': 1, 'Estados Unidos': 1}
Nombres de mayores de edad:" ['Sofía Rodríguez', 'Lucía Gómez', 'Miguel Sánchez', 'Ana García', 'Diego Fernández', 'María Pérez', 'Andrés Díaz']
Total de mayores de edad: 7
Total de menores de edad: 3
Total de personas mexicanas: 3
Porcentaje de personas mexicanas: 30.0%
===============================
"""