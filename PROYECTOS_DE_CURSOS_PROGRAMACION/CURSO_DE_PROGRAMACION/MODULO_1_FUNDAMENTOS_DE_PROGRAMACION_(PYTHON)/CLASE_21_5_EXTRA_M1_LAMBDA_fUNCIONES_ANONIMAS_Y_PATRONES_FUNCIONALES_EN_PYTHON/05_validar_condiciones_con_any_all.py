# 📝 05_validar_condiciones_con_any_all.py

#1️⃣ Crear una lista de precios de productos (enteros o float)
precios = [80, 110, 120, 95, 100, 150, 180, 200, 250, 300]

#2️⃣ Definir un valor mínimo aceptable
minimo  = 70

#3️⃣ Verificar si TODOS los precios son mayores o iguales al mínimo usando all()
resultado_all = all(m >= minimo for m in precios)

#4️⃣ Definir un valor de alerta para precios muy altos
alerta = 140

#5️⃣ Verificar si ALGÚN precio excede el valor de alerta usando any()
resultado_any = any(a > alerta for a in precios)

#6️⃣ Imprimir los resultados de ambas condiciones con mensajes claros
print(f"Todos los precios son mayores o iguales al mínimo: {resultado_all}")
print(f"Algún precio excede el valor de alerta: {resultado_any}")

#7️⃣ Mostrar “✅ Todo válido” o “⚠️ Hay precios fuera de rango” según el resultado
if resultado_all:
    print("✅ Todo válido")
else:
    print("⚠️ Hay precios fuera de rango")

#8️⃣ Reescribir una de las condiciones usando map() + lambda para practicar el patrón funcional
resultado_all_map = all(map(lambda x: x >= minimo, precios))
print(f"Todos los precios son mayores o iguales al mínimo: {resultado_all_map}")
resultado_any_map = any(map(lambda x: x > alerta, precios))
print(f"Algún precio excede el valor de alerta: {resultado_any_map}")

"""
RESPUESTA TERMINAL
Todos los precios son mayores o iguales al mínimo: True
Algún precio excede el valor de alerta: True
✅ Todo válido
Todos los precios son mayores o iguales al mínimo: True
Algún precio excede el valor de alerta: True
"""