#===================================================================================================================
"""
#! 🧠 CLASE 19 EJERCICIO 3

#?📌 Nombre: Clasificar notas académicas con mensajes dinámicos
🔑 Tema central: múltiples condiciones `if / elif / else`, uso de rangos, funciones con retorno textual

#! 🎯 OBJETIVO DEL EJERCICIO
Crear una función que reciba una nota numérica (de 0 a 100)
y devuelva un mensaje de texto que clasifique esa nota** según un sistema de evaluación.
"""
#===================================================================================================================
def clasificar_nota(nota: float) -> str:

    if not (0 <= nota <= 100):
        return "❌ Nota inválida"
    elif 90 <= nota <= 100:
        return "🎓 Excelente"
    elif 75 <= nota < 90:
        return "👍 Muy bien"
    elif 60 <= nota < 75:
        return "🙂 Bien"
    elif 50 <= nota < 60:
        return "🟡 Aprobado justo"
    else:
        return "❌ Reprobado"
#todo#===================================================================================================================
while True:
    nombre_completo = input("Por favor, introduce tu nombre (solo letras y espacios): ")                                 
    nombre_limpio = nombre_completo.strip() 

    if not nombre_limpio:
        print("El nombre no puede estar vacío. Inténtalo de nuevo.")
    elif not all(word.isalpha() for word in nombre_limpio.split()):
        print("El nombre solo debe contener letras. Inténtalo de nuevo.")
    else:
        nombre_formateado = ' '.join(word.capitalize() for word in nombre_limpio.split())
        break
#todo#===================================================================================================================
while True:
    try:
        nota_str = input("Introduce tu nota (entre 0 y 100): ")
        nota = float(nota_str)
        if 0 <= nota <= 100:
            break
        else:
            print("La nota debe estar entre 0 y 100. Inténtalo de nuevo.")
    except ValueError:
        print("Eso no parece un número válido. Por favor, introduce un número.")

resultado = clasificar_nota(nota)
print(f"Hola {nombre_formateado}, tu nota es {nota} y tu desempeño es: {resultado}")
#===================================================================================================================
"""
=== RESPUESTA DE EJEMPLO TESTEADO EN CONSOLA ===

eje1:
Por favor, introduce tu nombre (solo letras y espacios): Gabriel espinosa Izada
Introduce tu nota (entre 0 y 100): 98.99999999999999999
Hola Gabriel Espinosa Izada, tu nota es 99.0 y tu desempeño es: 🎓 Excelente

eje2:
Por favor, introduce tu nombre (solo letras y espacios): gabo 123
El nombre solo debe contener letras. Inténtalo de nuevo.
Por favor, introduce tu nombre (solo letras y espacios): Gabo
Introduce tu nota (entre 0 y 100): 105
La nota debe estar entre 0 y 100. Inténtalo de nuevo.
Introduce tu nota (entre 0 y 100): 99.9999999999999999999999999999999
Hola Gabo, tu nota es 100.0 y tu desempeño es: 🎓 Excelente

eje3:
Por favor, introduce tu nombre (solo letras y espacios):                             CRISTINA espinosa Izada
Introduce tu nota (entre 0 y 100): dies 
Eso no parece un número válido. Por favor, introduce un número.
Introduce tu nota (entre 0 y 100): -80
La nota debe estar entre 0 y 100. Inténtalo de nuevo.
Introduce tu nota (entre 0 y 100): 108
La nota debe estar entre 0 y 100. Inténtalo de nuevo.
Introduce tu nota (entre 0 y 100): 55
Hola Cristina Espinosa Izada, tu nota es 55.0 y tu desempeño es: 🟡 Aprobado justo
"""
#===================================================================================================================