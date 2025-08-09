
#! === 🟪 Ejercicio 2 – Formatear nombre completo correctamente === #!
#? 🎯 Objetivo: Limpiar espacios innecesarios y capitalizar correctamente el 
#? nombre y apellido de una persona usando .strip() y .title()

#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
while True:
    nombre_completo = input(Style.BRIGHT + Fore.CYAN +"👤 Por favor ingrese su nombre completo (solo letras y espacios): ")
    nombre_limpio = nombre_completo.strip()

    if not nombre_limpio:
        print(Fore.RED +"🚫 El nombre no puede estar vacío. inténtelo nuevamente")
    elif not all(palabra.isalpha() for palabra in nombre_limpio.split()):
        print(Fore.YELLOW +"❌ Solo se permiten letras. No uses números ni símbolos.")
    else:
        nombre_formateado = ' '.join(palabra.title() for palabra in nombre_limpio.split())
        print(Fore.MAGENTA + "Nombre ingresado correctamente")
        print(Fore.CYAN + f"👋 {nombre_formateado} sea usted Bienvenido")
        break

#! === RESPUESTA DE CONSOLA === #!
"""
👤 Por favor ingrese su nombre completo (solo letras y espacios): gABO134
❌ El nombre solo puede contener letras. inténtelo nuevamente
👤 Por favor ingrese su nombre completo (solo letras y espacios):          gabriel ESPINOSA IZADA
Nombre ingresado correctamente
👋 Gabriel Espinosa Izada sea usted Bienvenido
"""