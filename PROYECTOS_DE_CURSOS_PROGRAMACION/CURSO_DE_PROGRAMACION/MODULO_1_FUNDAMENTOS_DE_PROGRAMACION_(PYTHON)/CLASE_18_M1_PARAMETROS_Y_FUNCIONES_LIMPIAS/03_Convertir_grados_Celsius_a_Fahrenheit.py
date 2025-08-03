"""
======================================================================================================
!🧪 EJERCICIO 3  CLASE 18
?📌 Nombre: Convertir grados Celsius a Fahrenheit
?🔑 Enfoque: función pura, documentada y matemáticamente precisa

!🎯 ¿Qué debe hacer el script?
1️⃣ Definir una función celsius_a_fahrenheit()
2️⃣ Recibir un solo parámetro obligatorio: grados_celsius
3️⃣ Calcular y retornar el resultado usando la fórmula oficial
4️⃣ Usar return, no print dentro de la función
5️⃣ Mostrar el resultado llamando a la función desde afuera

!🧠 TEORÍA  Conversión de unidades con funciones limpias

?1️⃣ ¿Qué es una conversión de unidades?
En programación, una conversión es transformar un valor expresado en una unidad a otra compatible.
En este caso: convertir grados Celsius a Fahrenheit, usando la fórmula matemática oficial:
TODO: [F = C * (9/5) + 32]
!Donde: 
⏺️C: grados Celsius (°C)
⏺️F: grados Fahrenheit (°F)

?2️⃣ ¿Por qué hacer esto con una función limpia?
Porque queremos que sea:
⏺️ Reutilizable 🔁
⏺️ Clara y profesional 💼
⏺️ Validada 📋
⏺️ Retornable sin imprimir directamente

?3️⃣ ¿Qué validaciones básicas puedes aplicar?
Puedes validar que la temperatura esté en un rango realista para evitar datos extremos 
(ej: menor que -273.15, que es el cero absoluto).
Aunque en este ejercicio no es obligatorio, puedes agregarlo como mejora pro si deseas.

?4️⃣ ¿Qué es round()?
Es una función de Python que redondea números decimales.
Ejemplo:
!round(34.567, 2)  # Devuelve: 34.57
La puedes usar para mostrar los grados con 1 o 2 decimales si quieres un resultado más limpio.

?5️⃣ ¿Cómo debería lucir una función bien escrita para esto?
⏺️ Con nombre claro
⏺️ Con parámetro obligatorio (celsius)
⏺️ Que use return
⏺️ Con docstring bien redactado
======================================================================================================
"""
def celsius_a_fahrenheit(grados_celsius: float) -> float:
    """    
    Convierte una temperatura de grados Celsius a Fahrenheit.    
    Parámetros:
    - grados_celsius (float): temperatura en grados Celsius.
    Retorna:
    - float: temperatura convertida en
    """
    grados_fahrenheit = grados_celsius * 9/5 + 32
    
    #3️⃣ Retornar el resultado, redondeado a 2 decimales
    return round(grados_fahrenheit, 2)

#4️⃣ Llamar a la función con al menos 2 temperaturas distintas
print(f"0 °C = {celsius_a_fahrenheit(0)} °F")  # 32.0 °F
print(f"25 °C = {celsius_a_fahrenheit(25)} °F")  # 77.0 °F