print("*********************************************************")
print("""=== Ejercicio 3 - tala de multiplicar === 
📌Crea un programa que:
Pida al usuario un número.
Muestre la tabla de multiplicar de ese número del 1 al 10
# """)
print("*********************************************************\n")
while True:
    try:
        num = int(input("🔢 Introduce el número: "))
        if num < 0:
            print("No se admiten números negativos")
            continue
        break
    except ValueError:
        print("⚠️ I ntroduzca un número entero válido")
print("------------------------------------------")
print(f"📊 Tabla de multiplicar del número: {num}")
print("------------------------------------------")
for i in range(1, 11):
    resul = num * i
    print(f"{num} X {i} = {resul}")
print("👋 fin")