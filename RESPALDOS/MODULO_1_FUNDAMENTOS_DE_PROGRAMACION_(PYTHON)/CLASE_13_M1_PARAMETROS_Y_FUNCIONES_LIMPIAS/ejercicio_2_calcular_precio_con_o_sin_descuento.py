"""============================================================================
#!🧪 Ejercicio 2 Clase 13

#?📌 Nombre: Calcular precio con o sin descuento
#?🔑 Concepto: Función limpia + parámetro opcional + validación de rango

#todo🎯 ¿Qué debe hacer la función?

1️⃣ Recibir dos parámetros:
• precio_base → obligatorio #!(número positivo)
• descuento → opcional, por defecto 0 #!(debe estar entre 0 y 100)

2️⃣Verificar que los valores sean válidos:
• precio_base > 0
• 0 <= descuento <= 100

3️⃣ Si todo es correcto, calcular el precio final:
#!presio_final == precio_base * (1 - descuento / 100)

4️⃣ Si hay algún valor inválido, retornar #!None
5️⃣ Agregar un docstring explicando el propósito de la función, 
los parámetros y el retorno.
============================================================================"""
def calcular_precio_final(precio_base, descuento=0):

    """
    Calcula el precio final aplicando un descuento opcional.
    Parámetros:
    precio_base (float): Precio original. Debe ser mayor a 0.
    descuento (float): Porcentaje de descuento (0 a 100). Por defecto es 0.
    Retorna:
    float: Precio final con descuento, o None si los valores no son válidos.
    """

    if precio_base <= 0 or not (0 <= descuento <= 100):
        return None

    return precio_base * (1 - descuento / 100)

print(calcular_precio_final(100))           
print(calcular_precio_final(200, 5))       
print(calcular_precio_final(-10, 20))       
print(calcular_precio_final(150, 120))
print(calcular_precio_final(150, -85))
