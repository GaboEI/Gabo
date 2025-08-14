# 🎓 **CLASE EXTRA JS 2.1 – CONSOLA AVANZADA**

---

## 🧠 1. ¿Por qué esta clase?

Hasta ahora se ha usado:

* `console.log()` para imprimir resultados
* `console.warn()` y `console.error()` para detectar errores
* `console.clear()` para limpiar el entorno

👉 Pero la consola tiene mucho más poder cuando estás depurando estructuras complejas, funciones anidadas o procesos que cambian en el tiempo.

Aquí entran en juego:

* `console.table()` → para representar **datos estructurados**
* `console.group()` / `console.groupEnd()` → para **organizar jerárquicamente la salida**
* `console.trace()` → para **detectar el orden de ejecución** de funciones o eventos

---

## 🔍 2. `console.table()` – Visualización estructurada

### 📘 Definición

```js
console.table(data);
```

> Muestra arrays u objetos **en forma de tabla**, con columnas y filas legibles.

### 🎯 ¿Cuándo se usa?

* Cuando trabajas con arrays de objetos (por ejemplo: usuarios, productos, tareas)
* Cuando quieres depurar qué contiene una estructura anidada
* Cuando necesitas **visualizar relaciones de datos** (índices, claves, valores)

---

### 🧪 Ejemplo mínimo

```js
const usuarios = [
  { nombre: "Ana", edad: 28 },
  { nombre: "Luis", edad: 34 },
  { nombre: "Carlos", edad: 41 }
];

console.table(usuarios);
```

### 📊 Salida en consola

| (index) | nombre | edad |
| ------- | ------ | ---- |
| 0       | Ana    | 28   |
| 1       | Luis   | 34   |
| 2       | Carlos | 41   |

---

## 📘 3. `console.group()` y `console.groupEnd()` – Jerarquía visual

### 📤 Definición

```js
console.group("Inicio");
  console.log("Dentro del grupo");
  console.group("Subgrupo");
    console.log("Dentro del subgrupo");
  console.groupEnd();
console.groupEnd();
```

> Crea una estructura visual **anidada** para depurar múltiples pasos de un proceso o agrupar partes del flujo.

### 📤 ¿Cuándo se usa?

* Cuando tu proceso tiene **subetapas**
* Cuando estás **depurando loops, validaciones o procesos de carga**
* Para **colapsar grupos** en la consola de navegador (mejor organización)

---

### 💡 Ejemplo real

```js
console.group("💼 Validación de usuario");
console.log("→ Validar email");
console.log("→ Validar contraseña");
console.groupEnd();
```

🔍 Esto se ve como una **sección expandible** en DevTools, y muy limpio en Node.js.

---

## 🧠 4. `console.trace()` – Seguimiento de flujo

### Definición

```js
console.trace("📍 Trazando llamada");
```

> Muestra la **pila de llamadas** (call stack) que llevó hasta ese punto del código.

### ¿Cuándo se usa?

* Cuando una función es llamada **desde muchas partes**
* Cuando algo inesperado ocurre y quieres **ver desde dónde fue llamado**
* Cuando estás depurando **eventos, errores o recursión**

---

### 🧪 Ejemplo típico

```js
function saludar() {
  console.trace("📍 Se llamó a saludar()");
}

function iniciar() {
  saludar();
}

iniciar();
```

🔎 La consola mostrará el recorrido completo:

```js
📍 Se llamó a saludar()
    at saludar (<archivo>:2)
    at iniciar (<archivo>:6)
    at <global>
```

Esto es **clave para depuración profesional**, sobre todo en proyectos reales con múltiples archivos y funciones.

---

## 🧭 DIAGRAMA DE FLUJO GENERAL

```js
Inicio
↓
¿Estoy depurando datos estructurados?
├── Sí → usar console.table()
↓
¿Quiero agrupar visualmente procesos o etapas?
├── Sí → usar console.group() y groupEnd()
↓
¿Necesito saber quién llamó a esta función?
├── Sí → usar console.trace()
↓
Mostrar datos con console.log(), warn(), error() según el contexto
↓
Fin
```

---

## 💼 APLICACIÓN PROFESIONAL

| Escenario real                      | Herramienta ideal |
| ----------------------------------- | ----------------- |
| Ver usuarios, productos, resultados | `console.table()` |
| Depurar flujos con pasos internos   | `console.group()` |
| Detectar llamadas inesperadas       | `console.trace()` |
| Depuración avanzada en entrevistas  | TODAS combinadas  |

---

## 🧩 ¿Qué es un `array` en JavaScript?

> Un **array** es una **estructura de datos ordenada y indexada**, que permite almacenar múltiples valores en una sola variable.

📦 Puedes imaginarlo como una **caja con compartimentos**, donde cada valor tiene un número (índice) asignado automáticamente.

---

### 📘 Sintaxis básica

```js
let frutas = ["manzana", "banana", "naranja"];
```

Esto crea un array con 3 elementos. Cada uno se puede acceder así:

```js
console.log(frutas[0]); // "manzana"
console.log(frutas[2]); // "naranja"
```

---

### 🔄 Comparación con Python

| Concepto         | JavaScript          | Python                |
| ---------------- | ------------------- | --------------------- |
| Tipo             | `array` (`[]`)      | `list` (`[]`)         |
| Índices          | 0-based             | 0-based               |
| Métodos comunes  | `.push()`, `.pop()` | `.append()`, `.pop()` |
| Tipo heterogéneo | Sí                  | Sí                    |

📌 En ambos lenguajes puedes tener:

```\\
let mezcla = [42, "hola", true]; // JS
mezcla = [42, "hola", True]      # Python
```

Peeeero en JS **los arrays son más versátiles** para el frontend, ya que se usan para **estructuras dinámicas, eventos, renderizado visual, filtros, etc.**. Por eso son protagonistas en muchas APIs y proyectos reales.

---

## 📊 ¿Por qué se menciona tanto?

Porque métodos como:

* `console.table()` → brillan cuando usas arrays de objetos
* `console.group()` → es útil cuando recorres arrays
* `console.trace()` → puede rastrear funciones que procesan arrays

---

¡Perfecto, Gabo! 🧠
Entramos ahora a la práctica profesional con el **Ejercicio 1** de esta Clase Extra JS 2.1.
Vamos a aplicar `console.table()` con datos estructurados y visualización realista.

---

## 🧪 EJERCICIO 1 – `01_visualizarEstructuraConTable.js`

---

## 🧠 1. Teoría

### 🧾 Tema central

Uso de `console.table()` para representar visualmente estructuras complejas de datos (arrays de objetos).

### 📌 Objetivo

* Crear una estructura de datos realista (como un catálogo de productos o una lista de usuarios).
* Mostrarla en la consola con `console.table()` para facilitar la depuración o presentación visual.
* Agregar al menos una propiedad booleana o numérica que pueda cambiar (por ejemplo: "activo", "en stock", "puntaje").

---

## 💡 2. Ejemplo mínimo ilustrativo (NO usarlo en tu ejercicio, solo para entender)

```js
const frutas = [
  { nombre: "Manzana", color: "Rojo", stock: 12 },
  { nombre: "Banana", color: "Amarillo", stock: 8 }
];

console.table(frutas);
```

---

## 🧭 3. Diagrama de flujo (formato Gabo)

```js
Inicio
↓
Crear array de objetos con al menos 4 elementos
↓
Cada objeto debe tener al menos 3 propiedades:
├── Texto (nombre, tipo, etc.)
├── Número (stock, precio, edad, etc.)
└── Booleano o estado (activo, disponible, etc.)
↓
Mostrar toda la estructura con console.table()
↓
Cierre
```

---

## 📁 4. Esqueleto guía (sin resolver)

```js
// Ejercicio 1: VISUALIZAR ESTRUCTURA CON TABLE

const ventaLibros = [
    {nombre: "Anatomía de las expresiones faciales", precio: 1550, disponible: true},
    {nombre: "El cuerpo se cura a sí mismo", precio: 550, disponible: false},
    {nombre: "Forma de la cabeza y el cuello", precio: 1550, disponible: true},
    {nombre: "Atlas clínico de puntos gatillo",precio: 1000, disponible: false},
    {nombre: "Atlas de Tricoscopia", precio: 1800, disponible: false}
];
const ventaLibrosconIndice = ventaLibros.map((ventaLibros, index) => ({
    No: index + 1,
    nombre: ventaLibros.nombre,
    precio: ventaLibros.precio,
    disponible: ventaLibros.disponible ? "Disponible" : "No disponible"
}));
console.table(ventaLibrosconIndice)

/* RESPUESTA DE CONSOLA ENBEVIDA 

┌─────────┬────┬────────────────────────────────────────┬────────┬─────────────────┐
│ (index) │ No │ nombre                                 │ precio │ disponible      │
├─────────┼────┼────────────────────────────────────────┼────────┼─────────────────┤
│ 0       │ 1  │ 'Anatomía de las expresiones faciales' │ 1550   │ 'Disponible'    │
│ 1       │ 2  │ 'El cuerpo se cura a sí mismo'         │ 550    │ 'No disponible' │
│ 2       │ 3  │ 'Forma de la cabeza y el cuello'       │ 1550   │ 'Disponible'    │
│ 3       │ 4  │ 'Atlas clínico de puntos gatillo'      │ 1000   │ 'No disponible' │
│ 4       │ 5  │ 'Atlas de Tricoscopia'                 │ 1800   │ 'No disponible' │
└─────────┴────┴────────────────────────────────────────┴────────┴─────────────────┘

*/
```

---

## 🧪 EJERCICIO 2 – `02_rastrearProcesoConGroup.js`

---

## 1. Teoría

### 📌 Tema central

Uso de `console.group()` y `console.groupEnd()` para **visualizar flujos jerárquicos** de procesos en consola.

### 🎯 Objetivo

* Simular un proceso de validación, compra, carga, etc., con **subpasos internos**
* Agrupar las etapas de forma **anidada y organizada visualmente**
* Incluir mensajes de `log()`, `warn()`, etc., **dentro de los grupos**

---

## 💡 2. Ejemplo mínimo ilustrativo (NO usar en tu solución)

```js
console.group("🔍 Validación de usuario");
console.log("→ Verificando email");
console.log("→ Verificando contraseña");
console.groupEnd();
```

Esto genera un bloque visual **plegable** en DevTools (o con indentación en Node), muy útil en flujos complejos.

---

## 💥 3. Diagrama de flujo (formato Gabo)

```/
Inicio
↓
Crear función principal (por ejemplo: procesarPedido o registrarUsuario)
↓
Dentro de esa función:
├── Abrir console.group("Inicio del proceso")
│   ↓
│   Mostrar log de inicio
│   ↓
│   Abrir subgrupo con console.group("Subproceso X")
│   ├── Mostrar acciones dentro
│   └── Cerrar subgrupo
│   ↓
│   Mostrar mensaje de cierre
└── Cerrar grupo principal
↓
Llamar a la función
↓
Fin
```

---

## 💥 4. Esqueleto guía (sin resolver)

```js
// EJERCICIO 2: RASTREAR PROCESO CON GROUP

function procesarPedido() {
    console.group("🛒 Inicio del pedido");

    console.log("🔍 Validar id del producto");
    console.log("✍️ Validar stock del producto en el almacén");
    console.log("📤 Validar sistema de logística");

    console.group("📦 Preparación del producto");
    console.log("🔖 Etiquetar producto");
    console.log("📏 Verificar dimensiones y peso");
    console.log("📦 Empaquetar producto");
    console.groupEnd();

    console.log("✅ Pedido procesado con éxito");

    console.groupEnd();
}

procesarPedido();

/* 
=================================================
RESPUESTA DE CONSOLA ENBEVIDA 
=================================================
node 02_rastrearProcesoConGroup.js
🛒 Inicio del pedido
    🔍 Validar id del producto
    ✍️ Validar stock del producto en el almacén
    📤 Validar sistema de logística
📦 Preparación del producto
    🔖 Etiquetar producto
    📏 Verificar dimensiones y peso
    📦 Empaquetar producto
    ✅ Pedido procesado con éxito
=================================================  
*/
```

---

## 🧪 EJERCICIO 3 – `03_seguirFlujoConTrace.js`

---

## ✍️ 1. Teoría

### 📘 Tema central

Uso de `console.trace()` para mostrar el **rastro de llamadas** que llevaron a ejecutar una función o instrucción específica.

### Objetivo

* Crear una cadena de funciones anidadas.
* Invocar una de ellas que, al ejecutarse, dispare un `console.trace()`.
* Observar en la consola el **stack de ejecución completo** (call stack).

---

## 💡 2. Ejemplo mínimo ilustrativo (NO usar en tu ejercicio)

```js
function c() {
  console.trace("📍 Trazando en c()");
}

function b() {
  c();
}

function a() {
  b();
}

a();
```

📌 Esto te mostrará el orden exacto de llamadas: `a()` → `b()` → `c()` → `trace`.

---

## 3. Diagrama de flujo (formato Gabo)

```.
Inicio
↓
Definir función A → llama a B
↓
Definir función B → llama a C
↓
Definir función C → ejecuta console.trace()
↓
Invocar función A (inicio del rastro)
↓
Consola muestra orden exacto de ejecución
↓
Fin
```

---

## 4. Esqueleto guía (sin resolver)

```js
// EJERCICIO 3: SEGUIR FLUJO CON TRACE:

function analizarProceso() {
    verificarDato();
}

function verificarDato() {
    ejecutarTarea();
}

function ejecutarTarea() {
    console.trace("📍 Trazando la ejecución del programa hasta aquí");
}

analizarProceso();

/* 
=================================================================================
RESPUESTA DE CONSOLA ENBEVIDA (las dirercciones fueron abreviadas manualmente )
=================================================================================
node 03_seguirFlujoConTrace.js
Trace: 📍 Trazando de la ejecucion del programa hasta aqui
    at ejecutarTarea (...js:12:13)
    at verrificarDatod (...js:8:5)
    at analizarProceso (...js:4:5)
    at Object.<anonymous> (...js:15:1)
    at Module._compile (node:internal/modules/cjs/loader:1688:14)
    at Object..js (node:internal/modules/cjs/loader:1820:10)
    at Module.load (node:internal/modules/cjs/loader:1423:32)
    at Function._load (node:internal/modules/cjs/loader:1246:12)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)
=================================================================================  
*/
```

---

🧪 Requisitos:

* Usa al menos 3 funciones encadenadas
* El mensaje en `console.trace()` debe explicar qué se está rastreando
* Comentarios claros, visualmente ordenado, estructura limpia

---

✅ ¡Clase Extra JS 2.1 cerrada y registrada oficialmente.

---

## 🧾 RESUMEN PEDAGÓGICO DE LA CLASE EXTRA JS 2.1

| Herramienta       | Dominio demostrado                               |
| ----------------- | ------------------------------------------------ |
| `console.table()` | ✔️ Visualización estructurada de datos           |
| `console.group()` | ✔️ Jerarquía de procesos en consola              |
| `console.trace()` | ✔️ Call stack para seguimiento real de funciones |

🟢 Todas las herramientas fueron explicadas, practicadas, ejecutadas, documentadas y evaluadas con rigor.
Tu participación fue impecable en cada paso. **Esto no es jugar a programar: esto es desarrollar con nivel.**

---
