#=== 🟥 Ejercicio 5 – Validar código identificador #===
#📄 Archivo sugerido: 05_validar_codigo_identificador.py 
#!🎯 Objetivo: Verificar que un código ingresado por el usuario cumpla con una estructura específica 
#! (por ejemplo, empieza con una letra y sigue con números, o un formato de tipo ABC123).

#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
while True:
    codigo = input("Por favor, ingresa tu código de identificación (o 'salir' para terminar): ")
    if codigo.lower() == 'salir':
        print(Fore.YELLOW + "Programa terminado.")
        break

    codigo = codigo.strip()
    error_messages = []

    # Check length
    if len(codigo) != 6:
        error_messages.append("❌ El código debe tener exactamente 6 caracteres.")
    
    # Check for spaces
    if " " in codigo:
        error_messages.append("❌ El código no debe contener espacios.")
    
    # Check first three characters (letters)
    if len(codigo) >= 3:
        primeros_tres = codigo[:3]
        if not primeros_tres.isalpha():
            error_messages.append("❌ Los primeros tres caracteres deben ser letras.")
        elif primeros_tres != primeros_tres.upper():
            error_messages.append("❌ Los primeros tres caracteres deben ser letras mayúsculas.")
    
    # Check last three characters (digits)
    if len(codigo) >= 6:
        ultimos_tres = codigo[3:]
        if not ultimos_tres.isdigit():
            error_messages.append("❌ Los últimos tres caracteres deben ser dígitos.")

    # Output results
    if not error_messages:
        print(Fore.GREEN + "✅ ¡El código de identificación es válido!")
    else:
        for message in error_messages:
            print(Fore.RED + message)
        print(Fore.YELLOW + "Por favor, intenta de nuevo.")

#! === RESPUESTA DE CONSOLA === #!
"""
Por favor, ingresa tu código de identificación (o 'salir' para terminar): AAA22045
❌ El código debe tener exactamente 6 caracteres.
Por favor, intenta de nuevo.
Por favor, ingresa tu código de identificación (o 'salir' para terminar): GAI980
✅ ¡El código de identificación es válido!
Por favor, ingresa tu código de identificación (o 'salir' para terminar): salir
Programa terminado.
"""