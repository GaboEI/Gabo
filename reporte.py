def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial


def calcular_suma(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    return suma


if __name__ == "__main__":
    n = int(input("Ingresa un número para generar el reporte: "))
    print(f"\nTabla de multiplicar del {n}:")
    tabla_multiplicar(n)

    factorial = calcular_factorial(n)
    print(f"\nEl factorial de {n} es: {factorial}")

    suma = calcular_suma(n)
    print(f"\nLa suma de los números del 1 a {n} es: {suma}")

    print("\n✅ Gracias por usar el Generador de Reportes con Funciones.")
