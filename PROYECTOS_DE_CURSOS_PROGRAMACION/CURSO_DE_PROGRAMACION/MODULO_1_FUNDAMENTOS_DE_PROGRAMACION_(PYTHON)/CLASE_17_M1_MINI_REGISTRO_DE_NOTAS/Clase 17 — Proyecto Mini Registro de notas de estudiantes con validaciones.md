# 📘 Clase 17 — Proyecto Mini: Registro de notas de estudiantes con validaciones

---

## 🎯 Objetivo del proyecto

Desarrollar un sistema sencillo y robusto que permita registrar, almacenar, mostrar y validar notas de estudiantes utilizando archivos de texto. Se aplicarán funciones, estructuras de control, validaciones y lectura/escritura de archivos.

---

## 🧠 Requisitos del sistema

- Solicitar el nombre del estudiante
- Validar que el nombre no esté vacío
- Solicitar la nota (número entre 0 y 100)
- Validar que sea un número válido
- Guardar en archivo con formato: `nombre - nota`
- Mostrar todos los registros luego de cada inserción

---

## 🧪 Ejercicio 01 — `01_registro_de_notas_validado.py`

**🎯 Objetivo:** Solicitar nombre y nota, validar los datos y registrar en archivo.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre del estudiante
↓
Validar que no esté vacío
↓
Solicitar nota
↓
Validar que sea un número entre 0 y 100
↓
Abrir archivo en modo 'a'
↓
Escribir registro "nombre - nota"
↓
Cerrar archivo
↓
Mostrar todos los registros
↓
Fin
```

### ✅ Código realizado

```python
import os

def registrar_nota():
    nombre = input("👤 Nombre del estudiante: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    try:
        nota = float(input("📊 Nota del estudiante (0-100): "))
        if nota < 0 or nota > 100:
            print("❌ La nota debe estar entre 0 y 100.")
            return
    except ValueError:
        print("❌ Entrada inválida. Debe ser un número.")
        return

    with open("notas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - {nota}\n")
        print("✅ Nota registrada correctamente.")

    print("\n📂 Registros actuales:")
    with open("notas.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())

# registrar_nota()  ← descomentar para probar
```

---

## 🧪 Ejercicio 02 — `02_menu_registro_notas.py`

**🎯 Objetivo:** Crear un menú para registrar múltiples notas o salir del programa.

### 🧭 Diagrama de flujo

```
Inicio
↓
Mostrar menú (1. Registrar, 2. Ver, 3. Salir)
↓
Si opción == 1:
    → Pedir nombre y nota (con validaciones)
    → Guardar en archivo
↓
Si opción == 2:
    → Leer y mostrar archivo
↓
Si opción == 3:
    → Salir
↓
Repetir menú
```

### ✅ Código realizado

```python
def menu():
    while True:
        print("\n📘 MENÚ - REGISTRO DE NOTAS")
        print("1. Registrar nota")
        print("2. Ver todas las notas")
        print("3. Salir")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            registrar_nota()
        elif opcion == "2":
            if os.path.exists("notas.txt"):
                with open("notas.txt", "r", encoding="utf-8") as archivo:
                    print("\n📋 Notas registradas:")
                    print(archivo.read())
            else:
                print("⚠️ No hay notas registradas aún.")
        elif opcion == "3":
            print("👋 Programa finalizado.")
            break
        else:
            print("❌ Opción inválida.")

# menu()  ← descomentar para probar
```

---

## 🧾 Cierre del proyecto

Este proyecto mini consolida lo aprendido en entradas validadas, estructuras de control, funciones reutilizables y persistencia de datos mediante archivos. Es la base sobre la que se pueden construir sistemas académicos reales, ampliando con promedios, búsquedas, edición y eliminación de registros.

---

## 🧠 Evaluación simbólica

🔹 Validación robusta de entradas: ✅ 🔹 Funciones reutilizables y claras: ✅ 🔹 Uso de archivos correcto: ✅ 🔹 Aplicación realista y escalable: ✅

📌 **Nota simbólica: 10.75/10** 💥 ¡Excelente dominio de lo aprendido!

