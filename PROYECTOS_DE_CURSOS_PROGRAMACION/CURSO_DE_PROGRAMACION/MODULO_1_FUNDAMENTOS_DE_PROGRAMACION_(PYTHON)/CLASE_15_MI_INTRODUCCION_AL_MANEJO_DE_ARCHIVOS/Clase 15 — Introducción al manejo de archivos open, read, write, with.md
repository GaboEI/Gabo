# 🧠 Clase 15 — Introducción al manejo de archivos: open, read, write, with

---

## 🎯 Objetivo de la clase

Aprender los fundamentos esenciales para trabajar con archivos de texto en Python mediante las funciones `open()`, `read()`, `write()` y la estructura `with`. Esta clase tiene como propósito desarrollar habilidades para leer y escribir archivos de forma segura, controlada y profesional.

---

## 📚 Fundamentos teóricos

### 🔹 ¿Qué es el manejo de archivos?

El manejo de archivos permite a los programas interactuar con el sistema de archivos del equipo: abrir archivos, leer su contenido, modificarlos o crearlos desde cero.

Los archivos pueden ser de texto plano (`.txt`) o binarios (como imágenes o audio), pero en esta clase trabajaremos con archivos de **texto plano**.

### 🔸 Función `open()`

```python
archivo = open("archivo.txt", "modo")
```

- `'r'` → lectura
- `'w'` → escritura (sobrescribe)
- `'a'` → añadir al final (append)
- `'x'` → creación exclusiva

### 🔸 Leer archivos

```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
```

- `read()` → lee todo
- `readline()` → una línea
- `readlines()` → lista de líneas

### 🔸 Escribir archivos

```python
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola mundo\n")
```

- `write()` escribe una cadena
- Si el archivo no existe, lo crea; si existe, lo sobrescribe

### 🔸 ¿Por qué usar `with`?

El bloque `with` garantiza que el archivo se cierre automáticamente al terminar su uso, incluso si ocurre un error.

---

## 🧪 Ejercicio 01 — `01_leer_archivo_txt.py`

**🎯 Objetivo:** Leer el contenido completo de un archivo `.txt` y mostrarlo en consola.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre de archivo
↓
Abrir archivo en modo lectura con 'with'
↓
Leer contenido con .read()
↓
Mostrar contenido en consola
↓
Fin
```

### ✅ Código realizado

```python
def leer_archivo():
    nombre = input("📄 Ingrese el nombre del archivo a leer: ")
    try:
        with open(nombre, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("📚 Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("❌ El archivo no existe.")

# leer_archivo()  ← descomentar para probar
```

---

## 🧪 Ejercicio 02 — `02_escribir_archivo_txt.py`

**🎯 Objetivo:** Escribir texto ingresado por el usuario en un nuevo archivo.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre del nuevo archivo
↓
Solicitar contenido a escribir
↓
Abrir archivo en modo escritura con 'with'
↓
Escribir contenido con .write()
↓
Confirmar operación
↓
Fin
```

### ✅ Código realizado

```python
def escribir_archivo():
    nombre = input("📝 Nombre del archivo nuevo: ")
    contenido = input("✏️ Escribe el contenido: ")
    with open(nombre, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
        print("✅ Archivo creado y contenido guardado correctamente.")

# escribir_archivo()  ← descomentar para probar
```

---

## 🧪 Ejercicio 03 — `03_append_archivo.py`

**🎯 Objetivo:** Añadir una nueva línea de texto al final de un archivo existente sin borrar su contenido.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre del archivo
↓
Solicitar línea a añadir
↓
Abrir archivo en modo 'a' (append)
↓
Añadir contenido con .write()
↓
Confirmar guardado
↓
Fin
```

### ✅ Código realizado

```python
def añadir_linea():
    nombre = input("📄 Nombre del archivo existente: ")
    linea = input("➕ Línea que deseas agregar: ")
    with open(nombre, "a", encoding="utf-8") as archivo:
        archivo.write("\n" + linea)
        print("✅ Línea añadida correctamente.")

# añadir_linea()  ← descomentar para probar
```

---

## 🧾 Cierre de la clase

Aprender a manejar archivos te permite guardar información persistente más allá de la ejecución del programa. Es un pilar fundamental del desarrollo de sistemas, automatización, backend, logs, configuración, y más.

Dominar las funciones `open`, `read`, `write`, y el uso del bloque `with` eleva tu nivel como programador hacia un enfoque más profesional y preparado para aplicaciones del mundo real.

---

## 🧠 Evaluación simbólica

🔸 Lectura segura de archivos: ✅ Domina `read()` y excepciones\


🔸 Escritura limpia y correcta: ✅ Aplicación de `write()` y `with`\


🔸 Añadir contenido sin sobrescribir: ✅ Perfecto uso de modo `a`\


🔸 Robustez, mensajes y estructura: ✅ Nivel alto

📌 **Nota simbólica: 10.5/10** 🎯 ¡Avance profesional confirmado!

