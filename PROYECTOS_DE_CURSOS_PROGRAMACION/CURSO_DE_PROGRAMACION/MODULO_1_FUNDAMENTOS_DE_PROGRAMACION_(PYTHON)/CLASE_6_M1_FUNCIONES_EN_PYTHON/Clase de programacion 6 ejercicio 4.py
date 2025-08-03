# ✅ Ejercicio 4: Función de Factorial
def Calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
        
    return factorial

n = int(input("Ingrese el numero para calcular su factorial; "))
resultado = Calcular_factorial(n)
print(f"\nEl factorial de {n} es: {resultado}")