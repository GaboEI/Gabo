#=================================================================================================================
"""
#todo: 🟩 CLASE 17 — Proyecto mini: Registro de notas de estudiantes con validaciones**

#!📘 Tema oficial validado: Proyecto práctico para consolidar lectura, escritura y manipulación de archivos, 
aplicando además validación de datos** y estructura funcional.

#!🧱 ESTRUCTURA DE LA CLASE 17
🔢 Cantidad de ejercicios: 1 gran proyecto dividido en 4 partes

#!🧠 **Contenido de la clase**
1. Teoría profunda sobre validación de entradas y control de errores.
2. Escritura estructurada de registros en archivo .txt.
3. Revisión y validación de notas (0 a 100).
4. Relectura y presentación del contenido al usuario.
5. Diseño limpio del programa (menús, mensajes claros).
6. Preparación para lógica más compleja: estructuras de datos.

#!📚 TEORÍA PROFUNDA
#!🔹 ¿Qué es una validación de entrada?

Es un proceso que se asegura de que los datos introducidos por el usuario **cumplen con reglas esperadas antes de 
procesarlos o guardarlos.

#? Por ejemplo:
* Que una nota esté entre 0 y 100
* Que el nombre no esté vacío
* Que se ingresen **números cuando se espera una nota

🔹 Tipos de validaciones comunes
| Tipo                | Ejemplo                               
| ------------------- | -------------------------------------- 
| De rango            | if 0 <= nota <= 100:                 
| De tipo             | try: int(input()) except ValueError: 
| De formato / vacíos | if nombre.strip() == "":             
| Personalizadas      | Nombre no puede ser “admin”, etc.      

🔹 Flujo típico de validación

#? Solicitar entrada
entrada = input("Introduce tu edad: ")

#? Validar que sea numérica
try:
    edad = int(entrada)
    if edad < 0:
        print("Edad no puede ser negativa")
    else:
        print("Edad válida:", edad)
except ValueError:
    print("Debes ingresar un número entero.")

#!🔹 ¿Por qué validar es importante?

* 🛡️ Evita errores del programa
* 🧼 Mejora la experiencia del usuario
* 💾 Protege la integridad de los datos almacenados
* ✅ Es un principio de desarrollo profesional real

#!🧠 Aplicación profesional
Este proyecto es la base de:
* Sistemas de gestión de estudiantes, encuestas, formularios
* Automatización de registro de datos
* Validación de usuarios en interfaces visuales o web
* Entrenamiento para interfaces de bases de datos más adelante
"""
#=================================================================================================================
print("Bienvenido al sistema de registro de notas.")
print("Escribe el nombre y la nota del estudiante. Para terminar, escribe 'salir' en el nombre.")
print("-" * 65)

def evaluar_nota(nota):
    if not (0 <= nota <= 100):
        return "❌ Error: Nota inválida"
    elif 90 <= nota <= 100:
        return "✅ Excelente"
    elif 75 <= nota < 90:
        return "🟩 Muy bien"
    elif 60 <= nota < 75:
        return "🟨 Bien"
    elif 50 <= nota < 60:
        return "🟧 Aprobado justo"
    else:
        return "🟥 Reprobado"

print("📜 Sistema de registro de notas. Ingrese 'salir' para terminar.")

while True:
    while True:
        nombre = input("👤 Nombre del estudiante o escriba 'salir' para finalizar: ").strip().title()
        if nombre.lower() == "salir":
            print("🔚 Programa finalizado. Gracias 👋")
            exit()
            break
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío.")
            continue
        if not all(c.isalpha() or c.isspace() for c in nombre):
            print("🆎 Error: El nombre solo puede contener letras y espacios.")
            continue
        break
    while True:
        try:
            nota = float(input("🔢 Nota [0-100]: "))
            evaluacion = evaluar_nota(nota)
            if "Error" in evaluacion:
                print(evaluacion)
                continue
        except ValueError:
            print("❌ Error: La nota debe ser un número real positivo.")
            continue

        with open("notas.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Nombre: {nombre}  Nota: {nota:.2f}  {evaluacion}\n")

        print(f"✔️  Nota:{nota:.2f} registrada con éxito para {nombre} ({evaluacion})")

        print("\n===💥 Notas Registradas 💥===")
        try:
            with open("notas.txt", "r", encoding="utf-8") as archivo:
                print(archivo.read())
            break
        except FileNotFoundError:
            print("🚫 No hay notas registradas aún.")
        print("🔚 Validacion de notas Finalizada. gracias👋")
        break

#=================================================================================================================
###! RESPUESTA DE LA TERMINAL
"""
📜 Sistema de registro de notas. Ingrese 'salir' para terminar.
👤 Nombre del estudiante o escriba 'salir' para finalizar: GABRIEL ESPINOSA IZADA
🔢 Nota [0-100]: 100
🔚 Validacion de notas Finalizada. gracias👋
✔️  Nota:100.00 registrada con éxito para Gabriel Espinosa Izada (✅ Excelente)

===💥 Notas Registradas 💥===
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente

👤 Nombre del estudiante o escriba 'salir' para finalizar: Cristina123
🆎 Error: El nombre solo puede contener letras y espacios.
👤 Nombre del estudiante o escriba 'salir' para finalizar: CRISTINA espinosa izada
🔢 Nota [0-100]: 85.999999999999
🔚 Validacion de notas Finalizada. gracias👋
✔️  Nota:86.00 registrada con éxito para Cristina Espinosa Izada (🟩 Muy bien)

===💥 Notas Registradas 💥===
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien

👤 Nombre del estudiante o escriba 'salir' para finalizar: Limiana Betancour Espinosa
🔢 Nota [0-100]: dies
❌ Error: La nota debe ser un número real positivo.
🔚 Validacion de notas Finalizada. gracias👋
🔢 Nota [0-100]: 70.5
🔚 Validacion de notas Finalizada. gracias👋
✔️  Nota:70.50 registrada con éxito para Limiana Betancour Espinosa (🟨 Bien)

===💥 Notas Registradas 💥===
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien

👤 Nombre del estudiante o escriba 'salir' para finalizar: Diego Betancour Espinosa
🔢 Nota [0-100]: 55.8945465568
🔚 Validacion de notas Finalizada. gracias👋
✔️  Nota:55.89 registrada con éxito para Diego Betancour Espinosa (🟧 Aprobado justo)

===💥 Notas Registradas 💥===
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien
Nombre: Diego Betancour Espinosa  Nota: 55.89  🟧 Aprobado justo

👤 Nombre del estudiante o escriba 'salir' para finalizar: Roberto mastrapa aguilar
🔢 Nota [0-100]: 25
🔚 Validacion de notas Finalizada. gracias👋
✔️  Nota:25.00 registrada con éxito para Roberto Mastrapa Aguilar (🟥 Reprobado)

===💥 Notas Registradas 💥===
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien
Nombre: Diego Betancour Espinosa  Nota: 55.89  🟧 Aprobado justo
Nombre: Roberto Mastrapa Aguilar  Nota: 25.00  🟥 Reprobado

👤 Nombre del estudiante o escriba 'salir' para finalizar: salir
🔚 Programa finalizado. Gracias 👋
"""
#=================================================================================================================
###! cONTENIDO DEL ARCHIVO notas.tx AL REALIZAR LA PRUEVA DE TERMINAL
"""
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien
Nombre: Diego Betancour Espinosa  Nota: 55.89  🟧 Aprobado justo
Nombre: Roberto Mastrapa Aguilar  Nota: 25.00  🟥 Reprobado
"""
#=================================================================================================================