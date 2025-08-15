# 🔰 Clase 00 — Tipos de datos: `int`, `float`, `str`, `bool`

---

## 🧠 TEORÍA

## 📚 Tema: **Tipos de datos primitivos en Python**

---

## 🔹 1. INTRODUCCIÓN GENERAL

En toda disciplina de programación, la base es entender qué tipo de información vamos a procesar. Los **tipos de datos primitivos** representan las **formas más elementales de información** que un programa puede manipular.

### ¿Por qué son importantes?

✅ Determinan cómo se almacena y manipula la información en memoria
✅ Afectan la **eficiencia del programa** (memoria, CPU)
✅ Permiten validar y controlar la lógica del software
✅ Son **la base para estructuras más complejas** como listas, clases o bases de datos

---

## 🔸 2. CATEGORÍAS DE TIPOS PRIMITIVOS EN PYTHON

| Tipo de dato | Nombre técnico | Ejemplo  | Descripción breve         |
| ------------ | -------------- | -------- | ------------------------- |
| `int`        | Entero         | `42`     | Números sin decimales     |
| `float`      | Punto flotante | `3.14`   | Números con parte decimal |
| `str`        | Cadena         | `"Hola"` | Texto entre comillas      |
| `bool`       | Booleano       | `True`   | Verdadero o Falso         |

Todos los demás tipos de Python (listas, tuplas, diccionarios, etc.) **se basan o construyen sobre estos.**

---

## 🔹 3. `int` → NÚMEROS ENTEROS

### 🎓 Definición técnica

Un `int` (integer) representa un **número entero firmado**, positivo o negativo, sin decimales.
💡 En Python, la clase interna que lo representa es: `int`.

### 📐 Representación interna

* Usa el sistema binario de 2's complement.
* Su tamaño es **dinámico**, solo limitado por la RAM (a diferencia de otros lenguajes).

### ✅ Ejemplos válidos

```python
edad = 25
numero_negativo = -198
cero = 0
```

### ⚠️ Errores comunes

* `25.0` → esto **no es int**, es `float`
* `"25"` → esto **no es int**, es `str`

### 🔍 Uso en programación profesional

* Contadores (`i += 1`)
* Indexado de listas
* Identificadores únicos (ID)
* Sistemas bancarios (cuentas, saldos enteros)

---

## 🔹 4. `float` → NÚMEROS DECIMALES

### 💥 Definición técnica

Un `float` (floating-point number) es un número **real** que contiene **una parte fraccionaria**, representado en coma flotante IEEE-754.

### 💥 Representación interna

```text
±mantisa × base^exponente → IEEE 754 doble precisión (64 bits)
```

### 💥 Ejemplos válidos

```python
pi = 3.14159
temperatura = -7.25
altura = 1.75
```

### ⚠️ Edge Cases

```python
0.00000001  # precisión limitada
0.1 + 0.2   # no da 0.3 exactamente → 0.30000000000000004 (por representación binaria)
```

### 📊 Uso en programación profesional

* Cálculos científicos
* Finanzas (aunque con `Decimal` para exactitud)
* Coordenadas y físicas (juegos, simulaciones)

---

## 🔹 5. `str` → CADENAS DE TEXTO

### Definición técnica

Una cadena (`str`) es una **secuencia inmutable de caracteres Unicode**.
🧠 Unicode: representación de caracteres multilenguaje, emojis, símbolos, etc.

### Ejemplos válidos

```python
nombre = "Gabo"
saludo = 'Hola, ¿cómo estás?'
emoji = "🚀"
```

### 🧪 Propiedades clave

* Indexable y sliceable
* Inmutable (no se puede cambiar un carácter directamente)
* Puede concatenarse: `"Hola " + "Gabo"` → `"Hola Gabo"`

### ⚠️ Errores frecuentes

* `"25"` es `str`, no `int`
* Comillas no balanceadas causan `SyntaxError`

### 🛠 Uso profesional

* Interfaces de usuario
* Registro de logs
* Validación de inputs
* Mensajes dinámicos (`f-strings`)

---

## 🔹 6. `bool` → LÓGICA BINARIA

### - Definición técnica

Un `bool` (booleano) representa un valor de **lógica binaria**, es decir: `True` o `False`.
Internamente es una subclase de `int`, por eso:

```python
True == 1  # True
False == 0 # True
```

### - Ejemplos válidos

```python
es_mayor_de_edad = True
tiene_permiso = False
```

### 🔁 Evaluación implícita

Estos valores se **evalúan como `False`** automáticamente:

```python
0, 0.0, '', [], {}, None
```

### ⚠️ Errores

* `"True"` (cadena) ≠ `True` (booleano)
* `1` no es exactamente lo mismo que `True`, aunque se comporta similar

### 🧠 Uso profesional

* Validaciones (`if x:`)
* Lógica de negocio
* Flags de estado
* Condiciones en bucles o funciones

---

## 🧩 COMPARATIVA Y CONVERSIÓN ENTRE TIPOS

| Origen       | Conversión a int | a float         | a str    | a bool |
| ------------ | ---------------- | --------------- | -------- | ------ |
| `int(3)`     | —                | `3.0`           | `"3"`    | `True` |
| `float(3.5)` | `3`              | —               | `"3.5"`  | `True` |
| `str("10")`  | `int("10")`      | `float("10.0")` | —        | `True` |
| `bool(True)` | `1`              | `1.0`           | `"True"` | —      |

---

## 🔽 DIAGRAMA DE FLUJO GENERAL: TIPO DE DATO ENTRANTE

```text
[Input del usuario]
        ↓
¿Es numérico?
        ↓
     ┌────────────┐
     │   Sí       │
     └────┬───────┘
          ↓
¿Tiene punto decimal?
          ↓
    ┌──────┬─────────┐
    │ Sí   │ No      │
    ↓      ↓         ↓
 [float] [int]     [str]
          ↓
     ¿Es "True"/"False"?
          ↓
      [bool] si corresponde
```

---

## 🛠 UTILIDAD PRÁCTICA EN PROYECTOS REALES

| Proyecto         | Tipo clave       | Uso                            |
| ---------------- | ---------------- | ------------------------------ |
| 🧾 Facturación   | `float`          | Totales, impuestos             |
| 🔐 Autenticación | `bool`           | ¿Está autenticado?             |
| 📦 Inventario    | `int`            | Unidades en stock              |
| 🌍 Web scraping  | `str`            | Extracción de texto HTML       |
| 🎮 Videojuego    | `float` y `bool` | Posición, gravedad, colisiones |

---

## 🧠 TÉCNICAS AVANZADAS / EDGE CASES

```python
# str a int con validación
numero = "25"
if numero.isdigit():
    numero = int(numero)

# bool como bandera de estado
activo = False
if not activo:
    print("El sistema está inactivo")

# float exacto con Decimal
from decimal import Decimal
resultado = Decimal("0.1") + Decimal("0.2")  # = 0.3 exacto
```

---

🟢 **Avanzamos al primer ejercicio** de la **Clase 00 — Tipos de datos primitivos**
🔢 Tema del ejercicio: **`int` (números enteros)**
📁 Archivo sugerido: `01_tipo_dato_entero.py`
🎯 Objetivo: Comprender cómo declarar, convertir, operar y validar enteros en Python.

---

## 🧭 DESCRIPCIÓN DEL EJERCICIO 01

### Nombre: `tipo_dato_entero`

🔹 Crea un programa que:

1. Solicite al usuario un valor numérico entero (input).
2. Verifique si es realmente un entero (no decimal, no texto).
3. Si lo es, conviértelo a `int`, muéstralo, multiplícalo por 2, y eleva al cuadrado.
4. Si **no** es entero válido, muestra un mensaje de error personalizado.
5. Agrega una función `es_entero_valido(valor: str) -> bool` que encapsule la lógica de validación.

---

## 🔽 DIAGRAMA DE FLUJO TEXTUAL

```text
[Inicio]
   ↓
Solicitar input al usuario → [input()]
   ↓
Llamar a es_entero_valido(valor)
   ↓
¿Es un número entero válido?
   ↓
 ┌── Sí ───────────────┐
 │ Convertir a int     │
 │ Mostrar valor       │
 │ Multiplicar x2      │
 │ Elevar al cuadrado  │
 └────┬──────────────┘
      ↓
  Imprimir resultados
      ↓
 ┌── No ──────────────┐
 │ Mostrar error:     │
 │ "El valor ingresado │
 │ no es un entero."   │
 └────┬──────────────┘
      ↓
    [Fin]
```

---

## 📦 ESQUELETO GUÍA COMENTADO

```python
# 01_tipo_dato_entero.py

#1️⃣ Función que verifica si una cadena representa un entero válido
def es_entero_valido(valor: str) -> bool:
    """
    Retorna True si el valor puede convertirse a un int sin errores.
    """
    # Eliminar espacios en blanco y verificar si está vacío
    valor = valor.strip()
    if not valor:
        return False
    
    # Manejar el signo negativo
    valor = valor.lstrip("-")
    
    # Verificar si todos los caracteres restantes son dígitos
    return valor.isdigit()

#2️⃣ Solicitar entrada al usuario
entrada = input("🔢 Ingresa un número entero: ")

#3️⃣ Verificar si es válido usando la función
if es_entero_valido(entrada):
    #4️⃣ Convertir el string a entero
    numero = int(entrada)

    #5️⃣ Operaciones con el entero
    multiplicacion = numero * 2
    cuadrado = numero ** 2

    #6️⃣ Mostrar resultados con f-strings
    print(f"✅ Número ingresado: {numero}")
    print(f"📈 El número multiplicado por 2 es: {multiplicacion}")
    print(f"📊 El número al cuadrado es: {cuadrado}")
else:
    #7️⃣ Mensaje de error si no es entero válido
    print("❌ El valor ingresado no es un número entero válido.")

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
🔢 Ingresa un número entero: 55
✅ Número ingresado: 55
📈 El número multiplicado por 2 es: 110
📊 El número al cuadrado es: 3025
====================================================================
"""
```

---

### 🧪 Ejercicio 02 — `02_tipo_dato_decimal.py`

🎯 Tema: **Tipo de dato `float` (número decimal)**
📁 Archivo sugerido: `02_tipo_dato_decimal.py`
📚 Objetivo: Validar, convertir y operar correctamente con decimales en Python, detectando errores comunes de precisión.

---

## 🔧 DESCRIPCIÓN DEL EJERCICIO

Desarrolla un programa que:

1. Solicite al usuario un valor decimal (float).
2. Verifique si es un número decimal válido (incluyendo negativos y decimales sin 0 a la izquierda como `.75`).
3. Si lo es, conviértelo a `float`, imprímelo, divide por 2, y muestra su raíz cuadrada.
4. Si no es válido, muestra un mensaje de error claro.
5. La validación debe estar encapsulada en la función:
   `es_decimal_valido(valor: str) -> bool`

---

## DIAGRAMA DE FLUJO TEXTUAL

```text
[Inicio]
   ↓
Solicitar input al usuario → [input()]
   ↓
Llamar a es_decimal_valido(valor)
   ↓
¿Es un número decimal válido?
   ↓
 ┌── Sí ───────────────┐
 │ Convertir a float   │
 │ Mostrar valor       │
 │ Dividir por 2       │
 │ Calcular raíz       │
 └────┬──────────────┘
      ↓
  Imprimir resultados
      ↓
 ┌── No ──────────────┐
 │ Mostrar error:     │
 │ "El valor ingresado │
 │ no es un decimal."  │
 └────┬──────────────┘
      ↓
    [Fin]
```

---

## ESQUELETO GUÍA COMENTADO (no resuelto)

```python
# 02_tipo_dato_decimal.py

# ✅ Ejercicio 02 — tipo_dato_decimal
# Objetivo: Validar, convertir y operar con decimales en Python

#1️⃣ Función para verificar si un string puede interpretarse como float
def es_decimal_valido(valor: str) -> bool:
    """
    Retorna True si la cadena representa un número decimal válido (float).
    Acepta negativos, punto flotante, y formas como '.5' o '3.'.
    """
    # Eliminar espacios en blanco
    valor = valor.strip()
    if not valor:  # Verificar si la cadena está vacía
        return False
    try:
        float(valor)
        return True
    except ValueError:
        return False

#2️⃣ Solicitar entrada al usuario
entrada = input("🔢 Ingresa un número decimal: ")

#3️⃣ Validar usando la función
if es_decimal_valido(entrada):
    #4️⃣ Convertir a float
    numero = float(entrada)

    #5️⃣ Realizar operaciones
    mitad = numero / 2
    raiz = numero ** 0.5 if numero >= 0 else None  # Raíz solo si ≥ 0

    #6️⃣ Mostrar resultados con formato limitado a 4 decimales
    print(f"✅ Número ingresado: {numero:.4f}")
    print(f"📈 Dividido por 2: {mitad:.4f}")

    #7️⃣ Mostrar raíz cuadrada solo si válida
    if raiz is not None:
        print(f"📊 Raíz cuadrada: {raiz:.4f}")
    else:
        print("⚠️ No se puede calcular la raíz cuadrada de un número negativo.")
else:
    #8️⃣ Error en entrada no válida
    print("❌ El valor ingresado no es un número decimal válido.")

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
🔢 Ingresa un número decimal: 3.14
✅ Número ingresado: 3.1400
📈 Dividido por 2: 1.5700
📊 Raíz cuadrada: 1.7720

🔢 Ingresa un número decimal: -2.5
✅ Número ingresado: -2.5000
📈 Dividido por 2: -1.2500
⚠️ No se puede calcular la raíz cuadrada de un número negativo.

🔢 Ingresa un número decimal: abc
❌ El valor ingresado no es un número decimal válido.

🔢 Ingresa un número decimal:  .5
✅ Número ingresado: 0.5000
📈 Dividido por 2: 0.2500
📊 Raíz cuadrada: 0.7071

🔢 Ingresa un número decimal:  
❌ El valor ingresado no es un número decimal válido.
====================================================================
""" 
```

---

## 📚 Consideraciones técnicas avanzadas

🔹 Usamos `try/except` porque `float()` acepta formas válidas como:

* `"3."`, `".5"`, `"-0.123"`, `"-3.0"`
  y no son fácilmente validables con `.replace(".", "", 1).isdigit()`.

🔹 La raíz cuadrada con `** 0.5` solo se aplica si el valor es `>= 0` para evitar `math domain error`.

🔹 En módulos futuros, podríamos usar `decimal.Decimal` para mayor precisión financiera.

---

### **Clase 00 — Tipos de datos: `str` (texto)**

🧠 Modo: profesional, estructurado y profundo
📁 Archivo sugerido: `03_tipo_dato_texto.py`
📚 Objetivo: Validar, manipular y aplicar cadenas de texto de forma funcional y segura

---

## 🧭 DESCRIPCIÓN DEL EJERCICIO

Construye un script que:

1. Solicite al usuario que ingrese su **nombre completo** (texto).
2. Valide que el texto **no esté vacío** y **no contenga solo espacios**.
3. Una vez validado:

   * Muestra el nombre en **mayúsculas**, **minúsculas**, **capitalizado** y **título**.
   * Imprime **la cantidad de letras** reales del nombre (sin contar espacios).
   * Separa el **primer nombre** del resto con `.split()` y lo imprime.
4. Si el input es inválido (cadena vacía o espacios), lanza un mensaje de error personalizado.
5. Todo el proceso de validación debe estar encapsulado en:

   ```python
   def es_nombre_valido(texto: str) -> bool:
   ```

---

## DIAGRAMA DE FLUJO

```text
[Inicio]
   ↓
Solicitar nombre → input()
   ↓
Validar con es_nombre_valido()
   ↓
¿Texto válido?
   ↓
 ┌── Sí ───────────────────────────────┐
 │ Mostrar en mayúsculas               │
 │ Mostrar en minúsculas               │
 │ Mostrar capitalizado (capitalize)   │
 │ Mostrar con formato título (title)  │
 │ Contar letras sin espacios          │
 │ Mostrar primer nombre (split)       │
 └────┬───────────────────────────────┘
      ↓
 ┌── No ─────────────────────────────┐
 │ Mostrar error: nombre inválido    │
 └────┬─────────────────────────────┘
      ↓
    [Fin]
```

---

## ESQUELETO GUÍA COMENTADO

```python
# 03_tipo_dato_texto.py

# ✅ Ejercicio 03 — tipo_dato_texto
# Objetivo: Validar y manipular texto ingresado por el usuario

#1️⃣ Función para validar que el nombre no esté vacío ni lleno de espacios
def es_nombre_valido(texto: str) -> bool:
    """
    Retorna True si el texto ingresado tiene al menos una letra real (no espacios).
    """
    texto = texto.strip()
    return bool(texto) and any(c.isalpha() for c in texto)

#2️⃣ Solicitar nombre completo al usuario
entrada = input("📝 Ingresa tu nombre completo: ")

#3️⃣ Verificar validez
if es_nombre_valido(entrada):
    #4️⃣ Mostrar formatos
    print(f"🔠 Mayúsculas: {entrada.upper()}")
    print(f"🔡 Minúsculas: {entrada.lower()}")
    print(f"🅰️ Capitalizado: {entrada.capitalize()}")
    print(f"📚 Formato título: {entrada.title()}")

    #5️⃣ Contar letras reales (sin contar espacios)
    cantidad_letras = len(entrada.replace(" ", ""))
    print(f"🔢 Total de letras (sin espacios): {cantidad_letras}")

    #6️⃣ Mostrar primer nombre
    primer_nombre = entrada.strip().split()[0]
    print(f"👤 Primer nombre: {primer_nombre}")
else:
    #7️⃣ Error si no es válido
    print("❌ Nombre inválido: debes ingresar texto no vacío.")
```

---

## 🧪 Casos de prueba esperados

| Entrada             | Resultado esperado                                  |
| ------------------- | --------------------------------------------------- |
| `"  "`              | ❌ Error: texto vacío                                |
| `"Juan"`            | Mayúsculas, minúsculas, etc.                        |
| `"Ana María López"` | Título: `"Ana María López"`, primer nombre: `"Ana"` |
| `"  mario  "`       | Trim correcto, cuenta letras: `5`, no `9`           |

---

## EJERCICIO 4 `04_tipo_dato_booleano.py`

📁 Archivo sugerido: `04_tipo_dato_booleano.py`
🎯 Objetivo: Interpretar entradas del usuario como valores booleanos y operar con lógica condicional profesional

---

## DESCRIPCIÓN DEL EJERCICIO

Desarrolla un programa que:

1. Solicite al usuario una respuesta tipo **sí/no** (por ejemplo: `"sí"`, `"no"`, `"s"`, `"n"`, `"yes"`, `"no"`, en cualquier capitalización).
2. Valide que la entrada sea reconocida como opción afirmativa o negativa.
3. Devuelva un valor booleano correspondiente: `True` para afirmación, `False` para negación.
4. En base a ese valor booleano, imprime un mensaje distinto según el caso (`if-else`).
5. Implementa una función pura:

   ```python
   def interpretar_como_booleano(respuesta: str) -> bool | None
   ```

   Esta función debe:

   * Aceptar y normalizar entradas comunes (`"sí"`, `"s"`, `"yes"`, etc.)
   * Devolver `True`, `False` o `None` si no se reconoce la respuesta
6. Si la respuesta no es reconocida, muestra: `"❌ Respuesta no válida."`

---

## - DIAGRAMA DE FLUJO TEXTUAL

```text
[Inicio]
   ↓
Solicitar respuesta al usuario → [input()]
   ↓
Pasar a interpretar_como_booleano(respuesta)
   ↓
¿Qué devuelve?
   ↓
 ┌── True ────────┐      ┌── False ─────────┐
 │ Mostrar mensaje│      │ Mostrar mensaje │
 │ afirmativo     │      │ negativo         │
 └──────┬─────────┘      └──────┬───────────┘
        ↓                      ↓
   ┌── None ─────────────────────────┐
   │ Mostrar error: no reconocida   │
   └────────────────────────────────┘
        ↓
      [Fin]
```

---

## 📦 ESQUELETO GUÍA COMENTADO (no resuelto)

```python
# 04_tipo_dato_booleano.py

# ✅ Ejercicio 04 — tipo_dato_booleano
# Objetivo: Interpretar respuestas como valores booleanos

#1️⃣ Función pura que interpreta una respuesta de texto como booleano
def interpretar_como_booleano(respuesta: str) -> bool | None:
    """
    Convierte una cadena tipo sí/no a un valor booleano.
    Retorna:
    - True para afirmaciones
    - False para negaciones
    - None si no se reconoce
    """
    # Normalizar entrada: eliminar espacios y convertir a minúsculas
    respuesta = respuesta.strip().lower()
    respuesta = respuesta.replace("ì", "í")  # Corregir posibles acentos

    respuestas_positivas = {"sí", "si", "s", "yes", "y", "yeah", "ok"}
    respuestas_negativas = {"no", "n", "nope"}

    if respuesta in respuestas_positivas:
        return True
    elif respuesta in respuestas_negativas:
        return False
    else:
        return None

#2️⃣ Entrada del usuario
entrada = input("🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): ")

#3️⃣ Interpretar como booleano
valor = interpretar_como_booleano(entrada)

#4️⃣ Mostrar resultados
print()  # Nueva línea para mejor legibilidad
if valor is True:
    print("✅ Continuamos con el proceso.")
elif valor is False:
    print("🛑 Proceso cancelado por el usuario.")
else:
    print("❌ Respuesta no válida. Debes responder con 'sí', 'no', 's', 'n', 'yes', 'y', etc.")

"""
=========================================================================================
=== RESPUESTA DE CONSOLA ===
=========================================================================================
🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): sí
✅ Continuamos con el proceso.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): No
🛑 Proceso cancelado por el usuario.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): y
✅ Continuamos con el proceso.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): yeah
✅ Continuamos con el proceso.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): nope
🛑 Proceso cancelado por el usuario.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): maybe
❌ Respuesta no válida. Debes responder con 'sí', 'no', 's', 'n', 'yes', 'y', etc.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y):   
❌ Respuesta no válida. Debes responder con 'sí', 'no', 's', 'n', 'yes', 'y', etc.

🤔 ¿Deseas continuar? (sí/no/s/n/yes/y): sì
✅ Continuamos con el proceso.
=========================================================================================
""" 
```

---

## 🧪 Casos esperados

| Entrada    | Salida        |
| ---------- | ------------- |
| `"sí"`     | ✅ Continuamos |
| `"NO"`     | 🛑 Cancelado  |
| `"y"`      | ✅ Continuamos |
| `"n"`      | 🛑 Cancelado  |
| `"quizás"` | ❌ No válida   |
| `" "`      | ❌ No válida   |

---

## 🧪 Ejercicio 05 — `05_validacion_combinada_de_tipos.py`

📚 Tema: **Validación cruzada de tipos primitivos `int`, `float`, `str`, `bool`**
📁 Nivel: Integrador, técnico, con aplicación realista
🎯 Objetivo: Aplicar todo lo aprendido para procesar y validar un conjunto mixto de datos

---

## - DESCRIPCIÓN DEL EJERCICIO

📘 Crea un script que simule la recepción de datos de un formulario web, donde el usuario debe ingresar:

1. 📛 **Nombre completo**
2. 🔢 **Edad**
3. 💰 **Salario mensual (decimal)**
4. 🟢 **¿Acepta términos? (sí/no)**

✅ El programa debe:

* Validar que:

  * El **nombre** sea texto real no vacío
  * La **edad** sea un número entero válido y mayor que 0
  * El **salario** sea un número decimal mayor o igual a 0
  * La **aceptación de términos** sea una afirmación reconocible

* Imprimir los datos procesados, con tipos ya convertidos (`str`, `int`, `float`, `bool`)

* Mostrar un resumen profesional en consola, como si se tratara de un sistema real

---

## - DIAGRAMA DE FLUJO

```text
[Inicio]
   ↓
Solicitar nombre completo
   ↓
¿Nombre válido?
   ↓
 ┌── No ──► Mostrar error y salir
 └── Sí
   ↓
Solicitar edad
   ↓
¿Edad válida y > 0?
   ↓
 ┌── No ──► Mostrar error y salir
 └── Sí
   ↓
Solicitar salario
   ↓
¿Decimal válido y ≥ 0?
   ↓
 ┌── No ──► Mostrar error y salir
 └── Sí
   ↓
Solicitar aceptación de términos (sí/no)
   ↓
¿Respuesta afirmativa?
   ↓
 ┌── No ──► Mostrar mensaje: "Debes aceptar los términos"
 └── Sí
   ↓
Mostrar resumen con:
- Nombre (formateado)
- Edad (int)
- Salario (float con 2 decimales)
- Aceptación: ✅
   ↓
[Fin]
```

---

## 🧱 FUNCIONES REQUERIDAS

Debés reutilizar (o volver a implementar) las siguientes funciones ya desarrolladas en clases anteriores:

```python
def es_nombre_valido(texto: str) -> bool
def es_entero_valido(valor: str) -> bool
def es_decimal_valido(valor: str) -> bool
def interpretar_como_booleano(respuesta: str) -> bool | None
```

---

## 🧪 REQUISITOS DE VALIDACIÓN

| Campo    | Validación                  | Conversión                    | Restricción extra |
| -------- | --------------------------- | ----------------------------- | ----------------- |
| Nombre   | No vacío, contiene letras   | `str.strip().title()`         | —                 |
| Edad     | Número entero > 0           | `int()`                       | Mayor que cero    |
| Salario  | Número decimal ≥ 0          | `float()`                     | No negativo       |
| Términos | `"sí", "s", "yes"` → `True` | `interpretar_como_booleano()` | Debe ser `True`   |

---

```python
# 05_validacion_combinada_de_tipos.py

# ✅ Ejercicio 05 — validacion_combinada_de_tipos
# Objetivo: Validar múltiples entradas simulando un formulario de sistema real

#1️⃣ FUNCIONES AUXILIARES

def es_nombre_valido(texto: str) -> bool:
    """Valida que el nombre no sea vacío ni solo espacios."""
    texto = texto.strip()
    return bool(texto) and any(c.isalpha() for c in texto)

def es_entero_valido(valor: str) -> bool:
    """Valida que un string representa un número entero (positivo o negativo)."""
    valor = valor.strip()
    return valor.lstrip("-").isdigit() and valor != "-"

def es_decimal_valido(valor: str) -> bool:
    """Valida si un string puede convertirse a float."""
    valor = valor.strip()
    if not valor:
        return False
    try:
        float(valor)
        return True
    except ValueError:
        return False

def interpretar_como_booleano(respuesta: str) -> bool | None:
    """Interpreta entradas tipo sí/no como booleano."""
    respuesta = respuesta.strip().lower().replace("ì", "í")
    respuestas_positivas = {"sí", "si", "s", "yes", "y", "yeah", "ok"}
    respuestas_negativas = {"no", "n", "nope"}
    if respuesta in respuestas_positivas:
        return True
    elif respuesta in respuestas_negativas:
        return False
    return None

#2️⃣ FUNCIÓN PRINCIPAL PARA EL FORMULARIO

def procesar_formulario() -> None:
    """Procesa el formulario con validaciones y reintentos."""
    print("📋 INGRESO DE DATOS\n")

    # Nombre
    while True:
        nombre = input("📝 Nombre completo: ").strip()
        if es_nombre_valido(nombre):
            nombre = " ".join(nombre.split())  # Normalizar espacios
            break
        print("❌ Nombre inválido: debe contener al menos una letra.")

    # Edad
    while True:
        edad_input = input("🔢 Edad: ").strip()
        if es_entero_valido(edad_input):
            edad = int(edad_input)
            if 0 < edad <= 150:  # Límite razonable para edad
                break
            print("❌ La edad debe estar entre 1 y 150 años.")
        else:
            print("❌ Edad inválida: debe ser un número entero.")

    # Salario
    while True:
        salario_input = input("💰 Salario mensual: ").strip()
        if es_decimal_valido(salario_input):
            salario = float(salario_input)
            if salario >= 0:  # Salario no negativo
                break
            print("❌ El salario no puede ser negativo.")
        else:
            print("❌ Salario inválido: debe ser un número decimal (ej. 1500.50).")

    # Términos
    while True:
        respuesta_terminos = input("✅ ¿Aceptas los términos y condiciones? (sí/no/s/n/yes/y): ")
        acepta = interpretar_como_booleano(respuesta_terminos)
        if acepta is not None:
            if acepta:
                break
            print("❌ No se puede continuar sin aceptar los términos.")
        else:
            print("❌ Respuesta no válida: usa 'sí', 'no', 's', 'n', 'yes', 'y', etc.")

    #3️⃣ SALIDA DE DATOS FINALES
    print("\n✅ DATOS REGISTRADOS:\n")
    print(f"👤 Nombre: {nombre.title()}")
    print(f"🎂 Edad: {edad} años")
    print(f"💵 Salario: ${salario:.2f}")
    print(f"📄 Términos aceptados: ✅ Sí")

#4️⃣ EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    procesar_formulario()

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
📋 INGRESO DE DATOS

📝 Nombre completo: John Doe
🔢 Edad: 30
💰 Salario mensual: 2500.75
✅ ¿Aceptas los términos y condiciones? (sí/no/s/n/yes/y): yes

✅ DATOS REGISTRADOS:

👤 Nombre: John Doe
🎂 Edad: 30 años
💵 Salario: $2500.75
📄 Términos aceptados: ✅ Sí
====================================================================
""
```

## 🏁 CLASE 00 — ESTADO: ✅ FINALIZADA CON EXCELENCIA

📂 Archivos documentados:

* `01_tipo_dato_entero.py`
* `02_tipo_dato_decimal.py`
* `03_tipo_dato_texto.py`
* `04_tipo_dato_booleano.py`
* `05_validacion_combinada_de_tipos.py`

📌 Todos cumplen con los criterios:

* Modularidad
* Validación de entrada
* Experiencia de usuario
* Salida profesional
