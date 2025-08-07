#🟩 Ejercicio 1 – Dividir una frase en palabras
#!🎯 Objetivo: Usar el método .split() para convertir una cadena completa en una lista de palabras separadas.


#====ESTILOS=====================================================================================================================
from colorama import init, Fore, Style
init(autoreset=True)


#====SCRIPT======================================================================================================================
def procesar_frase():
    try:
        frase = input(Fore.GREEN +"✍️  Por favor escribe una frase ").strip().capitalize()
        if not frase:
            raise ValueError("La frase no puede estar vacía")


        palabras = frase.split()
        print(Fore.CYAN +f"📜 Lista de palabras: {palabras}")
        print(Fore.CYAN +f"🔢 total de palabras: {len(palabras)}")


        palabra_mas_larga = max(palabras, key=len)
        print(Fore.YELLOW + f"🕹️ Palabra mas larga: [{palabra_mas_larga}] con {len(palabra_mas_larga)} letsas")


        frecuencias = {palabra: palabras.count(palabra) for palabra in set(palabras)}
        print(Fore.MAGENTA + f"Frecuencia de palabras: {frecuencias}")


    except ValueError as e:
        print(Fore.RED +f"🚫 Error: {e}")
    except Exception as e:
        print(Fore.RED +f"⚠️ Error inesperado: {e}")


procesar_frase()


#====RESPUESTA DE LA CONSOLA=====================================================================================================
"""
✍️  Por favor escribe una frase Las cicatrices son recordatorios de que fuimos más fuertes que nuestras heridas.
📜 Lista de palabras: ['Las', 'cicatrices', 'son', 'recordatorios', 'de', 'que', 'fuimos', 'más', 'fuertes', 'que', 
'nuestras', 'heridas.']
🔢 total de palabras: 12
🕹️ Palabra mas larga: [recordatorios] con 13 letras
Frecuencia de palabras: {'fuertes': 1, 'de': 1, 'Las': 1, 'más': 1, 'recordatorios': 1, 'fuimos': 1, 'nuestras': 1, 'que': 
2, 'cicatrices': 1, 'heridas.': 1, 'son': 1}
"""
#================================================================================================================================
