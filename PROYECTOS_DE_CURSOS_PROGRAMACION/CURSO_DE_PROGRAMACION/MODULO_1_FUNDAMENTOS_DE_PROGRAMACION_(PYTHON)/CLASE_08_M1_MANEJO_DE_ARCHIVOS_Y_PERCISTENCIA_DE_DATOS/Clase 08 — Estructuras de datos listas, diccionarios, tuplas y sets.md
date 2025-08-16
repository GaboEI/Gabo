# 🧮 Clase 08 — Estructuras de datos: listas, diccionarios, tuplas y sets (versión extendida)

---

## 🎯 Objetivo de la clase

Dominar el uso de las principales estructuras de datos en Python: **listas**, **diccionarios**, **tuplas** y **sets**. Aprender a manipular, acceder, iterar y modificar datos de manera eficiente y segura. Aplicar estos conocimientos en escenarios reales de desarrollo.

---

## 📚 Teoría profunda

Python provee estructuras de datos integradas que permiten almacenar y trabajar con colecciones de elementos. Cada estructura tiene propiedades particulares que las hacen más adecuadas según el caso de uso.

### 🟦 1. Listas (`list`)
- Ordenadas y mutables
- Pueden contener elementos duplicados
- Indexadas

```python
frutas = ["manzana", "pera", "uva"]
```

#### Métodos útiles:
- `.append(x)`, `.remove(x)`, `.insert(i, x)`, `.pop()`, `.sort()`, `.reverse()`

### 🟨 2. Diccionarios (`dict`)
- No ordenados (hasta Python 3.6), mutables
- Almacenan pares clave-valor

```python
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
```

#### Métodos útiles:
- `.get(clave)`, `.keys()`, `.values()`, `.items()`, `.update()`

### 🟥 3. Tuplas (`tuple`)
- Ordenadas e inmutables
- Usadas cuando los datos no deben cambiar

```python
coordenadas = (10, 20)
```

#### Propiedades:
- Menor uso de memoria
- Se puede desempaquetar fácilmente

### 🟩 4. Conjuntos (`set`)
- No ordenados, sin elementos duplicados
- Muy rápidos para comprobación de pertenencia

```python
colores = {"rojo", "verde", "azul"}
```

#### Operaciones útiles:
- `.add(x)`, `.discard(x)`, `.union()`, `.intersection()`, `.difference()`

---

## 💡 Aplicaciones profesionales

- Listas: procesamiento de colecciones de datos como productos, clientes, resultados.
- Diccionarios: almacenamiento estructurado de información (como JSON o registros).
- Tuplas: coordenadas, configuraciones inmutables, constantes múltiples.
- Sets: eliminación de duplicados, comparación rápida de pertenencia.

---

## 🧪 Ejercicios prácticos

---

### ✍️ 01_listado_de_tareas.py

**🎯 Objetivo:** Crear, modificar y mostrar una lista de tareas pendientes del usuario.

#### 🧭 Diagrama de flujo
```
Inicio
↓
Crear lista vacía
↓
Agregar varias tareas con append()
↓
Eliminar una tarea con remove()
↓
Ordenar lista
↓
Mostrar lista final
↓
Fin
```

#### ✅ Código realizado
```python
tareas = []
tareas.append("Estudiar Python")
tareas.append("Leer un libro")
tareas.append("Hacer ejercicio")

tareas.remove("Leer un libro")
tareas.sort()

print("📋 Tareas pendientes:")
for t in tareas:
    print("-", t)
```

---

### ✍️ 02_informacion_de_usuario.py

**🎯 Objetivo:** Utilizar un diccionario para almacenar y mostrar los datos de un usuario.

#### 🧭 Diagrama de flujo
```
Inicio
↓
Crear diccionario con claves: nombre, edad, ciudad
↓
Acceder a valores por clave
↓
Mostrar mensaje personalizado
↓
Fin
```

#### ✅ Código realizado
```python
usuario = {
    "nombre": "Laura",
    "edad": 28,
    "ciudad": "Bogotá"
}

print(f"👤 Usuario: {usuario['nombre']}, {usuario['edad']} años, vive en {usuario['ciudad']}.")
```

---

### ✍️ 03_coordenadas_gps.py

**🎯 Objetivo:** Usar una tupla para representar coordenadas geográficas.

#### 🧭 Diagrama de flujo
```
Inicio
↓
Definir tupla con latitud y longitud
↓
Desempaquetar tupla
↓
Mostrar coordenadas formateadas
↓
Fin
```

#### ✅ Código realizado
```python
coordenadas = (4.6097, -74.0818)  # Bogotá
latitud, longitud = coordenadas
print(f"📍 Ubicación: Latitud {latitud}, Longitud {longitud}")
```

---

### ✍️ 04_colores_unicos.py

**🎯 Objetivo:** Mostrar solo los colores únicos usando un set.

#### 🧭 Diagrama de flujo
```
Inicio
↓
Crear lista con colores repetidos
↓
Convertir a set para eliminar duplicados
↓
Mostrar conjunto resultante
↓
Fin
```

#### ✅ Código realizado
```python
colores = ["rojo", "azul", "rojo", "verde", "azul"]
colores_unicos = set(colores)
print("🎨 Colores únicos:", colores_unicos)
```

---

## 🧾 Cierre de la clase

Dominar las estructuras de datos es clave para todo programador. Saber cuándo usar cada una te permite escribir código más limpio, más rápido y más escalable. Son la base de estructuras más complejas como pilas, colas, árboles y bases de datos.

---

## 🧠 Evaluación simbólica

🔹 Estructuras cubiertas: ✅ 4 (listas, diccionarios, tuplas, sets)
🔹 Aplicación profesional: ✅ Incluida
🔹 Ejercicios resueltos con diagramas: ✅ 4
🔹 Buenas prácticas de sintaxis: ✅ Mantenidas
🔹 Nota simbólica: **10.25/10**

📘 **Clase completamente documentada. ¡Listísima para GitHub, Gabo! 🚀**

