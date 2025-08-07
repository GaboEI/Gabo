# 🟩 **CLASE 18 – Manipulación de Strings: `.split()`, `.strip()`, `.join()`, slicing**

📘 **Tema oficial validado**
🎯 *Aprender a dividir, limpiar, unir y extraer partes de texto con técnicas fundamentales de programación en Python.*

---

## 🧠 ¿Por qué esta clase es clave en tu formación?

### ✔️ Porque **todo programa real manipula texto**

* Formularios, inputs, logs, nombres de archivos, correos, etc.
* Procesamiento de datos (como CSV, JSON, HTML, APIs, scraping)
* Automatización de tareas administrativas

> Si dominas las cadenas, puedes “entender y limpiar el lenguaje de las máquinas”.

---

## 📚 PARTE 1: `.split()` — DIVIDIR TEXTO

### 🔹 Definición

El método `.split()` divide una cadena en partes más pequeñas (lista), usando un separador (espacio por defecto).

### 🔹 Sintaxis

```python
cadena.split(separador)
```

### 🔹 Ejemplos

```python
frase = "Hola Gabo, bienvenido al curso"
palabras = frase.split()
print(palabras)  # ['Hola', 'Gabo,', 'bienvenido', 'al', 'curso']
```

```python
correo = "gabo@correo.com"
usuario = correo.split("@")[0]
print(usuario)  # 'gabo'
```

### 🔹 Casos profesionales

* Leer líneas separadas por comas o puntos
* Dividir palabras clave
* Extraer partes de rutas, emails, etc.

---

## 📚 PARTE 2: `.strip()` — LIMPIAR TEXTO

### Definición

El método `.strip()` elimina **espacios u otros caracteres innecesarios** al inicio y al final de una cadena.

### Sintaxis

```python
cadena.strip()         # Elimina espacios
cadena.strip("abc")    # Elimina los caracteres indicados
```

### Ejemplos

```python
nombre = "   Gabriel Espinosa   "
print(nombre.strip())  # 'Gabriel Espinosa'
```

```python
linea = "###Hola###"
print(linea.strip("#"))  # 'Hola'
```

### Casos profesionales

* Limpiar inputs de usuario
* Validar campos vacíos
* Preparar texto para ser guardado o exportado

---

## 📚 PARTE 3: `.join()` — UNIR TEXTO

### -Definición

`.join()` une elementos de una lista de strings en **una sola cadena**, usando un separador.

### -Sintaxis

```python
separador.join(lista)
```

### -Ejemplos

```python
palabras = ["Hola", "Gabo", "bienvenido"]
frase = " ".join(palabras)
print(frase)  # 'Hola Gabo bienvenido'
```

```python
csv = ",".join(["Juan", "23", "Cuba"])
print(csv)  # 'Juan,23,Cuba'
```

### -Casos profesionales

* Crear archivos tipo CSV
* Unir textos para generar logs, reportes
* Construir frases dinámicas o plantillas

---

## 📚 PARTE 4: **Slicing** — EXTRAER POR POSICIÓN

### _Definición

Slicing permite **extraer partes de una cadena** indicando su posición.

### _Sintaxis

```python
cadena[inicio:fin:paso]
```

* `inicio`: índice inicial (incluido)
* `fin`: índice final (no incluido)
* `paso`: (opcional) saltos

### _Ejemplos

```python
texto = "Python es poderoso"
print(texto[0:6])   # 'Python'
print(texto[11:])   # 'poderoso'
print(texto[-9:])   # también 'poderoso'
```

```python
palabra = "Gabriel"
print(palabra[::-1])  # 'leirbaG' (texto invertido)
```

### _Casos profesionales

* Extraer nombres, fechas, códigos de producto
* Manipular estructuras semiestructuradas (como logs)
* Validar formatos

---

## 🎓 Resumen de cada método

| Método     | ¿Qué hace?                           | Retorna           |
| ---------- | ------------------------------------ | ----------------- |
| `.split()` | Divide string en partes              | Lista             |
| `.strip()` | Elimina caracteres innecesarios      | String limpio     |
| `.join()`  | Une una lista de strings             | String resultante |
| slicing    | Extrae parte del string por posición | Substring         |

---

## 🧠 Aplicación real en la vida profesional

Este conocimiento se usa en:

* Automatización de formularios y validaciones
* Conversión de datos de texto a estructuras
* Web scraping, análisis de archivos, APIs
* Preprocesamiento de datos en Machine Learning
* Bots, dashboards, paneles de monitoreo

---
