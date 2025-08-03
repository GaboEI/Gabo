"""
#! 🧠 CLASE 14  Manejo de errores: try, except, else, finally

#? 📘 Módulo 1 (Ampliado)  Clase 14 de 30

#? 🎯 Objetivo de esta clase
#todo: Aprender a manejar errores de forma controlada y elegante usando las estructuras que ofrece Python:

#!Palabra clave	              ¿Qué hace?

try	                          #?Intenta ejecutar un bloque de código “peligroso”
except	                      #?Captura errores si ocurrieron
else	                      #?Se ejecuta solo si no hubo errores en el try
finally	                      #?Se ejecuta siempre, haya o no errores (para cerrar archivos, limpiar memoria, etc.)
"""
#?🧱 Estructura general
#! ry:
    # Código que puede lanzar un error
#! except TipoDeError:
    # Código a ejecutar si ocurre ese error
#! else:
    # Código que se ejecuta si NO hay errores
#! finally:
    # Código que SIEMPRE se ejecuta

#?🎯 Ejemplo 1: división segura

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "❌ No puedes dividir entre cero"
    else:
        return f"✅ Resultado: {resultado}"
    finally:
        print("🧹 Operación finalizada")

print(dividir(10, 2))   # ✅ Resultado: 5.0
print(dividir(5, 0))    # ❌ No puedes dividir entre cero

"""
#?🧪 ¿Dónde lo vas a usar en tu vida como programador?
✅ Validación de formularios y entradas de usuario
✅ Conexiones a internet o a base de datos
✅ Apertura, lectura y escritura de archivos
✅ Automatización sin que el programa se caiga
✅ Manejo de errores en APIs y servidores

#!📘 Esta clase tiene 2 ejercicios prácticos:
*Nº	   Nombre del ejercicio	Concepto central
?1️⃣	División segura con try/except	Manejo básico de error
?2️⃣	Registro de usuarios con else y finally	Flujo completo de control
"""