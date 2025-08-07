#================================================================================================================================
"""
🟩 Ejercicio 4  Extraer con slicing
📄 Archivo sugerido: 04_extraer_con_slicing.py
🎯 Objetivo: Usar la sintaxis de slicing ([inicio:fin:paso]) para extraer partes específicas de un string (como nombre, código, extensión, etc.).
"""

#====ESTILOS=====================================================================================================================
from colorama import init, Fore, Style
init(autoreset=True)

#====SCRIPT======================================================================================================================
texto = input(Fore.CYAN + "🆎 Por favor, ingresa una cadena de texto: " + Style.RESET_ALL).strip()


primeros_cuatro = texto[0:4]
ultimos_tres = texto[-3:]
subcadena = texto[3:9]
invertida = texto[::-1]

print(f"\n{Fore.GREEN}Resultados:{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Cadena original:{Style.RESET_ALL} {texto}")
print(f"{Fore.YELLOW}Primeros 4 caracteres:{Style.RESET_ALL} {primeros_cuatro}")
print(f"{Fore.YELLOW}Últimos 3 caracteres:{Style.RESET_ALL} {ultimos_tres}")
print(f"{Fore.YELLOW}Subcadena (posiciones 3 a 8):{Style.RESET_ALL} {subcadena}")
print(f"{Fore.YELLOW}Cadena invertida:{Style.RESET_ALL} {invertida}")

print(f"{Fore.YELLOW}Longitud de la cadena:{Style.RESET_ALL} {len(texto)}")

#====RESPUESTA DE LA CONSOLA=====================================================================================================
"""
🆎 Por favor, ingresa una cadena de texto: La vida es como un espejo: si sonríes, te devuelve la sonrisa

Resultados:
Cadena original: La vida es como un espejo: si sonríes, te devuelve la sonrisa
Primeros 4 caracteres: La v
Últimos 3 caracteres: isa
Subcadena (posiciones 3 a 8): vida e
Cadena invertida: asirnos al evleuved et ,seírnos is :ojepse nu omoc se adiv aL
Longitud de la cadena: 61
"""
#================================================================================================================================