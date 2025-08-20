# 🐍 validar_correo_modular.py
"""Debe pedir el correo al usuario, validarlo 
y retornarlo si es correcto"""

def pedir_correo():
    while True:
        correo = input("📧 Ingrese su correo: ").strip()

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
            print("🟩 Correo registrado con exito")
            return correo


def saludar_con_correo(correo):
    print(f"Gracias, hemos registrado el correo: {correo}")

correo_valido = pedir_correo()
saludar_con_correo(correo_valido)

"""
================================================================
=== RESPUESTA DE CONSOLA ===
================================================================
📧 Ingrese su correo: 123
❌ Error: El correo debe contener '@'.

📧 Ingrese su correo: @gabo123
❌ Error: El correo debe contener (.).

📧 Ingrese su correo: ..gabo
❌ Error: El correo debe contener '@'.

📧 Ingrese su correo: gespinosaizada03gmail.com
❌ Error: El correo debe contener '@'.

📧 Ingrese su correo: GESPINOSAIZADA03@GMAIL.COM
🟩 Correo registrado con exito
Gracias, hemos registrado el correo: gespinosaizada03@gmail.com
================================================================
"""