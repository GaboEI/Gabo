# ✅ Ejercicio Final Integrador - Clase 6
# 1️⃣ Función para imprimir la tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
# 2️⃣ Función para calcular el factorial
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial
# 3️⃣ Función para calcular la suma del 1 al numero
def calcular_suma(numero):
    suma = 0
    for i in range(1 + numero + 1):
        suma += i
    return suma
# 4️⃣ Captura del número del usuario
n = int(input("Ingrese el numero para generar el reporte: "))
# 5️⃣ Llamadas a las funciones
print(f"Tabla de multiplicar del {n}:")
tabla_multiplicar(n)
factorial = calcular_factorial(n)
print(f"\nEl factorial de {n} es: {factorial}")
suma = calcular_suma(n)
print(f"\nLa suma de los números del 1 a {n} es: {suma}")
# 6️⃣ Mensaje de cierre
print("\n✅ Gracias por usar el Generador de Reportes con Funciones.")