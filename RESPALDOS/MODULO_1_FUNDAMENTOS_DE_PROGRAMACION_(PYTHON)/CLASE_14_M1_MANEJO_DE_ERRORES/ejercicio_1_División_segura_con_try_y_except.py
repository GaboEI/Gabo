"""=================================================================================================
#!🧪 EJERCICIO 1 CLASE 14

#?📌 Nombre: División segura con try y except
#?🔑 Concepto: Captura de errores comunes con manejo claro

#!🎯 ¿Qué debe hacer la función?

1️⃣Pedir al usuario dos números: numerador y denominador.
2️⃣Intentar dividir el numerador entre el denominador.
3️⃣Si todo está bien, mostrar el resultado.
4️⃣Si el usuario intenta dividir entre cero, capturar el error y mostrar un mensaje elegante.
5️⃣Si el usuario escribe texto u otro valor inválido, mostrar un mensaje de error también.
6️⃣Usar una función limpia con try y except.
================================================================================================="""
def divicion_segura():

    try:
        numero_uno = float(input("🔢 Ingrese el numerador: "))
        numero_dos = float(input("🔢 Ingrese el denoninador: "))
        resultado = numero_uno / numero_dos

    except ZeroDivisionError:
        print("❌ Error! no puede dividir entre cero")
    except ValueError:
        print("⚠️ Error: deves de ingresar solo numeros")
    else:
        print(f"✅ El resultado de la división es: {resultado}")
divicion_segura()