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
# Ejercicio 03 - lectura_y_escritura_csv.py
# Objetivo: Leer y escribir archivos CSV usando el módulo csv
# aplicando banderas booleanas para el control del flujo.
# -----------------------------------------------------------
#1️⃣ Importar el módulo csv y, si se desea, datetime y os.
import csv
import datetime
import os
from tabulate import tabulate

# CONSTANTES
#2️⃣ Definir el nombre del archivo CSV a usar.
ARCHIVO_CSV = "03_lectura_y_escritura_csv.csv"

#3️⃣ Definir la lista de ENCABEZADOS (fieldnames)
ENCABEZADOS = ["Nombre", "ID", "Teléfono", "Status"]
FECHA = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")


#4️⃣ Crear una lista de diccionarios con datos de ejemplo.
clientes = [
    {"Nombre": "Eduardo", "ID": 4258, "Teléfono": "+79625875689", "Status":"VIP"},
    {"Nombre": "Ramon", "ID": 98575, "Teléfono": "+79215896514", "Status":"VIP"},
    {"Nombre": "Francisco", "ID": 56587, "Teléfono": "+79678564287", "Status":"CASUAL"},
    {"Nombre": "Juan", "ID": 89875, "Teléfono": "+79628550045", "Status":"INVITADO"},
    {"Nombre": "Pedro", "ID": 89854, "Teléfono": "+79855743337", "Status":"BLOQUEADO"},
    {"Nombre": "Ana", "ID": 70235, "Teléfono": "+79626963706", "Status":"VIP"}
]


#5️⃣ Inicializar una bandera
archivo_creado = False
lectura_exitosa = False

#6️⃣ Abrir el archivo CSV en modo escritura ("w") con 'with open'
try:
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=ENCABEZADOS)
        escritor_csv.writeheader()
        escritor_csv.writerows(clientes)
        archivo_creado = True
except Exception as error_escritura:
    print(f"❌ ERROR: {error_escritura} al crear el archivo")

if os.path.exists(ARCHIVO_CSV):
    #7️⃣ Mostrar un mensaje de confirmación
    print(f"✅ Archivo '{ARCHIVO_CSV}' creado correctamente.\n")

else:
    print("⚠️ Advertencia: No se pudo crear el archivo CSV.")

#8️⃣ Abrir nuevamente el archivo CSV en modo lectura ("r")
try:
    with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        datos = list(lector_csv)
        if not datos:
            raise ValueError("❌ El archivo está vacío o sin datos válidos")
        print(f"⏱️  Fecha de creación: {FECHA}.\n")
        print(tabulate(datos, headers="keys", tablefmt="fancy_grid"))
        lectura_exitosa = True
except Exception as error_lectura:
    print(f"❌ ERROR: {error_lectura} al leer el archivo")
else:
    print("\n📑 Lectura realizada sin errores. ")
finally:
    if lectura_exitosa:
        print("\n❇️ Estado final: LECTURA EXITOSA")
    else:
        print("\n✴️ Estado final: ERROR EN LA LECTURA")
```

```terminal
"""
RESPUESTA DE CONSOLA
------------------------------------------------------------------
✅ Archivo '03_lectura_y_escritura_csv.csv' creado correctamente.

⏱️  Fecha de creación: 16.10.2025 20:10.

╒═══════════╤═══════╤══════════════╤═══════════╕
│ Nombre    │    ID │     Teléfono │ Status    │
╞═══════════╪═══════╪══════════════╪═══════════╡
│ Eduardo   │  4258 │ +79625875689 │ VIP       │
├───────────┼───────┼──────────────┼───────────┤
│ Ramon     │ 98575 │ +79215896514 │ VIP       │
├───────────┼───────┼──────────────┼───────────┤
│ Francisco │ 56587 │ +79678564287 │ CASUAL    │
├───────────┼───────┼──────────────┼───────────┤
│ Juan      │ 89875 │ +79628550045 │ INVITADO  │
├───────────┼───────┼──────────────┼───────────┤
│ Pedro     │ 89854 │ +79855743337 │ BLOQUEADO │
├───────────┼───────┼──────────────┼───────────┤
│ Ana       │ 70235 │ +79626963706 │ VIP       │
╘═══════════╧═══════╧══════════════╧═══════════╛

📑 Lectura realizada sin errores.

❇️ Estado final: LECTURA EXITOSA
------------------------------------------------------------------
"""
```

---

# 📁 **Ejercicio 04 – guardar_y_cargar_json.py**

---

## 🎯 **1. Objetivo del ejercicio**

Aprender a **guardar y cargar información estructurada en formato JSON**, aplicando control de flujo con banderas booleanas, buenas prácticas de manejo de archivos y validaciones lógicas.

Este ejercicio busca que comprendas cómo:

- Serializar (guardar) estructuras de Python (`listas`, `diccionarios`) en archivos JSON.
- Deserializar (cargar) esa información desde el archivo al programa.
- Controlar los estados de lectura y escritura con banderas booleanas y manejo de excepciones.

**Aplicación profesional:**
El formato JSON se usa en **APIs, bases de datos NoSQL (como MongoDB), almacenamiento de configuración**, y comunicación entre aplicaciones.
Dominarlo es esencial para cualquier desarrollador profesional.

---

## 📘 **2. Teoría aplicada**

### 🔹 ¿Qué es JSON?

**JSON (JavaScript Object Notation)** es un formato ligero de intercambio de datos.
Es legible por humanos, compatible con casi todos los lenguajes de programación y se basa en una estructura **clave → valor**.

Ejemplo conceptual:

```json
{
  "nombre": "Gabo",
  "edad": 27,
  "lenguajes": ["Python", "JavaScript", "C#"],
  "activo": true
}
```

---

### 🔹 Estructura básica

Un archivo JSON puede contener:

- **Objetos** `{}` → equivalentes a diccionarios de Python.
- **Listas** `[]` → equivalentes a listas de Python.
- **Valores primitivos:** `str`, `int`, `float`, `bool`, `null` (en Python: `None`).

---

### 🔹 Módulo estándar `json`

Python incluye el módulo `json` para manejar este formato.
Funciones principales:

| Función                   | Descripción                                    |
| ------------------------- | ---------------------------------------------- |
| `json.dump(obj, archivo)` | Guarda un objeto Python en un archivo JSON     |
| `json.load(archivo)`      | Carga (lee) el contenido JSON desde un archivo |
| `json.dumps(obj)`         | Convierte un objeto Python en un string JSON   |
| `json.loads(cadena)`      | Convierte una cadena JSON en un objeto Python  |

Parámetros útiles:

- `indent=4` → para formatear con sangría legible.
- `ensure_ascii=False` → para permitir caracteres en español correctamente.

---

### 🔹 Conceptos clave a aplicar

1. **Serialización:** convertir estructuras Python a formato JSON.
2. **Deserialización:** convertir JSON a estructuras Python.
3. **Control con banderas:** determinar si el archivo fue guardado o cargado exitosamente.
4. **Manejo de excepciones:** capturar errores de lectura/escritura o JSON malformado.

---

### 🔹 Flujo lógico general

1. Crear una estructura Python (lista o diccionario).
2. Guardarla en un archivo `.json` usando `json.dump()`.
3. Leer ese mismo archivo con `json.load()`.
4. Verificar con una bandera si el proceso fue exitoso.
5. Mostrar la información cargada, formateada y legible.

---

## 🧪 **3. Ejemplo práctico**

Supón que tienes una lista de usuarios y deseas guardar y recuperar sus datos:

```python
import json

usuarios = [
    {"nombre": "Ana", "edad": 28, "rol": "admin"},
    {"nombre": "Luis", "edad": 31, "rol": "usuario"}
]

# Guardar
with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)

# Leer
with open("usuarios.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
    print(datos)
```

Salida esperada:

```
[{'nombre': 'Ana', 'edad': 28, 'rol': 'admin'}, {'nombre': 'Luis', 'edad': 31, 'rol': 'usuario'}]
```

💡 Observa que el JSON preserva la estructura original del objeto Python.

---

## 🧭 **4. Diagrama de flujo**

```
Inicio
 ↓
Bandera_guardado = False
Bandera_carga = False
 ↓
├── Crear estructura de datos (lista o diccionario)
│       ↓
│       Guardar en archivo JSON
│       ↓
│       ├── ¿Se guardó correctamente?
│       │       ├── Sí → Bandera_guardado = True
│       │       └── No → Mostrar error
↓
¿Bandera_guardado == True?
├── Sí → Proceder a lectura
└── No → Terminar programa
 ↓
Abrir archivo JSON en modo lectura
 ↓
├── Leer contenido con json.load()
│       ├── ¿Archivo válido?
│       │       ├── Sí → Bandera_carga = True
│       │       └── No → Mostrar error
│
├── Mostrar datos cargados en pantalla
└── Mostrar cantidad de registros cargados
↓
🟥 (Mejoras opcionales)
🟥 ├── Añadir timestamp de guardado (datetime.now())
🟥 ├── Verificar existencia del archivo antes de leer (os.path.exists())
🟥 ├── Guardar copia de respaldo (backup.json)
🟥 └── Usar try/except para manejar JSONDecodeError
↓
Fin
```

---

## 🧱 📁 **Ejercicio 04 – guardar_y_cargar_json.py**

```python
# ---------------------------------------------------------------------
# Ejercicio 04 - guardar_y_cargar_json.py
# Objetivo: Guardar y cargar datos estructurados en formato JSON
# usando el módulo json y controlando el flujo con banderas booleanas.
# ---------------------------------------------------------------------
#1️⃣ Importar el módulo json y opcionalmente datetime y os.
import json
import os
from datetime import datetime
#from tabulate import tabulate # -> No supe como usarlo

#2️⃣ Definir el nombre del archivo JSON a usar.
ARCHIVO_JSON = "04_guardar_y_cargar_json.json"
FECHA = datetime.now().strftime("📆 %d.%m.%Y ⏱️  %H:%M")
#print(FECHA)

#3️⃣ Crear una estructura de datos Python (lista o diccionario)
carrito_de_compras = {
    "usuario": {
        "id_usuario": 20391, "nombre": "Gabriel Espinosa", "correo": "gabo@example.com",
        "pais": "Rusia", "moneda": "RUB", "miembro_vip": True
    },
    "carrito": {
        "fecha_creacion": "2025-10-16",
        "productos": [
            {
                "id_producto": 101, "nombre": "Teclado Mecánico RGB", "categoria": "Periféricos",
                "marca": "KeyChron", "precio_unitario": 8490.99, "cantidad": 1, "en_stock": True,
                "descuento": {"tipo": "porcentaje", "valor": 10},
                "envio": {"metodo": "Estándar", "costo": 300.0, "tiempo_estimado": "3-5 días"},
                "valoraciones": [5, 4, 5, 4, 5]
            },
            {
                "id_producto": 204, "nombre": "Mouse Logitech MX Master 3S", "categoria": "Periféricos",
                "marca": "Logitech", "precio_unitario": 11290.00, "cantidad": 2, "en_stock": True,
                "descuento": {"tipo": "fijo", "valor": 500},
                "envio": {"metodo": "Express", "costo": 450.0, "tiempo_estimado": "1-2 días"},
                "valoraciones": [5, 5, 5, 4, 5]
            },
            {
                "id_producto": 509, "nombre": "SSD NVMe 1TB Kingston Fury Renegade", "categoria": "Almacenamiento",
                "marca": "Kingston", "precio_unitario": 12500.75, "cantidad": 1, "en_stock": False,
                "descuento": {"tipo": None, "valor": 0},
                "envio": {"metodo": "No disponible", "costo": 0.0, "tiempo_estimado": None},
                "valoraciones": [5, 4, 5, 5, 5, 4]
            }
        ],
        "totales": {
            "subtotal": 0.0, "descuentos_totales": 0.0, "envio_total": 0.0,
            "iva": 0.0, "total_final": 0.0
        }
    },
    "historial": [
        {"id_pedido": 9001, "fecha": "2025-07-15", "total_pagado": 18990.50,
         "metodo_pago": "Tarjeta Visa", "estado": "Entregado",
         "productos": ["Monitor LG UltraWide 29”", "Soporte VESA"]},
        {"id_pedido": 9002, "fecha": "2025-09-10", "total_pagado": 5990.00,
         "metodo_pago": "YooMoney", "estado": "Enviado",
         "productos": ["Auriculares Sony WH-1000XM5"]}
    ],
    "preferencias": {
        "direccion_envio": {
            "pais": "Rusia", "ciudad": "San Petersburgo", "codigo_postal": "190000",
            "direccion": "Nevsky Prospekt 28, Apt. 4", "telefono_contacto": "+7 911 234-5678"
        },
        "idioma": "es", "modo_oscuro": True,
        "notificaciones": {"ofertas": True, "envios": True, "recomendaciones": False}
    }
}

# 1️⃣ Definir archivos y variables principales
ARCHIVO_JSON = "04_guardar_y_cargar_json.json"
BACKUP_JSON = "usuarios_backup.json"
FECHA = datetime.now().strftime("📆 %d.%m.%Y ⏱️ %H:%M")

\
guardado_exitoso = False
carga_exitosa = False

# 4️⃣ Crear copia de seguridad antes de sobrescribir el archivo principal
if os.path.exists(ARCHIVO_JSON):
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo_original:
            contenido = archivo_original.read()
        with open(BACKUP_JSON, "w", encoding="utf-8") as respaldo:
            respaldo.write(contenido)
        print(f"🗂️ Copia de respaldo creada correctamente → {BACKUP_JSON}")
    except Exception as e:
        print(f"⚠️ No se pudo crear la copia de respaldo: {e}")

# 5️⃣ Guardar los datos actualizados
try:
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo_json:
        json.dump(carrito_de_compras, archivo_json, indent=4, ensure_ascii=False)
        guardado_exitoso = True
except Exception as error_escritura:
    print(f"❌ ERROR al guardar el archivo: {error_escritura}")
else:
    print(f"\n✅ Archivo '{ARCHIVO_JSON}' creado correctamente ({FECHA})")

# 6️⃣ Leer y validar el contenido del archivo
if guardado_exitoso:

    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo_json:
            datos_json = json.load(archivo_json)
            carga_exitosa = True
            print(f"\n🗃️ CONTENIDO DEL ARCHIVO → {ARCHIVO_JSON}\n")
            print(datos_json)
    except json.JSONDecodeError as e:
        print(f"❌ Error de decodificación JSON: {e}")
    except Exception as e:
        print(f"❌ Error general al leer el archivo: {e}")
    else:
        total_registros = len(datos_json)
        print(f"📑 Lectura exitosa. Total de registros principales: {total_registros}")
    finally:
        estado = "LECTURA EXITOSA" if carga_exitosa else "ERROR EN LA LECTURA"
        print(f"\n🧭 Estado final: {estado}")
else:
    print("🛑 Error al crear o acceder al archivo JSON.")
```

```
"""
RESPUSTA DE CONSOLA
🗂️ Copia de respaldo creada correctamente → usuarios_backup.json

✅ Archivo '04_guardar_y_cargar_json.json' creado correctamente (📆 16.10.2025 ⏱️ 23:55)

🗃️ CONTENIDO DEL ARCHIVO → 04_guardar_y_cargar_json.json

{'usuario': {'id_usuario': 20391, (...) True, 'recomendaciones': False}}}
📑 Lectura exitosa. Total de registros principales: 4

🧭 Estado final: LECTURA EXITOSA

"""
```

---

# 🧩 **Ejercicio Extra 4.5 – gestión_de_inventario_json.py**

---

## 🎯 **Objetivo del ejercicio**

Aplicar lo aprendido sobre **lectura, escritura y actualización de ficheros JSON** para crear un pequeño sistema de gestión de inventario que:

1. Guarde la información de los productos en un archivo `.json`.
2. Permita actualizar el stock y recalcular los totales.
3. Genere una **copia de respaldo automática (backup)** del inventario actualizado.
4. Use **banderas booleanas y manejo de excepciones** para controlar el flujo.

💼 _Simula una parte real de un sistema de e-commerce o control de almacén._

---

## 🧠 **Teoría breve aplicada**

- **JSON** se usará para persistir el inventario de productos: cada producto será un diccionario con claves como `nombre`, `precio`, `stock`, `categoria`, `activo`.
- Se usarán funciones del módulo `json`:

  - `json.dump()` para guardar los datos.
  - `json.load()` para cargarlos.

- Se aplicarán banderas booleanas (`guardado_exitoso`, `lectura_exitosa`) para controlar el flujo.
- Se integrará `datetime` para registrar la fecha de actualización del inventario.

---

## 🧪 **Ejemplo conceptual (sin código ejecutable)**

**Entrada inicial (`inventario.json`):**

```json
[
  {
    "id": 101,
    "nombre": "Laptop Asus ZenBook",
    "precio": 125000.0,
    "stock": 3
  },
  { "id": 102, "nombre": "Monitor Dell 27\"", "precio": 85000.0, "stock": 2 },
  {
    "id": 103,
    "nombre": "Teclado Mecánico Logitech",
    "precio": 15000.0,
    "stock": 6
  }
]
```

**Proceso esperado:**

1. Cargar inventario.
2. Modificar el stock de un producto (por ejemplo, restar una unidad vendida).
3. Recalcular el valor total del inventario (`precio * stock`).
4. Guardar el inventario actualizado en el mismo archivo.
5. Crear un backup (`inventario_backup.json`) con marca temporal.

**Salida esperada:**

```
✅ Inventario actualizado correctamente.
📦 Productos registrados: 3
💰 Valor total en stock: 420,000.00 RUB
🕒 Última actualización: 17/10/2025 22:40
```

---

## 🧭 **Diagrama de flujo**

```
Inicio
 ↓
Bandera_guardado = False
Bandera_lectura = False
 ↓
¿Existe el archivo inventario.json?
├── No → Crear archivo base con lista de productos inicial
└── Sí → Continuar
 ↓
Abrir archivo en modo lectura
 ↓
├── Cargar datos con json.load()
│       ↓
│       ├── Calcular valor total actual
│       └── Mostrar productos
↓
Modificar stock o precios (simulación interna)
 ↓
Recalcular totales
 ↓
Abrir archivo en modo escritura
 ↓
├── Guardar nuevos datos con json.dump()
│       ├── Bandera_guardado = True
│       └── Mostrar mensaje de confirmación
↓
🟥 (Mejora opcional)
🟥 ├── Crear copia backup con datetime.now() → inventario_backup.json
🟥 ├── Agregar campo “ultima_actualizacion” a cada producto
🟥 └── Validar errores de lectura con except json.JSONDecodeError
↓
Fin
```

---

## 🧱 **Ejercicio Extra 4.5 - gestión_de_inventario_json.py**

```python
# -----------------------------------------------------------
# Ejercicio Extra 4.5 - gestión_de_inventario_json.py
# Objetivo: Reforzar el manejo de lectura/escritura JSON creando
# un mini sistema de gestión de inventario persistente.
# -----------------------------------------------------------

#1️⃣ Importar los módulos necesarios:
#    - json (para serializar/deserializar)
#    - os (para verificar existencia de archivo)
#    - datetime (para fecha de actualización)

#2️⃣ Definir nombres de archivo:
#    ARCHIVO_INVENTARIO = "inventario.json"
#    ARCHIVO_BACKUP = "inventario_backup.json"

#3️⃣ Inicializar banderas:
#    guardado_exitoso = False
#    lectura_exitosa = False

#4️⃣ Comprobar si existe el archivo de inventario:
#    - Si no existe, crear uno con una lista inicial de productos.
#    - Cada producto debe incluir: id, nombre, precio, stock, categoria.

#5️⃣ Intentar abrir el archivo y cargar datos con json.load():
#    - Cambiar bandera lectura_exitosa = True si no hay errores.
#    - Si ocurre json.JSONDecodeError, mostrar mensaje de advertencia.

#6️⃣ Mostrar en pantalla un resumen del inventario:
#    - Número de productos registrados.
#    - Valor total del inventario (sumatoria precio * stock).

#7️⃣ Simular una actualización (por ejemplo, reducir stock de un producto).
#    - Realizar los cálculos y actualizar los valores.

#8️⃣ Guardar nuevamente el archivo actualizado con json.dump()
#    - indent=4, ensure_ascii=False
#    - Cambiar bandera guardado_exitoso = True

#9️⃣ Si guardado_exitoso:
#    - Crear archivo de respaldo (backup) con los mismos datos.
#    - Incluir fecha y hora de actualización dentro del JSON.

#🔟 Mostrar mensaje final de confirmación:
#    - Inventario actualizado y respaldado correctamente.
#    - Mostrar fecha y hora del respaldo.

#🟥 Mejora opcional (nota extra):
#    - Calcular y mostrar el producto más caro y el de mayor stock.
#    - Generar reporte visual tabulado si conoces 'tabulate'.
```

---

## 💡 **Objetivo pedagógico**

Este ejercicio tiene un propósito único: **consolidar tu dominio de JSON en contexto real**.
Al terminarlo, deberías poder:

- Crear, leer, modificar y guardar archivos JSON sin errores.
- Implementar flujos con banderas y backups automáticos.
- Manipular estructuras anidadas y cálculos derivados (totales).

---
