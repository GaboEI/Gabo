#=== VALIDAR EDAD Y CATEGORIA ===
"""
Este ejercicio aplica validación de datos y clasificación por rangos usando condicionales.
La idea central es:
	1.	Solicitar la edad de una persona.
	2.	Validar que sea un número entero positivo y dentro de un rango lógico (por ejemplo, 0 a 120 años).
	3.	Clasificar a la persona en una categoría según la edad (niño, adolescente, adulto, adulto mayor, etc.).
	4.	Mostrar el resultado con un mensaje claro.

Definiciones clave:
	•	Validación de entrada: Comprobar que los datos son del tipo correcto y cumplen reglas de negocio.
	•	Clasificación por rangos: Asignar una etiqueta según un valor numérico que cae en un rango definido.
	•	Condicional múltiple (if / elif / else): Permite manejar más de dos posibles rutas lógicas.
"""


#=== SCRIPT ===
while True:
    edad_str = input("👉 Por favor, introduce tu edad: ")
    try:
        edad = int(edad_str)
        if 0 <= edad <= 120:
            break
        else:
            print(f"⚠️ ¡Error! La edad '{edad}' no es un valor lógico. Por favor, introduce una edad entre 0 y 120.")
            
    except ValueError:
        print("❌ ¡Error! Eso no parece un número. Por favor, introduce un número entero.")

if edad < 13:
    categoria = "👶 Niño"
elif 13 <= edad < 18:
    categoria = "🧑‍🦱 Adolescente"
elif 18 <= edad < 65:
    categoria = "👨 Adulto"
else:  
    categoria = "👵 Adulto mayor"

print(f"🎉 ¡Genial! Tu categoría es: **{categoria}**.")
print("¡Gracias por usar nuestro programa! 😊")

#=== REAPUESTAS DE CONSOLA ===
"""
Ejemplo 1: Entrada válida
Salida de la consola:
👉 Por favor, introduce tu edad: 35
🎉 ¡Genial! Tu categoría es: **👨 Adulto**.
¡Gracias por usar nuestro programa! 😊

Ejemplo 2: Entrada no numérica
Salida de la consola:
👉 Por favor, introduce tu edad: hola
❌ ¡Error! Eso no parece un número. Por favor, introduce un número entero.
👉 Por favor, introduce tu edad: 25
🎉 ¡Genial! Tu categoría es: **👨 Adulto**.
¡Gracias por usar nuestro programa! 😊

Ejemplo 3: Entrada fuera de rango
Salida de la consola:
👉 Por favor, introduce tu edad: 150
⚠️ ¡Error! La edad '150' no es un valor lógico. Por favor, introduce una edad entre 0 y 120.
👉 Por favor, introduce tu edad: 17
🎉 ¡Genial! Tu categoría es: **🧑‍🦱 Adolescente**.
¡Gracias por usar nuestro programa! 😊
"""