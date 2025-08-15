# 04_tipo_dato_booleano.py

# ✅ Ejercicio 04 — tipo_dato_booleano
# Objetivo: Interpretar respuestas como valores booleanos

#1️⃣ Función pura que interpreta una respuesta de texto como booleano
def interpretar_como_booleano(respuesta: str) -> bool | None:
    """
    Convierte una cadena tipo sí/no a un valor booleano.
    Retorna:
    - True para afirmaciones
    - False para negaciones
    - None si no se reconoce
    """
    # Normalizar entrada: eliminar espacios y convertir a minúsculas
    respuesta = respuesta.strip().lower()
    respuesta = respuesta.replace("ì", "í")  # Corregir posibles acentos

    respuestas_positivas = {"sí", "si", "s", "yes", "y", "yeah", "ok"}
    respuestas_negativas = {"no", "n", "nope"}

    if respuesta in respuestas_positivas:
        return True
    elif respuesta in respuestas_negativas:
        return False
    else:
        return None

#2️⃣ Entrada del usuario
entrada = input("🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): ")

#3️⃣ Interpretar como booleano
valor = interpretar_como_booleano(entrada)

#4️⃣ Mostrar resultados
print()  # Nueva línea para mejor legibilidad
if valor is True:
    print("✅ Continuamos con el proceso.")
elif valor is False:
    print("🛑 Proceso cancelado por el usuario.")
else:
    print("❌ Respuesta no válida. Debes responder con 'sí', 'no', 's', 'n', 'yes', 'y', etc.")

"""
=========================================================================================
=== RESPUESTA DE CONSOLA ===
=========================================================================================
🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): sí
✅ Continuamos con el proceso.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): No
🛑 Proceso cancelado por el usuario.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): y
✅ Continuamos con el proceso.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): yeah
✅ Continuamos con el proceso.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): nope
🛑 Proceso cancelado por el usuario.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): maybe
❌ Respuesta no válida. Debes responder con 'sí', 'no', 's', 'n', 'yes', 'y', etc.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y):   
❌ Respuesta no válida. Debes responder con 'sí', 'no', 's', 'n', 'yes', 'y', etc.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): sì
✅ Continuamos con el proceso.
=========================================================================================
""" 