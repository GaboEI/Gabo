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

### 🧩 DIAGRAMAS DE FLUJO — ESTILO GABO

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
