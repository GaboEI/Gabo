#=== 🏁 Ejercicio 05 – Revisar crédito simplificado ===#

def revisar_credito_simplificado():
    # Constantes para valores fijos
    EDAD_MINIMA = 21
    INGRESOS_MINIMOS = 1500
    HISTORIAL_VALIDO = ["b", "e"]
    MENSAJE_REINTENTAR = "Inténtelo nuevamente."

    # Entrada y validación del nombre
    while True:
        nombre_completo = input("👤 Por favor, ingrese su nombre completo (solo letras y espacios): ")
        nombre_limpio = nombre_completo.strip()

        if not nombre_limpio:
            print(f"🚫 El nombre no puede estar vacío. {MENSAJE_REINTENTAR}")
        elif not all(palabra.isalpha() for palabra in nombre_limpio.split()):
            print(f"❌ El nombre solo puede contener letras. {MENSAJE_REINTENTAR}")
        else:
            nombre_formateado = ' '.join(palabra.capitalize() for palabra in nombre_limpio.split())
            print("✅ Nombre ingresado correctamente.")
            print(f"👋 ¡Bienvenido, {nombre_formateado}!")
            break

    # Entrada y validación de la edad
    while True:
        try:
            edad = int(input(f"🎂 {nombre_formateado}, por favor ingrese su edad: "))
            if edad <= 0:
                print(f"❌ La edad debe ser un número positivo. {MENSAJE_REINTENTAR}")
                continue
            else:
                print("✅ Edad ingresada correctamente.")
                break
        except ValueError:
            print(f"🚫 La edad debe ser un número entero. {MENSAJE_REINTENTAR}")

    # Entrada y validación de los ingresos
    while True:
        try:
            ingresos = float(input(f"💸 {nombre_formateado}, por favor ingrese sus ingresos mensuales: "))
            if ingresos <= 0:
                print(f"❌ Los ingresos deben ser un número positivo. {MENSAJE_REINTENTAR}")
                continue
            else:
                print("✅ Ingresos ingresados correctamente.")
                break
        except ValueError:
            print(f"🚫 Los ingresos deben ser un número válido. {MENSAJE_REINTENTAR}")

    # Entrada y validación del historial crediticio
    while True:
        pedir_historial = input(f"✍️ {nombre_formateado}, por favor indique si su historial crediticio es bueno o excelente [b/e]: ")
        pedir_historial_minuscula = pedir_historial.lower()

        if pedir_historial_minuscula in HISTORIAL_VALIDO:
            print(f"🎉 ¡Felicidades, {nombre_formateado}! Su historial crediticio es válido.")
            break
        else:
            print(f"🚫 Opción inválida. Por favor, escriba 'b' o 'e' para continuar. {MENSAJE_REINTENTAR}")

    # Evaluar condiciones para aprobar o rechazar el crédito
    if edad >= EDAD_MINIMA and ingresos >= INGRESOS_MINIMOS and pedir_historial_minuscula in HISTORIAL_VALIDO:
        print(f"🪙 ¡Felicidades, {nombre_formateado}! Su crédito ha sido aprobado.")
    else:
        print(f"🥹 Lo sentimos, {nombre_formateado}. Su crédito ha sido rechazado.")

    # Mensaje final
    print(f"🏦 Gracias por usar nuestro sistema de crédito, {nombre_formateado}. Vuelva pronto.")

revisar_credito_simplificado()

#=== REAPUESTAS DE CONSOLA ===#
"""
👤 Por favor, ingrese su nombre completo (solo letras y espacios): gabo123
❌ El nombre solo puede contener letras. Inténtelo nuevamente.
👤 Por favor, ingrese su nombre completo (solo letras y espacios):   Gabriel ESPINOSA
✅ Nombre ingresado correctamente.
👋 ¡Bienvenido, Gabriel Espinosa!
🎂 Gabriel Espinosa, por favor ingrese su edad: 27ANOS
🚫 La edad debe ser un número entero. Inténtelo nuevamente.
🎂 Gabriel Espinosa, por favor ingrese su edad: -8
❌ La edad debe ser un número positivo. Inténtelo nuevamente.
🎂 Gabriel Espinosa, por favor ingrese su edad: 27
✅ Edad ingresada correctamente.
💸 Gabriel Espinosa, por favor ingrese sus ingresos mensuales: MUCHOS
🚫 Los ingresos deben ser un número válido. Inténtelo nuevamente.
💸 Gabriel Espinosa, por favor ingrese sus ingresos mensuales: -9
❌ Los ingresos deben ser un número positivo. Inténtelo nuevamente.
💸 Gabriel Espinosa, por favor ingrese sus ingresos mensuales: 9000.56
✅ Ingresos ingresados correctamente.
✍️ Gabriel Espinosa, por favor indique si su historial crediticio es bueno o excelente [b/e]: BUENICIMO
🚫 Opción inválida. Por favor, escriba 'b' o 'e' para continuar. Inténtelo nuevamente.
✍️ Gabriel Espinosa, por favor indique si su historial crediticio es bueno o excelente [b/e]: e
🎉 ¡Felicidades, Gabriel Espinosa! Su historial crediticio es válido.
🪙 ¡Felicidades, Gabriel Espinosa! Su crédito ha sido aprobado.
🏦 Gracias por usar nuestro sistema de crédito, Gabriel Espinosa. Vuelva pronto.
"""