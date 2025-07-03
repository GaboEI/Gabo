# Script para encontrar el numero faltante en una serie consecutiva de 1..n

def encontrar_faltante(numeros):
    n = len(numeros) + 1
    suma_esperada = n * (n + 1) // 2
    suma_real = sum(numeros)
    return suma_esperada - suma_real

if __name__ == "__main__":
    entrada = input("Ingresa una serie de numeros separados por espacio: ")
    lista = [int(x) for x in entrada.split()]
    faltante = encontrar_faltante(lista)
    print(f"El numero faltante es: {faltante}")
