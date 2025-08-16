# 🧠 Clase 10 — Proyecto Integrador Intermedio: Gestor de Tareas con Archivos

---

## 🎯 Objetivo de la clase

Diseñar e implementar una aplicación de consola que funcione como un **gestor de tareas**, utilizando funciones, estructuras de control, estructuras de datos y manejo de archivos. Este proyecto intermedio consolida múltiples áreas clave del lenguaje Python en una solución semiprofesional.

---

## 📚 Fundamentos teóricos

Un **gestor de tareas** permite:

- Añadir tareas
- Listar tareas
- Marcar tareas como completadas
- Eliminar tareas
- Guardar y recuperar datos desde archivos de texto

Esto implica el dominio de:

- Funciones definidas por el usuario
- Condicionales `if`, `elif`, `else`
- Bucles `while` y `for`
- Listas y diccionarios
- Manipulación de archivos (`open()`, `read()`, `write()`, `with`)

---

## 🧪 Ejercicio 01 — `01_gestor_tareas_basico.py`

**🎯 Objetivo:** Crear un gestor de tareas simple con almacenamiento en archivo de texto.

### 🧭 Diagrama de flujo

```
Inicio
↓
Cargar archivo con tareas
↓
Mostrar menú
↓
Esperar opción del usuario
├── 1: Añadir tarea
│   └── Pedir descripción y guardar
├── 2: Mostrar tareas
│   └── Leer y mostrar archivo
├── 3: Marcar como completada
│   └── Editar archivo
├── 4: Eliminar tarea
│   └── Quitar línea específica
├── 5: Salir
↓
Guardar cambios
↓
Fin
```

### ✅ Código realizado

```python
import os

def cargar_tareas():
    if not os.path.exists("tareas.txt"):
        return []
    with open("tareas.txt", "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo.readlines()]

def guardar_tareas(tareas):
    with open("tareas.txt", "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def mostrar_tareas(tareas):
    print("\n📋 Tareas:")
    if not tareas:
        print("(No hay tareas registradas)")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")

def añadir_tarea(tareas):
    descripcion = input("Escribe la nueva tarea: ").strip()
    if descripcion:
        tareas.append("[ ] " + descripcion)

def marcar_completada(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("¿Qué tarea completaste? N°: ")) - 1
        if 0 <= indice < len(tareas):
            if tareas[indice].startswith("[x]"):
                print("✅ Ya estaba completada.")
            else:
                tareas[indice] = tareas[indice].replace("[ ]", "[x]", 1)
        else:
            print("❌ Número fuera de rango.")
    except ValueError:
        print("❌ Entrada no válida.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("¿Qué tarea deseas eliminar? N°: ")) - 1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
        else:
            print("❌ Número fuera de rango.")
    except ValueError:
        print("❌ Entrada no válida.")

def menu():
    print("""
🔧 Menú de Gestor de Tareas
1. Añadir tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
""")

def main():
    tareas = cargar_tareas()
    while True:
        menu()
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            añadir_tarea(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print("👋 Cambios guardados. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
```

---

## 🧾 Cierre de la clase

Esta clase nos prepara para manejar datos persistentes y estructuras dinámicas dentro de una aplicación real. Hemos aplicado todo lo aprendido sobre modularización, entrada/salida, estructuras de datos y validación de errores, enfocándonos en la experiencia del usuario final y en la escalabilidad del código.

---

## 🧠 Evaluación simbólica

🔹 Modularización: ✅ Excelente uso de funciones 🔹 Validaciones: ✅ Estructuradas y útiles 🔹 Manejo de archivos: ✅ Con apertura segura y escritura limpia 🔹 UX de consola: ✅ Clara, profesional 🔹 Nota simbólica: **10.75/10**

📦 **Clase finalizada, lista para ser subida a tu portafolio profesional. ¡Bravo, Gabo!** 🚀🧑‍💻

