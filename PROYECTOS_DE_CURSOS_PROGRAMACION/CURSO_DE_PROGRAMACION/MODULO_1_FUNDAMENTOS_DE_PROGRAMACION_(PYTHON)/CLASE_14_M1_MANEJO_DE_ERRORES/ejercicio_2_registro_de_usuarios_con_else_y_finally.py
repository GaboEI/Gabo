#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
!🧪 EJERCICIO 2  CLASE 14
?📌 Nombre: Registro de usuarios con else y finally
todo:🔑 Concepto: flujo completo de control de errores

?🎯 ¿Qué debe hacer el script?
1️⃣Solicitar al usuario que ingrese su nombre de usuario.
2️⃣Validar que el nombre contenga solo letras (sin números ni símbolos).
3️⃣Si el nombre es válido: Mostrar mensaje de bienvenida dentro del else.
4️⃣Si hay error (números, símbolos, etc.): Capturarlo y mostrar un mensaje personalizado.
5️⃣Usar finally para mostrar un mensaje que siempre se imprima, por ejemplo:"Gracias por usar el sistema."
"""
#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※

def registrar_usuario():
    try:
        nombre = input("⚙️ Ingresa el nimbre del usuario: ").strip().title()                 

        if not nombre.isalpha():                                             
            raise ValueError("🚫El nombre solo deve de contener letras")

    except ValueError as error:
        print(f"⚠️ Error: {error}")

    else:
        print(f"👋 Bienvenido, {nombre}🎉")

    finally:
        print(f"🔒{nombre}, Gracias por usar el programa")

registrar_usuario()