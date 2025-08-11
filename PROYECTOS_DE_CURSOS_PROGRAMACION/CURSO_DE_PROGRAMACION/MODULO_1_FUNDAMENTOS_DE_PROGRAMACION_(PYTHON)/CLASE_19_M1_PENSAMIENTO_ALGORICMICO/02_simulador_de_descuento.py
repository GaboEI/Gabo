#=== SIMULADOR DE DESCUENTO ===#
"""
! Este ejercicio aplica cálculo de descuentos con condicionales.
La lógica principal consiste en:
1- Recibir el precio y la cantidad de un producto.
2- Determinar si se aplica un descuento según una condición (por ejemplo, cantidad mínima o monto total).
3- Calcular el precio final considerando el descuento si aplica.
4- Mostrar al usuario el detalle del precio: subtotal, descuento aplicado (o no) y total a pagar.
! Definiciones clave:
* Descuento porcentual: reducción expresada como porcentaje del precio original (ej. 15%).
* Condicional (if / else): estructura que decide si aplicar el descuento.
* Validación: asegurarse de que la cantidad y el precio no sean negativos o cero.
"""

#=== SCRIPT ===#
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

subtotal = precio_unitario * cantidad

if cantidad > 5:

    descuento = subtotal * 0.10  
else:
    descuento = 0

total_final = subtotal - descuento

print(f"Subtotal: ${subtotal:.2f}")
if descuento > 0:
    print(f"Descuento aplicado (10%): ${descuento:.2f}")
else:
    print("No se aplicó descuento.")
print(f"Total final: ${total_final:.2f}")

#=== RESPUESTA DE LA CONSOLA ===#
"""
EJEMPLO 1:
Ingrese el precio unitario del producto: 77
Ingrese la cantidad de productos: 5
Subtotal: $385.00
No se aplicó descuento.
Total final: $385.00
"""