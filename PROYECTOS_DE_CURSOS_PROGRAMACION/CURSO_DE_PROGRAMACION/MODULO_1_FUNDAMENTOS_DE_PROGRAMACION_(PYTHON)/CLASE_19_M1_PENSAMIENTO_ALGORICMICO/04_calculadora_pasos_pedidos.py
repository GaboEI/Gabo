#===  Calculadora pasos pedidos ===#

#=== SCRIPT ===#
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio > 0:
            break  
        else:
            print("Error: El precio debe ser un número positivo. Inténtelo de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de productos: "))
        if cantidad > 0:
            break  
        else:
            print("Error: La cantidad debe ser un número entero positivo. Inténtelo de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número entero.")

subtotal = precio * cantidad
impuesto = subtotal * 0.08
envio = 5.0
total = subtotal + impuesto + envio

print("\n--- Desglose de la compra ---")
print(f"Subtotal: €{subtotal:.2f}")
print(f"Impuesto (8%): €{impuesto:.2f}")
print(f"Envío: €{envio:.2f}")
print("-----------------------------")
print(f"Total: €{total:.2f}")

#=== REAPUESTAS DE CONSOLA ===#
"""
Ejemplo 1:
Ingrese el precio del producto: 2000
Ingrese la cantidad de productos: 41

--- Desglose de la compra ---
Subtotal: €82000.00
Impuesto (8%): €6560.00
Envío: €5.00
-----------------------------
Total: €88565.00

Ejemplo 2:
Ingrese el precio del producto: redf**
Error: Entrada no válida. Por favor, ingrese un número.
Ingrese el precio del producto: 
"""