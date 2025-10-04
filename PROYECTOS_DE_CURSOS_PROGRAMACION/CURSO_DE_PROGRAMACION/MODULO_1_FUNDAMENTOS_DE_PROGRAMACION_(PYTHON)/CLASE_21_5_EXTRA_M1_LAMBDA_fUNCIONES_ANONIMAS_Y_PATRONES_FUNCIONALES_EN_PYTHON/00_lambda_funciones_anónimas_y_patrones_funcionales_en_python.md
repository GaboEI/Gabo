# Clase Extra 21.5 — Lambda, funciones anónimas y patrones funcionales en Python

---

## 🟢 INTRODUCCIÓN: ¿Por qué necesitamos funciones anónimas?

Imagina que estás limpiando, transformando o analizando datos en una sola línea.
En estos contextos donde las operaciones son **breves, específicas y desechables**, escribir una función formal con `def` puede resultar innecesario, incluso contraproducente.

📍 Aquí es donde entran las **funciones anónimas**, también llamadas **funciones `lambda`**, como herramientas **expresivas, rápidas y funcionales**.

---

### 📘 1. FUNCIONES `lambda`: Definición formal y estructura

#### 🧬 Definición técnica

Una función `lambda` en Python es una **función anónima** que se declara en una sola línea, usando la palabra clave `lambda`.
Se utiliza típicamente para operaciones simples que requieren ser evaluadas inmediatamente o pasadas como argumento.

#### ⚙️ Sintaxis

```python
lambda parámetros: expresión
```

📌 Equivale a:

```python
def nombre(parametros):
    return expresión
```

#### 🧾 Ejemplo directo

```python
doble = lambda x: x * 2
print(doble(5))  # Salida: 10
```

---

### 🧪 COMPARACIÓN `lambda` vs `def`

| Aspecto             | `def`               | `lambda`                         |
| ------------------- | ------------------- | -------------------------------- |
| 🧠 Legibilidad      | Alta, clara         | Baja en funciones complejas      |
| 📦 Múltiples líneas | Sí                  | No                               |
| 🧾 Nombre propio    | Obligatorio         | Opcional (anónima)               |
| 🔁 Reutilización    | Alta                | Baja (normalmente descartable)   |
| ⚙️ Uso frecuente    | Funciones generales | Funciones en contexto específico |

📌 **Conclusión:**
Usa `lambda` cuando la operación sea **inmediata, breve y localizada**.
Usa `def` para funciones **reusables, complejas o documentadas**.

---

### 🧰 2. FUNCIONES DE ORDEN SUPERIOR

Vamos a estudiar las funciones que **reciben otras funciones como argumentos**.
Estas permiten aplicar lógica funcional compacta y expresiva.

#### 🧪 2.1 `map(function, iterable)`

🔍 **Transforma** cada elemento de una lista usando una función.

```python
numeros = [1, 2, 3, 4]
doblados = list(map(lambda x: x * 2, numeros))
# Resultado: [2, 4, 6, 8]
```

```python
# Convertir texto a mayúsculas
palabras = ['hola', 'mundo']
resultado = map(lambda palabra: palabra.upper(), palabras)
print(list(resultado))  # ['HOLA', 'MUNDO']
```

```python
# Sumar elementos de dos listas
a = [1, 2, 3]
b = [4, 5, 6]
resultado = map(lambda x, y: x + y, a, b)
print(list(resultado))  # [5, 7, 9]
```

```python
# Convertir una lista de temperaturas en °C a °F

Fórmula: F = C * 9/5 + 32

celsius = [0, 10, 20, 30]
fahrenheit = map(lambda c: c * 9/5 + 32, celsius)
print(list(fahrenheit))  # [32.0, 50.0, 68.0, 86.0]
```

```python
# Dado un listado de strings con números, convertirlos a enteros
datos = ['1', '2', '3', '42']
enteros = map(lambda x: int(x), datos)
print(list(enteros))  # [1, 2, 3, 42]
```

```python
# Quitar espacios en blanco de una lista de strings
nombres = ['  ana  ', 'juan ', ' pedro']
limpios = map(lambda x: x.strip(), nombres)
print(list(limpios))  # ['ana', 'juan', 'pedro']
```

```python
# Elevar al cuadrado solo los pares (usando map + filter + lambda)

numeros = [1, 2, 3, 4, 5, 6]

pares = filter(lambda x: x % 2 == 0, numeros)
cuadrados = map(lambda x: x ** 2, pares)

print(list(cuadrados))  # [4, 16, 36]
```

> Profesionalmente útil para: procesamiento masivo de datos, pipelines funcionales, limpieza de listas.

---

#### 🧪 2.2 `filter(function, iterable)`

🔍 **Filtra** elementos de una lista según una condición booleana.

```python
pares = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# Resultado: [2, 4, 6]
```

> Se usa en validación dinámica, filtrado de datos estructurados, respuestas a condiciones.

---

#### 🧪 2.3 `sorted(iterable, key=función)`

🔍 Ordena usando una función que **extrae la clave de ordenamiento**.

```python
personas = [{'nombre': 'Ana', 'edad': 30}, {'nombre': 'Luis', 'edad': 25}]
ordenadas = sorted(personas, key=lambda p: p['edad'])
# Ordena por edad
```

> Ideal para ordenamiento por múltiples criterios, ranking, interfaces dinámicas.

---

#### 🧪 2.4 `any()` y `all()`

Estas funciones evalúan condiciones booleanas **de listas enteras**.

```python
valores = [0, True, False]
print(any(valores))  # True (al menos uno es True)
print(all(valores))  # False (no todos son True)
```

> Útiles en validaciones globales, sistemas de reglas, chequeo de integridad de datos.

---

### 📌 CASOS BORDE Y CONDICIONES REALES

#### ⚠️ `lambda` en expresiones complejas → Evitar

```python
# Ejemplo desaconsejado
func = lambda x: (x * 2 if x > 0 else x / 2 if x < 0 else 0)
```

🔴 Difícil de leer, de mantener, propenso a errores.

📈 **Buena práctica:**
Cuando hay más de una condición, más de una operación, o más de un nivel lógico: usa `def`.

---

### 🧠 APLICACIONES PROFESIONALES

📌 En el mundo real, `lambda` + funciones de orden superior se aplican en:

1. 🧼 **Limpieza y normalización de datos**
2. 📊 **Visualización de datos filtrados**
3. 🛠️ **Transformaciones en APIs REST (FastAPI, Flask)**
4. 🔄 **Procesamiento de listas anidadas en JSON**
5. 🤖 **Filtros dinámicos en interfaces gráficas o dashboards**
6. 🧪 **Validaciones encadenadas en formularios complejos**

---

### 🔍 EJEMPLO PROFESIONAL: Filtro de usuarios por edad y país

```python
usuarios = [
    {"nombre": "Ana", "edad": 28, "pais": "Cuba"},
    {"nombre": "Luis", "edad": 35, "pais": "México"},
    {"nombre": "Elena", "edad": 22, "pais": "Cuba"}
]

cubanos_mayores = list(filter(
    lambda u: u["pais"] == "Cuba" and u["edad"] >= 25,
    usuarios
))
```

📈 Esto es **funcional, compacto y expresivo**.

---

### 🧩 DIAGRAMAS DE FLUJO

#### Ejemplo: `filter()` con `lambda` para filtrar mayores de edad

```Ejemplo
Inicio
↓
Definir lista de personas (diccionarios con 'edad')
↓
Aplicar filter() con función lambda → edad >= 18
↓
Recorrer cada elemento:
├── Sí → mantener en la lista
└── No → descartar
↓
Convertir resultado a lista final
↓
Mostrar lista de mayores de edad
↓
Fin
```

---

### 📎 Enlace útil — Documentación oficial de Python

* 🔗 [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda)
* 🔗 [`map`](https://docs.python.org/3/library/functions.html#map)
* 🔗 [`filter`](https://docs.python.org/3/library/functions.html#filter)
* 🔗 [`sorted`](https://docs.python.org/3/howto/sorting.html)
* 🔗 [`any`, `all`](https://docs.python.org/3/library/functions.html#any)

---

🎯 ¡Muy bien observado, Gabo!
Tu comentario es 100% correcto y demuestra pensamiento crítico de alto nivel 🧠💥

---

### 🔍 **Análisis de tu observación:**

Tú dijiste:

> “Me mandas a hacer una lista de números enteros y luego me mandas a validar si los valores son numéricos pero de eso ya se encarga la propia orden del ejercicio.”

✅ Cierto. Si la lista **ya está declarada por el programador**, como:

```python
numeros = [1, 2, 3, 4]
```

## 📁 `01_lambda_basica_en_lista.py`

---

### 🎯 Objetivo del ejercicio (reafirmado)

Transformar los elementos de una lista **predefinida** de números enteros, duplicando su valor con una función `lambda`, utilizando `map()` de forma limpia y funcional.

---

### 🔄 Diagrama de flujo

```/
Inicio
↓
Definir lista fija de enteros
↓
Aplicar map() con función lambda para duplicar valores
↓
Convertir resultado a lista
↓
Mostrar lista resultante
↓
(🔴 Mejora) Calcular suma original y suma transformada
↓
(🔴 Mejora) Mostrar diferencia entre cada número original y su duplicado
↓
Fin
```

### 🔧 EJERCICIO 1 ( `01_lambda_basica_en_lista.py` )

```python
#📝 01_lambda_basica_en_lista.py

#1️⃣ Crear una lista fija de números enteros
num = [47, 82, 13, 65, 29, 93, 56]
print(f"Lista Original: {num}")

#2️⃣ Aplicar la función map() con una función lambda para duplicar cada número
#3️⃣ Convertir el resultado de map() en una lista con list()
duplicado = list(map(lambda x: x*2, num))

#4️⃣ Imprimir la lista resultante en consola
print(f"Lista duplicada: {duplicado}")

#5️⃣ (Opcional) Mostrar la suma de la lista original y la suma de la lista resultante
sum_original = sum(num)
sum_duplicado = sum(duplicado)
print(f"""
Suma de la lista original: {sum_original}
Suma de la lista duplicada: {sum_duplicado} 
"""
)

#6️⃣ (Opcional) Mostrar la diferencia entre cada par (original → transformado)
print("Diferencia entre cada par [original -> transformado]:")
for original, duplicado in zip (num, duplicado):
    print(f"{original} -> {duplicado}, diferencia: {duplicado - original}")
```

```.
"""
RESPUESTA DE TERMINAL
Lista Original: [47, 82, 13, 65, 29, 93, 56]
Lista duplicada: [94, 164, 26, 130, 58, 186, 112]

Suma de la lista original: 385
Suma de la lista duplicada: 770 

Diferencia entre cada par [original -> transformado]:
47 -> 94, diferrencia: 47
82 -> 164, diferrencia: 82
13 -> 26, diferrencia: 13
65 -> 130, diferrencia: 65
29 -> 58, diferrencia: 29
93 -> 186, diferrencia: 93
56 -> 112, diferrencia: 56
"""
```

---

## 📁 Ejercicio: `02_uso_de_map_con_lambda.py`

---

### 🎯 **1. Objetivo del ejercicio**

Simular un sistema de **cálculo automático de precios finales con IVA incluido**, usando `lambda` y `map()` para aplicar una operación matemática funcional a una lista de precios.

✅ En este ejercicio desarrollarás:

* Lógica aplicada a procesos de negocios
* Aplicación declarativa de funciones
* Pensamiento vectorizado (operar sobre listas, no valores individuales)

---

### 📘 **2. Teoría aplicada al ejercicio**

#### 📌 ¿Qué es `map()`?

`map()` aplica una función (como una `lambda`) **a cada elemento de una lista**. Devuelve un objeto que contiene los resultados.

#### 📌 ¿Qué hace una `lambda` aquí?

Aplica una fórmula:
💰 `precio_con_iva = precio_sin_iva * 1.21`
(donde el 21% es el impuesto)

Esta operación puede hacerse **en una línea**, con:

```python
lambda p: p * 1.21
```

---

### 🧪 **3. Ejemplo práctico**

Supongamos que tienes estos precios base:

```python
precios_sin_iva = [100, 200, 50]
```

La función `map(lambda p: p * 1.21, precios_sin_iva)` te devuelve:

```python
[121.0, 242.0, 60.5]
```

✅ Esta técnica se usa muchísimo en tiendas, catálogos, APIs, generación de facturas, hojas de cálculo automáticas, etc.

---

### 🧠 **4. Diagrama de flujo**

```Inicio
Inicio
↓
Definir lista de precios base sin IVA
↓
Aplicar map() con lambda para calcular precio final (x1.21)
↓
Convertir el resultado a lista
↓
Mostrar lista de precios con IVA
↓
(🔴 Mejora) Mostrar comparación precio original → precio con IVA
↓
(🔴 Mejora) Calcular e imprimir el monto total del IVA recaudado
↓
Fin
```

---

### 🔧 Ejercicio: `02_uso_de_map_con_lambda.py`

```python
# 📝 02_uso_de_map_con_lambda.py
"""
🎯: Simular un sistema de cálculo automático de precios finales con IVA 
incluido, usando `lambda` y `map()` para aplicar una operación matemática 
funcional a una lista de precios.
"""

# 1️⃣ Crear una lista de precios base (enteros o flotantes)
precios_base = [10.5, 77.5, 13, 10.59, 45.25, 40.5]
print(f"Lista de precios original: {[f'{precio:.2f}' for precio in precios_base]}")

# 2️⃣ y 3️⃣ Aplicar map() con lambda para calcular precios con IVA y convertir a lista
precios_con_iva = list(map(lambda p: p * 1.21, precios_base))

# 4️⃣ Imprimir la lista con precios con IVA (formateada a 2 decimales)
print(f"Lista de precios con 21% de IVA: {[f'{precio:.2f}' for precio in precios_con_iva]}")

# 5️⃣ Mostrar cada par: precio original → precio con IVA
print("\nPrecios originales -> Con IVA (21%)")
for original, con_iva in zip(precios_base, precios_con_iva):
    print(f"{original:.2f} -> {con_iva:.2f}")

# 6️⃣ (Opcional) Calcular el IVA total recaudado
suma_precios_base = sum(precios_base)
suma_precios_con_iva = sum(precios_con_iva)
iva_recaudado = suma_precios_con_iva - suma_precios_base
print(f"\nIVA total recaudado: {iva_recaudado:.2f}")
```

```.
"""
RESPUESTA DE TERMINAL
Lista de precios original: 
['10.50', '77.50', '13.00', '10.59', '45.25', '40.50']

Lista de precios con 21% de IVA: 
['12.71', '93.77', '15.73', '12.81', '54.75', '49.00']

Precios originales -> Con IVA (21%)
10.50 -> 12.71
77.50 -> 93.77
13.00 -> 15.73
10.59 -> 12.81
45.25 -> 54.75
40.50 -> 49.00

IVA total recaudado: 41.44
"""
```

---

🚀 ¡Vamos con todo, Gabo! Entramos ahora en una herramienta clave del pensamiento funcional: **`filter()`**.
Este ejercicio consolida la lógica de selección condicional en listas. Y como siempre, lo desarrollamos con el rigor que exige tu curso universitario intensivo 🧠📘

---

## 📁 Ejercicio: `03_filtrar_precios_altos_con_filter.py`

---

### ✓ **1. Objetivo del ejercicio**

Aplicar la función `filter()` junto con una función `lambda` para **seleccionar los precios que superen cierto umbral definido**, simulando un sistema que filtra productos de alto valor para destacarlos.

Con esto aprenderás:

* Pensamiento declarativo con `filter()`
* Aplicación real de criterios dinámicos
* Uso conjunto de `lambda` + `filter` en estructuras funcionales

---

### ✓ **2. Teoría aplicada al ejercicio**

---

#### 📌 ¿Qué es `filter()`?

Es una función **de orden superior** que:

> Toma una función y una colección (lista, tupla, etc.), y **devuelve solo los elementos para los que la función retorne `True`**.

🧠 Es ideal cuando necesitas **seleccionar** elementos **según una condición**, sin escribir bucles manuales.

---

#### ✓ Sintaxis general

```python
filter(funcion, iterable)
```

🔸 `funcion`: puede ser una función tradicional (`def`) o una función anónima (`lambda`)
🔸 `iterable`: la colección sobre la que quieres aplicar el filtro

---

### ✓ **3. Ejemplo práctico**

```python
precios = [50, 150, 30, 200, 80]

precios_altos = list(filter(lambda x: x > 100, precios))
```

🔍 Resultado: `[150, 200]`

📌 El filtro mantuvo **solo los precios mayores a 100**.

---

### 🧠 ¿Cuándo usar `filter()` profesionalmente?

* 🛒 E-commerce: filtrar productos por precio mínimo
* 📊 Finanzas: seleccionar ingresos por encima de cierto umbral
* 🎓 Educación: elegir notas mayores a 7
* 🧼 Limpieza de datos: eliminar elementos vacíos o inválidos

---

## ✓ 4. Diagrama de flujo

```.
Inicio
↓
Definir lista de precios
↓
Definir umbral mínimo (ej: 100)
↓
Aplicar filter() con lambda para seleccionar precios > umbral
↓
Convertir el resultado a lista
↓
Mostrar precios filtrados
↓
(🔴 Mejora) Mostrar cuántos elementos fueron filtrados y su porcentaje respecto al total
↓
(🔴 Mejora) Mostrar cada par: original → “✅ pasa” o “❌ no pasa” usando map() y zip()
↓
Fin
```

---

## 🧩 Ejercicio: `03_filtrar_precios_altos_con_filter.py`

```python
#📝 03_filtrar_precios_altos_con_filter.py

#1️⃣ Crear una lista de precios (pueden ser enteros o float)
precios = [10.3, 25.5, 8.5, 15.5, 100, 300, 4, 23, 5]

#2️⃣ Definir un valor umbral para considerar un precio “alto”
umbral = 115

#3️⃣ Aplicar filter() con una función lambda que conserve solo los precios mayores al umbral
#4️⃣ Convertir el resultado de filter() en una lista
precios_altos = list(filter(lambda x: x > umbral, precios))

#5️⃣ Imprimir la lista final de precios filtrados
print(f"Lista de precios filtrados: {precios_altos}")

#6️⃣ Mostrar la cantidad y el porcentaje de precios filtrados respecto al total
cantidad_precios_altos = len(precios_altos)
porcentaje_precios_altos = (cantidad_precios_altos / len(precios)) * 100
print(f"Cantidad de precios altos: {cantidad_precios_altos}")
print(f"Porcentaje de precios altos: {porcentaje_precios_altos:.2f}%")

#7️⃣ Mostrar una lista con los pares: precio original + estado ("✅ pasa" o "❌ no pasa")
for precio in precios:
    if precio > umbral:
        print(f"{precio:.2f} -> ✅ pasa")
    else:
        print(f"{precio:.2f} -> ❌ no pasa")
```

```terminal
"""
RESPUESTA DE TERMINAL
Lista de precios filtrados: [100, 300]
Cantidad de precios altos: 2
Porcentaje de precios altos: 14.29%
10.30 -> ❌ no pasa
25.50 -> ❌ no pasa
8.50 -> ❌ no pasa
15.50 -> ❌ no pasa
100.00 -> ✅ pasa
300.00 -> ✅ pasa
"""
```

---

🧠 ¡Vamos con todo, Gabo!
Este ejercicio marca un **salto de calidad**, porque entramos en el mundo de **ordenamientos personalizados** con `sorted()` y su argumento `key=` — un patrón funcional **clave** para el mundo real.

---

## 📁 Ejercicio: `04_ordenar_productos_con_sorted_key.py`

---

### **1. Objetivo del ejercicio**

Aplicar la función `sorted()` con `key=lambda` para ordenar una lista de productos (representados como tuplas o diccionarios) según diferentes criterios:

* 🔢 Por precio (de menor a mayor)
* 🔠 Por nombre del producto
* 🔄 Por orden inverso de alguno de los anteriores (mejora)

Este ejercicio simula funcionalidades reales de:

* 🛒 tiendas online
* 📊 reportes contables
* 🧩 catálogos interactivos
* 🔎 filtros de búsqueda en sistemas de inventario

---

### 📘 **2. Teoría del concepto `sorted()` y `key=`**

---

#### ✅ ¿Qué es `sorted()`?

Es una función incorporada de Python que:

> Devuelve una **nueva lista ordenada** sin modificar la original.

🧠 A diferencia de `.sort()` (que modifica en sitio), `sorted()` permite mantener tu dato original **intacto**.

#### Sintaxis general

```python
sorted(iterable, key=función, reverse=False)
```

* `iterable`: lista, tuplas, strings, etc.
* `key`: función que dice **por qué campo** se debe ordenar
* `reverse`: si es `True`, ordena al revés

---

### 🔍 ¿Qué hace `key=`?

Permite definir el **criterio de ordenación**. Es ahí donde
 usamos:

```python
key=lambda x: x[1]   # Ordenar por segundo valor
key=lambda x: x["precio"]  # Ordenar por campo específico
```

Esto da **flexibilidad total** para ordenar lo que quieras, como quieras.

---

### **3. Ejemplo práctico**

Supongamos:

```python
productos = [("Manzana", 1.5), ("Banana", 0.9), ("Sandía", 3.2)]
```

Ordenar por precio:

```python
ordenados = sorted(productos, key=lambda x: x[1])
```

📦 Resultado:

```.
[('Banana', 0.9), ('Manzana', 1.5), ('Sandía', 3.2)]
```

🔄 Inverso:

```python
ordenados = sorted(productos, key=lambda x: x[1], reverse=True)
```

---

## 🧠 4. Diagrama de flujo

```.
Inicio
↓
Definir lista de productos (nombre, precio)
↓
Aplicar sorted() con key=lambda para ordenar por precio
↓
Mostrar lista ordenada por precio
↓
(🔴 Mejora) Aplicar sorted() con key=lambda para ordenar por nombre
↓
(🔴 Mejora) Aplicar sorted() con reverse=True para ordenar por precio descendente
↓
Mostrar todas las variantes de ordenamiento
↓
Fin
```

---

## Ejercicio: `04_ordenar_productos_con_sorted_key.py`

```python
# 📝 04_ordenar_productos_con_sorted_key.py

productos = [
    ("teclado", 11.99),
    ("telefono", 100.75),
    ("audifono", 45.00)
    
]

# Ordenar por precio (menor a mayor)
print("\nProductos ordenados por precio (ascendente):")
print("-" * 45)
ordenados_precio = sorted(productos, key=lambda producto: producto[1])
for nombre, precio in ordenados_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f}")

# Ordenar por nombre alfabéticamente
print("\nProductos ordenados por nombre (alfabético):")
print("-" * 45)
ordenados_nombre = sorted(productos, key=lambda producto: producto[0])
for nombre, precio in ordenados_nombre:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f}")

# Ordenar por precio (mayor a menor)
print("\nProductos ordenados por precio (descendente):")
print("-" * 45)
ordenados_precio_desc = sorted(productos, key=lambda producto: producto[1], reverse=True)
for nombre, precio in ordenados_precio_desc:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f}")
```

```TERMINAL
"""
RESPUESTA TERRMINAL 
Productos ordenados por precio (ascendente):
---------------------------------------------
Producto: teclado      | Precio: $ 11.99
Producto: audifono     | Precio: $ 45.00
Producto: telefono     | Precio: $100.75

Productos ordenados por nombre (alfabético):
---------------------------------------------
Producto: audifono     | Precio: $ 45.00
Producto: teclado      | Precio: $ 11.99
Producto: telefono     | Precio: $100.75

Productos ordenados por precio (descendente):
---------------------------------------------
Producto: telefono     | Precio: $100.75
Producto: audifono     | Precio: $ 45.00
Producto: teclado      | Precio: $ 11.99
"""
```

---

## 📁 Ejercicio: `05_validar_condiciones_con_any_all.py`

---

### **1. Objetivo del ejercicio 5**

Aplicar las funciones `any()` y `all()` para validar si una lista de productos cumple con ciertas condiciones, como:

* ✅ Todos los precios son mayores a un mínimo aceptable (`all`)
* ⚠️ Al menos un producto excede cierto valor límite de riesgo (`any`)

Con esto aprenderás a construir verificadores lógicos potentes en una sola línea de código. Esto es **oro puro** en automatización, reglas de negocio, validaciones masivas y testing.

---

### 📘 **2. Teoría aplicada: `any()` y `all()`**

---

#### 🔎 ¿Qué hacen?

| Función | Retorna `True` si...                               | Ideal para...                                           |
| ------- | -------------------------------------------------- | ------------------------------------------------------- |
| `all()` | **Todos** los elementos de la colección son `True` | Validaciones estrictas (💼 contratos, pagos, seguridad) |
| `any()` | **Algún** elemento de la colección es `True`       | Detección de alerta (⚠️ fraude, errores, excepciones)   |

Ambas recorren internamente el iterable, evaluando expresiones lógicas. Por eso funcionan increíblemente bien con `map()` + `lambda`.

---

### 💼 **3. Ejemplo práctico**

```python
precios = [120, 150, 90, 110]

# ¿Todos los precios son mayores a 80?
resultado = all(p > 80 for p in precios)  # ✅ True

# ¿Algún precio supera 140?
alerta = any(p > 140 for p in precios)    # ⚠️ True
```

🧠 Estas construcciones evitan el uso de múltiples bucles `for` o `if` innecesarios.

---

## 4. Diagrama de flujo

```diagrama
Inicio
↓
Definir lista de precios
↓
Aplicar all(): verificar si todos los precios ≥ mínimo permitido
↓
Aplicar any(): verificar si algún precio > umbral crítico
↓
Mostrar resultados booleanos de ambas condiciones
↓
(🔴 Mejora) Imprimir mensajes personalizados según resultados (ej: “✅ Todo correcto” o “❗ Hay precios peligrosos”)
↓
(🔴 Mejora) Aplicar validaciones con map() + lambda en vez de comprensión de listas
↓
Fin
```

---

## Ejercicio: `05_validar_condiciones_con_any_all.py`

```python
# 📝 05_validar_condiciones_con_any_all.py

#1️⃣ Crear una lista de precios de productos (enteros o float)
precios = [80, 110, 120, 95, 100, 150, 180, 200, 250, 300]

#2️⃣ Definir un valor mínimo aceptable
minimo  = 70

#3️⃣ Verificar si TODOS los precios son mayores o iguales al mínimo usando all()
resultado_all = all(m >= minimo for m in precios)

#4️⃣ Definir un valor de alerta para precios muy altos
alerta = 140

#5️⃣ Verificar si ALGÚN precio excede el valor de alerta usando any()
resultado_any = any(a > alerta for a in precios)

#6️⃣ Imprimir los resultados de ambas condiciones con mensajes claros
print(f"Todos los precios son mayores o iguales al mínimo: {resultado_all}")
print(f"Algún precio excede el valor de alerta: {resultado_any}")

#7️⃣ Mostrar “✅ Todo válido” o “⚠️ Hay precios fuera de rango” según el resultado
if resultado_all:
    print("✅ Todo válido")
else:
    print("⚠️ Hay precios fuera de rango")

#8️⃣ Reescribir una de las condiciones usando map() + lambda para practicar el patrón funcional
resultado_all_map = all(map(lambda x: x >= minimo, precios))
print(f"Todos los precios son mayores o iguales al mínimo: {resultado_all_map}")
resultado_any_map = any(map(lambda x: x > alerta, precios))
print(f"Algún precio excede el valor de alerta: {resultado_any_map}")
```

```terminal
"""
RESPUESTA TERMINAL
Todos los precios son mayores o iguales al mínimo: True
Algún precio excede el valor de alerta: True
✅ Todo válido
Todos los precios son mayores o iguales al mínimo: True
Algún precio excede el valor de alerta: True
"""
```

---

📚 **Mini repaso integrador — Clase Extra 21.5**
🎓 *Lambda, funciones anónimas y patrones funcionales en Python*

Vamos a consolidar lo aprendido con una síntesis profesional de lo esencial, reforzando conexiones entre conceptos y recordando su aplicación real 🧠⚙️

---

## 🧩 1. ¿Qué aprendi en esta clase?

Esta clase aprerndo a pensar como un programador funcional:

| Concepto            | ¿Qué hace?                                        | ¿Cuándo lo usas?                           | Ejemplo clave                        |
| ------------------- | ------------------------------------------------- | ------------------------------------------ | ------------------------------------ |
| `lambda`            | Función anónima en una línea                      | Cuando no necesitas definir `def` completo | `lambda x: x * 2`                    |
| `map()`             | Aplica una función a cada elemento de un iterable | Transformar en lote                        | `map(lambda x: x.upper(), nombres)`  |
| `filter()`          | Filtra elementos según condición                  | Limpiar listas, seleccionar datos          | `filter(lambda x: x > 100, precios)` |
| `sorted()` + `key=` | Ordena por criterio personalizado                 | Listados, dashboards, reportes             | `sorted(lista, key=lambda x: x[1])`  |
| `any()`             | Retorna `True` si *alguno* cumple condición       | Alertas, detección temprana                | `any(p > 200 for p in precios)`      |
| `all()`             | Retorna `True` si *todos* cumplen condición       | Reglas estrictas, validaciones             | `all(p >= 80 for p in precios)`      |

---

## 📊 2. ¿Qué patrones funcionales ya domino?

🧠 Este tipo de código:

```python
all(map(lambda p: p >= 100, precios))
```

✅ Uso:

* Expresión booleana
* Función anónima
* Iterador funcional

Y se traduce a:

> “¿Todos los precios son mayores o iguales a 100?”

Esto evita escribir bucles `for`, `if`, `append`, etc.
⚡ ¡Rápido, limpio y profesional!

---

## 📈 3. Aplicaciones reales de estos conceptos

💼 Donde puedo usarlos:

* **e-commerce**: filtrar productos, validar stock, ordenar por precio
* **análisis financiero**: detectar movimientos sospechosos (`any()`), validar consistencia (`all()`)
* **automación de tareas**: transformar archivos, nombres, estructuras (`map()`)
* **desarrollo web**: ordenar resultados antes de mostrar (`sorted(key=...)`)
* **AI y ciencia de datos**: preprocesamiento de datos, pipelines funcionales

---

## 🔄 4. Conexiones entre funciones

Muchos de estos conceptos pueden **encadenarse** como bloques de lego 🧱:

```python
productos = [("Laptop", 1000), ("Mouse", 20), ("Teclado", 45)]

ordenados = sorted(
    filter(lambda x: x[1] > 30, productos),
    key=lambda x: x[1]
)
```

👉 Primero filtra los productos más caros → luego los ordena por precio.

---

## 🧠 5. Patrón mental integrador

```ejemplo
👁️ Observar estructura de datos
↓
❓ Definir condición o transformación deseada
↓
⚙️ Elegir función adecuada: map / filter / sorted / any / all
↓
🧱 Componer expresiones limpias y declarativas
↓
✅ Obtener resultado final limpio y validable
```

---

🚀 **MINI PROYECTO FUNCIONAL FINAL — Clase Extra 21.5**
🎓 *Integración total de `lambda`, `map()`, `filter()`, `sorted()`, `any()` y pensamiento funcional declarativo*
📦 Nombre del archivo: `06_analisis_funcional_de_inventario.py`

---

### 🎯 Objetivo

Simularás un análisis inteligente de un **inventario de productos**, combinando *transformaciones, filtrado, ordenamiento y validación funcional*.

🔎 Usarás expresiones compactas y potentes que procesen datos como si estuvieras construyendo una mini-API o una lógica de backend real.

---

### 📘 Contexto lógico del ejercicio

Dispones de una lista de productos, donde cada producto tiene:

* Nombre (str)
* Precio (float)
* Stock (entero)

Tu sistema debe:

1. 🔍 Filtrar los productos que están disponibles (`stock > 0`)
2. 💸 Aumentar sus precios en un 10% con `map()`
3. 📊 Ordenarlos por precio actualizado (`sorted(key=...)`)
4. ⚠️ Verificar si **algún producto supera los $500** (`any()`)
5. 📋 Mostrar el resultado final con nombre, nuevo precio, stock
6. (🔴 Mejora opcional) Filtrar productos con nombres que contengan una letra clave (ej: "a", "e") con `filter() + lambda + in`

---

## 🧠 Diagrama de flujo profesional

```Inicio
Inicio
↓
Definir lista de productos con nombre, precio y stock
↓
Filtrar productos disponibles (stock > 0) → filter()
↓
Aplicar aumento del 10% a los precios → map()
↓
Ordenar productos por precio actualizado → sorted(key=...)
↓
Verificar si algún producto supera $500 → any()
↓
Mostrar resultados: nombre | precio nuevo | stock
↓
(🔴 Mejora opcional): filtrar productos con letra clave en nombre
↓
Fin
```

---

## 💻 INI PROYECTO FUNCIONAL FINAL


```python
# 📝 06_analisis_funcional_de_inventario.py

#1️⃣ Crear una lista de productos como tuplas: (nombre, precio, stock)
productos = [
    ("Laptop", 450.00, 5),
    ("Mouse", 20.00, 10),
    ("Teclado", 30.00, 8),
    ("Monitor", 150.00, 3)   
]
print("Lista de productos original:")
print("-" * 45)
for nombre, precio, stock in productos:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#2️⃣ Usar filter() para seleccionar solo los productos con stock > 0
en_stock = list(filter(lambda p: p[2] > 0, productos))
print("Lista de productos con stock > 0:")
print("-" * 45)
for nombre, precio, stock in en_stock:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#3️⃣ Usar map() para aumentar el precio en 10% a cada producto disponible
aumento_precio = list(map(lambda p: (p[0], p[1] * 1.10, p[2]), en_stock))
print("Lista de productos con aumento de precio:")
print("-" * 45)
for nombre, precio, stock in aumento_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#4️⃣ Usar sorted() con key=lambda para ordenar por el nuevo precio (índice 1)
ordenado_precio = sorted(aumento_precio, key=lambda p: p[1])
print("Lista de productos ordenados por precio:")
print("-" * 45)
for nombre, precio, stock in ordenado_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#5️⃣ Usar any() para verificar si algún producto supera los $250
pista = any(p[1] > 250 for p in aumento_precio)
print(f"Algún producto supera los $250: {pista}")
print("\n")

#6️⃣ Imprimir los productos resultantes en formato tabular
#    👉 Usa f-strings con alineación
for nombre, precio, stock in ordenado_precio:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")

#7️⃣ Aplicar otro filter() para mostrar solo productos cuyo nombre contenga una letra clave (ej: "a")
clave = "a"
producto_clave = list(filter(lambda p: clave in p[0], ordenado_precio))
print("Lista de productos con letra clave:")
print("-" * 45)
for nombre, precio, stock in producto_clave:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
print("\n")

#8️⃣ Imprimir los productos resultantes en formato tabular
for nombre, precio, stock in producto_clave:
    print(f"Producto: {nombre:<12} | Precio: ${precio:>6.2f} | Stock: {stock}")
```

```terminal
""
Lista de productos original:
---------------------------------------------
Producto: Laptop       | Precio: $450.00 | Stock: 5
Producto: Mouse        | Precio: $ 20.00 | Stock: 10
Producto: Teclado      | Precio: $ 30.00 | Stock: 8
Producto: Monitor      | Precio: $150.00 | Stock: 3


Lista de productos con stock > 0:
---------------------------------------------
Producto: Laptop       | Precio: $450.00 | Stock: 5
Producto: Mouse        | Precio: $ 20.00 | Stock: 10
Producto: Teclado      | Precio: $ 30.00 | Stock: 8
Producto: Monitor      | Precio: $150.00 | Stock: 3


Lista de productos con aumento de precio:
---------------------------------------------
Producto: Laptop       | Precio: $495.00 | Stock: 5
Producto: Mouse        | Precio: $ 22.00 | Stock: 10
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Monitor      | Precio: $165.00 | Stock: 3


Lista de productos ordenados por precio:
---------------------------------------------
Producto: Mouse        | Precio: $ 22.00 | Stock: 10
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Monitor      | Precio: $165.00 | Stock: 3
Producto: Laptop       | Precio: $495.00 | Stock: 5


Algún producto supera los $250: True


Producto: Mouse        | Precio: $ 22.00 | Stock: 10
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Monitor      | Precio: $165.00 | Stock: 3
Producto: Laptop       | Precio: $495.00 | Stock: 5
Lista de productos con letra clave:
---------------------------------------------
Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Laptop       | Precio: $495.00 | Stock: 5


Producto: Teclado      | Precio: $ 33.00 | Stock: 8
Producto: Laptop       | Precio: $495.00 | Stock: 5
"""
```

---
