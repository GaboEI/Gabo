#================================================================================================================================
#!🟩 Ejercicio 2 – Limpieza de nombres con .strip()
#📄 Archivo sugerido: 02_limpieza_entrada_strip.py
#🎯 Objetivo: Usar .strip() para limpiar entradas de texto y validar que los nombres ingresados sean correctos y profesionales.

#====ESTILOS=====================================================================================================================
from colorama import init, Fore, Style
init(autoreset=True)

#====SCRIPT======================================================================================================================
while True:
    nombre_completo = input(Style.BRIGHT + Fore.CYAN +"👤 Por favor ingrese su nombre completo (solo letras y espacios): ")
    nombre_limpio = nombre_completo.strip()


    if not nombre_limpio:
        print(Fore.RED +"🚫 El nombre no puede estar vacío. inténtelo nuevamente")
    elif not all(palabra.isalpha() for palabra in nombre_limpio.split()):
        print(Fore.YELLOW +"❌ El nombre solo puede contener letras. inténtelo nuevamente")
    else:
        nombre_formateado = ' '.join(palabra.capitalize() for palabra in nombre_limpio.split())
        print(Fore.MAGENTA +"Nombre ingresado correctamente")
        print(Fore.GREEN +f"👋 {nombre_formateado} sea usted Bienvenido")
        break
#====RESPUESTA DE LA CONSOLA=====================================================================================================
"""
👤 Por favor ingrese su nombre completo (solo letras y espacios): Gabo9807
❌ El nombre solo puede contener letras. inténtelo nuevamente
👤 Por favor ingrese su nombre completo (solo letras y espacios): 
🚫 El nombre no puede estar vacío. inténtelo nuevamente
👤 Por favor ingrese su nombre completo (solo letras y espacios):            GABRIEL ESPINOSA izada
Nombre ingresado correctamente
👋 Gabriel Espinosa Izada sea usted Bienvenido
"""
#================================================================================================================================
