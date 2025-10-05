# **Clase Extra – Consolidación Avanzada del Módulo 1

---

## 🧠 1. Banderas Booleanas y Estructuras Anidadas

### 📘 Concepto teórico

Una **bandera booleana** (o *flag*) es una variable de tipo `bool` (`True` o `False`) que se utiliza para **controlar el flujo lógico de un programa**.
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
            cliente_con_deuda = cliente["nombre"]
            break  # Rompe el segundo bucle
    if factura_pendiente:
        break  # Rompe el primero también

if factura_pendiente:
    print(f"⚠️ Cliente con factura pendiente: {cliente_con_deuda}")
else:
    print("✅ Todas las facturas están pagadas.")
```

### 💡 Claves profesionales

* La bandera **simplifica** la lectura frente a condiciones encadenadas.
* Evita **romper múltiples bucles** de manera desordenada.
* Permite un **control centralizado** del estado lógico del programa.

---

### 🧭 Diagrama de flujo (estilo Gabo)

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

* `csv.reader()` → lee línea a línea
* `csv.writer()` → escribe listas como filas
* `DictReader` / `DictWriter` → trabajan directamente con diccionarios

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

* `json.dump()` / `json.load()` → guardar y leer desde archivos
* `json.dumps()` / `json.loads()` → convertir entre str y diccionario

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

* Simplifica código dentro de `map`, `filter`, `sorted`, etc.
* Ideal para procesamiento de datos o iteraciones simples.

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

* Carga datos de un `.csv` con productos.
* Usa banderas booleanas para marcar si falta stock.
* Actualiza un `.json` con los cambios.
* Genera un reporte binario de respaldo.
* Usa `datetime` para registrar la fecha de ejecución.
* Implementa `lambda`, `map`, `filter`, `any` y `all` para validar y transformar datos.

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

✨ Hasta aquí la **teoría avanzada completa** de esta clase extra.
A partir de aquí entraremos en la **Fase 2 – Ejercicios guiados y diagramas**, donde crearás los programas paso a paso.

¿Deseas que avancemos a la **Fase 2 (diagramas + esqueletos de los ejercicios 1 y 2)**, o prefieres reforzar primero alguno de los conceptos teóricos (`lambda`, banderas, o módulos estándar)?
