# 03_tipo_dato_texto.py

# ✅ Ejercicio 03 — tipo_dato_texto
# Objetivo: Validar y manipular texto ingresado por el usuario

#1️⃣ Función para validar que el nombre no esté vacío ni lleno de espacios
def es_nombre_valido(texto: str) -> bool:
    """
    Retorna True si el texto ingresado tiene al menos una letra real (no espacios).
    """
    texto = texto.strip()
    return bool(texto) and any(c.isalpha() for c in texto)

#2️⃣ Solicitar nombre completo al usuario
entrada = input("📝 Ingresa tu nombre completo: ")

#3️⃣ Verificar validez
if es_nombre_valido(entrada):
    # Normalizar espacios múltiples
    entrada = " ".join(entrada.split())

    #4️⃣ Mostrar formatos
    print(f"\n✅ Nombre ingresado: {entrada}")
    print(f"🔠 Mayúsculas: {entrada.upper()}")
    print(f"🔡 Minúsculas: {entrada.lower()}")
    print(f"🅰️ Capitalizado: {entrada.capitalize()}")
    print(f"📚 Formato título: {entrada.title()}")

    #5️⃣ Contar letras reales (solo caracteres alfabéticos)
    cantidad_letras = sum(c.isalpha() for c in entrada)
    print(f"🔢 Total de letras (sin espacios ni símbolos): {cantidad_letras}")

    #6️⃣ Mostrar primer nombre
    primer_nombre = entrada.split()[0] if entrada.split() else ""
    print(f"👤 Primer nombre: {primer_nombre}")
else:
    #7️⃣ Error si no es válido
    print("❌ Nombre inválido: debes ingresar texto con al menos una letra.")

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
📝 Ingresa tu nombre completo: John Doe
✅ Nombre ingresado: John Doe
🔠 Mayúsculas: JOHN DOE
🔡 Minúsculas: john doe
🅰️ Capitalizado: John doe
📚 Formato título: John Doe
🔢 Total de letras (sin espacios ni símbolos): 7
👤 Primer nombre: John

📝 Ingresa tu nombre completo:   Mary Jane Watson  
✅ Nombre ingresado: Mary Jane Watson
🔠 Mayúsculas: MARY JANE WATSON
🔡 Minúsculas: mary jane watson
🅰️ Capitalizado: Mary jane watson
📚 Formato título: Mary Jane Watson
🔢 Total de letras (sin espacios ni símbolos): 14
👤 Primer nombre: Mary

📝 Ingresa tu nombre completo: 123
❌ Nombre inválido: debes ingresar texto con al menos una letra.

📝 Ingresa tu nombre completo:   
❌ Nombre inválido: debes ingresar texto con al menos una letra.

📝 Ingresa tu nombre completo: John123 Doe
✅ Nombre ingresado: John123 Doe
🔠 Mayúsculas: JOHN123 DOE
🔡 Minúsculas: john123 doe
🅰️ Capitalizado: John123 doe
📚 Formato título: John123 Doe
🔢 Total de letras (sin espacios ni símbolos): 7
👤 Primer nombre: John123
====================================================================
""" 