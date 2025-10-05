# 📝 06_analisis_funcional_de_inventario.py

#1️⃣ Crear una lista de productos como tuplas: (nombre, precio, stock)
productos = [
    ("Laptop", 450.00, 5),
    ("Mouse", 20.00, 10),
    ("Teclado", 30.00, 8),
    ("Monitor", 150.00, 3)   
]
print("Lista de productos original:")
print("-" * 45)
for nombre, precio, stock in productos:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#2️⃣ Usar filter() para seleccionar solo los productos con stock > 0
en_stock = list(filter(lambda p: p[2] > 0, productos))
print("Lista de productos con stock > 0:")
print("-" * 45)
for nombre, precio, stock in en_stock:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#3️⃣ Usar map() para aumentar el precio en 10% a cada producto disponible
aumento_precio = list(map(lambda p: (p[0], p[1] * 1.10, p[2]), en_stock))
print("Lista de productos con aumento de precio:")
print("-" * 45)
for nombre, precio, stock in aumento_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#4️⃣ Usar sorted() con key=lambda para ordenar por el nuevo precio (índice 1)
ordenado_precio = sorted(aumento_precio, key=lambda p: p[1])
print("Lista de productos ordenados por precio:")
print("-" * 45)
for nombre, precio, stock in ordenado_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#5️⃣ Usar any() para verificar si algún producto supera los $250
pista = any(p[1] > 250 for p in aumento_precio)
print(f"Algún producto supera los $250: {pista}")
print("\n")

#6️⃣ Imprimir los productos resultantes en formato tabular
#    👉 Usa f-strings con alineación
for nombre, precio, stock in ordenado_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")

#7️⃣ Aplicar otro filter() para mostrar solo productos cuyo nombre contenga una letra clave (ej: "a")
clave = "a"
producto_clave = list(filter(lambda p: clave in p[0], ordenado_precio))
print("Lista de productos con letra clave:")
print("-" * 45)
for nombre, precio, stock in producto_clave:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#8️⃣ Imprimir los productos resultantes en formato tabular
for nombre, precio, stock in producto_clave:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")

"""
Lista de productos original:
---------------------------------------------
Producto: Laptop       | Precio: $450.00 | Stock: 5
Producto: Mouse        | Precio: $ 20.00 | Stock: 10
Producto: Teclado      | Precio: $ 30.00 | Stock: 8
Producto: Monitor      | Precio: $150.00 | Stock: 3


Lista de productos con stock > 0:
---------------------------------------------
Producto: Laptop       | Precio: $450.00 | Stock: 5
Producto: Mouse        | Precio: $ 20.00 | Stock: 10
Producto: Teclado      | Precio: $ 30.00 | Stock: 8
Producto: Monitor      | Precio: $150.00 | Stock: 3


Lista de productos con aumento de precio:
---------------------------------------------
Producto: Laptop       | Precio: $495.00 | Stock: 5
Producto: Mouse        | Precio: $ 22.00 | Stock: 10
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Monitor      | Precio: $165.00 | Stock: 3


Lista de productos ordenados por precio:
---------------------------------------------
Producto: Mouse        | Precio: $ 22.00 | Stock: 10
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Monitor      | Precio: $165.00 | Stock: 3
Producto: Laptop       | Precio: $495.00 | Stock: 5


Algún producto supera los $250: True


Producto: Mouse        | Precio: $ 22.00 | Stock: 10
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Monitor      | Precio: $165.00 | Stock: 3
Producto: Laptop       | Precio: $495.00 | Stock: 5
Lista de productos con letra clave:
---------------------------------------------
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Laptop       | Precio: $495.00 | Stock: 5


Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Laptop       | Precio: $495.00 | Stock: 5
"""