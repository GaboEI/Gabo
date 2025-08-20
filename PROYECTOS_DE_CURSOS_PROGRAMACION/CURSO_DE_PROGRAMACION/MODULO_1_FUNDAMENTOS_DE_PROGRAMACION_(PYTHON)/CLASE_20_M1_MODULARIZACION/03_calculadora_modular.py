# 🐍 calculadora_modular.py
# Calculadora que realiza operaciones básicas según el diagrama de flujo

def pedir_operacion():
    """Muestra un menú de operaciones, pide una opción y valida que sea válida."""
    
    while True:
        print("""
--------------------------
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------      
""")
        try:
            opcion = int(input("📧 Seleccione una operación (1-4): "))
            
            if opcion in [1, 2, 3, 4]:
                if opcion == 1:
                    return "suma"
                elif opcion == 2:
                    return "resta"
                elif opcion == 3:
                    return "multiplicación"
                else:
                    return "división"
            else:
                print("❌ Error: Debe ingresar un número entre 1 y 4.")
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")


def pedir_numeros():
    while True:
        try:
            num1 = float(input("🔢 Ingrese el primer número: "))
            num2 = float(input("🔢 Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("❌ Error: Debe ingresar números válidos.")


def calcular_resultado(op, num1, num2):
    """Calcula el resultado según la operación. Valida división por cero."""
    if op == "suma":
        return num1 + num2
    elif op == "resta":
        return num1 - num2
    elif op == "multiplicación":
        return num1 * num2
    elif op == "división":
        if num2 == 0:
            print("❌ Error: no se puede dividir por cero")
            return None
        return num1 / num2

def mostrar_resultado(resultado):
    if resultado is not None:
        print(f"🟩 El resultado es: {resultado:.2f}")


# Flujo principal
operacion = pedir_operacion()
numero1, numero2 = pedir_numeros()
resultado = calcular_resultado(operacion, numero1, numero2)
mostrar_resultado(resultado)

"""
=============================================
=== RESPUESTA DE CONSOLA ===
=============================================
OPCION INVALIDA:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 1
🔢 Ingrese el primer número: qq
❌ Error: Debe ingresar números válidos.

OPCION 1 SUMA :
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 1
🔢 Ingrese el primer número: 22
🔢 Ingrese el segundo número: 44.999
🟩 El resultado es: 67.00

OPCION 2 RESTA:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 2
🔢 Ingrese el primer número: 3
🔢 Ingrese el segundo número: 22.8905765
🟩 El resultado es: -19.89

OPCION 3 MULTIPLICACION:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 3
🔢 Ingrese el primer número: 78587
🔢 Ingrese el segundo número: 22.99999999999
🟩 El resultado es: 1807501.00

OPCION 4 DIVISION ENTRE CERO:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 4
🔢 Ingrese el primer número: 1
🔢 Ingrese el segundo número: 0
❌ Error: no se puede dividir por cero

OPCION 4 DIVISION:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 4
🔢 Ingrese el primer número: 2
🔢 Ingrese el segundo número: 454543645.4654             
🟩 El resultado es: 0.00
=============================================
"""