# 🐍 06_calculadora_menu_funcional.py

def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")
    print("==================")

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("❌ Error: Opción debe estar entre 1 y 5")
        except ValueError:
            print("❌ Error: Ingrese un número válido")

def pedir_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("❌ Error: Ingrese números válidos")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def mostrar_resultado(resultado):
    print("\n==================")
    print(f"Resultado: {resultado}")
    print("==================\n")

def salir():
    print("\n¡Gracias por usar la calculadora!")
    print("👋 Programa finalizado")

def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 5:
            salir()
            break
            
        num1, num2 = pedir_numeros()
        
        try:
            if opcion == 1:
                resultado = sumar(num1, num2)
            elif opcion == 2:
                resultado = restar(num1, num2)
            elif opcion == 3:
                resultado = multiplicar(num1, num2)
            elif opcion == 4:
                resultado = dividir(num1, num2)
                
            mostrar_resultado(resultado)
            
        except ValueError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 1
Ingrese el primer número: 5
Ingrese el segundo número: 3

==================
Resultado: 8.0
==================

=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 4
Ingrese el primer número: 10
Ingrese el segundo número: 0
❌ Error: No se puede dividir por cero

=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 3
Ingrese el primer número: 4
Ingrese el segundo número: 5

==================
Resultado: 20.0
==================

=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 5

¡Gracias por usar la calculadora!
👋 Programa finalizado
====================================================================
"""