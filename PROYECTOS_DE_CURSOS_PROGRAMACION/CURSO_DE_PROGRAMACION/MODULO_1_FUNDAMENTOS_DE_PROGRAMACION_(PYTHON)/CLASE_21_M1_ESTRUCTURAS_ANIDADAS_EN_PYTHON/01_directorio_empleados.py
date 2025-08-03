personas = [
    {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 25, "ciudad": "Barcelona"}
]
for i, persona in enumerate(personas):
    print(f"{i}:{persona["nombre"]},de la Ciudad de: {persona["ciudad"]}")