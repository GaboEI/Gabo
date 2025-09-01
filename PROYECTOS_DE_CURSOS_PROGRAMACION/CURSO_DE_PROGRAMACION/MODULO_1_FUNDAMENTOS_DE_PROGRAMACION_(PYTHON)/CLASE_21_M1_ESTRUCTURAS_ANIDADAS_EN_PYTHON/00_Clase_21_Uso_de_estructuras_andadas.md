# 🏷️ **Clase 21 – Uso de estructuras anidadas (listas de diccionarios, etc.)**

📍 **Módulo 01 – Fundamentos de Programación (Python)**

---

## 🎯 Objetivo general de esta clase

> Aprender a manejar **estructuras anidadas** en Python, especialmente **listas que contienen diccionarios** y **diccionarios que contienen listas**, para representar, acceder, filtrar, modificar y validar datos complejos que simulan bases de datos, catálogos o registros. Esta habilidad será esencial para trabajar con archivos JSON, APIs, formularios, automatización y estructuras del mundo real.

---

## 🧠 1. ¿Qué es una estructura anidada?

Una **estructura anidada** es aquella que contiene **otras estructuras dentro de sí**.
Por ejemplo:

```python
[
  {"nombre": "Gabo", "edad": 26},
  {"nombre": "María", "edad": 30}
]
```

Aquí tenemos una **lista** que contiene **diccionarios** → esta es una **estructura anidada**.

También podría ser al revés:

```python
{
  "grupoA": ["Ana", "Luis", "Mario"],
  "grupoB": ["Sofía", "Pablo"]
}
```

Un **diccionario** que tiene como valores **listas**. También es estructura anidada.

---

## 📘 Tipos comunes de estructuras anidadas

| Tipo                        | Ejemplo                   | Uso común                 |
| --------------------------- | ------------------------- | ------------------------- |
| Lista de diccionarios       | `[{"id":1}, {"id":2}]`    | Bases de datos temporales |
| Diccionario con listas      | `{"grupo":["a","b"]}`     | Agrupación por categoría  |
| Diccionario de diccionarios | `{"u1":{"nombre":"Ana"}}` | Configuraciones o JSON    |
| Lista de listas             | `[[1,2],[3,4]]`           | Tablas, matrices          |

---

## 🧪 ¿Por qué son importantes?

🔍 En la vida profesional vas a usar estructuras anidadas para:

* Leer archivos `.json` de APIs o servicios externos
* Representar tablas (como Excel) dentro del código
* Crear aplicaciones CRUD con múltiples registros
* Modelar objetos complejos antes de usar clases u OOP

---

## 📚 2. Teoría aplicada – Listas de diccionarios

Vamos a analizar:

```python
estudiantes = [
    {"nombre": "Gabo", "nota": 9},
    {"nombre": "Laura", "nota": 7.5},
    {"nombre": "Luis", "nota": 8}
]
```

🔁 Para recorrer:

```python
for estudiante in estudiantes:
    print(estudiante["nombre"], "-", estudiante["nota"])
```

✔️ Aquí `estudiante` es un diccionario por cada vuelta del ciclo.

---

## 🧪 Acceso a datos anidados

```python
print(estudiantes[0]["nombre"])  # Gabo
print(estudiantes[2]["nota"])    # 8
```

📌 Combinamos **índice de la lista** con **clave del diccionario**.

---

## 🧠 Buenas prácticas

* 🔍 Verifica que las claves existan antes de acceder: `if "nombre" in estudiante:`
* 🔄 Usa bucles para iterar por cada elemento
* ❌ Evita estructuras anidadas excesivas sin control (3 o más niveles profundos → usar clases o bases de datos)

---

## 📘 Documentación oficial útil

* [Listas en Python](https://docs.python.org/es/3/tutorial/datastructures.html#more-on-lists)
* [Diccionarios en Python](https://docs.python.org/es/3/tutorial/datastructures.html#dictionaries)

---

## 🎓 3. Casos profesionales de uso

💼 **Ejemplo real 1 – Sistema de notas de estudiantes:**

```python
notas = [
  {"nombre": "Ana", "notas": [7, 8, 10]},
  {"nombre": "Carlos", "notas": [6, 5, 9]}
]
```

💼 **Ejemplo real 2 – Inventario de productos:**

```python
productos = [
  {"sku": "A123", "stock": 10, "categorias": ["ropa", "verano"]},
  {"sku": "B456", "stock": 5, "categorias": ["electrónica", "hogar"]}
]
```

---

## 📊 4. Diagrama de flujo general para manejo de estructuras anidadas

```.
Inicio
↓
Definir lista de diccionarios (o viceversa)
↓
Recorrer con bucle (for)
↓
├── Acceder a claves internas
│   └── Mostrar / evaluar / modificar
↓
Aplicar lógica deseada (filtros, condiciones, etc.)
↓
Fin
```

---

## 🧱 5. Mini teoría sobre modificación dentro del bucle

```python
for estudiante in estudiantes:
    if estudiante["nombre"] == "Gabo":
        estudiante["nota"] = 10
```

👁️‍🗨️ Esto modifica **directamente** la estructura original.
📌 Si necesitas no tocar la original, debes hacer una copia (`copy.deepcopy()`).

---

## 🧩 6. Lógica de filtrado profesional

🎯 Buscar estudiantes con nota mayor a 8:

```python
for e in estudiantes:
    if e["nota"] > 8:
        print(e["nombre"])
```

🧠 Puedes crear una **nueva lista filtrada**:

```python
mejores = [e for e in estudiantes if e["nota"] > 8]
```

---

## 🧪 BONUS – Combinación realista

```python
empresa = {
    "departamentos": [
        {"nombre": "Ventas", "empleados": ["Ana", "Luis"]},
        {"nombre": "Marketing", "empleados": ["Gabo", "Lucía"]}
    ]
}
```

Para acceder a Gabo:

```python
print(empresa["departamentos"][1]["empleados"][0])
```

💡 ¡Estás recorriendo 3 niveles! (diccionario → lista → diccionario → lista)

---

## 🔍 Casos complejos a evitar sin OOP

Si tienes esto:

```python
[
  {
    "cliente": {
        "nombre": "Gabo",
        "pedidos": [
            {"producto": "Mouse", "precio": 10},
            {"producto": "Teclado", "precio": 20}
        ]
    }
  }
]
```

Esto **sí se puede usar**, pero debe ser cuidadosamente controlado.

Más adelante, lo resolveremos con **clases** o almacenamiento en **bases de datos relacionales / JSON**.

---

## 📦 Conclusión de la teoría

✅ Las estructuras anidadas son esenciales para representar datos reales en Python.
✅ Entender cómo recorrerlas, acceder a sus valores y modificarlas correctamente es clave para:

* Automatización
* Desarrollo web (backend)
* Bases de datos simuladas
* Manipulación de archivos JSON

---

¡Excelente, Gabo! Vamos con toda la potencia al **primer ejercicio** de esta clase 💥

---

# 🧪 Ejercicio 1: `01_lista_de_diccionarios.py`

---

## 🎯 1. Objetivo del ejercicio

Aprender a:

* Crear una **lista de diccionarios** que contenga varios registros de personas (nombre, edad, país).
* Recorrer esta estructura para **mostrar** sus elementos de forma ordenada.
* Aplicar buenas prácticas de legibilidad y formateo.
* Familiarizarte con estructuras anidadas del tipo más usado en proyectos reales con JSON o APIs.

---

## 📚 2. Teoría específica del ejercicio

### 📌 ¿Qué es una lista de diccionarios?

Una **lista de diccionarios** es una estructura donde cada elemento de la lista es un diccionario independiente.
Es comúnmente utilizada para simular una tabla con filas y columnas en código.

```python
# Lista de diccionarios simulando una tabla
[
  {"nombre": "Gabo", "edad": 26, "país": "Cuba"},
  {"nombre": "María", "edad": 30, "país": "México"},
]
```

### 🧠 Lógica a aplicar:

1. Definir una lista con al menos 3 diccionarios.
2. Cada diccionario debe tener las mismas claves (`nombre`, `edad`, `país`).
3. Recorrer la lista con `for`.
4. Mostrar de forma clara los datos de cada persona.

---

## ✅ 3. Ejemplo (no parte del ejercicio, solo demostrativo)

```python
personas = [
    {"nombre": "Ana", "edad": 22, "país": "Chile"},
    {"nombre": "Luis", "edad": 27, "país": "Colombia"}
]

for persona in personas:
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("País:", persona["país"])
    print("----")
```

🔍 Este código recorre una estructura anidada tipo: **lista de diccionarios**
En cada vuelta accede a las claves internas del diccionario actual.

---

## 🔽 4. Diagrama de flujo (texto plano)

```::
Inicio
↓
Definir lista con 3 o más diccionarios
↓
Cada diccionario debe tener:
├── Clave "nombre"
├── Clave "edad"
└── Clave "país"
↓
Recorrer la lista con un bucle for
↓
Para cada diccionario:
├── Mostrar "Nombre: [valor]"
├── Mostrar "Edad: [valor]"
└── Mostrar "País: [valor]"
↓
(🟥 Mejora opcional: Validar que las claves existan con 'if clave in dict')
↓
(🟥 Mejora opcional: Aplicar .title() para mostrar el nombre capitalizado)
↓
Fin
```

---

## 🧱 5. 01_lista_de_diccionarios.py

```python
# 01_lista_de_diccionarios.py

personas = [
    {"nombre": "Gabriel", "edad": 27, "pais": "Cuba"},
    {"nombre": "Eduardo", "edad": 32, "pais": "USA"},
    {"nombre": "Roberto", "edad": 21, "pais": "Brasil"}
]

for persona in personas:
    
    if "nombre" in persona:
        print("nombre:", persona["nombre"].title())
    else:
        print("nombre: No Disponoble")
    
    
    if "edad" in persona:
        print("edad:", persona["edad"])
    else:
        print("edad: No Disponoble")
    
    
    if "pais" in persona:
        print("pais:", persona["pais"].capitalize())
    else:
        print("pais: No Disponoble")
    print("=" * 30)

"""
==============================
===   RESPUESTA DE CONSOLA ===
==============================
nombre: Gabriel
edad: 27
pais: Cuba
==============================
nombre: Eduardo
edad: 32
pais: Usa
==============================
nombre: Roberto
edad: 21
pais: Brasil
==============================
"""
```

---

¡Excelente, Gabo! 🔥
Comenzamos con el **Ejercicio 2** de esta clase. Subimos un poco el nivel aplicando lógica de **búsqueda filtrada** dentro de estructuras anidadas. Prepárate para trabajar con precisión de cirujano 👨‍💻🔎

---

# 🧪 Ejercicio 2: `02_busqueda_en_diccionarios.py`

---

## 🎯 1. Objetivo del ejercicio

Desarrollar un sistema que permita al usuario **buscar un registro específico** dentro de una lista de diccionarios, aplicando:

* Entrada dinámica (`input()`)
* Comparación con claves internas (`if`)
* Búsqueda en estructuras anidadas
* Manejo de entrada no encontrada
* Validación y presentación profesional del resultado

---

## 📚 2. Teoría aplicada del ejercicio

### 📌 ¿Qué es una búsqueda en estructuras anidadas?

Es el proceso de **recorrer una estructura compleja (como una lista de diccionarios)** para encontrar coincidencias según una condición, generalmente definida por el usuario o por un parámetro.

---

### 🧠 Lógica general aplicada

1. El usuario ingresa un nombre (u otro dato clave).
2. Recorres cada diccionario dentro de la lista.
3. Compruebas si alguno de los valores coincide con lo ingresado.
4. Si encuentras coincidencia, muestras los datos.
5. Si no, informas que no fue encontrado.

---

## ✅ 3. Ejemplo simple (sólo para comprensión, no copiar)

```python
clientes = [
  {"nombre": "Gabo", "edad": 27},
  {"nombre": "Ana", "edad": 30}
]

buscar = input("Ingrese el nombre del cliente: ")

for cliente in clientes:
    if cliente["nombre"].lower() == buscar.lower():
        print("¡Cliente encontrado!")
```

🔍 Aquí usamos `.lower()` para hacer la búsqueda **insensible a mayúsculas y minúsculas** → *esto será parte de la mejora opcional*.

---

## 🔽 4. Diagrama de flujo (texto plano, profesional)

```
Inicio
↓
Definir lista de diccionarios con al menos 4 registros
↓
Solicitar al usuario un dato a buscar (por nombre, por ejemplo)
↓
Normalizar entrada del usuario (🟥 Mejora opcional: .strip().lower())
↓
Iniciar bucle for sobre la lista
↓
└── Para cada elemento (diccionario):
     ├── Comparar el campo objetivo con la entrada del usuario
     ├── Si coincide:
     │   ├── Mostrar todos los datos de ese registro
     │   └── Marcar que se encontró resultado
     └── Si no coincide:
         Continuar iterando
↓
Al terminar el bucle:
├── Si se encontró algún registro → no hacer nada adicional
└── Si no se encontró ninguno → mostrar mensaje de “no encontrado”
↓
🟥 Mejora opcional: permitir búsqueda parcial con operador in
↓
Fin
```

---

## 🧱 02_busqueda_en_diccionarios.py

```python
# 02_busqueda_en_diccionarios.py

#1️⃣ Crear una lista llamada "personas" con al menos 4 diccionarios
# Cada diccionario debe tener: "nombre", "edad", "pais"
persona = [
    {"nombre": "Gabriel", "edad": 27, "pais": "Cuba"},
    {"nombre": "Eduardo", "edad": 32, "pais": "USA"},
    {"nombre": "Roberto", "edad": 21, "pais": "Brasil"},
    {"nombre": "Juan", "edad": 25, "pais": "Ecuador"}
]

#2️⃣ Solicitar al usuario que ingrese el nombre que desea buscar
print("\n=== BÚSQUEDA DE PERSONAS ===")
busqueda = input("👤 Ingrese el nombre a buscar: ").strip().lower()

#3️⃣ Definir una variable bandera para saber si se encuentra o no el registro
encontrado = False

#4️⃣ Iniciar un bucle for que recorra la lista de diccionarios
for clave in persona:
    #5️⃣ Dentro del bucle:
    # Comparar si el valor de "nombre" coincide con lo ingresado por el usuario
    if busqueda in  clave["nombre"].lower():
        print("\n✅ Registro encontrado:")
        print(f"Nombre: {clave['nombre']}")
        print(f"Edad: {clave['edad']} años")
        print(f"Pais: {clave['pais']}")
        print("-" * 30)
        encontrado = True
        break

#6️⃣ Fuera del bucle:
# Si la bandera sigue siendo False, mostrar mensaje de “No se encontró el registro”
if not encontrado:
    print("\n ❌ No se encontró ningún registro con ese nombre.")

print("\n=== BÚSQUEDA FINALIZADA ===")
```

```..
"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
=== BÚSQUEDA DE PERSONAS ===
👤 Ingrese el nombre a buscar: Roberto

✅ Registro encontrado:
Nombre: Roberto
Edad: 21 años
Pais: Brasil
------------------------------

=== BÚSQUEDA FINALIZADA ===
====================================================================
=== BÚSQUEDA DE PERSONAS ===
👤 Ingrese el nombre a buscar: ardo

✅ Registro encontrado:
Nombre: Eduardo
Edad: 32 años
Pais: USA
------------------------------
=== BÚSQUEDA FINALIZADA ===
====================================================================
=== BÚSQUEDA DE PERSONAS ===
👤 Ingrese el nombre a buscar: python

❌ No se encontró ningún registro con ese nombre.

=== BÚSQUEDA FINALIZADA ===
====================================================================
"""
```

---
