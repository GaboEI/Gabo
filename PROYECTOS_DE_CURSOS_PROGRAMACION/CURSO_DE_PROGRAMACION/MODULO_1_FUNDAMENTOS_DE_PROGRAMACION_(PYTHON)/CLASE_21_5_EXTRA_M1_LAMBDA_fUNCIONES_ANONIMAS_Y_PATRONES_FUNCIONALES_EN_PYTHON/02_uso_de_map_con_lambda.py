# 📝 02_uso_de_map_con_lambda.py
"""
🎯: Simular un sistema de cálculo automático de precios finales con IVA 
incluido, usando `lambda` y `map()` para aplicar una operación matemática 
funcional a una lista de precios.
"""

# 1️⃣ Crear una lista de precios base (enteros o flotantes)
precios_base = [10.5, 77.5, 13, 10.59, 45.25, 40.5]
print(f"Lista de precios original: {[f'{precio:.2f}' for precio in precios_base]}")

# 2️⃣ y 3️⃣ Aplicar map() con lambda para calcular precios con IVA y convertir a lista
precios_con_iva = list(map(lambda p: p * 1.21, precios_base))

# 4️⃣ Imprimir la lista con precios con IVA (formateada a 2 decimales)
print(f"Lista de precios con 21% de IVA: {[f'{precio:.2f}' for precio in precios_con_iva]}")

# 5️⃣ Mostrar cada par: precio original → precio con IVA
print("\nPrecios originales -> Con IVA (21%)")
for original, con_iva in zip(precios_base, precios_con_iva):
    print(f"{original:.2f} -> {con_iva:.2f}")

# 6️⃣ (Opcional) Calcular el IVA total recaudado
suma_precios_base = sum(precios_base)
suma_precios_con_iva = sum(precios_con_iva)
iva_recaudado = suma_precios_con_iva - suma_precios_base
print(f"\nIVA total recaudado: {iva_recaudado:.2f}")

"""
RESPUESTA DE TERMINAL
Lista de precios original: 
['10.50', '77.50', '13.00', '10.59', '45.25', '40.50']

Lista de precios con 21% de IVA: 
['12.71', '93.77', '15.73', '12.81', '54.75', '49.00']

Precios originales -> Con IVA (21%)
10.50 -> 12.71
77.50 -> 93.77
13.00 -> 15.73
10.59 -> 12.81
45.25 -> 54.75
40.50 -> 49.00

IVA total recaudado: 41.44
"""