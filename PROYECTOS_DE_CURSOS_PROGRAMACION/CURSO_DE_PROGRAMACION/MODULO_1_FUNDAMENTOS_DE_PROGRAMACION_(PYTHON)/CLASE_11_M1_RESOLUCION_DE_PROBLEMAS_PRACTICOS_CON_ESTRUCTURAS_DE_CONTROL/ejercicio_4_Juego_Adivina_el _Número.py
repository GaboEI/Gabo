# === Ejercicio 4 – Juego: Adivina el Número ===
import random
def jugar():
    secreto = random.randint(1, 100)
    intentos = 0
    print("🎲 Bienvenido al juego: Adivina el número entre [1 y 100]\n")
    while True:
        try:
            num = int(input("🔢Ingresa tu intento: "))
            intentos += 1
            if num > secreto:
                print(f"⬆️ ¡Huy! El {num} es demassido alto, intente nuevamente\n")
            elif num < secreto:
                print(f"⬇️ ¡Huy! El {num} es demassido bajo, intente nuevamente\n")
            else:
                print(f"🎉 ¡Correcto! El número era {secreto}. Lo lograste en {intentos} intentos.\n")
                break
        except ValueError:
            print("🔴 Solo se permiten números enteros.")
jugar() 