# 🧠 Clase 16 — Escritura y lectura de archivos de texto

---

## 🎯 Objetivo de la clase

Profundizar en el uso de los modos de apertura de archivos (`r`, `w`, `a`, `r+`, `w+`, `a+`) y técnicas combinadas de lectura y escritura. Aprender a manipular contenido de archivos sin sobrescribirlo, leer desde posiciones específicas y realizar validaciones robustas al interactuar con archivos de texto.

---

## 📚 Fundamentos teóricos

### 🔹 Modos de apertura avanzados

- `'r'`: lectura (error si no existe)
- `'w'`: escritura (crea o sobrescribe)
- `'a'`: añadir (crea si no existe)
- `'r+'`: lectura y escritura (no borra contenido)
- `'w+'`: escritura y lectura (borra si existe)
- `'a+'`: añadir y lectura (crea si no existe)

### 🔸 Posicionamiento del cursor con `.seek()`

```python
archivo.seek(posicion)
```
Permite mover el cursor del archivo a una posición específica (por bytes).

### 🔸 Lectura después de escritura
Cuando abrimos en modo `a+` o `w+`, si queremos leer debemos usar `.seek(0)` primero para mover el cursor al inicio.

### 🔸 Validación de existencia de archivo
```python
import os
os.path.exists("archivo.txt")
```
Permite comprobar si el archivo existe antes de intentar abrirlo.

---

## 🧪 Ejercicio 01 — `01_sobrescribir_vs_append.py`

**🎯 Objetivo:** Mostrar la diferencia entre sobrescribir y añadir al escribir archivos.

### 🧭 Diagrama de flujo
```
Inicio
↓
Solicitar nombre del archivo
↓
Solicitar modo de escritura ('w' o 'a')
↓
Solicitar contenido a escribir
↓
Abrir archivo con modo elegido
↓
Escribir contenido
↓
Confirmar resultado
↓
Fin
```

### ✅ Código realizado
```python
def escribir_personalizado():
    nombre = input("📄 Nombre del archivo: ")
    modo = input("🔧 Modo ('w' para sobrescribir, 'a' para añadir): ")
    contenido = input("📝 Contenido a guardar: ")

    if modo not in ('w', 'a'):
        print("❌ Modo inválido.")
        return

    with open(nombre, modo, encoding="utf-8") as archivo:
        archivo.write(contenido + "\n")
        print("✅ Contenido guardado correctamente.")

# escribir_personalizado()  ← descomentar para probar
```

---

## 🧪 Ejercicio 02 — `02_lectura_y_sobrescritura.py`

**🎯 Objetivo:** Leer el contenido original de un archivo, mostrarlo, y luego permitir su sobrescritura.

### 🧭 Diagrama de flujo
```
Inicio
↓
Solicitar nombre del archivo
↓
Leer y mostrar contenido original
↓
Solicitar nuevo contenido
↓
Sobrescribir el archivo con nuevo contenido
↓
Confirmar
↓
Fin
```

### ✅ Código realizado
```python
def leer_y_reemplazar():
    nombre = input("📂 Archivo a modificar: ")
    try:
        with open(nombre, "r", encoding="utf-8") as archivo:
            original = archivo.read()
            print("📜 Contenido actual:\n" + original)

        nuevo = input("✏️ Nuevo contenido: ")

        with open(nombre, "w", encoding="utf-8") as archivo:
            archivo.write(nuevo)
            print("✅ Contenido reemplazado.")
    except FileNotFoundError:
        print("❌ El archivo no existe.")

# leer_y_reemplazar()  ← descomentar para probar
```

---

## 🧪 Ejercicio 03 — `03_mezclar_lectura_y_escritura.py`

**🎯 Objetivo:** Leer, añadir contenido, y volver a mostrar todo en el mismo archivo usando `a+`.

### 🧭 Diagrama de flujo
```
Inicio
↓
Solicitar nombre del archivo
↓
Abrir en modo 'a+'
↓
Solicitar línea nueva
↓
Añadir línea con .write()
↓
Mover cursor al inicio con .seek(0)
↓
Leer y mostrar contenido actualizado
↓
Fin
```

### ✅ Código realizado
```python
def añadir_y_mostrar():
    nombre = input("📘 Nombre del archivo: ")
    try:
        with open(nombre, "a+", encoding="utf-8") as archivo:
            linea = input("➕ Línea nueva: ")
            archivo.write("\n" + linea)
            archivo.seek(0)
            print("📖 Contenido completo actualizado:\n")
            print(archivo.read())
    except Exception as e:
        print(f"❌ Error: {e}")

# añadir_y_mostrar()  ← descomentar para probar
```

---

## 🧾 Cierre de la clase

Dominar la lectura y escritura avanzada de archivos permite construir sistemas con persistencia sólida, edición dinámica de datos y procesamiento de registros. Saber utilizar `r+`, `a+`, validaciones y posicionamiento del cursor es fundamental para software profesional.

Esta clase representa una transición entre el uso básico de archivos y el procesamiento robusto que veremos en futuros proyectos y sistemas más complejos. 💡

---

## 🧠 Evaluación simbólica

🔹 Entendimiento profundo de modos `r+`, `a+`, `w+`: ✅
🔹 Lectura y escritura combinada: ✅
🔹 Validaciones y robustez del flujo: ✅
🔹 Aplicación profesional real: ✅

📌 **Nota simbólica: 10.75/10** 🎯 ¡Nivel intermedio profesional alcanzado!

