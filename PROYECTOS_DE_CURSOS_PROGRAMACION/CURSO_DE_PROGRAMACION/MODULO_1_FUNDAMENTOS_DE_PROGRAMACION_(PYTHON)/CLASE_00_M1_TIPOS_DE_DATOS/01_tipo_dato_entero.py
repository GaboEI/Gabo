# 01_tipo_dato_entero.py

#1️⃣ Función que verifica si una cadena representa un entero válido
def es_entero_valido(valor: str) -> bool:
    """
    Retorna True si el valor puede convertirse a un int sin errores.
    """
    # Eliminar espacios en blanco y verificar si está vacío
    valor = valor.strip()
    if not valor:
        return False
    
    # Manejar el signo negativo
    valor = valor.lstrip("-")
    
    # Verificar si todos los caracteres restantes son dígitos
    return valor.isdigit()

#2️⃣ Solicitar entrada al usuario
entrada = input("🔢 Ingresa un número entero: ")

#3️⃣ Verificar si es válido usando la función
if es_entero_valido(entrada):
    #4️⃣ Convertir el string a entero
    numero = int(entrada)

    #5️⃣ Operaciones con el entero
    multiplicacion = numero * 2
    cuadrado = numero ** 2

    #6️⃣ Mostrar resultados con f-strings
    print(f"✅ Número ingresado: {numero}")
    print(f"📈 El número multiplicado por 2 es: {multiplicacion}")
    print(f"📊 El número al cuadrado es: {cuadrado}")
else:
    #7️⃣ Mensaje de error si no es entero válido
    print("❌ El valor ingresado no es un número entero válido.")

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
🔢 Ingresa un número entero: 55
✅ Número ingresado: 55
📈 El número multiplicado por 2 es: 110
📊 El número al cuadrado es: 3025
====================================================================
"""
