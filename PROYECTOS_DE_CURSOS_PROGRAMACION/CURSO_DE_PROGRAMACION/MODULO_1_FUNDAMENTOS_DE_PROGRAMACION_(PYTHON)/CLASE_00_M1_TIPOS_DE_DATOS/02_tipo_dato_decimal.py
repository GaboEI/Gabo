# 02_tipo_dato_decimal.py

# ✅ Ejercicio 02 — tipo_dato_decimal
# Objetivo: Validar, convertir y operar con decimales en Python

#1️⃣ Función para verificar si un string puede interpretarse como float
def es_decimal_valido(valor: str) -> bool:
    """
    Retorna True si la cadena representa un número decimal válido (float).
    Acepta negativos, punto flotante, y formas como '.5' o '3.'.
    """
    # Eliminar espacios en blanco
    valor = valor.strip()
    if not valor:  # Verificar si la cadena está vacía
        return False
    try:
        float(valor)
        return True
    except ValueError:
        return False

#2️⃣ Solicitar entrada al usuario
entrada = input("🔢 Ingresa un número decimal: ")

#3️⃣ Validar usando la función
if es_decimal_valido(entrada):
    #4️⃣ Convertir a float
    numero = float(entrada)

    #5️⃣ Realizar operaciones
    mitad = numero / 2
    raiz = numero ** 0.5 if numero >= 0 else None  # Raíz solo si ≥ 0

    #6️⃣ Mostrar resultados con formato limitado a 4 decimales
    print(f"✅ Número ingresado: {numero:.4f}")
    print(f"📈 Dividido por 2: {mitad:.4f}")

    #7️⃣ Mostrar raíz cuadrada solo si válida
    if raiz is not None:
        print(f"📊 Raíz cuadrada: {raiz:.4f}")
    else:
        print("⚠️ No se puede calcular la raíz cuadrada de un número negativo.")
else:
    #8️⃣ Error en entrada no válida
    print("❌ El valor ingresado no es un número decimal válido.")

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
🔢 Ingresa un número decimal: 3.14
✅ Número ingresado: 3.1400
📈 Dividido por 2: 1.5700
📊 Raíz cuadrada: 1.7720

🔢 Ingresa un número decimal: -2.5
✅ Número ingresado: -2.5000
📈 Dividido por 2: -1.2500
⚠️ No se puede calcular la raíz cuadrada de un número negativo.

🔢 Ingresa un número decimal: abc
❌ El valor ingresado no es un número decimal válido.

🔢 Ingresa un número decimal:  .5
✅ Número ingresado: 0.5000
📈 Dividido por 2: 0.2500
📊 Raíz cuadrada: 0.7071

🔢 Ingresa un número decimal:  
❌ El valor ingresado no es un número decimal válido.
====================================================================
""" 