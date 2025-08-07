#================================================================================================================================
#!#!📄 Archivo sugerido: 03_unir_datos_join.py
#!🎯 Objetivo: Usar el método .join() para combinar múltiples piezas de información en una sola cadena de texto estructurada, 
#! estilo CSV o tabla profesional.

#====ESTILOS=====================================================================================================================
from colorama import init, Fore, Style
init(autoreset=True)

#====SCRIPT======================================================================================================================
while True:
    nombre_completo = input(Style.BRIGHT + Fore.CYAN + "👤 Por favor ingrese su nombre completo (solo letras y espacios): ")
    nombre_limpio = nombre_completo.strip()

    if not nombre_limpio:
        print(Fore.RED + "🚫 El nombre no puede estar vacío. Inténtelo nuevamente")
    elif not all(palabra.isalpha() for palabra in nombre_limpio.split()):
        print(Fore.YELLOW + "❌ El nombre solo puede contener letras. Inténtelo nuevamente")
    else:
        nombre_formateado = ' '.join(palabra.capitalize() for palabra in nombre_limpio.split())
        print(Fore.MAGENTA + "Nombre ingresado correctamente")
        print(Fore.GREEN + f"👋 {nombre_formateado} sea usted Bienvenido")
        break

# 2️⃣ Solicitar edad, validarla y convertirla a string
while True:
    try:
        edad_input = input(Style.BRIGHT + Fore.CYAN + "🎂 Ingrese su edad (número entero positivo): ").strip()
        edad = int(edad_input)  
        if edad <= 0:
            print(Fore.YELLOW + "❌ La edad debe ser un número positivo. Inténtelo nuevamente")
            continue
        edad = str(edad)  
        print(Fore.MAGENTA + "✅ Edad ingresada correctamente")
        break
    except ValueError:
        print(Fore.RED + "🚫 Error: La edad debe ser un número entero. Inténtelo nuevamente")
    except KeyboardInterrupt:
        print(Fore.RED + "\n🔚 Programa interrumpido por el usuario.")
        exit()

# 3️⃣ Solicitar país y limpiarlo
while True:
    pais = input(Style.BRIGHT + Fore.CYAN + "🌍 Ingrese su país (solo letras y espacios): ").strip()

    if not pais:
        print(Fore.RED + "🚫 El país no puede estar vacío. Inténtelo nuevamente")
    elif not all(palabra.isalpha() for palabra in pais.split()):
        print(Fore.YELLOW + "❌ El país solo puede contener letras. Inténtelo nuevamente")
    else:
        pais_formateado = ' '.join(palabra.capitalize() for palabra in pais.split())
        print(Fore.MAGENTA + "País ingresado correctamente")
        break

# 4️⃣ Crear una lista con los tres elementos
# Usamos nombre_formateado para mantener el formato con mayúsculas
datos = [nombre_formateado, edad, pais_formateado]

# 5️⃣ Aplicar .join() con coma como separador
resultado = ",".join(datos)

# 6️⃣ Mostrar el resultado final en consola
print(Style.BRIGHT + Fore.BLUE + "📋 Resultado final: " + resultado)

#====RESPUESTA DE LA CONSOLA=====================================================================================================
"""
Por favor ingrese su nombre completo (solo letras y espacios): GABO123
❌ El nombre solo puede contener letras. Inténtelo nuevamente
👤 Por favor ingrese su nombre completo (solo letras y espacios): 
🚫 El nombre no puede estar vacío. Inténtelo nuevamente
👤 Por favor ingrese su nombre completo (solo letras y espacios):        GABRIEL ESPINOSA izada
Nombre ingresado correctamente
👋 Gabriel Espinosa Izada sea usted Bienvenido
🎂 Ingrese su edad (número entero positivo): edad = 27a
🚫 Error: La edad debe ser un número entero. Inténtelo nuevamente
🎂 Ingrese su edad (número entero positivo): -9
❌ La edad debe ser un número positivo. Inténtelo nuevamente
🎂 Ingrese su edad (número entero positivo): 27
✅ Edad ingresada correctamente
🌍 Ingrese su país (solo letras y espacios): 123
❌ El país solo puede contener letras. Inténtelo nuevamente
🌍 Ingrese su país (solo letras y espacios): 😎Cuba
❌ El país solo puede contener letras. Inténtelo nuevamente
🌍 Ingrese su país (solo letras y espacios): Cuba
País ingresado correctamente
📋 Resultado final: Gabriel Espinosa Izada,27,Cuba
"""
#================================================================================================================================