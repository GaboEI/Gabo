# **Clase Extra** – Consolidación Avanzada del Módulo 1

---

## 🧠 1. Banderas Booleanas y Estructuras Anidadas

### 📘 Concepto teórico

Una **bandera booleana** (o _flag_) es una variable de tipo `bool` (`True` o `False`) que se utiliza para **controlar el flujo lógico de un programa**.
Sirve para indicar si algo ha ocurrido, si una condición se ha cumplido o si una acción debe ejecutarse o no.

En estructuras anidadas, las banderas permiten **salir de múltiples niveles de bucles** o **controlar validaciones complejas** sin romper la legibilidad del código.

### 🔬 Ejemplo profesional

Supón que trabajas en un sistema que busca si un cliente tiene una factura pendiente dentro de una base de datos anidada (lista → diccionarios → listas):

```python
clientes = [
    {"nombre": "Ana", "facturas": [{"id": 1, "estado": "pagada"}, {"id": 2, "estado": "pendiente"}]},
    {"nombre": "Luis", "facturas": [{"id": 3, "estado": "pagada"}]},
]

factura_pendiente = False

for cliente in clientes:
    for factura in cliente["facturas"]:
        if factura["estado"] == "pendiente":
            factura_pendiente = True
            cliente_endeudado = cliente["nombre"]
            break
    if factura_pendiente == True:
        print(f"⚠️ Cliente con factura pendiente: {cliente_endeudado}")
    else:
        print(f"✅ Cliente al día: {cliente['nombre']}")
```

### 💡 Claves profesionales

- La bandera **simplifica** la lectura frente a condiciones encadenadas.
- Evita **romper múltiples bucles** de manera desordenada.
- Permite un **control centralizado** del estado lógico del programa.

---

### 🧭 Diagrama de flujo

```
Inicio
 ↓
Bandera = False
 ↓
├── Recorrer lista de clientes
│    ↓
│    ├── Recorrer facturas de cliente
│    │     ↓
│    │     ├── ¿Factura pendiente?
│    │     │       ↓
│    │     │       ├── Sí → Bandera = True → Guardar cliente → Romper bucle interno
│    │     │       └── No → Continuar
│    │
│    └── ¿Bandera True? → Romper bucle externo
↓
¿Bandera True?
├── Sí → Mostrar cliente con deuda
└── No → Mostrar todo pagado
↓
Fin
```

---

## 📂 2. Manejo Profesional de Ficheros: CSV, JSON y Binarios

### 🧾 2.1 Archivos CSV

Un archivo **CSV (Comma Separated Values)** almacena datos en formato de texto separados por comas, ideal para intercambiar información entre sistemas (por ejemplo, entre Python y Excel).

**Módulo estándar:** `csv`

- `csv.reader()` → lee línea a línea
- `csv.writer()` → escribe listas como filas
- `DictReader` / `DictWriter` → trabajan directamente con diccionarios

```python
import csv

# Escritura
with open("empleados.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "cargo", "salario"])
    writer.writeheader()
    writer.writerow({"nombre": "Ana", "cargo": "Gerente", "salario": 4200})
    writer.writerow({"nombre": "Luis", "cargo": "Analista", "salario": 3100})

# Lectura
with open("empleados.csv", newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["nombre"], fila["salario"])
```

---

### 🔐 2.2 Archivos JSON

**JSON (JavaScript Object Notation)** es un formato universal para representar datos estructurados.
Se usa para guardar **configuraciones, datos de usuario, respuestas de API**, etc.

**Módulo estándar:** `json`

- `json.dump()` / `json.load()` → guardar y leer desde archivos
- `json.dumps()` / `json.loads()` → convertir entre str y diccionario

```python
import json

usuarios = {"id": 1, "nombre": "Gabo", "nivel": "avanzado"}

# Guardar JSON
with open("usuario.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)

# Leer JSON
with open("usuario.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data["nombre"])
```

💼 Aplicación profesional: almacenamiento de **estado persistente** (por ejemplo, la agenda de la clase 22).

---

### 💾 2.3 Archivos Binarios

Los archivos binarios almacenan datos en **formato no legible** (bytes).
Se usan para guardar imágenes, modelos, bases de datos, o estados serializados.

```python
datos = {"usuario": "Gabo", "puntaje": 95}

import pickle  # Librería para serialización binaria

# Guardar
with open("datos.bin", "wb") as f:
    pickle.dump(datos, f)

# Leer
with open("datos.bin", "rb") as f:
    cargado = pickle.load(f)
    print(cargado)
```

---

## 🧮 3. Importación y Uso Profesional de Módulos

### 🔹 Módulo `os`

Permite interactuar con el sistema operativo (rutas, carpetas, archivos).
Ejemplo:

```python
import os
ruta = os.getcwd()          # Obtiene el directorio actual
archivos = os.listdir(ruta) # Lista archivos
print(archivos)
```

Uso profesional: scripts que automatizan tareas del sistema, limpieza de logs, gestión de backups.

---

### 🔹 Módulo `sys`

Ofrece acceso a variables y funciones del intérprete de Python.
Ejemplo: parámetros desde la línea de comandos o salida del programa.

```python
import sys
if len(sys.argv) < 2:
    print("Uso: python script.py <nombre>")
    sys.exit(1)
nombre = sys.argv[1]
print(f"Hola {nombre}")
```

---

### 🔹 Módulo `datetime`

Manejo profesional de fechas y horas.

```python
from datetime import datetime

hoy = datetime.now()
print(hoy.strftime("%d/%m/%Y - %H:%M:%S"))
```

Ideal para registrar acciones en logs, agendas y sistemas con persistencia temporal.

---

### 🔹 Módulo `math`

Proporciona funciones matemáticas precisas y rápidas (logaritmos, raíces, trigonometría).
Ejemplo profesional: cálculos de tasas, estadísticas, normalización de datos.

```python
import math
angulo = 45
rad = math.radians(angulo)
print(math.sin(rad))
```

---

## ⚙️ 4. Funciones Funcionales y Expresiones Lambda

Python admite un **paradigma funcional** que permite tratar funciones como datos.

---

### 🔹 `lambda` (Expresiones anónimas)

Sintaxis compacta para definir funciones de una sola línea.

```python
doble = lambda x: x * 2
print(doble(5))  # → 10
```

**Diferencias clave frente a `def`:**

| Aspecto | `lambda`           | `def`             |
| ------- | ------------------ | ----------------- |
| Nombre  | Anónima            | Nombrada          |
| Alcance | Una sola expresión | Bloque múltiple   |
| Retorno | Implícito          | Requiere `return` |
| Uso     | Funciones cortas   | Lógica extensa    |

**Ventajas profesionales:**

- Simplifica código dentro de `map`, `filter`, `sorted`, etc.
- Ideal para procesamiento de datos o iteraciones simples.

---

### 🔹 `map()`

Aplica una función a cada elemento de un iterable.

```python
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8]
```

💡 Uso real: normalizar columnas numéricas en CSV, convertir cadenas a mayúsculas, etc.

---

### 🔹 `filter()`

Filtra los elementos que cumplen una condición.

```python
pares = list(filter(lambda x: x % 2 == 0, numeros))
```

---

### 🔹 `sorted(key=...)`

Permite ordenar listas o diccionarios por una clave personalizada.

```python
personas = [{"nombre": "Ana", "edad": 30}, {"nombre": "Luis", "edad": 25}]
ordenadas = sorted(personas, key=lambda p: p["edad"])
```

---

### 🔹 `any()` y `all()`

Evalúan condiciones sobre colecciones booleanas.

```python
valores = [True, False, True]
print(any(valores))  # True  (si al menos uno es True)
print(all(valores))  # False (si todos son True)
```

Aplicación real: validaciones múltiples, filtros de datos, verificaciones de integridad.

---

## 🧩 5. Aplicación Profesional Integrada

En proyectos reales, todos estos conceptos se combinan.
Imagina un **sistema de gestión de inventario**:

- Carga datos de un `.csv` con productos.
- Usa banderas booleanas para marcar si falta stock.
- Actualiza un `.json` con los cambios.
- Genera un reporte binario de respaldo.
- Usa `datetime` para registrar la fecha de ejecución.
- Implementa `lambda`, `map`, `filter`, `any` y `all` para validar y transformar datos.

---

## 📜 Diagrama de flujo global (resumen de toda la clase)

```
Inicio
 ↓
Importar módulos necesarios
 ↓
Cargar datos desde CSV
 ↓
Procesar datos con map/filter/lambda
 ↓
¿Algún valor inválido? (any)
 ├── Sí → Registrar en log con datetime → Bandera error = True
 └── No → Continuar
 ↓
Actualizar archivo JSON (estado persistente)
 ↓
Generar copia de seguridad binaria
 ↓
Mostrar resultados ordenados (sorted)
 ↓
¿Bandera error?
 ├── Sí → Alerta al usuario
 └── No → Mensaje de éxito
 ↓
Fin
```

---

# 📁 **Ejercicio 01 – control_con_bandera_booleana.py**

---

## 🎯 **1. Objetivo del ejercicio**

Aplicar el uso de **banderas booleanas (`True` / `False`)** para **controlar el flujo lógico** dentro de una estructura anidada de bucles.
El propósito es que el programa **detecte una condición específica** (por ejemplo, la aparición de un valor o evento) y **detenga el flujo completo** de búsqueda cuando se cumpla, usando una bandera como interruptor de estado.

En términos profesionales, esto entrena la habilidad de **controlar múltiples niveles de iteración sin romper la estructura del código**, algo esencial en scripts de automatización, búsquedas en bases de datos, y validaciones de sistemas.

---

## 📘 **2. Teoría aplicada al ejercicio**

### 🔹 ¿Qué es una bandera booleana?

Una **bandera booleana** es una variable lógica (tipo `bool`) que se utiliza como **indicador de estado**:

- `True` → la condición deseada ha ocurrido.
- `False` → aún no ha ocurrido o fue rechazada.

Su función principal es **mantener memoria temporal del estado** dentro de bucles o estructuras condicionales.
Es como un **semáforo lógico**: enciende y apaga un comportamiento programado según las condiciones que surgen durante la ejecución.

---

### 🔹 Lógica general de uso

1. Se **inicializa la bandera** en `False`.
2. Se **recorre una estructura** (lista, matriz, archivo, etc.).
3. En cada iteración se **verifica una condición**.
4. Si la condición se cumple, se cambia la bandera a `True` y (opcionalmente) se rompe el bucle.
5. Al final del proceso, se **consulta la bandera** para decidir el resultado.

---

### 🧠 Concepto clave

La bandera reemplaza condiciones anidadas confusas o cortes abruptos como `break` repetidos, otorgando **claridad estructural** y un control de flujo profesional.

En programación avanzada, las banderas también son útiles para:

- Señalar errores o excepciones detectadas.
- Indicar estados de conexión, autenticación, guardado, etc.
- Activar o desactivar funciones o secciones de código.

---

## 🧪 **3. Ejemplo explicativo**

**Caso:** Verificar si existe al menos un número negativo en una lista bidimensional (estructura anidada).

```python
matriz = [
    [4, 7, 2],
    [9, -1, 5],
    [8, 3, 6]
]

encontro_negativo = False  # bandera inicial

for fila in matriz:
    for numero in fila:
        if numero < 0:
            encontro_negativo = True
            break
    if encontro_negativo:
        break

if encontro_negativo:
    print("⚠️ Hay al menos un número negativo.")
else:
    print("✅ Todos los números son positivos.")
```

**Qué hace aquí la bandera:**

- Se inicializa en `False`.
- Cambia a `True` cuando encuentra un negativo.
- Controla ambos bucles de salida de forma limpia.
- Permite evaluar el resultado al final.

---

## 🧩 **4. Diagrama de flujo**

```
Inicio
 ↓
Bandera = False
 ↓
├── Recorrer filas de la matriz
│     ↓
│     ├── Recorrer números en la fila
│     │      ↓
│     │      ├── ¿Número < 0?
│     │      │      ├── Sí → Bandera = True → Romper bucle interno
│     │      │      └── No → Continuar
│     │
│     └── ¿Bandera == True?
│            ├── Sí → Romper bucle externo
│            └── No → Continuar con siguiente fila
↓
¿Bandera == True?
├── Sí → Mostrar mensaje de número negativo
└── No → Mostrar mensaje de éxito
↓
Fin
```

🟥 **(Mejora opcional para nota extra)**
Agrega una **variable de control de posición (i, j)** que guarde la ubicación exacta donde se detectó el valor negativo y muéstrala al final.
Esto entrena la captura contextual sin aumentar la complejidad del flujo.

```
🟥  ├── Guardar posición [i, j] del valor negativo
🟥  ├── Mostrar posición al final del programa
```

---

## 🧱 **5. Ejercicio 01** - `control_con_bandera_booleana.py`

```python
# -----------------------------------------------------------
# Ejercicio 01 - control_con_bandera_booleana.py
# Objetivo: Usar una bandera booleana para detener una búsqueda
# dentro de una estructura anidada.
# -----------------------------------------------------------

# 1. Definición de la Matriz de Ejemplo (Array 2D)
matriz = [
    [10, 20, 30],
    [40, -5, 60], # ¡Aquí está el negativo!
    [70, 80, 90]
]

# 2. Inicialización de Variables (INICIO del diagrama de flujo)
bandera_negativo = False  # Bandera = False
pos_i = -1                # Pos_i = -1 (Fila)
pos_j = -1                # Pos_j = -1 (Columna)

# 3. Recorrido de la Matriz
# El 'enumerate' nos da el índice (i, j) y el valor en cada iteración.

# Recorrer filas (Bucle externo con índice i)
for i, fila in enumerate(matriz):
    # Recorrer números en la fila (Bucle interno con índice j)
    for j, numero in enumerate(fila):

        # ¿Número < 0?
        if numero < 0:
            # Sí -> Se encontró un negativo
            bandera_negativo = True

            # 🟥 Guardar posición [i, j] del valor negativo (MEJORA)
            pos_i = i
            pos_j = j

            # Romper bucle interno
            break

    # ¿Bandera == True?
    if bandera_negativo:
        # Sí -> Romper bucle externo
        break

# 4. Resultado Final
print("-" * 52)

# ¿Bandera == True?
if bandera_negativo:
    # Sí -> Mostrar mensaje de número negativo y su posición
    print("¡ERROR: Se detectó un número negativo!")
    # 🟥 Mostrar posición al final del programa (MEJORA)
    print(f"El valor negativo se encontró en la posición: [{pos_i}, {pos_j}]")
else:
    # No -> Mostrar mensaje de éxito
    print("ÉXITO: La matriz no contiene números negativos.")
```

```
"""
RESPUETA CONSOLA:
----------------------------------------------------
¡ERROR: Se detectó un número negativo!
El valor negativo se encontró en la posición: [1, 1]
"""
```

---

# 📁 **Ejercicio 02 – busqueda_en_estructura_anidada.py**

---

## 🎯 **1. Objetivo del ejercicio**

Diseñar un programa que **busque un elemento o conjunto de elementos que cumplan condiciones específicas** dentro de una estructura anidada (por ejemplo, lista de diccionarios o lista de listas), utilizando una **bandera booleana** para controlar el flujo lógico y evitar recorridos innecesarios.

El propósito es aprender a **localizar datos complejos sin romper la estructura del programa**, aplicando control booleano, estructuras anidadas, condicionales combinadas y conceptos de lectura limpia y eficiente.

---

## 📘 **2. Teoría aplicada**

### 🔹 Concepto central: **Búsqueda condicional en estructuras anidadas**

Una **estructura anidada** es aquella que contiene otros elementos estructurados (listas dentro de listas, diccionarios dentro de listas, etc.).
La búsqueda condicional en estas estructuras requiere recorrerlas cuidadosamente sin perder el contexto de **qué elemento pertenece a quién**.

Ejemplo clásico:
Buscar un alumno que tenga una nota mayor a 90 y viva en una ciudad específica dentro de una lista de diccionarios.

---

### 🔹 Idea lógica

1. Recorrer cada elemento principal de la estructura (por ejemplo, cada registro o fila).
2. Dentro de cada uno, analizar los subelementos o claves internas.
3. Evaluar una o varias condiciones lógicas combinadas (`and`, `or`).
4. Si la condición se cumple, activar una bandera booleana y detener la búsqueda.
5. Al finalizar, mostrar el resultado según el estado de la bandera.

---

### 🔹 Conceptos teóricos clave

**1️⃣ Condiciones múltiples**
Permiten combinar criterios de búsqueda.
Ejemplo:

```python
if alumno["nota"] > 90 and alumno["ciudad"] == "Madrid":
```

Esto verifica dos criterios al mismo tiempo, permitiendo búsquedas precisas.

**2️⃣ Banderas y flujo controlado**
Igual que en el ejercicio anterior, la bandera sirve para detener los bucles o indicar que un resultado fue hallado.

**3️⃣ Control semántico de estado**
Puedes mantener variables que indiquen _quién_ o _qué_ se encontró.
Ejemplo: `alumno_encontrado = {}` o `nombre_objetivo = None`.

**4️⃣ Uso profesional en la vida real**
Este patrón de búsqueda es usado en:

- Motores de búsqueda internos (bases de datos pequeñas en memoria).
- Validaciones de integridad (comprobar si un registro ya existe).
- Filtros de datos en sistemas automatizados (ERP, CRM, etc.).

---

## 🧪 **3. Ejemplo práctico**

Supón que tienes una lista de clientes y necesitas saber si alguno tiene una compra superior a $1000 en una categoría específica.

```python
clientes = [
    {"nombre": "Ana", "compras": [{"monto": 500, "categoria": "hogar"}, {"monto": 1200, "categoria": "electrónica"}]},
    {"nombre": "Luis", "compras": [{"monto": 200, "categoria": "hogar"}]},
    {"nombre": "Carla", "compras": [{"monto": 800, "categoria": "electrónica"}]}
]
```

**Lógica esperada:**

- Recorrer clientes.
- Recorrer sus compras.
- Buscar una compra con monto > 1000 **y** categoría = "electrónica".
- Si se encuentra, bandera = `True`, registrar el cliente, y romper los bucles.

Resultado esperado:

```
⚠️ Cliente con compra destacada encontrado: Ana
```

---

## 🧭 **4. Diagrama de flujo**

```
Inicio
 ↓
Bandera = False
Cliente_encontrado = None
 ↓
├── Recorrer lista de clientes
│      ↓
│      ├── Recorrer lista de compras de cada cliente
│      │       ↓
│      │       ├── ¿Monto > 1000 AND categoría == "electrónica"?
│      │       │       ├── Sí → Bandera = True
│      │       │       │       ├── Guardar nombre del cliente
│      │       │       │       ├── Romper bucle interno
│      │       │       └── No → Continuar buscando
│      │
│      └── ¿Bandera == True?
│              ├── Sí → Romper bucle externo
│              └── No → Continuar con el siguiente cliente
↓
¿Bandera == True?
├── Sí → Mostrar cliente encontrado
└── No → Mostrar mensaje “no se encontró compra destacada”
↓
Fin
```

🟥 **(Mejoras opcionales para nota extra):**

```
🟥 ├── Guardar también el monto y categoría del resultado encontrado.
🟥 ├── Escribir en un pequeño archivo .csv o .json el resultado (solo con conocimientos de esta clase).
🟥 └── Mostrar un resumen estructurado con datetime.now() (registro temporal profesional).
```

---

## 🧱 **5. Ejercicio 02 – busqueda_en_estructura_anidada.py**

```python
# -----------------------------------------------------------
# Ejercicio 02 - busqueda_en_estructura_anidada.py
# Objetivo: Buscar un elemento que cumpla condiciones
# específicas dentro de una estructura anidada usando
# una bandera booleana para controlar el flujo lógico.
# -----------------------------------------------------------

import datetime
import json
import csv

NOW = datetime.datetime.now()
FECHA_FORMATIADA = NOW.strftime("%d/%m/%Y %H:%M")
ARCHIVO_JSON = "resultado_busqueda.json"
ARCHIVO_CSV = "resultado_busqueda.csv"

ENCABEZADOS = ["nombre", "monto", "articulo", "cantidad", "categoria", "fecha de registro"]

#1️⃣ Crear una estructura de datos anidada
carrito_compras = [
    {
        "Nombre": "Eduardo",
        "compras": [
            {"monto": 300, "articulo": "pantalones", "cantidad": 1, "categoria": "ropa"},
            {"monto": 800, "articulo": "audifonos", "cantidad": 2, "categoria": "electronica"},
        ],
    },
    {
        "Nombre": "Javier",
        "compras": [
            {"monto": 900, "articulo": "platos", "cantidad": 20, "categoria": "hogar"},
            {"monto": 1800, "articulo": "faros", "cantidad": 4, "categoria": "automotriz"},
            {"monto": 200, "articulo": "libro", "cantidad": 1, "categoria": "papeleria"},
        ],
    },
    {
        "Nombre": "Virginia",
        "compras": [
            {"monto": 100, "articulo": "cepillo", "cantidad": 2, "categoria": "hogar"},
            {"monto": 750, "articulo": "destornillador", "cantidad": 4, "categoria": "herramienta"},
            {"monto": 50, "articulo": "carne", "cantidad": "2kg", "categoria": "alimentos"},
        ],
    },

]

#2️⃣ Inicializar la bandera booleana en False.
encontrados = False
compra_de_alimentos = None

#3️⃣ Iniciar bucles.
for cliente in carrito_compras:

    #4️⃣ Iniciar bucle interno
    for compra in cliente["compras"]:
        if compra["categoria"] == "alimentos" and compra["articulo"] == "carne":

            compra_de_alimentos = {
                "nombre": cliente["Nombre"],
                "monto": compra["monto"],
                "articulo": compra["articulo"],
                "cantidad": compra["cantidad"],
                "categoria": compra["categoria"],
                "fecha de registro": FECHA_FORMATIADA
            }
            break

    if compra_de_alimentos:
        break

if compra_de_alimentos:
    print("✅ EXITO EN LA BUSQUEDA: AL MENOS UNA DE LAS COMPRAS FUE DE ALIMENTOS\n")
    print("-" * 90)
    # ✅ CORRECCIÓN DE CONSISTENCIA: La columna "Articulo"
    print(f"{'Nombre':<15}{'Monto':<10}{'Articulo':<15}{'Cantidad':<10}{'Categoria':<15}{'Fecha':<15}")
    print("-" * 90)
    print(
            f"{compra_de_alimentos['nombre']:<15}"
            f"{compra_de_alimentos['monto']:<10}"
            f"{compra_de_alimentos['articulo']:<15}"
            f"{compra_de_alimentos['cantidad']:<10}"
            f"{compra_de_alimentos['categoria']:<15}"
            f"{compra_de_alimentos['fecha de registro']:<15}"
           )

    # 💾 GUARDAR EN JSON
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo_json_guardar:
        json.dump(compra_de_alimentos, archivo_json_guardar, indent=4 )

    # 📝 GUARDAR EN CSV
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=ENCABEZADOS)
        escritor_csv.writeheader()
        escritor_csv.writerow(compra_de_alimentos)

    print(f"\nResultado de la busqueda guardado en los archivos: {ARCHIVO_JSON} y {ARCHIVO_CSV}")

else:
    print("❌ FRACASO EN LA BUSQUEDA: NINGUNA COMPRA ES DE ALIMENTOS")
```

```terminal
"""
RESPUESTA DE CONSOLA:
✅ EXITO EN LA BUSQUEDA: AL MENOS UNA DE LAS COMPRAS FUE DE ALIMENTOS

------------------------------------------------------------------------------------------
Nombre         Monto     Articulo       Cantidad  Categoria      Fecha
------------------------------------------------------------------------------------------
Virginia       50        carne          2kg       alimentos      16/10/2025 00:27

Resultado de la busqueda guardado en los archivos: resultado_busqueda.json y resultado_busqueda.csv
```

```json
contenido del archivo: resultado_busqueda.json
{
    "nombre": "Virginia",
    "monto": 50,
    "articulo": "carne",
    "cantidad": "2kg",
    "categoria": "alimentos",
    "fecha de registro": "16/10/2025 00:27"
}
"""
```

`contenido  del archivo: resultado_busqueda.csv`
| nombre | monto | articulo | cantidad | categoria | fecha de registro |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Virginia | 50 | carne | 2kg | alimentos | 16/10/2025 00:27 |

---

# 📁 **Ejercicio 03 – lectura_y_escritura_csv.py**

---

## 🎯 **1. Objetivo del ejercicio**

Aprender a **leer y escribir archivos CSV** de forma profesional en Python utilizando el módulo estándar `csv`, con estructuras limpias, encabezados definidos, codificación correcta y control de flujo con banderas booleanas.

El objetivo es dominar cómo transformar estructuras de datos (listas, diccionarios) en archivos CSV y viceversa, de forma **segura, escalable y automatizable**.

En términos profesionales, esto te prepara para:

- Procesar reportes de ventas, usuarios o inventarios.
- Exportar datos a Excel o sistemas externos.
- Integrar lectura/escritura en flujos automatizados (ERP, CRM, etc.).

---

## 📘 **2. Teoría aplicada**

### 🔹 ¿Qué es un archivo CSV?

**CSV (Comma-Separated Values)** es un formato de texto plano que organiza información en **filas y columnas**, separadas por comas (`,`) o puntos y coma (`;`), según la configuración regional.
Cada fila representa un registro, y cada columna, un campo.

Ejemplo de un archivo CSV:

```
nombre,edad,ciudad
Ana,25,Madrid
Luis,30,Sevilla
```

---

### 🔹 Módulo estándar `csv`

Python incluye el módulo `csv` para leer y escribir archivos de este tipo.
Ofrece dos clases principales:

- `csv.reader()` → para **leer líneas** del archivo (modo fila por fila).
- `csv.writer()` → para **escribir filas** (listas o tuplas).
  Además, tiene variantes orientadas a diccionarios:
- `csv.DictReader()` → cada fila se convierte en un diccionario.
- `csv.DictWriter()` → escribe directamente desde diccionarios.

---

### 🔹 Lógica de trabajo con CSV

1. Abrir el archivo con `open()`, especificando:

   - Ruta del archivo.
   - Modo de apertura (`"r"` para leer, `"w"` o `"a"` para escribir o agregar).
   - `newline=""` (para evitar líneas en blanco adicionales en Windows).
   - `encoding="utf-8"` (para evitar errores con caracteres especiales).

2. Crear un **lector o escritor** con `csv.reader()` o `csv.writer()`.

3. Iterar o escribir los datos según sea necesario.

4. Cerrar el archivo (o dejar que lo haga el contexto `with`).

---

### 🔹 Concepto de cabecera (header)

El **encabezado** define el orden de las columnas en un CSV.
Usarlo garantiza la coherencia entre escritura y lectura, y evita desalineación de datos.

---

### 🔹 Banderas booleanas aplicadas

En este ejercicio también puedes usar una **bandera de control**, por ejemplo:

- `archivo_creado = False`
  → para indicar si el archivo fue generado correctamente o no.
  Esta práctica es útil para notificar al usuario o controlar procesos automáticos.

---

## 🧪 **3. Ejemplo práctico**

Imagina que tienes una lista de productos y quieres guardarla en un CSV y luego leerla:

```python
import csv

productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Teclado", "precio": 100, "stock": 25},
    {"nombre": "Ratón", "precio": 75, "stock": 40}
]

# Escritura
with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "stock"])
    escritor.writeheader()
    escritor.writerows(productos)

# Lectura
with open("productos.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila)
```

Salida esperada:

```
{'nombre': 'Laptop', 'precio': '1200', 'stock': '5'}
{'nombre': 'Teclado', 'precio': '100', 'stock': '25'}
{'nombre': 'Ratón', 'precio': '75', 'stock': '40'}
```

---

## 🧭 **4. Diagrama de flujo**

```
Inicio
 ↓
Bandera = False
 ↓
├── Definir encabezados de columnas (fieldnames)
│     ↓
│     Crear lista de diccionarios con los datos a guardar
 ↓
Abrir archivo CSV en modo escritura ("w")
 ↓
├── Crear escritor CSV con DictWriter
│     ├── Escribir encabezado
│     └── Escribir filas (writerows)
↓
Cerrar archivo automáticamente con 'with'
↓
Bandera = True (archivo creado)
↓
Mostrar mensaje de éxito
↓
Abrir archivo CSV en modo lectura ("r")
↓
├── Crear lector CSV con DictReader
│     ├── Recorrer cada fila
│     └── Mostrar resultados leídos en pantalla
↓
¿Lectura exitosa?
├── Sí → Mostrar confirmación de lectura
└── No → Mostrar mensaje de error
↓
🟥 (Mejoras opcionales)
🟥 ├── Añadir verificación previa de existencia del archivo con os.path.exists()
🟥 ├── Agregar marca temporal con datetime.now() en cada registro
🟥 └── Guardar también una copia de respaldo (backup) en otra ruta
↓
Fin
```

---

## 🧱 📁 **Ejercicio 03 – lectura_y_escritura_csv.py**

```python
# -----------------------------------------------------------
# Ejercicio 03 - lectura_y_escritura_csv.py
# Objetivo: Leer y escribir archivos CSV usando el módulo csv
# aplicando banderas booleanas para el control del flujo.
# -----------------------------------------------------------

#1️⃣ Importar el módulo csv y, si se desea, datetime y os.
#    (Estos servirán para la mejora opcional 🟥)

#2️⃣ Definir el nombre del archivo CSV a usar.
#    Ejemplo: ARCHIVO = "productos.csv"

#3️⃣ Definir la lista de encabezados (fieldnames)
#    Ejemplo: ENCABEZADOS = ["nombre", "precio", "stock"]

#4️⃣ Crear una lista de diccionarios con datos de ejemplo.
#    Cada diccionario representa una fila (registro).

#5️⃣ Inicializar una bandera en False (archivo_creado = False)
#    Esto servirá para controlar si la escritura fue exitosa.

#6️⃣ Abrir el archivo CSV en modo escritura ("w") con 'with open'
#        - Crear un objeto escritor (DictWriter)
#        - Escribir el encabezado (writeheader)
#        - Escribir todas las filas (writerows)
#        - Cambiar la bandera a True al finalizar.

#7️⃣ Mostrar un mensaje de confirmación si archivo_creado == True
#        Caso contrario, mostrar advertencia.

#8️⃣ Abrir nuevamente el archivo CSV en modo lectura ("r")
#        - Crear un objeto lector (DictReader)
#        - Recorrer el contenido e imprimir cada fila.

#9️⃣ (Opcional 🟥) Mejoras con conocimientos actuales:
#        - Verificar si el archivo existe antes de leer (os.path.exists)
#        - Añadir campo de "fecha de registro" con datetime.now()
#        - Crear una copia de respaldo del archivo (backup.csv)
#        - Manejar posibles excepciones con try/except (nivel profesional)

#🔟 Mostrar mensaje final de estado de lectura (éxito o error).
```

---
