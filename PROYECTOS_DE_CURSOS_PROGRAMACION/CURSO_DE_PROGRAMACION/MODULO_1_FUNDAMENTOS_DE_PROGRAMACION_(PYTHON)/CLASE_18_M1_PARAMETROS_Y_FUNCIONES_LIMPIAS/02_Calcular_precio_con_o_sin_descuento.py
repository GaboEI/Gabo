"""
=======================================================================================
!🧪 EJERCICIO 2  CLASE 18
?📌 Nombre: Calcular precio con o sin descuento
🔑 Enfoque: lógica con parámetro opcional + función reutilizable

!🎯 ¿Qué debe hacer el script?
1️⃣ Definir una función llamada calcular_precio()
2️⃣ Recibir como parámetros: precio (obligatorio) | descuento (opcional, por defecto 0)
3️⃣ Validar que el descuento esté entre 0 y 100
4️⃣ Calcular el precio final
5️⃣ Retornar ese precio final
6️⃣ Mostrar el resultado en consola llamando a la función con y sin descuento

=======================================================================================
"""
def calcular_precio(precio: float, descuento: float = 0.0) -> float:
    """
    Calcula el precio final de un producto aplicando un descuento opcional.
    Parámetros:
    - precio (float): precio base del producto.
    - descuento (float, opcional): porcentaje de descuento entre 0 y 100. Por defecto 0.
    Retorna:
    - float: precio final después del descuento.
    """
    if precio <= 0:
        return "Error: el precio debe ser mayor que 0."
    if not 0 <= descuento <= 100:
        return "Error: el descuento debe estar entre 0 y 100."
    descuento_aplicado = precio * (descuento/100)
    precio_final = precio - descuento_aplicado
    return precio_final

resultado1 = calcular_precio(100,20)
print(f"Precio con descuento (100, 20%): {resultado1}")
resultado1 = calcular_precio(100)
print(f"Precio sin descuento 100: {resultado1}")
