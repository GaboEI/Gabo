
#! === 🟪 Ejercicio 3 – Reemplazar palabras prohibidas por asteriscos === #!
"""
🎯 Objetivo: Detectar si una frase contiene una palabra "prohibida" (por ejemplo, groserías, 
spam, etc.) y reemplazarla por asteriscos *****, sin alterar el resto del texto.
"""
#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
frase = input(Fore.CYAN + "Ingrese una frase: ")
palabra_prohibida = input(Fore.CYAN + "😎 Ingrese la palabra prohibida: ")

# Limpiar entradas
frase_limpia = frase.strip()
palabra_limpia = palabra_prohibida.strip()

# Verificar y reemplazar
if palabra_limpia.lower() in frase_limpia.lower():
    # Reemplazar palabra (ignorando mayúsculas/minúsculas)
    frase_modificada = frase_limpia
    for palabra in frase_limpia.split():
        if palabra.lower() == palabra_limpia.lower():
            frase_modificada = frase_modificada.replace(palabra, "*" * len(palabra))
    print(Fore.GREEN + f"Frase modificada: {frase_modificada}")
else:
    print(Fore.YELLOW + "La palabra prohibida no fue encontrada en la frase.")

#! === RESPUESTA DE CONSOLA === #!
"""
Ingrese una frase: No hay caminos para la paz; la paz es el camino 
😎 Ingrese la palabra prohibida: caminos
Frase modificada: No hay ******* para la paz; la paz es el camino
"""