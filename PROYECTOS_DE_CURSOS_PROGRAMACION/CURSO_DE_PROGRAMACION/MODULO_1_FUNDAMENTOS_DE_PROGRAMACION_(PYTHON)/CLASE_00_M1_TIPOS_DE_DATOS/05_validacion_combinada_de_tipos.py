# 05_validacion_combinada_de_tipos.py

# ✅ Ejercicio 05 — validacion_combinada_de_tipos
# Objetivo: Validar múltiples entradas simulando un formulario de sistema real

#1️⃣ FUNCIONES AUXILIARES

def es_nombre_valido(texto: str) -> bool:
    """Valida que el nombre no sea vacío ni solo espacios."""
    texto = texto.strip()
    return bool(texto) and any(c.isalpha() for c in texto)

def es_entero_valido(valor: str) -> bool:
    """Valida que un string representa un número entero (positivo o negativo)."""
    valor = valor.strip()
    return valor.lstrip("-").isdigit() and valor != "-"

def es_decimal_valido(valor: str) -> bool:
    """Valida si un string puede convertirse a float."""
    valor = valor.strip()
    if not valor:
        return False
    try:
        float(valor)
        return True
    except ValueError:
        return False

def interpretar_como_booleano(respuesta: str) -> bool | None:
    """Interpreta entradas tipo sí/no como booleano."""
    respuesta = respuesta.strip().lower().replace("ì", "í")
    respuestas_positivas = {"sí", "si", "s", "yes", "y", "yeah", "ok"}
    respuestas_negativas = {"no", "n", "nope"}
    if respuesta in respuestas_positivas:
        return True
    elif respuesta in respuestas_negativas:
        return False
    return None

#2️⃣ FUNCIÓN PRINCIPAL PARA EL FORMULARIO

def procesar_formulario() -> None:
    """Procesa el formulario con validaciones y reintentos."""
    print("📋 INGRESO DE DATOS\n")

    # Nombre
    while True:
        nombre = input("📝 Nombre completo: ").strip()
        if es_nombre_valido(nombre):
            nombre = " ".join(nombre.split())  # Normalizar espacios
            break
        print("❌ Nombre inválido: debe contener al menos una letra.")

    # Edad
    while True:
        edad_input = input("🔢 Edad: ").strip()
        if es_entero_valido(edad_input):
            edad = int(edad_input)
            if 0 < edad <= 150:  # Límite razonable para edad
                break
            print("❌ La edad debe estar entre 1 y 150 años.")
        else:
            print("❌ Edad inválida: debe ser un número entero.")

    # Salario
    while True:
        salario_input = input("💰 Salario mensual: ").strip()
        if es_decimal_valido(salario_input):
            salario = float(salario_input)
            if salario >= 0:  # Salario no negativo
                break
            print("❌ El salario no puede ser negativo.")
        else:
            print("❌ Salario inválido: debe ser un número decimal (ej. 1500.50).")

    # Términos
    while True:
        respuesta_terminos = input("✅ ¿Aceptas los términos y condiciones? (sí/no/s/n/yes/y): ")
        acepta = interpretar_como_booleano(respuesta_terminos)
        if acepta is not None:
            if acepta:
                break
            print("❌ No se puede continuar sin aceptar los términos.")
        else:
            print("❌ Respuesta no válida: usa 'sí', 'no', 's', 'n', 'yes', 'y', etc.")

    #3️⃣ SALIDA DE DATOS FINALES
    print("\n✅ DATOS REGISTRADOS:\n")
    print(f"👤 Nombre: {nombre.title()}")
    print(f"🎂 Edad: {edad} años")
    print(f"💵 Salario: ${salario:.2f}")
    print(f"📄 Términos aceptados: ✅ Sí")

#4️⃣ EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    procesar_formulario()

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
📋 INGRESO DE DATOS

📝 Nombre completo: John Doe
🔢 Edad: 30
💰 Salario mensual: 2500.75
✅ ¿Aceptas los términos y condiciones? (sí/no/s/n/yes/y): yes

✅ DATOS REGISTRADOS:

👤 Nombre: John Doe
🎂 Edad: 30 años
💵 Salario: $2500.75
📄 Términos aceptados: ✅ Sí
====================================================================
""" 
