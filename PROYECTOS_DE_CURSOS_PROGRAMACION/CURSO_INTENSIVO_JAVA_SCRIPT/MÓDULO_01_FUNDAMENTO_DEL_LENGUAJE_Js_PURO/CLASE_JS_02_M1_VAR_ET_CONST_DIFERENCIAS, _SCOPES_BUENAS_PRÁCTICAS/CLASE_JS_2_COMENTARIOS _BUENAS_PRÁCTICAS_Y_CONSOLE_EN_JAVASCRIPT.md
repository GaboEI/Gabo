# 🎓 **COMENTARIOS, BUENAS PRÁCTICAS Y USO PROFESIONAL DE `CONSOLE`**

---

## 🧠 1. COMENTARIOS EN JAVASCRIPT

---

## 🔤 ¿Qué es un comentario?

Un **comentario** es una parte del código que el intérprete de JavaScript **ignora por completo**. Su propósito es ayudar a los programadores (presentes y futuros) a **comprender mejor el código**.

No tienen impacto en la ejecución. Son como notas escritas en los márgenes de un libro 📓.

---

## ✍️ Sintaxis oficial

JavaScript soporta dos tipos de comentarios:

```js
// 1️⃣ Comentario de una sola línea

/*
2️⃣ Comentario
   de múltiples líneas
*/
```

---

### 🎯 ¿Cuándo usar cada uno?

| Tipo    | Uso recomendado                                                        |
| ------- | ---------------------------------------------------------------------- |
| `//`    | Para comentarios breves o aclaraciones puntuales                       |
| `/* */` | Para documentar bloques de código, encabezados o anotaciones complejas |

---

## 🧱 Buenas prácticas profesionales

⚠️ **Comentar mal puede ser peor que no comentar.** Un mal comentario genera confusión, repite lo obvio o se vuelve obsoleto.

### ✅ Comentarios útiles

```js
// 1️⃣ Calcula el precio final con descuento aplicado
let precioFinal = precioBase * 0.9;
```

### ❌ Comentarios inútiles

```js
// 1️⃣ Multiplica por 0.9
let precioFinal = precioBase * 0.9; // ← Esto ya es evidente
```

---

## 🛑 ¿Cuándo NO comentar?

* No comentes lo obvio o lo que ya se entiende leyendo el código.
* No expliques qué hace una función línea por línea si su nombre lo dice todo.
* No uses comentarios como excusa para tener un código desordenado.

---

## 💼 Estilo profesional recomendado

🔸 Usa **verbos activos**: “Calcula”, “Verifica”, “Devuelve”, “Inicializa”…
🔸 Siempre en **presente**: "Comprueba si el usuario es admin", no "Este bloque comprobaba…"
🔸 **Evita sarcasmo, emojis o jergas** si estás trabajando en equipo (profesionalismo ante todo).
🔸 Usa tu comentario como una guía útil para quien **no escribió tu código**.

---

## 📦 2. USO PROFESIONAL DE `console`

---

## 🧮 ¿Qué es `console`?

`console` es un objeto global en los entornos de ejecución de JavaScript (como navegadores o Node.js) que ofrece **métodos de depuración y diagnóstico**.

### 🔎 Traducción real: `console` es una **herramienta de comunicación entre el programador y el entorno**

---

## 🔧 Métodos clave de `console`

| Método                                   | Descripción                                                  |
| ---------------------------------------- | ------------------------------------------------------------ |
| `console.log()`                          | Muestra un mensaje general o valor                           |
| `console.warn()`                         | Muestra una advertencia visual (amarilla) ⚠️                 |
| `console.error()`                        | Muestra un error (rojo) ❌                                    |
| `console.info()`                         | Mensaje informativo (similar a `log`) ℹ️                     |
| `console.clear()`                        | Limpia la consola completamente                              |
| `console.table()`                        | Muestra datos tabulares (arrays/objetos) en formato de tabla |
| `console.group()` / `console.groupEnd()` | Agrupa mensajes de forma jerárquica                          |

---

### 📌 Ejemplo: Diferencia entre `log`, `warn` y `error`

```js
console.log("Todo normal aquí");
console.warn("¡Cuidado! Algo no se ve bien");
console.error("¡Error crítico detectado!");
```

---

### 🧪 Bonus: `console.table()`

```js
const usuarios = [
  { nombre: "Ana", edad: 28 },
  { nombre: "Luis", edad: 34 }
];

console.table(usuarios);
```

🔍 Esto mostrará los datos en una **tabla clara y legible** en la consola.

---

## 🎯 Buenas prácticas con `console`

* Usa `console.log()` para rastrear valores **durante el desarrollo**, pero **no lo dejes en producción.**
* Prefiere `console.warn()` o `console.error()` para **marcar errores visuales claros**.
* Evita usar `console` como una forma perezosa de no validar errores o excepciones.
* Usa `console.clear()` para limpiar el entorno al reiniciar una función compleja.
* Utiliza `console.table()` para depurar arrays de objetos, especialmente en estructuras de datos.

---

## 🧠 Errores comunes a evitar

| Error                                | Consecuencia                                                    |
| ------------------------------------ | --------------------------------------------------------------- |
| Usar `console.log()` en todos lados  | Pierdes la distinción entre info, advertencia y error           |
| Dejar logs en producción             | Puede exponer datos sensibles o ensuciar la consola del usuario |
| No limpiar la consola                | Puede hacerte perder información útil durante el debugging      |
| No usar `table` con arrays complejos | Dificulta leer la estructura de datos                           |

---

## 💻 Diagrama de flujo del uso de comentarios y consola

```,
Inicio
↓
¿Código ya es claro por sí mismo?
├── Sí → No comentes (mantén limpio)
└── No ↓
  ¿Comentario aporta valor o contexto real?
  ├── No → No lo pongas
  └── Sí ↓
     ¿Es sobre un error o advertencia?
     ├── Sí → Usa console.warn() o console.error()
     └── No ↓
        ¿Quieres ver la estructura?
        ├── Sí → Usa console.table()
        └── No → Usa console.log()
↓
¿Ya terminaste de depurar?
├── Sí → Limpia con console.clear()
└── No → Continúa probando ↓
↓
Fin
```

---

## 📌 Aplicación profesional real

* En entrevistas técnicas, saber **cuándo y cómo usar `console`** demuestra madurez como programador.
* En debugging profesional, `console.warn()` permite **marcar errores suaves sin romper el flujo**.
* En proyectos reales, **documentar el "por qué" de una lógica compleja con comentarios** puede evitar bugs años después.
* En trabajo en equipo, los buenos comentarios son una forma de comunicación asincrónica.

---

## 📘 ¿Qué es una variable en JavaScript?

Una **variable** es un contenedor que guarda un valor.
En JavaScript moderno, se declaran con `let` o `const`.

```js
let nombre = "Gabo"; // Puedes cambiar su valor luego
const pi = 3.1416;    // No puedes cambiarlo
```

---

### 🧪 ¿Cómo se hace una operación?

```js
let precioBase = 100;
let impuesto = precioBase * 0.18;
```

Esto **multiplica** el valor de `precioBase` por `0.18` y guarda el resultado en `impuesto`.

---

### 📤 ¿Cómo se muestra un resultado?

```js
console.log(impuesto);
```

O más profesional:

```js
console.log("El impuesto es:", impuesto);
```

---

### 💡 Mini ejemplo completo

```js
let precioBase = 100;
let impuesto = precioBase * 0.18;
let total = precioBase + impuesto;

console.log("Precio base:", precioBase);
console.log("Impuesto (18%):", impuesto);
console.log("Precio final:", total);
```

Esto imprime:

```js
Precio base: 100
Impuesto (18%): 18
Precio final: 118
```

## 📄 index.html explicado línea por línea

Este archivo HTML está diseñado para ejecutar código JavaScript en el navegador y entender **qué hace cada parte de su estructura**. Aquí no copiamos sin pensar: **cada línea tiene un propósito claro**. Vamos a analizarla desde la raíz.

---

## ✅ Código completo

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Escribe un texto (No se muestra en la web)</title>
</head>
<body>
  <h1>Escribe un texto (Se verá en la página como texto grande)</h1>

  <script src="nombreDelArchivo.js"></script>
</body>
</html>
```

---

## 🔍 Explicación línea por línea

## `<!DOCTYPE html>`  

Declara que el documento es HTML5. Es obligatoria y debe ir al inicio.

## `<html lang="es">`  

Etiqueta raíz del documento. El atributo `lang="es"` indica que el contenido está en español.

## `<head> ... </head>`

Sección invisible para el usuario. Aquí se configuran metadatos, título, codificación, enlaces a estilos y scripts.

## `<meta charset="UTF-8">`

Define la codificación del texto para soportar acentos, ñ, emojis, etc. Fundamental para evitar errores de caracteres.

## `<title>Escribe un texto (No se muestra en la web)</title>`

Título de la pestaña del navegador. No se muestra dentro de la página.

## `<body> ... </body>`  

Todo el contenido visible va dentro del `<body>`. Aquí se colocan encabezados, párrafos, botones, imágenes, etc.

## `<h1>Escribe un texto (Se verá en la página como texto grande)</h1>`

Encabezado de nivel 1 que da una instrucción al usuario. Se verá en la página como texto grande.

## `<script src="nombreDelArchivo.js"></script>`  

Esta línea es la clave: **carga tu archivo JavaScript** y lo ejecuta al cargar la página.  
`src="..."` indica el nombre del archivo que quieres ejecutar.

## `</html>`

Cierra el documento HTML.

---

## 🧭 Resumen estructural

```,
<!DOCTYPE html>         → Tipo de documento
<html>                  → Inicio del HTML
  <head>                → Configuración del documento
    <meta>              → Codificación de texto
    <title>             → Título de la pestaña
  </head>
  <body>                → Zona visible
    <h1>                → Encabezado visible
    <script>            → Carga y ejecuta JS
  </body>
</html>                 → Cierre del documento
```

---

---

## 💥 Recomendaciones para ejecutarlo

* Abre este archivo en el navegador (Chrome)
* Presiona `F12` y ve a la pestaña **"Consola"**
* Asegúrate de que el archivo `.js` esté en la misma carpeta.

---

## 🔧 EJERCICIO 1 `01_comentar_codigo_depurado.js`

---

### 🎯 Objetivo

Crear un pequeño script funcional que **calcule el precio final de un producto** aplicando un impuesto (18%), **comentando cada línea de forma profesional**.

---

### 📘 Lógica aplicada

* Definir el precio base
* Calcular el impuesto (18% del precio)
* Sumar el impuesto al precio base
* Mostrar cada paso con `console.log()`
* Comentar **qué hace cada línea**, pero sin repetir lo obvio

---

### 🧭 DIAGRAMA DE FLUJO

```js
Inicio
↓
Definir el precio base del producto
↓
Calcular el impuesto (precio * 0.18)
↓
Sumar impuesto al precio base para obtener precio final
↓
Mostrar todos los valores con console.log()
↓
Agregar comentarios útiles que expliquen la intención de cada línea
↓
Fin
```

---

## 🧱 ESQUELETO GUÍA COMENTADO (sin resolver)

```js
//! EJERCICIO 1: COMENTAR CÓDIGO DEPURADO
//============================================================================//
/* 🎯 Objetivo:
Crear un script que calcule el precio final de un producto aplicando un impuesto del 18%,
con comentarios profesionales para cada línea.

📘 Lógica aplicada:
- Definir el precio base del producto.
- Calcular el impuesto (18% del precio base).
- Sumar el impuesto al precio base para obtener el precio final.
- Mostrar cada paso en la consola con formato claro.
*/

// Definir el precio base del producto
let precioBase = 8000;

// Calcular el impuesto (18% del precio base)
let impuesto = precioBase * 0.18;

// Calcular el precio final sumando el precio base y el impuesto
let precioFinal = precioBase + impuesto;

// Mostrar resultados en la consola con formato claro
console.log("------------------------");
console.log("       RESULTADOS       ");
console.log("------------------------");
console.log("Precio Base: " + precioBase);
console.log("Impuesto (18%): " + impuesto);
console.log("Precio Final: " + precioFinal);
console.log("------------------------")

//============================================================================//
/* RESULTADOS DE CONSOLA AL EJECUTAR EL SCRIPT:
------------------------
       RESULTADOS       
------------------------
Precio Base: 8000
Impuesto (18%): 1440
Precio Final: 9440
------------------------
*/
//============================================================================///
```

---

🧠 **EJERCICIO 2 – `02_comentarios_utiles_vs_inutiles.js`**

---

## ✅ 1. TEORÍA PUNTUAL DEL CONCEPTO

### 📘 Tema: Comentarios útiles vs inútiles

Los **comentarios útiles** son aquellos que:

* Explican *el porqué* de una decisión, no *el qué* ya evidente en el código.
* Ayudan a futuros lectores (incluyéndote a ti mismo) a entender la intención o la lógica detrás.
* Se usan para aclarar partes no triviales, *no para repetir lo obvio*.

Por el contrario, los **comentarios inútiles**:

* Repiten lo que ya dice el código.
* Añaden ruido en lugar de claridad.
* En proyectos reales, son considerados **un mal hábito profesional**.

---

### 🧩 Regla de oro

> **Comenta lo necesario para entender lo que no es obvio.**
> Lo evidente en el código bien escrito **no necesita explicación.**

---

## 🧪 2. EJEMPLO MÍNIMO

```js
// ❌ Inútil
let x = 5; // Declara x con valor 5

// ✅ Útil
let impuesto = precio * 0.18; // Aplica el 18% correspondiente al IVA vigente
```

En el primer caso, el comentario **no aporta nada**.
En el segundo, **el comentario explica el contexto real del 0.18**, que no es evidente solo mirando el número.

---

## 🧭 3. DIAGRAMA DE FLUJO

```js
Inicio
↓
Escribir una función o bloque simple de código
↓
Comentar cada línea primero con comentarios inútiles (tipo novato)
↓
Luego reescribir la misma lógica con comentarios útiles (tipo profesional)
↓
Comparar y reflexionar sobre ambos estilos
↓
Fin
```

---

## 🧱 4. ESQUELETO GUÍA COMENTADO (sin resolución)

```js
// EJERCICIO 2 - Comentarios Útiles vs. Inútiles

// 1️⃣ Bloque con comentarios inútiles

// Variables para realizar una división
let numero1 = 8000; // Variable que almacena el dividendo
let numero2 = 2; // Variable que almacena el divisor

// Calcula la división de numero1 entre numero2
let resultado = numero1 / numero2;

// Muestra el resultado en la consola
console.log(resultado);

// 2️⃣ Bloque con comentarios útiles

// Cálculo del precio final de un producto con descuento
let valorInicial = 125; 
let descuento = valorInicial * 18 / 100; // 18% de descuento
let precioFinal = valorInicial - descuento; 

console.log("El precio final a pagar es: " + precioFinal);

/* Reflexión:
El primer bloque incluye comentarios redundantes que repiten 
lo que el código ya hace evidente, lo que lo hace menos claro. 
El segundo bloque utiliza comentarios concisos y útiles, 
explicando el propósito de las variables y operaciones, logrando 
mayor limpieza y claridad.
*/

/*RESPUESTA DE CONSOLA ENBEVIDA
4000
El precio final a pagar es: 147.5
*/
```

---

🧠 **EJERCICIO 3 – `03_manejo_de_console_log.js`**

---

## 🟨 1. TEORÍA PUNTUAL DEL CONCEPTO

### 📘 Tema: Uso profesional de `console.log()` en scripts funcionales

#### 🔍 ¿Qué es `console.log()`?

Es un método del objeto `console` que permite **mostrar información en la consola** del navegador o de Node.js. Se utiliza para:

* Ver valores de variables
* Rastrear el flujo de ejecución
* Comprobar resultados intermedios
* Depurar errores o validar lógica

---

### 🎯 ¿Por qué es importante dominar `console.log()`?

Porque durante las primeras fases de desarrollo (y aún como profesional), `console.log()` es tu forma más directa de:

* Comunicarte con el código
* Confirmar que todo funciona como esperas
* Presentar datos de forma comprensible

Pero si se usa mal, se vuelve confuso, repetitivo o inútil.

---

## ✅ 2. EJEMPLO MÍNIMO

❌ Mal uso (mensaje poco claro):

```js
console.log(x);
```

✅ Buen uso (contexto + claridad):

```js
console.log("Edad del usuario:", edad);
```

✅ Mejor aún (encabezado visual):

```js
console.log("==== RESULTADOS DE CÁLCULO ====");
console.log("Área total:", area);
console.log("Volumen total:", volumen);
```

---

## ✅ 3. DIAGRAMA DE FLUJO

```,
Inicio
↓
Definir tres números (pueden ser notas, edades, etc.)
↓
Calcular el promedio entre ellos
↓
Usar console.log() para mostrar:
├── Cada número original (con mensaje claro)
├── El total sumado (opcional)
└── El promedio final
↓
Incluir separadores visuales si es necesario
↓
Fin
```

---

## ✅ 4. ESQUELETO GUÍA COMENTADO (sin resolver)

📂 Nombre del archivo: `03_manejo_de_console_log.js`

```js
// EJERCICIO 3 – Manejo profesional de console.log()

// 1️⃣ Notas de tres materias de un estudiante
let notaMatematica = 88;
let notaFisica = 100;
let notaQuimica = 56;

// Cálculo del promedio de las tres materias
let promedio = (notaMatematica + notaFisica + notaQuimica) / 3;

// Imprime la clasificación de las materias y el promedio en un formato claro
console.log("CLASIFICACIÓN POR MATERIAS DEL ESTUDIANTE");
console.log("-----------------------------------------");
console.log("Clasificación en Matemática: " + notaMatematica);
console.log("Clasificación en Física: " + notaFisica);
console.log("Clasificación en Química: " + notaQuimica);
console.log("-----------------------------------------");
console.log("El promedio final del estudiante es: " + promedio.toFixed(2));

/* RESPUESTA DE CONSOLA 

CLASIFICACIÓN POR MATERIAS DEL ESTUDIANTE
-----------------------------------------
Clasificación en Matemática: 88
Clasificación en Física: 100
Clasificación en Química: 56
-----------------------------------------
El promedio final del estudiante es: 81.33
*/
```

---

🧠 **EJERCICIO 4 – `04_depuracion_con_console_warn_error.js`**
📚 *Clase JS 2 – Curso Intensivo de JavaScript con Gabo*

---

## 💥 1. TEORÍA PUNTUAL DEL CONCEPTO

### 📘 Tema: Depuración visual con `console.warn()` y `console.error()`

#### 🛠 ¿Qué es depurar?

**Depurar (debugging)** es el proceso de encontrar y corregir errores o comportamientos inesperados en el código.
Una parte fundamental de este proceso es **comunicar visualmente los problemas**.

---

### 🟡 `console.warn()`

📢 Muestra un **aviso o advertencia** en la consola, sin detener la ejecución.
Se usa cuando algo **podría causar un error**, pero aún se puede continuar.

```js
console.warn("El valor ingresado está vacío");
```

---

### 🔴 `console.error()`

💥 Muestra un **error grave**. Sirve para indicar fallos críticos que **sí deben ser corregidos**.

```js
console.error("Formato no válido: se esperaba un número");
```

Ambos métodos ayudan a que tu consola se convierta en una **herramienta profesional de diagnóstico**, y no solo un volcador de datos.

---

## 💥 2. EJEMPLO MÍNIMO

```js
let nombre = "";

if (nombre === "") {
  console.warn("⚠️ El nombre está vacío");
}

if (!isNaN(nombre)) {
  console.error("❌ El nombre no debe ser un número");
}
```

Este código **no detiene la ejecución**, pero la consola muestra claramente qué está mal.

---

## 💥 3. DIAGRAMA DE FLUJO

```js
Inicio
↓
Definir una variable simulando entrada de usuario
↓
Verificar si está vacía
├── Sí → Mostrar advertencia con console.warn()
↓
Verificar si tiene números
├── Sí → Mostrar error con console.error()
└── No → Continuar y mostrar un mensaje normal
↓
Fin
```

---

## 💥 4. ESQUELETO GUÍA COMENTADO (sin resolver)

📂 Nombre del archivo: `04_depuracion_con_console_warn_error.js`

```js
// EJERCICIO 4 – Depuración con console.warn() y console.error()

// Definimos el nombre de usuario
let nombreUsuario = "Gabriel"

// Valida si el campo de nombre está vacío o no definido
if (nombreUsuario === "") {
    console.warn("⚠️ Alerta: El campo de nombre está vacío");
}
// Valida si el nombre contiene números
else if (!isNaN(nombreUsuario)) {
    console.error("❌ Error: El nombre no debe contener números");
}
// Muestra mensaje de bienvenida si las validaciones pasan
else {
    console.log("-".repeat(50));
    console.log("✅ Bienvenido/a, " + nombreUsuario);
    console.log("-".repeat(50));
}

/* RESPUESTA DE CONSOLA 

ejemplo1: let nombreUsuario = "Gabriel";
--------------------------------------------------
✅ Bienvenido/a, Gabriel
--------------------------------------------------

ejemplo2: let nombreUsuario = "98072216508";
❌ Error: El nombre no debe contener números

ejemplo3: let nombreUsuario = 
⚠️ Alerta: El campo de nombre está vacío

*/
```

---

🧠 **EJERCICIO 5 – `05_limpiar_consola_automaticamente.js`**

---

## 🏁 1. TEORÍA PUNTUAL DEL CONCEPTO

### 📘 Tema: `console.clear()` y limpieza profesional de consola

---

### 🔎 ¿Qué hace `console.clear()`?

> Limpia por completo la consola antes de mostrar los nuevos resultados.
> Ideal para evitar acumulación de líneas, confusión visual o datos antiguos que ya no son relevantes.

---

### 📌 ¿Por qué usarlo?

* Para que el usuario o programador **vea solo la información relevante**
* Para que cada ejecución sea **clara, limpia y enfocada**
* Se usa mucho en pruebas interactivas, ciclos de desarrollo y scripts CLI

---

## 🛠 ¿Dónde se coloca?

🔹 Normalmente se coloca **al inicio del script**
🔹 Así, antes de que se imprima cualquier cosa, se borra la consola automáticamente

---

### 🔁 Cuidado

* En navegadores, `console.clear()` puede no funcionar si las DevTools tienen la opción “Preservar registro” activa
* En Node.js funciona perfectamente

---

## 🏁 2. EJEMPLO MÍNIMO

```js
console.clear(); // Limpia la consola primero

let usuario = "Gabo";
console.log("Bienvenido, " + usuario);
```

---

## 🏁 3. DIAGRAMA DE FLUJO

```🏁
Inicio
↓
Limpiar la consola con console.clear()
↓
Declarar variables necesarias (ej: producto, precio, descuento)
↓
Calcular valores finales
↓
Imprimir resultados con console.log() de forma clara
↓
Fin
```

---

## 🏁 4. ESQUELETO GUÍA COMENTADO (sin resolver)

📂 Nombre del archivo: `05_limpiar_consola_automaticamente.js`

```js
//! EJERCICIO 5 – Limpiar consola automáticamente
console.clear();

let producto = "telefono";
let precioBase = 1200;
let descuento = 0.35; // 35% de descuento

let descuentoAplicado = precioBase * descuento;
let precioFinal = precioBase - descuentoAplicado;

console.log("----------------------------");
console.log("📱 Detalles de la compra");
console.log("----------------------------");
console.log("Producto: " + producto);
console.log("Precio base: $" + precioBase);
console.log("Descuento aplicado: $" + descuentoAplicado);
console.log("Precio final: $" + precioFinal);
console.log("----------------------------");

/* RESPUESTA DE CONSOLA 
----------------------------
📱 Detalles de la compra
----------------------------
Producto: telefono
Precio base: $1200
Descuento aplicado: $420
Precio final: $780
----------------------------
*/
```

---

🎓 **CIERRE OFICIAL – CLASE JS 2**
📚 *Tema: Comentarios, buenas prácticas y uso profesional de `console`*
🗂️ *Curso Intensivo de JavaScript  — Módulo 1*

---

## 📌 CONTENIDO IMPARTIDO

En esta clase abordamos **la base profesional para escribir código que se entiende y se depura**, no solo que se ejecuta.

---

### 🧠 Conceptos cubiertos

1. **Comentarios útiles vs inútiles** – Qué explicar, qué no, cómo comentar como profesional.
2. **Uso correcto de `console.log()`** – Comunicación visual clara en la consola.
3. **Depuración con `console.warn()` y `console.error()`** – Reportar errores y advertencias de forma visual sin detener el programa.
4. **Limpieza con `console.clear()`** – Hacer que tu consola sea limpia, clara y enfocada.

---

### ⚙️ Ejercicios realizados

| Nº  | Nombre del archivo                        | Estado     | Nota  |
| --- | ----------------------------------------- | ---------- | ----- |
| 1️⃣ | `01_comentar_codigo_depurado.js`          | ✅ Aprobado | 10/10 |
| 2️⃣ | `02_comentarios_utiles_vs_inutiles.js`    | ✅ Aprobado | 10/10 |
| 3️⃣ | `03_manejo_de_console_log.js`             | ✅ Aprobado | 10/10 |
| 4️⃣ | `04_depuracion_con_console_warn_error.js` | ✅ Aprobado | 10/10 |
| 5️⃣ | `05_limpiar_consola_automaticamente.js`   | ✅ Aprobado | 10/10 |

---
