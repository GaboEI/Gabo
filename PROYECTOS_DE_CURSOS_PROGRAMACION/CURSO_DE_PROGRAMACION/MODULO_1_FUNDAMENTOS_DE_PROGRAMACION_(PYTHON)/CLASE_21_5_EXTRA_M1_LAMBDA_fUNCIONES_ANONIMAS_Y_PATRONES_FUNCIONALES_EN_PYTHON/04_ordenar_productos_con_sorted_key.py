# 📝 04_ordenar_productos_con_sorted_key.py

productos = [
    ("teclado", 11.99),
    ("telefono", 100.75),
    ("audifono", 45.00)
    
]

# Ordenar por precio (menor a mayor)
print("\nProductos ordenados por precio (ascendente):")
print("-" * 45)
ordenados_precio = sorted(productos, key=lambda producto: producto[1])
for nombre, precio in ordenados_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f}")

# Ordenar por nombre alfabéticamente
print("\nProductos ordenados por nombre (alfabético):")
print("-" * 45)
ordenados_nombre = sorted(productos, key=lambda producto: producto[0])
for nombre, precio in ordenados_nombre:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f}")

# Ordenar por precio (mayor a menor)
print("\nProductos ordenados por precio (descendente):")
print("-" * 45)
ordenados_precio_desc = sorted(productos, key=lambda producto: producto[1], reverse=True)
for nombre, precio in ordenados_precio_desc:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f}")

"""
RESPUESTA TERRMINAL 
Productos ordenados por precio (ascendente):
---------------------------------------------
Producto: teclado      | Precio: $ 11.99
Producto: audifono     | Precio: $ 45.00
Producto: telefono     | Precio: $100.75

Productos ordenados por nombre (alfabético):
---------------------------------------------
Producto: audifono     | Precio: $ 45.00
Producto: teclado      | Precio: $ 11.99
Producto: telefono     | Precio: $100.75

Productos ordenados por precio (descendente):
---------------------------------------------
Producto: telefono     | Precio: $100.75
Producto: audifono     | Precio: $ 45.00
Producto: teclado      | Precio: $ 11.99
"""
