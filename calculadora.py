# Calculadora con historial

historial_archivo = "historial.txt"


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicacion de a y b."""
    return a * b


def dividir(a, b):
    """Devuelve la division de a entre b, validando b != 0."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def guardar_en_historial(texto):
    """Guarda una linea en el archivo de historial."""
    with open(historial_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")


def ver_historial():
    """Imprime el contenido del historial si existe."""
    try:
        with open(historial_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                print("\n=== Historial ===")
                print(contenido)
            else:
                print("\nHistorial vacío.")
    except FileNotFoundError:
        print("\nHistorial vacío.")


def limpiar_historial():
    """Limpia el archivo de historial."""
    open(historial_archivo, "w", encoding="utf-8").close()
    print("Historial limpiado.")


# Bucle principal con menú
if __name__ == "__main__":
    while True:
        print(
            """
=== Calculadora con Historial ===
[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir
[5] Ver historial
[6] Limpiar historial
[0] Salir
"""
        )
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                resultado = sumar(a, b)
                print(f"Resultado: {resultado}")
                guardar_en_historial(f"{a} + {b} = {resultado}")
            except ValueError:
                print("⚠️ Debe ingresar números válidos.")
        elif opcion == "2":
            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                resultado = restar(a, b)
                print(f"Resultado: {resultado}")
                guardar_en_historial(f"{a} - {b} = {resultado}")
            except ValueError:
                print("⚠️ Debe ingresar números válidos.")
        elif opcion == "3":
            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                resultado = multiplicar(a, b)
                print(f"Resultado: {resultado}")
                guardar_en_historial(f"{a} * {b} = {resultado}")
            except ValueError:
                print("⚠️ Debe ingresar números válidos.")
        elif opcion == "4":
            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                resultado = dividir(a, b)
                print(f"Resultado: {resultado}")
                guardar_en_historial(f"{a} / {b} = {resultado}")
            except ValueError as e:
                print(f"⚠️ Error: {e}")
        elif opcion == "5":
            ver_historial()
        elif opcion == "6":
            limpiar_historial()
        elif opcion == "0":
            break
        else:
            print("⚠️ Opción inválida.")
