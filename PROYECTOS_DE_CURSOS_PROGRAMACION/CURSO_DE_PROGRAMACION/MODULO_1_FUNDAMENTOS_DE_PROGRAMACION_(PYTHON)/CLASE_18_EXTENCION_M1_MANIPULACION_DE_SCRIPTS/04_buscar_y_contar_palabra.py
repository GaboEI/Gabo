#! === 🟩 Ejercicio 4 – Buscar y contar palabra clave === #!
"""
🎯 Objetivo: Localizar la posición de la primera aparición 
de una palabra clave en un texto y contar cuántas veces aparece, 
usando .find() y .count().
"""
#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
while True:
    texto_original = input(Fore.MAGENTA + "🆎 Por favor ingrese el texto: ").strip().lower()
    palabra_clave = input(Fore.MAGENTA + "📜 Por favor ingrese la palabra clave: ").strip().lower()
    
    posicion = texto_original.find(palabra_clave)
    cantidad = texto_original.count(palabra_clave)  # Fixed: use variable instead of string literal

    if posicion == -1:
        print(Fore.RED + f"❌ No se encontró la palabra '{palabra_clave}'")
    else:
        # 6️⃣ Mostrar posición y número de repeticiones
        print(Fore.GREEN + f"✅ La palabra '{palabra_clave}' fue encontrada:")
        print(Fore.GREEN + f"   - Primera aparición en posición: {posicion}")
        print(Fore.GREEN + f"   - Número de repeticiones: {cantidad}")
    
    # Preguntar si desea continuar
    continuar = input(Fore.CYAN + "¿Desea analizar otro texto? (s/n): ").strip().lower()
    if continuar != 's':
        break

print(Fore.YELLOW + "🏁 Programa finalizado")

#! === RESPUESTA DE CONSOLA === #!
"""
🆎 Por favor ingrese el texto: No podemos resolver nuestros problemas con el mismo razonamiento que usamos cuando los creamos
📜 Por favor ingrese la palabra clave: resolver
✅ La palabra 'resolver' fue encontrada:
   - Primera aparición en posición: 11
   - Número de repeticiones: 1
¿Desea analizar otro texto? (s/n): s
🆎 Por favor ingrese el texto: Vive como si fueras a morir mañana; aprende como si fueras a vivir siempre
📜 Por favor ingrese la palabra clave: feliz
❌ No se encontró la palabra 'feliz'
¿Desea analizar otro texto? (s/n): n
🏁 Programa finalizado
"""