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

## 🏁 Ejercicio 1: `01_lista_de_diccionarios.py`

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

### 🧠 Lógica a aplicar

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

## 🧪 Ejercicio 2: `02_busqueda_en_diccionarios.py`

---

## 🟨 1. Objetivo del ejercicio

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

```,
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

## 💥 Ejercicio 3: `03_agregar_y_modificar.py`

---

## 💥 1. Objetivo del ejercicio

Aprender a:

* **Agregar nuevos registros** (diccionarios) a una lista existente.
* **Modificar registros existentes** si el usuario lo desea.
* Usar estructuras condicionales (`if`, `for`, `else`) para decidir entre agregar o actualizar.
* Trabajar con **estructuras dinámicas** que crecen o cambian durante la ejecución.
* Preparar las bases para futuros proyectos CRUD y simulaciones de bases de datos.

---

## 📚 2. Teoría del concepto aplicado

### 📌 ¿Por qué es importante aprender a agregar y modificar registros?

En programación real, los datos **no son estáticos**. A menudo necesitas:

* Registrar nuevos usuarios, productos, estudiantes, clientes...
* Corregir o actualizar información ya existente
* Hacer que el sistema responda a la **entrada del usuario** y **cambie la estructura de datos** en tiempo real

Este ejercicio simula **una tabla dinámica** o una pequeña **base de datos en memoria**.

---

### 🧠 Lógica aplicada

#### A. Agregar

1. Crear un nuevo diccionario con claves como `"nombre"`, `"edad"`, `"pais"`.
2. Añadir ese diccionario a la lista con `.append()`.

#### B. Modificar

1. Recorrer la lista.
2. Si se encuentra el registro, permitir al usuario **editar algún campo**.
3. Confirmar el cambio.

---

## ✅ 3. Ejemplo para comprender la lógica

```python
personas = [{"nombre": "Gabo", "edad": 26, "pais": "Cuba"}]

nuevo = {"nombre": "Ana", "edad": 30, "pais": "Perú"}
personas.append(nuevo)  # ← Agregar

for p in personas:
    if p["nombre"] == "Gabo":
        p["edad"] = 27  # ← Modificar
```

---

## 🔽 4. Diagrama de flujo (formato estándar Gabo)

```Inicio
Inicio
↓
Definir lista inicial con 3 o más diccionarios
↓
Mostrar menú:
├── 1. Agregar nueva persona
└── 2. Modificar persona existente
↓
Leer opción del usuario
↓
Si opción == 1:
├── Solicitar datos: nombre, edad, país
├── Crear nuevo diccionario con esos datos
└── Agregarlo a la lista con append()
↓
Si opción == 2:
├── Solicitar nombre de la persona a modificar
├── Recorrer lista
│   ├── Si coincide:
│   │   ├── Mostrar datos actuales
│   │   ├── Solicitar nuevos valores (o dejar en blanco para mantener)
│   │   └── Actualizar el diccionario
│   └── Si no coincide → seguir buscando
└── Al terminar:
     ├── Si fue modificado → Confirmar
     └── Si no se encontró → Mostrar mensaje
↓
(🟥 Mejora opcional: validar si la persona ya existe antes de agregarla)
↓
(🟥 Mejora opcional: permitir repetir menú hasta que el usuario decida salir)
↓
Mostrar lista final actualizada
↓
Fin
```

---

## 03_agregar_y_modificar.py

```python
# Lista inicial de personas
personas = [
    {"nombre": "Ana", "edad": 25, "pais": "España"},
    {"nombre": "Juan", "edad": 30, "pais": "México"},
    {"nombre": "Sofía", "edad": 22, "pais": "Argentina"}
]

while True:
    # Mostrar menú
    print("\nMenú de opciones:")
    print("1. Agregar nuevo registro")
    print("2. Modificar registro existente")
    print("Escribe 'salir' para terminar")
    
    # Solicitar opción
    opcion = input("Selecciona una opción: ").lower()
    
    # Salir del programa
    if opcion == "salir":
        break
    
    # Opción 1: Agregar nuevo registro
    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        # Comprobar si el nombre ya existe
        existe = False
        for persona in personas:
            if persona["nombre"].lower() == nombre.lower():
                existe = True
                break
        if existe:
            print("Error: El nombre ya existe en la lista.")
        else:
            try:
                edad = int(input("Ingresa la edad: "))
                pais = input("Ingresa el país: ")
                # Crear y agregar nuevo registro
                nuevo_registro = {"nombre": nombre, "edad": edad, "pais": pais}
                personas.append(nuevo_registro)
                print("Registro agregado correctamente.")
            except ValueError:
                print("Error: La edad debe ser un número entero.")
    
    # Opción 2: Modificar registro existente
    elif opcion == "2":
        nombre = input("Ingresa el nombre de la persona a modificar: ")
        encontrado = False
        for persona in personas:
            if persona["nombre"].lower() == nombre.lower():
                encontrado = True
                # Mostrar datos actuales
                print(f"\nDatos actuales: {persona}")
                # Solicitar nuevos datos
                nuevo_nombre = input("Nuevo nombre (presiona Enter para mantener el actual): ")
                nueva_edad = input("Nueva edad (presiona Enter para mantener la actual): ")
                nuevo_pais = input("Nuevo país (presiona Enter para mantener el actual): ")
                
                # Actualizar campos si se proporcionaron nuevos valores
                if nuevo_nombre:
                    persona["nombre"] = nuevo_nombre
                if nueva_edad:
                    try:
                        persona["edad"] = int(nueva_edad)
                    except ValueError:
                        print("Error: La edad debe ser un número entero. No se modificó la edad.")
                if nuevo_pais:
                    persona["pais"] = nuevo_pais
                print("Registro modificado correctamente.")
                break
        if not encontrado:
            print("No se encontró ese registro.")
    
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 'salir'.")

# Mostrar lista final
print("\nLista final de personas:")
for persona in personas:
    print(persona)

"""
```

```,
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: 1
Ingresa el nombre: Juan
Error: El nombre ya existe en la lista.

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: 1 
Ingresa el nombre: Ramon
Ingresa la edad: 24
Ingresa el país: Mexico
Registro agregado correctamente.

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: 2
Ingresa el nombre de la persona a modificar: Juan

Datos actuales: {'nombre': 'Juan', 'edad': 30, 'pais': 'México'}
Nuevo nombre (presiona Enter para mantener el actual): Juan Alberto
Nueva edad (presiona Enter para mantener la actual): 23
Nuevo país (presiona Enter para mantener el actual): Mexico
Registro modificado correctamente.

Menú de opciones:
1. Agregar nuevo registro
2. Modificar registro existente
Escribe 'salir' para terminar
Selecciona una opción: salir

Lista final de personas:
{'nombre': 'Ana', 'edad': 25, 'pais': 'España'}
{'nombre': 'Juan Alberto', 'edad': 23, 'pais': 'Mexico'}
{'nombre': 'Sofía', 'edad': 22, 'pais': 'Argentina'}
{'nombre': 'Ramon', 'edad': 24, 'pais': 'Mexico'}
====================================================================
"""
```

---

🧠 Este ejercicio te entrena para cosas como:

* Menús interactivos
* Bases de datos en memoria
* Interacción tipo CRUD (Create, Read, Update, Delete)

---

## 🟨 Ejercicio 4: `04_validar_y_contar_elementos.py`

---

## ⏺️ 1. Objetivo del ejercicio

* Validar ciertos **criterios** dentro de una lista de diccionarios.
* **Contar cuántos registros cumplen** condiciones específicas.
* Mostrar estadísticas simples como:

  * Número de personas mayores de edad
  * Cuántos son de un país determinado
  * Cantidad total vs filtrada
* Aplicar lógica condicional (`if`, `>=`, `==`, etc.) con estructuras anidadas.

---

## 📚 2. Teoría aplicada

### 📌 ¿Qué es validar y contar?

👉 **Validar** significa comprobar si una condición lógica se cumple:
Ejemplo: `if persona["edad"] >= 18:`

👉 **Contar** es incrementar un valor (contador) cada vez que algo sucede.
Ejemplo: `contador += 1` si la condición se cumple.

---

### 🧠 Aplicaciones reales

Esto es muy usado para:

* Contar cuántos usuarios activos hay
* Filtrar clientes de un país
* Saber cuántos productos superan cierto stock
* Generar reportes dinámicos en dashboards

---

## 🟨 3. Ejemplo para comprender la lógica

```python
personas = [
    {"nombre": "Ana", "edad": 25, "pais": "España"},
    {"nombre": "Luis", "edad": 17, "pais": "México"},
    {"nombre": "Sara", "edad": 21, "pais": "Argentina"}
]

mayores = 0

for persona in personas:
    if persona["edad"] >= 18:
        mayores += 1

print("Total de mayores de edad:", mayores)
```

---

## 🔽 4. Diagrama de flujo textual

```Inicio
Inicio
↓
Definir lista con 4 o más personas (diccionarios con "nombre", "edad", "pais")
↓
Inicializar contadores en 0:
├── contador_mayores
├── contador_menores
├── contador_mexicanos (ejemplo)
↓
Recorrer lista con bucle for
↓
└── Para cada persona:
     ├── Validar si edad >= 18 → contador_mayores += 1
     ├── Si edad < 18 → contador_menores += 1
     ├── Si pais == "México" (ignorar mayúsculas) → contador_mexicanos += 1
     ├── (🟥 Mejora opcional: validar claves antes de acceder con "in")
     ├── (🟥 Mejora opcional: usar .lower() para evitar errores de escritura)
↓
Mostrar los resultados finales:
├── Total de mayores
├── Total de menores
├── Total de personas de México
↓
🧠 Bonus

* 🟡 Mostrar el porcentaje de personas mexicanas vs total
* 🟡 Crear un diccionario de contadores por país (`{"México": 2, "Cuba": 1, ...}`)
* 🟡 Guardar en una lista aparte los nombres de los mayores de edad

🔹 **No obligatorios**, pero si aplicas uno, cuenta como punto extra ⭐
Fin
```

--

## 🧱 5. 04_validar_y_contar_elementos.py

```python
# 04_validar_y_contar_elementos.py

# Base de datos
estudiantes = [ 
    {"nombre": "Carlos López", "edad": 17, "pais": "México"},
    {"nombre": "Sofía Rodríguez", "edad": 20, "pais": "Argentina"},
    {"nombre": "Juan Martínez", "edad": 16, "pais": "México"},
    {"nombre": "Lucía Gómez", "edad": 22, "pais": "España"},
    {"nombre": "Miguel Sánchez", "edad": 19, "pais": "México"},
    {"nombre": "Ana García", "edad": 24, "pais": "Chile"},
    {"nombre": "Valeria Torres", "edad": 15, "pais": "Perú"},
    {"nombre": "Diego Fernández", "edad": 21, "pais": "Colombia"},
    {"nombre": "María Pérez", "edad": 18, "pais": "Brasil"},
    {"nombre": "Andrés Díaz", "edad": 23, "pais": "Estados Unidos"}
]

#contadores:
contador_mayores = 0
contador_menores = 0
contador_mexicanos = 0


for e in estudiantes:

    if "pais"  in e and "edad" in e:
        
        if e["edad"] >= 18:
            contador_mayores += 1

        if e["edad"] < 18:
            contador_menores += 1
        
        if e["pais"].lower() == "méxico":
            contador_mexicanos += 1
            porcentaje_mexicanos = (contador_mexicanos / 10) * 100
        
contadores_pais = {}
for e in estudiantes:
    contadores_pais[e["pais"]] = contadores_pais.get(e["pais"], 0) + 1

mayores_edad = []
for e in estudiantes:
    if "pais" in e and "edad" in e:
        if e["edad"] >= 18:
            mayores_edad.append(e["nombre"])




print(f"""
=== ESTADISTICAS ===
Contadores por país: {contadores_pais}
Nombres de mayores de edad:" {mayores_edad}
Total de mayores de edad: {contador_mayores}
Total de menores de edad: {contador_menores}
Total de personas mexicanas: {contador_mexicanos}
Porcentaje de personas mexicanas: {porcentaje_mexicanos}%
""")
```

```,
"""
=============================================
===       RESPUESTA DE CONSOLA            ===
=============================================
=== ESTADISTICAS ===
Contadores por país: {'México': 3, 
'Argentina': 1, 'España': 1, 
'Chile': 1, 'Perú': 1, 'Colombia': 1, 
'Brasil': 1, 'Estados Unidos': 1}
Nombres de mayores de edad:" 
['Sofía Rodríguez', 'Lucía Gómez', 
'Miguel Sánchez', 'Ana García', 
'Diego Fernández', 'María Pérez', 
'Andrés Díaz']
Total de mayores de edad: 7
Total de menores de edad: 3
Total de personas mexicanas: 3
Porcentaje de personas mexicanas: 30.0%
=============================================
"""
```

---

## 🧪 Ejercicio Opcional 5: `05_menu_sobre_estructura_anidada.py`

---

## 🔢 1. Objetivo del ejercicio

* Crear un **menú interactivo** que permita al usuario consultar, filtrar y analizar una lista de diccionarios.
* Reforzar todo lo aprendido en esta clase: estructuras anidadas, validación, contadores, búsqueda, filtrado y presentación.
* Simular un sistema básico de navegación tipo **"sistema de usuarios" o "base de datos visual"**.
* Aplicar **pensamiento algorítmico completo** con entrada de usuario, flujo de control, condicionales, bucles y funciones de apoyo.

---

## 🔢 2. Teoría aplicada

### 📌 ¿Qué es un menú interactivo?

Un **menú interactivo** es una forma de presentar al usuario distintas opciones para **interactuar con un sistema**, usando entradas (input) y seleccionando rutas lógicas (if/elif/else).

---

### 🧠 Lógica que vas a entrenar

* Uso de `while True` + `break` para mantener el programa activo hasta que el usuario salga.
* Crear opciones como:

  * Ver todos los registros
  * Buscar personas por país
  * Contar cuántos cumplen una condición
  * Mostrar los mayores de edad
* Control de entradas y presentación profesional.

---

## 🔢 3. Ejemplo para comprender la lógica

```python
# Menú simulado
while True:
    print("\nMENÚ DE CONSULTA")
    print("1. Ver todas las personas")
    print("2. Mostrar solo los mayores de edad")
    print("3. Filtrar por país")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Mostrar todos
    elif opcion == "2":
        # Mostrar mayores
    elif opcion == "3":
        # Pedir país y filtrar
    elif opcion == "4":
        break
    else:
        print("Opción inválida")
```

---

## 🔽 4. Diagrama de flujo textual (nivel profesional)

```.
Inicio
↓
Definir lista de personas (diccionarios con "nombre", "edad", "pais")
↓
Iniciar bucle while True (menú persistente)
↓
Mostrar opciones:
├── 1. Ver todos los registros
├── 2. Mostrar mayores de edad
├── 3. Buscar por país
├── 4. Contar por país
├── 5. Salir
↓
Leer opción del usuario
↓
└── if opción == 1:
     └── Recorrer lista y mostrar todos los registros
↓
└── if opción == 2:
     ├── Recorrer lista
     └── Mostrar solo los que tienen edad >= 18
↓
└── if opción == 3:
     ├── Pedir país al usuario
     ├── Recorrer lista
     ├── Si coincide (usar .lower()), mostrar
     └── (🟥 Mejora opcional: contar cuántos coinciden)
↓
└── if opción == 4:
     ├── Crear diccionario contadores por país
     └── Mostrar resultado agrupado
↓
└── if opción == 5:
     └── break
↓
(🟥 Mejora opcional: validar claves antes de acceder)
↓
(🟥 Mejora opcional: convertir nombre y país en formato capitalizado al mostrar)
↓
Volver al menú (loop)
↓
Fin
```

---

## 🧱 05_menu_sobre_estructura_anidada.py

```python
# 05_menu_sobre_estructura_anidada.py

# Base de datos
personas = [
    {"nombre": "Carlos López", "edad": 17, "pais": "México"},
    {"nombre": "Sofía Rodríguez", "edad": 20, "pais": "Argentina"},
    {"nombre": "Juan Martínez", "edad": 16, "pais": "México"},
    {"nombre": "Lucía Gómez", "edad": 22, "pais": "España"},
    {"nombre": "Miguel Sánchez", "edad": 19, "pais": "México"},
    {"nombre": "Ana García", "edad": 24, "pais": "Chile"},
    {"nombre": "Valeria Torres", "edad": 15, "pais": "Perú"},
    {"nombre": "Diego Fernández", "edad": 21, "pais": "Colombia"},
    {"nombre": "María Pérez", "edad": 18, "pais": "Brasil"},
    {"nombre": "Andrés Díaz", "edad": 23, "pais": "USA"}
]

def recorrer_lista():
    for p in personas:
        for clave, valor in p.items():
            print(clave, ":", valor)
    print()  # Salto de línea adicional

def mayor_18():
    mayores = [p for p in personas if p["edad"] >= 18]
    if mayores:
        for p in mayores:
            print(p)
    else:
        print("😔 No hay personas mayores de edad en la lista.")
    print()  # Salto de línea adicional

def buscador_pais():
    pais_buscado = input("🌍 ¡Hola! ¿Qué país te gustaría buscar? ")
    if not pais_buscado:
        print("⚠️ Por favor, ingresa un país válido. 😊")
        return
    contador_pais = 0
    for p in personas:
        if "pais" in p and p["pais"].lower() == pais_buscado.lower():
            print(f"🎉 {p['nombre']} - {p['edad']} años - {p['pais']}")
            contador_pais += 1
    if contador_pais == 0:
        print("😕 No se encontraron coincidencias para ese país.")
    else:
        print(f"🌟 ¡Coincidencias totales encontradas: {contador_pais}!")
    print()  # Salto de línea adicional

def personas_por_pais():
    nuevo_dic = {}
    for p in personas:
        if "pais" in p:
            pais = p["pais"]
            nuevo_dic[pais] = nuevo_dic.get(pais, 0) + 1
    if nuevo_dic:
        print("🌎 Países y cantidades:")
        print("-" * 20)
        for pais, cantidad in sorted(nuevo_dic.items(), key=lambda x: x[1], reverse=True):
            print(f"{pais:<10} | {cantidad} persona(s) 🌐")
    else:
        print("😔 No hay datos de países disponibles.")
    print()  # Salto de línea adicional

opciones = {
    1: recorrer_lista,
    2: mayor_18,
    3: buscador_pais,
    4: personas_por_pais
}

print("🎉 ¡Bienvenido al Menú de Personas! 🌟\nExplora la base de datos con estas opciones divertidas:")
while True:
    print("\n=== MENÚ PRINCIPAL === 🌈")
    print("1. 📋 Ver todos los registros")
    print("2. 🎂 Mostrar mayores de edad")
    print("3. 🌍 Buscar por país")
    print("4. 📊 Ver conteo por país")
    print("Escribe 'salir' para terminar 😊")
    
    entrada = input("Selecciona una opción: ")
    
    if entrada.lower() == "salir":
        print("\n🙋‍♂️ ¡Gracias por usar el programa! ¡Hasta luego! 🌟")
        break
    
    try:
        numero = int(entrada)
        if numero in opciones:
            opciones[numero]()   # Llamar a la función correspondiente
        else:
            print("\n⚠️ Oops! Esa opción no existe, elige otra. 😄")
    except ValueError:
        print("\n⚠️ Uy! Ingresa un número o 'salir', por favor. 😊")
```

```..
"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
🎉 ¡Bienvenido al Menú de Personas! 🌟
Explora la base de datos con estas opciones divertidas:

=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 1
nombre : Carlos López
edad : 17
pais : México
nombre : Sofía Rodríguez
edad : 20
pais : Argentina
nombre : Juan Martínez
edad : 16
pais : México
nombre : Lucía Gómez
edad : 22
pais : España
nombre : Miguel Sánchez
edad : 19
pais : México
nombre : Ana García
edad : 24
pais : Chile
nombre : Valeria Torres
edad : 15
pais : Perú
nombre : Diego Fernández
edad : 21
pais : Colombia
nombre : María Pérez
edad : 18
pais : Brasil
nombre : Andrés Díaz
edad : 23
pais : USA


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 2
{'nombre': 'Sofía Rodríguez', 'edad': 20, 'pais': 'Argentina'}
{'nombre': 'Lucía Gómez', 'edad': 22, 'pais': 'España'}
{'nombre': 'Miguel Sánchez', 'edad': 19, 'pais': 'México'}
{'nombre': 'Ana García', 'edad': 24, 'pais': 'Chile'}
{'nombre': 'Diego Fernández', 'edad': 21, 'pais': 'Colombia'}
{'nombre': 'María Pérez', 'edad': 18, 'pais': 'Brasil'}
{'nombre': 'Andrés Díaz', 'edad': 23, 'pais': 'USA'}


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 3
🌍 ¡Hola! ¿Qué país te gustaría buscar? usa
🎉 Andrés Díaz - 23 años - USA
🌟 ¡Coincidencias totales encontradas: 1!


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: 4
🌎 Países y cantidades:
--------------------
México     | 3 persona(s) 🌐
Argentina  | 1 persona(s) 🌐
España     | 1 persona(s) 🌐
Chile      | 1 persona(s) 🌐
Perú       | 1 persona(s) 🌐
Colombia   | 1 persona(s) 🌐
Brasil     | 1 persona(s) 🌐
USA        | 1 persona(s) 🌐


=== MENÚ PRINCIPAL === 🌈
1. 📋 Ver todos los registros
2. 🎂 Mostrar mayores de edad
3. 🌍 Buscar por país
4. 📊 Ver conteo por país
Escribe 'salir' para terminar 😊
Selecciona una opción: salir

🙋‍♂️ ¡Gracias por usar el programa! ¡Hasta luego! 🌟
====================================================================
"""
```

---

## > 🏁 Clase 21 finalizada
