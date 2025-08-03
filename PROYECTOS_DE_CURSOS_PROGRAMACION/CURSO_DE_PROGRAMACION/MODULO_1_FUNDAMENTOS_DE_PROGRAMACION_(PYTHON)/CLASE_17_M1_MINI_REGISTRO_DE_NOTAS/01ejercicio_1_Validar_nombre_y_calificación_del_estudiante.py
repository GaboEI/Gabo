"""
=========================================================================================
!🧪 EJERCICIO 1 – CLASE 17
?📌 Nombre: Validar nombre y calificación del estudiante
todo::🔑 Enfoque: validación segura de entradas + formato correcto

?🎯 ¿Qué debe hacer este script?
1️⃣ Pedir al usuario que ingrese el nombre del estudiante
2️⃣ Verificar que el nombre:
----No esté vacío
----Solo contenga letras (sin números ni símbolos)
3️⃣ Pedir una calificación
4️⃣ Verificar que la calificación:
-----Sea un número (int o float)
-----Esté entre 0 y 10 inclusive
5️⃣ Si todo es válido, mostrar en consola
todo:: ✅ Registro válido: Carla - Nota: 8.5
=========================================================================================
"""

def validar_nombre():
    print("\n" + "="*50)
    print("   📋 REGISTRO DE NOMBRE")
    print("="*50)
    
    while True:
        try:
            nombre = input("\n👤 Ingrese su nombre aquí 👉 ").strip().title()
            if all(parte.isalpha() for parte in nombre.split()):
                print(f"\n🔓 Nombre válido: {nombre}")
            else:
                raise ValueError("Solo se aceptan letras (A-Z).")
        except ValueError as c:
            print(f"\n⚠️ Error: {c}")
        except Exception as d:
            print(f"\n🫥 Error inesperado: {d}")
        else:
            print(f"\n✅ Entrada aceptada: {nombre}\n")
            print("="*50)
            return nombre

def pedir_nota(nombre):
    print("\n" + "="*50)
    print(f"   📝 REGISTRO DE NOTA PARA {nombre}")
    print("="*50)
    
    while True:
        try:
            nota = float(input("\n🔢 Ingrese su clasificación aquí (0-10) 👉 "))
            if 0 <= nota <= 10:
                print(f"\n✅ Clasificación válida: {nota:.2f}")
                break
            else:
                raise ValueError(f"{nombre}, la nota debe estar entre 0 y 10.")
        except ValueError as t:
            print(f"\n🚫 Error: {t} Ingresa un número válido.")
        finally:
            print(f"\n🎆{nombre}, gracias por usar el registro de estudiantes. ¡Hasta pronto👋!")
            print("="*50)

# Ejecución del programa
nombre = validar_nombre()
pedir_nota(nombre)








