#🧪 Ejercicio 04 — registro_usuarios_modular.py

"""🎯 Objetivo: Aplicar modularización para registrar información básica 
de usuarios: nombre, edad y correo, con validaciones y salida formateada."""

def pedir_nombre():
    
    while True:
        try:
            nombre_completo = input("Ingrese su nombre y apellido: ").strip()
            palabras = nombre_completo.split()
            if not palabras:
                print("❌ No puede estar vacío")
                continue
            if len(palabras) < 2:
                print("❌ Debe ingresar al menos un nombre y un apellido")
                continue
            elif all(palabra.isalpha() for palabra in palabras):
                nombre_formateado = " ".join(p.capitalize() for p in palabras)
                print(f"✅ Nombre válido: {nombre_formateado}")
                return nombre_formateado
            else:
                print("❌ Solo se permiten letras en el nombre y apellido")
        except KeyboardInterrupt:
            print("\n❌ Entrada cancelada por el usuario")
            return None

def pedir_edad(nombre_formateado):
    while True:
        try:
            entrada = input(f"{nombre_formateado}, ingrese su edad: ").strip()
            if not entrada:
                print(f"❌ {nombre_formateado}, el campo de la edad no puede estar vacío")
                continue
            edad = int(entrada)
            if edad <= 0 or edad > 120:
                print("❌ Error: esa edad parece falsa 🤔")
                continue
            print(f"🟩 {nombre_formateado}, su edad ha sido registrada con éxito")
            return edad
        except ValueError:
            print("❌ Error: ingrese un número válido para la edad")
        except KeyboardInterrupt:
            print("\n❌ Entrada cancelada por el usuario")
            return None
            

def pedir_correo(nombre_formateado):
    while True:
        correo = input(f"📧 {nombre_formateado}, Ingrese su correo: ").strip()

        if not correo:
            print("❌ El Campo correo no puede estar vacio")
            continue
        elif "@" not in correo:
            print("❌ Error: El correo debe contener '@'.")
            continue
        elif "." not in correo:
            print("❌ Error: El correo debe contener (.).")
            continue
        elif correo.startswith(("@", ".")) or correo.endswith(("@", ".")):
            print("Error: El correo no puede empezar ni terminar con '@' o '.'.")
            continue
        elif correo.count("@") != 1:
            print("Error: El correo debe contener exactamente un '@'.")
            continue
        elif correo.find("@") >= correo.rfind("."):
            print("Error: El '@' debe estar antes del último punto.")
            continue
        elif " " in correo:
            print("Error: El correo no puede contener espacios.")
            continue
        else:
            correo = correo.lower()
            print(f"🟩 {nombre_formateado} su correo fue registrado con exito")
            return correo

def mostrar_usuario(nombre_formateado, edad, correo):
    print("\nDatos registrados:")
    print(f"Nombre: {nombre_formateado}")
    print(f"Edad: {edad}")
    print(f"Correo: {correo}")


if __name__ == "__main__":
    nombre = pedir_nombre()
    if nombre:
        edad = pedir_edad(nombre)
        if edad is not None:
            correo = pedir_correo(nombre)
            if correo:
                mostrar_usuario(nombre, edad, correo)

"""
===========================================================================
===                  RESPUESTA DE CONSOLA                               ===
===========================================================================
Ingrese su nombre y apellido: gabo123                                      
❌ Debe ingresar al menos un nombre y un apellido
Ingrese su nombre y apellido:     GABRRIEL 
❌ Debe ingresar al menos un nombre y un apellido
Ingrese su nombre y apellido:      GABRIEL ESPINOSA izada
✅ Nombre válido: Gabriel Espinosa Izada
Gabriel Espinosa Izada, ingrese su edad: wwew
❌ Error: ingrese un número válido para la edad
Gabriel Espinosa Izada, ingrese su edad: 0
❌ Error: esa edad parece falsa 🤔
Gabriel Espinosa Izada, ingrese su edad: 152
❌ Error: esa edad parece falsa 🤔
Gabriel Espinosa Izada, ingrese su edad: 27
🟩 Gabriel Espinosa Izada, su edad ha sido registrada con éxito
📧 Gabriel Espinosa Izada, Ingrese su correo: @
❌ Error: El correo debe contener (.).
📧 Gabriel Espinosa Izada, Ingrese su correo: .
❌ Error: El correo debe contener '@'.
📧 Gabriel Espinosa Izada, Ingrese su correo: GESPINOSAIZADA03@GMAIL.COM
🟩 Gabriel Espinosa Izada su correo fue registrado con exito

Datos registrados:
Nombre: Gabriel Espinosa Izada
Edad: 27
Correo: gespinosaizada03@gmail.com
===========================================================================
"""