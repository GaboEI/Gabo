# 🟪 **CLASE 18 EXTENSIÓN – Métodos útiles de strings**

---
📘 *Ampliación natural posterior a la Clase 18 oficial – Aprobada por Gabo*
🎯 Tema: Métodos avanzados de string para transformación, consulta y validación textual.

## 📚 TEORÍA PROFUNDA – MÉTODOS ÚTILES DE STRINGS

Los strings (`str`) en Python no son simples textos:
Son **objetos que tienen métodos internos incorporados**, que puedes aplicar directamente para manipular, transformar y consultar datos de forma profesional.

Vamos uno por uno con definiciones, ejemplos y casos reales.

---

## 🧠 1. `.upper()` y `.lower()`

### 🔹 `.upper()`

Convierte **todo el texto** a **mayúsculas**.

```python
texto = "hola mundo"
print(texto.upper())  # 'HOLA MUNDO'
```

### 🔹 `.lower()`

Convierte **todo el texto** a **minúsculas**.

```python
texto = "Python ES Genial"
print(texto.lower())  # 'python es genial'
```

🔧 **Casos reales:**

* Comparar textos sin importar mayúsculas/minúsculas
* Preparar datos para sistemas que requieren formato uniforme
* Transformar campos para búsqueda

---

## 🧠 2. `.replace()`

### 🔹 ¿Qué hace?

Reemplaza **una subcadena por otra**.

```python
frase = "Hola Gabo"
print(frase.replace("Gabo", "Mundo"))  # 'Hola Mundo'
```

### 🔹 Sintaxis

```python
texto.replace("antiguo", "nuevo")
```

📌 También sirve para eliminar:

```python
texto.replace(" ", "")  # elimina todos los espacios
```

🔧 **Casos reales:**

* Corregir errores comunes de escritura
* Preparar texto para exportar (quitar símbolos)
* Censurar palabras

---

## 🧠 3. `.startswith()` y `.endswith()`

### 🔹 `.startswith(substring)`

Devuelve `True` si el texto **comienza con** esa subcadena.

```python
codigo = "ABC123"
print(codigo.startswith("ABC"))  # True
```

### 🔹 `.endswith(substring)`

Devuelve `True` si el texto **termina con** esa subcadena.

```python
archivo = "informe.pdf"
print(archivo.endswith(".pdf"))  # True
```

🔧 **Casos reales:**

* Verificar extensiones de archivo
* Validar prefijos de código o identificadores
* Control de formatos

---

## 🧠 4. `.title()` y `.capitalize()`

### 🔹 `.title()`

Convierte la primera letra de **cada palabra** a mayúscula.

```python
nombre = "gabo espinosa"
print(nombre.title())  # 'Gabo Espinosa'
```

### 🔹 `.capitalize()`

Convierte solo la **primera letra del string** a mayúscula, el resto en minúscula.

```python
titulo = "hOLa mUnDo"
print(titulo.capitalize())  # 'Hola mundo'
```

🔧 **Casos reales:**

* Estilizar nombres, títulos, encabezados
* Mostrar campos correctamente formateados en formularios

---

## 🧠 5. `.find()` y `.index()`

### 🔹 `.find("texto")`

Devuelve la **posición (índice)** donde aparece la subcadena.
Si no la encuentra, devuelve `-1`.

```python
frase = "Python es poderoso"
print(frase.find("es"))  # 7
```

### 🔹 `.index("texto")`

Hace lo mismo que `.find()`, pero **lanza error** si no encuentra.

```python
frase.index("no-existe")  # ❌ ValueError
```

🔧 **Casos reales:**

* Buscar palabras clave en descripciones
* Extraer partes desde una posición específica
* Validar contenido

---

## 🧠 6. `.count()`

### ⏺️ ¿Qué hace?

Cuenta cuántas veces aparece una subcadena.

```python
texto = "gabo gabo gabo"
print(texto.count("gabo"))  # 3
```

🔧 **Casos reales:**

* Contar ocurrencias de palabras, símbolos, etc.
* Verificar repeticiones en texto plano

---

## 🧠 7. `.isdigit()`, `.isalpha()`, `.isalnum()`

| Método       | ¿Qué valida?                                |
| ------------ | ------------------------------------------- |
| `.isdigit()` | Solo números                                |
| `.isalpha()` | Solo letras (sin espacios)                  |
| `.isalnum()` | Letras y números (sin espacios ni símbolos) |

```python
"123".isdigit()   # True
"abc".isalpha()   # True
"abc123".isalnum()  # True
"abc 123".isalnum() # False
```

🔧 **Casos reales:**

* Validar inputs antes de guardar o procesar
* Evitar errores en conversiones
* Seguridad de datos

---

## 🧠 8. `.strip()`, `.lstrip()`, `.rstrip()` (repaso rápido)

Ya visto antes, pero aquí va de nuevo por contexto:

| Método      | Elimina...             |
| ----------- | ---------------------- |
| `.strip()`  | Espacios a ambos lados |
| `.lstrip()` | Solo al inicio         |
| `.rstrip()` | Solo al final          |

---

## 🧠 9. `.split()` (combinado con otros métodos)

```python
frase = "  hola mundo  "
palabras = frase.strip().lower().split()
print(palabras)  # ['hola', 'mundo']
```

🔧 Así puedes combinar `.strip()`, `.lower()` y `.split()` para hacer **preprocesamiento de texto real**, como se hace en proyectos de scraping, IA o limpieza de datos.

---

## 📊 TABLA RESUMEN DE MÉTODOS ÚTILES

| Método          | ¿Para qué sirve?                    |
| --------------- | ----------------------------------- |
| `.upper()`      | Convertir todo en mayúsculas        |
| `.lower()`      | Convertir todo en minúsculas        |
| `.replace()`    | Reemplazar texto                    |
| `.startswith()` | Verificar inicio de texto           |
| `.endswith()`   | Verificar final de texto            |
| `.title()`      | Capitalizar cada palabra            |
| `.capitalize()` | Capitalizar solo la primera palabra |
| `.find()`       | Buscar posición de una subcadena    |
| `.count()`      | Contar cuántas veces aparece algo   |
| `.isdigit()`    | ¿Solo números?                      |
| `.isalpha()`    | ¿Solo letras?                       |
| `.isalnum()`    | ¿Letras y números (sin símbolos)?   |

---

## 📂 LISTADO DE EJERCICIOS (Clase 18 Extensión)

| Nº  | Archivo sugerido                     | Nombre del ejercicio                                | Métodos enfocados                           |
| --- | ------------------------------------ | --------------------------------------------------- | ------------------------------------------- |
| 1️⃣ | `01_validar_archivo_pdf.py`          | Verificar si un archivo es `.pdf`                   | `.endswith()`                               |
| 2️⃣ | `02_formatear_nombre_completo.py`    | Formatear nombre y apellido correctamente           | `.strip()`, `.title()`                      |
| 3️⃣ | `03_reemplazar_palabra.py`           | Reemplazar palabras prohibidas por asteriscos       | `.replace()`                                |
| 4️⃣ | `04_buscar_y_contar_palabra.py`      | Buscar palabra clave y contar cuántas veces aparece | `.find()`, `.count()`                       |
| 5️⃣ | `05_validar_codigo_identificador.py` | Validar estructura de un código alfanumérico        | `.startswith()`, `.isalnum()`, `.isdigit()` |

---
