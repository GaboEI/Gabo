"""
===================================================================================================
!🧪 EJERCICIO 2  CLASE 17
?📌 Nombre: Guardar múltiples registros en archivo con append
todo::🔑 Enfoque: escritura segura en modo “a” (append) para acumular datos

?🎯 ¿Qué debe hacer el programa?
1️⃣ Pedir nombre y calificación del estudiante #!(puedes reutilizar lo que hiciste antes).
2️⃣ uardar esa información en un archivo llamado notas.txt, en este formato:
todo:: Nombre: Ana Torres | Nota: 8.5
3️⃣ Usar el modo de apertura "a" para que no se sobreescriba lo anterior.
4️⃣ Repetir el proceso hasta que el usuario diga que no quiere ingresar más estudiantes.
5️⃣ Validar todos los datos, tal como hiciste en el ejercicio anterior.
===================================================================================================
"""
def registrar_estudiante():
    print("\n" + "★"*50)
    print("📋 REGISTRO DE NOMBRE")
    print("★"*50)

    # Validar nombre (solo letras, puede tener espacios)
    while True:
        try:
            nombre = input("\n👤 Ingrese su nombre aquí 👉 ").strip().title()
            if all(parte.isalpha() for parte in nombre.split()):
                print(f"\n🔓 Nombre válido: {nombre}")
                break  # Salir del bucle de validación del nombre
            else:
                raise ValueError("Solo se aceptan letras (A-Z).")
        except ValueError as c:
            print(f"\n⚠️ Error: {c}")
        except Exception as d:
            print(f"\n🫥 Error inesperado: {d}")

    # Validar nota (número entre 0 y 10)
    while True:
        try:
            nota = float(input(f"\n🔢 {nombre}, ingrese su nota del [0-10] a continuación 👉 "))
            if 0 <= nota <= 10:
                print(f"\n✅ Nota: {nota:.2f}, válida")
                break
            else:
                raise ValueError(f"\n❌ {nombre}, la nota debe estar entre [0-10]")
        except ValueError as c:
            print(f"⚠️ Error: {c}, Ingrese una nota válida")

    print(f"\n📜 Registro completado: {nombre} | 🔢 Nota: {nota:.2f}")
    print("★"*50)
    return nombre, nota

# Bucle principal: repetir hasta que el usuario diga que no
while True:
    nombre, nota = registrar_estudiante()

    # Abrir el archivo 'notas.txt' en modo 'a' (append)
    with open("notas.txt", "a", encoding="utf-8") as file:  # Corregido el nombre del archivo
        file.write(f"\n📜 Registro completado: {nombre} | 🔢 Nota: {nota:.2f}\n")
        print(f"\n💾 Datos guardados en notas.txt: Nombre: {nombre} | Nota: {nota:.2f}")

    # Preguntar si desea continuar
    continuar = input("\n¿Deseas ingresar otro estudiante? (s/n): ").lower()
    if continuar != "s":
        print("\n" + "★"*50)
        print("🏁 REGISTRO FINALIZADO")
        print("📜 Los datos han sido guardados en 'notas.txt'")
        print("★"*50)
        break