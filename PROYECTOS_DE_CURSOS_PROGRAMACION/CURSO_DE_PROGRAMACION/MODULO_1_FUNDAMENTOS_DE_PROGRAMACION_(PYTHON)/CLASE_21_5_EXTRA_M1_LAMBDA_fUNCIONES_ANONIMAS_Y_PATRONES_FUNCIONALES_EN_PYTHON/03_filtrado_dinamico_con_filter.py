#📝 03_filtrar_precios_altos_con_filter.py

#1️⃣ Crear una lista de precios (pueden ser enteros o float)
precios = [10.3, 25.5, 8.5, 15.5, 100, 300, 4, 23, 5]

#2️⃣ Definir un valor umbral para considerar un precio “alto”
umbral = 115

#3️⃣ Aplicar filter() con una función lambda que conserve solo los precios mayores al umbral
#4️⃣ Convertir el resultado de filter() en una lista
precios_altos = list(filter(lambda x: x > umbral, precios))

#5️⃣ Imprimir la lista final de precios filtrados
print(f"Lista de precios filtrados: {precios_altos}")

#6️⃣ Mostrar la cantidad y el porcentaje de precios filtrados respecto al total
cantidad_precios_altos = len(precios_altos)
porcentaje_precios_altos = (cantidad_precios_altos / len(precios)) * 100
print(f"Cantidad de precios altos: {cantidad_precios_altos}")
print(f"Porcentaje de precios altos: {porcentaje_precios_altos:.2f}%")

#7️⃣ Mostrar una lista con los pares: precio original + estado ("✅ pasa" o "❌ no pasa")
for precio in precios:
    if precio > umbral:
        print(f"{precio:.2f} -> ✅ pasa")
    else:
        print(f"{precio:.2f} -> ❌ no pasa")

"""
RESPUESTA DE TERMINAL
Lista de precios filtrados: [100, 300]
Cantidad de precios altos: 2
Porcentaje de precios altos: 14.29%
10.30 -> ❌ no pasa
25.50 -> ❌ no pasa
8.50 -> ❌ no pasa
15.50 -> ❌ no pasa
100.00 -> ✅ pasa
300.00 -> ✅ pasa
"""