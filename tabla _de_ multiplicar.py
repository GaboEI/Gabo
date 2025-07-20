print("*****************************")
print("* Tablas de multiplicar 📐 *")
print("*****************************\n")

try:
    limite = int(input("¿Hasta qué número quieres ver las tablas? (máximo 20): "))

    if limite < 1 or limite > 20:
        print("Error: Debes elegir un número entre 1 y 20.")
    else:
        # Cabeceras
        for tabla in range(1, limite + 1):
            print(f"Tabla del {tabla}".ljust(15), end="")
        print()  # salto de línea

        # Líneas de multiplicación
        for multiplicador in range(1, 11):
            for tabla in range(1, limite + 1):
                resultado = tabla * multiplicador
                print(f"{tabla} x {multiplicador} = {resultado}".ljust(15), end="")
            print()  # salto de línea

except ValueError:
    print("Error: Solo se permiten números enteros.")