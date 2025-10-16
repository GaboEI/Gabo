import csv

productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Teclado", "precio": 100, "stock": 25},
    {"nombre": "Ratón", "precio": 75, "stock": 40}
]

# Escritura
with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "stock"])
    escritor.writeheader()
    escritor.writerows(productos)

# Lectura
with open("productos.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila)