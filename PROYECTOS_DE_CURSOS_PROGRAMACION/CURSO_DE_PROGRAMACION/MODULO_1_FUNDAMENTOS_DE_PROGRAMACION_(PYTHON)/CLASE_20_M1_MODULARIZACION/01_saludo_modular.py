# 🐍 EJERCICIO 1 saludo_modular.py
"""🎯 Objetivo: Aprender a separar la lógica de entrada, 
procesamiento y salida en funciones simples y reutilizables."""

def pedir_nombre():
    while True:
        nombre_completo = input("👤Ingrese su nombre y apellido: ").strip()
        palabras = nombre_completo.split()

        if not palabras:
            print("❌ No puede estar vacío")
            continue
        elif all(palabra.isalpha() for palabra in palabras):
            nombre_formateado = " ".join(p.capitalize() for p in palabras)
            print(f"✅ Nombre válido: {nombre_formateado}")
            
        else:
            print("❌ Solo se permiten letras en el nombre y apellido")
            continue
        return nombre_formateado

def saludar_usuario(nombre_formateado):
    print(f"¡Bienvenido, {nombre_formateado}! Es un placer saludarlo.")

nombre_usuario = pedir_nombre()
saludar_usuario(nombre_usuario)

"""
=============================================================
=== RESPUESTA DE CONSOLA ===
=============================================================

👤Ingrese su nombre y apellido: Gabriel123
❌ Solo se permiten letras en el nombre y apellido
👤Ingrese su nombre y apellido: 
❌ No puede estar vacío
👤Ingrese su nombre y apellido: GabRRIEL ESPINOSA IZADA
✅ Nombre válido: Gabrriel Espinosa Izada
¡Bienvenido, Gabrriel Espinosa Izada! Es un placer saludarlo.
=============================================================
"""