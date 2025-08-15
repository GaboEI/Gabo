# VARIABLES Y CONSTANTES

---

## 🎓 1. ¿Qué es una variable en programación?

Una **variable** en programación es un **espacio con nombre en memoria RAM** que usamos para almacenar temporalmente un **valor que puede cambiar** mientras el programa está en ejecución.

🔁 En lenguaje simple:
Una variable es **como una etiqueta** que se le pega a una caja. Puedes cambiar lo que hay dentro de la caja, pero la etiqueta sigue siendo la misma.

📦 Ejemplo mental:

```plaintext
Caja con etiqueta: edad
Contenido: 25
```

📚 En Python, las variables se crean automáticamente en el momento que se **les asigna un valor**, gracias a su **tipado dinámico**.

---

## 📏 2. ¿Qué es una constante?

Una **constante** es **una variable cuyo valor no debe cambiar** a lo largo del programa.

📌 Python **no tiene constantes reales**, pero por **convención profesional**, se declaran **en mayúsculas** para indicar que **no deben modificarse**.

📦 Ejemplo mental:

```plaintext
Etiqueta: PI
Contenido: 3.1416  (¡no se debe tocar!)
```

✍️ En código:

```python
PI = 3.1416
```

Aunque técnicamente podrías cambiar su valor, **nunca deberías hacerlo** si está en mayúsculas, ya que eso rompe las buenas prácticas.

---

## 🧠 3. Analogía mental: memoria RAM = pizarra temporal

Imagina la **RAM** como una gran **pizarra blanca** donde el sistema va anotando datos temporales mientras ejecutas programas.

Cada vez que creas una variable, estás escribiendo en esa pizarra:

```.
↓ Declaración
├── nombre: temperatura
└── valor: 22.5
```

Si luego haces:

```python
temperatura = 25.0
```

La pizarra **borra** el anterior `22.5` y **escribe** `25.0`.
Esto se llama **reasignación de valor**.

---

## 🧪 4. Notación formal: `nombre = valor`

🧪 Esta es la **estructura básica universal** en Python para declarar variables:

```python
nombre = valor
```

📌 El símbolo `=` no significa "igual" como en matemáticas. En programación, significa:
**“Asigna a esta variable este valor”** → también llamado **operador de asignación**.

---

## 📐 5. Tipado dinámico en Python

🧪 Python es un lenguaje de **tipado dinámico**, lo que significa que **no necesitas declarar el tipo** de la variable: Python lo infiere automáticamente.

```python
x = 10        # int
x = "Hola"    # str
x = 3.14      # float
x = True      # bool
```

✔️ Esto **facilita el código**, pero también implica que debes tener **claridad sobre los tipos de datos** para evitar errores lógicos más adelante.

---

## ♻️ 6. Reasignación de valores

Puedes cambiar el valor de una variable en cualquier momento:

```python
usuario = "Gabo"
usuario = "Carlos"
```

📌 Solo existirá el **último valor asignado**. El anterior se elimina de la RAM si no está en uso.

---

## 🔏 7. Mutabilidad

✍️ El **valor** almacenado en una variable puede ser:

* **Mutable:** puede cambiar internamente sin cambiar de referencia (ej. listas, diccionarios).
* **Inmutable:** no puede modificarse internamente (ej. int, float, str, bool).

✅ En esta clase trabajaremos con tipos **inmutables**.

---

## ✅ Hasta aquí cubrimos

| Concepto        | Descripción breve                                    |
| --------------- | ---------------------------------------------------- |
| Variable        | Espacio en RAM que almacena un dato temporal         |
| Constante       | Variable que **no se debe cambiar** (por convención) |
| Tipado dinámico | Python detecta el tipo automáticamente               |
| Asignación `=`  | Da un valor a una variable                           |
| Reasignación    | Se puede cambiar el valor más adelante               |
| Mutabilidad     | Inmutable: el valor no puede cambiar internamente    |

---

## 📐 1. Declaración y asignación de variables

### 📌 Definición formal

> Una **variable** es una **asociación nombrada** a una **dirección de memoria** que contiene un valor.

### 🧠 Sintaxis básica en Python

```python
nombre_variable = valor
```

⚠️ Ojo: **no se usa `let`, `var` ni `int` como en otros lenguajes** (JavaScript, C, Java…).
Python infiere automáticamente el tipo, y no es necesario “declarar” antes de asignar.

---

### 🧪 Ejemplos básicos

```python
nombre = "Gabo"       # str
edad = 32             # int
altura = 1.75         # float
es_programador = True # bool
```

---

## 🔍 2. ¿Qué sucede en memoria?

```plaintext
↓ Código
├── edad = 32
↓ RAM
├── [variable: edad] → [valor: 32]  (tipo int)
```

Cada vez que declaras una variable, Python reserva un espacio y lo etiqueta con el nombre.

🧠 Python también **etiqueta internamente** el tipo de dato. Puedes comprobarlo con:

```python
type(edad)  # <class 'int'>
```

---

## 🎯 3. Reglas de sintaxis en nombres de variables

### ✅ Permitido

* Letras (a-z, A-Z)
* Números (pero **no al inicio**)
* Guiones bajos (`_`)
* Mayúsculas o minúsculas (es **sensible**)

```python
cliente = "Ana"
cliente_2 = "Luis"
_dato_privado = 15
```

### ❌ No permitido

* Empezar con números
* Incluir espacios
* Usar signos raros: `@`, `!`, `-`, `*`, etc.
* Usar palabras reservadas de Python (`for`, `if`, `class`, `def`, `import`, etc.)

```python
2edad = 30         ❌ inválido
nombre completo = "Juan" ❌ inválido
for = "algo"       ❌ reservado
```

---

## 🧠 4. Tipado dinámico vs estático

| Concepto             | Python (tipado dinámico) | C / Java (tipado estático)        |
| -------------------- | ------------------------ | --------------------------------- |
| ¿Se declara tipo?    | ❌ No                     | ✅ Sí                              |
| ¿Puede cambiar tipo? | ✅ Sí                     | ❌ No sin casting explícito        |
| ¿Flexible?           | ✅ Muy flexible           | 🚫 Menos flexible pero más seguro |

```python
x = 5
x = "cinco"
x = True
```

Python lo permite, pero **no es buena práctica profesional cambiar tipos constantemente.**

---

## 🧲 5. Constantes por convención

### 🔒 Python no bloquea las constantes, pero sí usamos un estándar

> **Una constante se escribe siempre en MAYÚSCULAS y no se modifica.**

```python
TASA_INTERES = 0.05
PI = 3.1416
EMPRESA = "1win"
```

✔️ Aunque Python **no prohíbe que se reasigne**, tú y tu equipo deben **respetar esa convención** como un acuerdo.

---

## 🧮 6. Mutabilidad: ¿se puede cambiar el contenido?

En esta clase trabajamos con **valores inmutables**:

| Tipo    | ¿Mutable? | Ejemplo de modificación                          |
| ------- | --------- | ------------------------------------------------ |
| `int`   | ❌ No      | `x = 5 → x = 10` (reasignación, no modificación) |
| `float` | ❌ No      | `pi = 3.14 → pi = 3.1416`                        |
| `str`   | ❌ No      | `"hola"` no se puede modificar letra por letra   |
| `bool`  | ❌ No      | `estado = True → estado = False`                 |

🚫 No puedes hacer:

```python
texto = "Hola"
texto[0] = "X"   # ❌ ERROR
```

---

## ✨ 7. Buenas prácticas en nombres de variables

### ✔️ Sigue la convención `snake_case`

```python
nombre_completo = "Ana Teresa"
total_productos = 42
```

📌 Así se mejora la legibilidad, especialmente en equipos profesionales.

### 🧼 Sé claro y explícito

```python
x = 42        ❌ opaco
cantidad = 42 ✅ claro
```

---

### 🧠 Conclusión de esta sección

| Tema clave                       | Dominado ✅ |
| -------------------------------- | ---------- |
| Sintaxis para declarar variables | ✅          |
| Nombres válidos e inválidos      | ✅          |
| Tipado dinámico en Python        | ✅          |
| Convención de constantes         | ✅          |
| Mutabilidad de los tipos         | ✅          |
| snake\_case profesional          | ✅          |

---

## 🧪 1. Ejemplo — Variable de texto (`str`)

```python
nombre = "Gabo"
print(nombre)        # Muestra: Gabo
print(type(nombre))  # Muestra: <class 'str'>
```

📌 Aquí:

* Se crea una variable llamada `nombre`.
* Se le asigna el valor `"Gabo"`, que es una cadena de texto.
* `type()` nos confirma que es de tipo `str`.

---

## 🔁 2. Ejemplo — Reasignación de variable (tipado dinámico)

```python
x = 10
print(x, type(x))    # Muestra: 10 <class 'int'>

x = "Diez"
print(x, type(x))    # Muestra: Diez <class 'str'>
```

📌 Aquí:

* `x` primero es un `int`.
* Luego pasa a ser un `str` sin errores.
* Python permite este cambio sin necesidad de castings.

⚠️ Pero en código profesional, **esto debe evitarse** para mantener coherencia semántica.

---

## 🔄 3. Ejemplo — Reasignación de valor sin cambiar tipo

```python
edad = 25
print("Edad inicial:", edad)

edad = 30
print("Edad actualizada:", edad)
```

📌 Aquí:

* La variable `edad` cambia de 25 a 30.
* El tipo (`int`) se mantiene.
* La **reasignación borra el valor anterior** de la memoria si no está referenciado.

---

## 🔠 4. Ejemplo — Constante por convención

```python
EMPRESA = "1win"
print(EMPRESA)
```

📌 Se declara en mayúsculas.
Aunque **se podría hacer esto**:

```python
EMPRESA = "OtraEmpresa"  # Técnicamente válido ❌ pero NO recomendado
```

… romperías la convención. Un equipo serio te penalizaría por ello.

---

## 🔍 5. Ejemplo — Nombres inválidos

```python
2nombre = "Juan"     # ❌ Error: no puede iniciar con número
nombre completo = "Ana"  # ❌ Error: no se permiten espacios
for = "dato"         # ❌ Error: 'for' es una palabra reservada
```

🔐 Siempre valida los nombres antes de usarlos.

---

## 📚 6. Ejemplo — Variables con booleanos

```python
activo = True
print(activo, type(activo))  # Muestra: True <class 'bool'>
```

👆 Útil para sistemas de estado (ON/OFF, login, acceso, etc.)

---

## 📐 7. Ejemplo — Usar `type()` para validar

```python
producto = "Teclado"
precio = 49.99
stock = 120
disponible = True

print(type(producto))   # str
print(type(precio))     # float
print(type(stock))      # int
print(type(disponible)) # bool
```

✔️ Confirmamos los tipos sin necesidad de anotarlos.

---

📌 Hasta aquí vimos:

| Variable   | Valor de ejemplo | Tipo    | Explicación breve                       |
| ---------- | ---------------- | ------- | --------------------------------------- |
| nombre     | "Gabo"           | `str`   | Texto                                   |
| edad       | 25               | `int`   | Número entero                           |
| precio     | 49.99            | `float` | Decimal                                 |
| disponible | True             | `bool`  | Booleano (sí/no)                        |
| EMPRESA    | "1win"           | `str`   | Constante por convención (no modificar) |

---

## Ejercicio 1️⃣ — `crear_variable_numerica_y_mostrarla`

---

## 🎯 Objetivo del ejercicio

* Comprender y aplicar la **asignación de una variable entera**
* Seguir buenas prácticas de **nombres en `snake_case`**
* Usar la función `print()` para mostrar el valor almacenado

---

## 🧠 Teoría puntual para este ejercicio

🔹 Una **variable** en Python se declara con la sintaxis:

```python
nombre_variable = valor
```

🔹 En este caso, usaremos el tipo `int`, que representa un número entero.

🔹 La función `print()` se usa para mostrar el contenido de una variable:

```python
print(nombre_variable)
```

🔹 Ejemplo general (no resolver):

```python
temperatura = 25
print(temperatura)
```

---

## 🔽 Diagrama de flujo del ejercicio

```.
Inicio
 ↓
Asignar un número entero a una variable llamada edad
 ↓
Mostrar el valor de la variable con print()
 ↓
Fin
```

---

## 🧱 Esqueleto guía del ejercicio `crear_variable_numerica_y_mostrarla.py`

```python
#1️⃣ Declarar una variable llamada edad y asignarle un número entero
edad = 25

#2️⃣ Mostrar el valor de la variable en consola
print(edad)

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
25
====================================================================
"""
```

---

🧠 ¡Perfecto, Gabo!
Comenzamos con el ejercicio 2️⃣ de la clase:

---

## 🧪 Ejercicio 2️⃣ — `reutilizar_variable_para_calculo`

---

## ✍️ Objetivo del ejercicio

* Comprender cómo **una variable puede cambiar su valor a lo largo del programa**
* Aplicar la idea de **reasignación** sin necesidad de crear una nueva variable
* Introducir la noción de **almacenar resultados intermedios** en la misma referencia

---

## ✍️ Teoría puntual para este ejercicio

🔹 Reutilizar una variable significa **asignarle un nuevo valor derivado del anterior**.

```python
# Antes
numero = 10

# Después
numero = numero + 5  # número ahora vale 15
```

📌 Este patrón es común cuando:

* Queremos acumular o modificar valores (contador, saldo, total, etc.)
* Necesitamos simplificar código sin declarar muchas variables nuevas

⚠️ En este punto **NO usaremos operadores abreviados** como `+=` porque aún no vimos operadores.

---

## 🔽 Diagrama de flujo

```.
Inicio
 ↓
Declarar una variable con un número base
 ↓
Reasignar la misma variable con un nuevo valor (suma)
 ↓
Mostrar el nuevo valor en consola
 ↓
Fin
```

---

## 🧱 Esqueleto guía del ejercicio `reutilizar_variable_para_calculo.py`

```python
#1️⃣ Crear una variable llamada valor_inicial con un número entero
valor_inicial = 50

#2️⃣ Reutilizar esa misma variable para sumarle otro número (ej: 10)
valor_inicial = valor_inicial + 10

#3️⃣ Mostrar el nuevo valor de la variable
print(valor_inicial)

"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
60
====================================================================
"""
```

---

🧠 ¡Perfecto, Gabo!
Comenzamos con el ejercicio 3️⃣ de esta clase:

---

## 🟨 Ejercicio 3️⃣ — `declarar_variable_con_texto_y_mostrar_tipo`

---

## 🟨 Objetivo del ejercicio

* Declarar una variable que contenga un texto (tipo `str`)
* Utilizar la función `type()` para **validar el tipo de dato**
* Mostrar ambos resultados en consola usando `print()`

---

## 🟨 Teoría puntual para este ejercicio

### 🔹 ¿Qué es `str`?

Es el tipo que representa cadenas de texto.
Toda secuencia entre comillas (`'` o `"`) se interpreta como texto en Python.

```python
nombre = "Gabo"
```

### 🔹 ¿Qué hace la función `type()`?

Devuelve el tipo de dato de una variable:

```python
x = "Hola"
print(type(x))  # <class 'str'>
```

✅ Esto es clave en Python porque su tipado es **dinámico**.
Validar el tipo puede ayudarte a evitar errores lógicos al operar.

---

## 🟨 Diagrama de flujo del ejercicio

```[]
Inicio
 ↓
Declarar una variable con texto (ej: nombre completo)
 ↓
Mostrar el valor con print()
 ↓
Mostrar el tipo con type()
 ↓
Fin
```

---

## 🧱 Esqueleto guía del ejercicio `declarar_variable_con_texto_y_mostrar_tipo.py`

```python
#1️⃣ Crear una variable llamada nombre_completo con un texto (entre comillas)
nombre_completo = "Ana López"

#2️⃣ Mostrar el valor de la variable en consola
print(nombre_completo)

#3️⃣ Mostrar el tipo de dato de esa variable usando type()
print(type(nombre_completo))

"""
============================
=== RESPUESTA DE CONSOLA ===
============================
Ana López
<class 'str'>
============================
"""
```

---

## 💥 Ejercicio 4️⃣ — `nombrar_variable_de_forma_erronea_y_corregir`

---

## 💥 Objetivo del ejercicio

* Detectar y **comprender por qué algunos nombres de variables son inválidos en Python**
* Aplicar las **reglas formales de sintaxis de nombres de variables**
* Corregir los nombres de manera profesional y clara

---

## 💥 Teoría puntual para este ejercicio

### ✅ Nombres de variables **válidos**:

* Comienzan con letra o guion bajo (`_`)
* Usan solo letras, números o guion bajo
* Son **sensibles a mayúsculas**
* No usan palabras reservadas del lenguaje

```python
nombre_completo = "Ana"
_dato_privado = 10
cliente2 = "Luis"
```

---

### ❌ Nombres de variables **inválidos**:

| Tipo de error        | Ejemplo           | ¿Por qué falla?                               |
| -------------------- | ----------------- | --------------------------------------------- |
| Inicia con número    | `2edad = 25`      | No puede iniciar con dígito                   |
| Contiene espacio     | `nombre completo` | Python no permite espacios en identificadores |
| Usa símbolo raro     | `total$ = 100`    | `$` no está permitido en nombres              |
| Es palabra reservada | `for = 3`         | `for` es parte del lenguaje                   |

---

## 💥 Diagrama de flujo

```💥
Inicio
 ↓
Escribir 3 nombres de variables inválidos
 ↓
Corregirlos aplicando buenas prácticas (snake_case)
 ↓
Mostrar sus valores en consola
 ↓
Fin
```

---

## 🧱 Esqueleto guía del ejercicio `nombrar_variable_de_forma_erronea_y_corregir.py`

```python
#1️⃣ Escribir 3 variables con errores de nombre (comentadas, no deben ejecutarse)
# 2edad = 30           # ❌ inicia con número
# nombre completo = "Carlos"  # ❌ contiene espacio
# for = 1              # ❌ palabra reservada

#2️⃣ Corregir cada una aplicando snake_case y nombres válidos
# edad = ___
# nombre_completo = ___
# iteracion = ___

#3️⃣ Mostrar los valores corregidos
# print(___)
# print(___)
# print(___)
```

---

📘 **EVALUACIÓN FINAL — CLASE 01: variables\_y\_constantes**

---

🎓 **Modalidad:** teórico-práctica
📊 **Estructura de evaluación:**

| Parte          | Contenido                   | Puntaje |
| -------------- | --------------------------- | ------- |
| 🧠 Teoría      | 2 preguntas conceptuales    | 2 pts   |
| 🧪 Práctica    | 1 ejercicio integrador      | 8 pts   |
| 🏁 Total final | Aprobación mínima: **7/10** | **/10** |

---

## 🧠 PARTE 1: PREGUNTAS TEÓRICAS (1 punto cada una)

✍️ **Pregunta 1:**
Explica con tus palabras qué es una constante en Python y cómo se representa.
Respuesta: definición clara, convención con mayúsculas, y por qué no se modifica.

✍️ **Pregunta 2:**
¿Por qué el siguiente nombre de variable genera error en Python?

```python
nombre completo = "Ana"
```

Respuesta: causa del error de sintaxis, y sugerencia de corrección válida.

---

## 🧪 PARTE 2: EJERCICIO INTEGRADOR FINAL

### 📄 Enunciado — `ejercicio_final_variables_y_constantes.py`

> 📌 **Contexto**: Estás desarrollando un pequeño script para mostrar información básica de un empleado de tu empresa.
> Debes declarar y mostrar correctamente las siguientes variables:

1. Una **constante** llamada `EMPRESA` con el nombre `"1win"`
2. Una variable `nombre_empleado` con cualquier nombre completo
3. Una variable `edad_empleado` con un número entero
4. Una variable `es_activo` que indique si el empleado está activo (`True` o `False`)
5. Mostrar todas las variables usando `print()`
6. Mostrar el tipo de cada una usando `type()` en líneas separadas

---

### ✅ Requisitos

* Estilo profesional en nombres (`snake_case`)
* La constante debe estar en mayúsculas
* No se deben usar operadores aún
* Código limpio, indentado, con comentarios si deseas

---

## 🧱 Esqueleto guía opcional (puedes ignorarlo si quieres hacerlo desde cero):

```python
# Declarar constante de empresa
EMPRESA = "Tech Solutions"

# Datos del empleado
nombre_empleado = "Laura Gómez"
edad_empleado = 28
es_activo = True

# Mostrar valores con etiquetas
print("Empresa:", EMPRESA)
print("Empleado:", nombre_empleado)
print("Edad:", edad_empleado)
print("Activo:", es_activo)

# Mostrar tipos con etiquetas
print("Tipo de empresa:", type(EMPRESA))
print("Tipo de empleado:", type(nombre_empleado))
print("Tipo de edad:", type(edad_empleado))
print("Tipo de activo:", type(es_activo))

"""
=================================
===    RESPUESTA DE CONSOLA   ===
=================================
Empresa: Tech Solutions
Empleado: Laura Gómez
Edad: 28
Activo: True
Tipo de empresa: <class 'str'>
Tipo de empleado: <class 'str'>
Tipo de edad: <class 'int'>
Tipo de activo: <class 'bool'>
=================================
"""
```

---

📊 **RESUMEN GENERAL — CLASE 01: `variables_y_constantes.md`**
📘 Módulo 01: Fundamentos de Programación en Python

---

### 🧱 ESTRUCTURA GENERAL DE LA CLASE

| Sección                         | Descripción breve                                                     |
| ------------------------------- | --------------------------------------------------------------------- |
| 📘 Introducción teórica         | Definición de variable, constante, tipado dinámico, mutabilidad       |
| 🧠 Definiciones y sintaxis      | Reglas de nombres, declaración, reasignación, tipo de datos           |
| 🔍 Ejemplos ilustrativos        | Casos reales: texto, números, booleanos, `type()`                     |
| 🧪 Ejercicios prácticos guiados | 4 ejercicios aplicados con retroalimentación rigurosa                 |
| 🧠 Evaluación final             | 2 preguntas teóricas + 1 ejercicio integrador calificado              |
| 🏁 Cierre                       | Nota final, feedback profesional, y preparación para la próxima clase |

---

### 🧪 EJERCICIOS RESUELTOS Y CALIFICADOS

| Nº  | Título del ejercicio                           | Estado        | Calificación |
| --- | ---------------------------------------------- | ------------- | ------------ |
| 1️⃣ | `crear_variable_numerica_y_mostrarla`          | ✅ Entregado   | ⭐️ 10 / 10   |
| 2️⃣ | `reutilizar_variable_para_calculo`             | ✅ Entregado   | ⭐️ 10 / 10   |
| 3️⃣ | `declarar_variable_con_texto_y_mostrar_tipo`   | ✅ Entregado   | ⭐️ 10 / 10   |
| 4️⃣ | `nombrar_variable_de_forma_erronea_y_corregir` | ✅ Entregado   | ⭐️ 10 / 10   |
| 🧠  | Preguntas teóricas                             | ✅ Respondidas | ⭐️ 2 / 2     |
| 🧪  | Ejercicio integrador final                     | ✅ Corregido   | ⭐️ 8 / 8     |

---

### 🧠 CONCEPTOS APRENDIDOS

| Categoría       | Conceptos clave                                                       |
| --------------- | --------------------------------------------------------------------- |
| 🧠 Variables    | Espacios nombrados en RAM que almacenan datos temporales              |
| 🔒 Constantes   | Variables en MAYÚSCULAS que no deben cambiar (por convención)         |
| ⚙️ Tipado       | Dinámico en Python: no se declara explícitamente el tipo              |
| 🔁 Reasignación | Una variable puede tomar un nuevo valor en cualquier momento          |
| 🧬 Mutabilidad  | Tipos inmutables (`int`, `float`, `str`, `bool`) usados en esta clase |
| ✍️ Sintaxis     | `nombre = valor` — no usar palabras reservadas ni símbolos inválidos  |
| 📐 Validación   | `type(variable)` para verificar tipo en tiempo de ejecución           |

---

### 📊 CALIFICACIÓN FINAL — CLASE 01

| Evaluación           | Puntaje alcanzado  | Puntaje máximo |
| -------------------- | ------------------ | -------------- |
| 🧠 Teoría            | 2.0                | 2.0            |
| 🧪 Práctica guiada   | 4 ejercicios × 2.5 | 10.0           |
| 🧪 Integrador final  | 8.0                | 8.0            |
| 📊 **Total general** | ✅ **20 / 20**      | **20 / 20**    |

---
