n = int(input("Ingrese el numero para generar el reporte: "))
# 1 tabla de multiplicar 
print(f"\nTabla de multiplicar del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 2 factorial 
factorial = 1
for i in range (1, n +1):
    factorial *= i 

print(f"\nEl factorial de {n} es: {factorial}")

# 3 suma de 1 a n 
suma = 0
for i in range(1, n + 1):
    
suma += i

print(f"\nLa suma de los numeros del 1 a {n} es: {suma}")

# 4 Mensaje Final 
print("\nGracias por usar el Generador de Reportes.")