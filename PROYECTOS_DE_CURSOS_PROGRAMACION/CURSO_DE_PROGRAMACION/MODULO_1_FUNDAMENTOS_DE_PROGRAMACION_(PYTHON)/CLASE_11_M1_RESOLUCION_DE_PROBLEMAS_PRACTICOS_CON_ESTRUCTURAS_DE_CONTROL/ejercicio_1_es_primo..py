def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
num = int(input("ingrese un numero "))
if es_primo(num):
    print(f"El {num}, es primo")
else:
    print(f"El {num}, no es primo")