# 📘 CLASE JS 3 – `var`, `let`, `const` y el **scope**

## 🧠 SECCIÓN 1 – LA DECLARACIÓN DE VARIABLES EN JS: HISTORIA Y CONTEXTO

### 📌 ¿Por qué existen tres formas de declarar variables?

JavaScript es un lenguaje **creado en 10 días** (por Brendan Eich en 1995), y en su versión inicial solo existía:

```js
var
```

Esta declaración era suficiente en un inicio para hacer scripts pequeños.
Pero con el tiempo y la evolución del desarrollo web, `var` comenzó a mostrar sus fallos, **especialmente en proyectos grandes**:

* No tiene *scope de bloque*
* Permite redeclaraciones sin errores
* Sufre de *hoisting silencioso*
* Puede causar bugs por *mutaciones inesperadas*

Por eso, con **ES6 (2015)**, llegaron dos nuevos aliados:

```js
let
const
```

Y desde entonces se considera **mala práctica usar `var`**, salvo que sea para entender código legacy o para entrevistas.

---

## 🧠 SECCIÓN 2 – DIFERENCIAS FUNDAMENTALES ENTRE `var`, `let` y `const`

### 📋 Cuadro comparativo profundo

| Característica               | `var`                      | `let`                   | `const`                                 |
| ---------------------------- | -------------------------- | ----------------------- | --------------------------------------- |
| Scope                        | Funcional (function scope) | De bloque (block scope) | De bloque (block scope)                 |
| Hoisting                     | Sí, con valor `undefined`  | Sí, pero con **TDZ**    | Sí, pero con **TDZ**                    |
| Reasignación                 | ✅ Permitida                | ✅ Permitida             | ❌ No permitida                          |
| Redeclaración en mismo scope | ✅ Permitida                | ❌ Error                 | ❌ Error                                 |
| Inicialización obligatoria   | ❌ No                       | ❌ No                    | ✅ Sí                                    |
| Inmutabilidad completa       | ❌ No (mutable)             | ❌ No (mutable)          | ⚠️ Solo referencia, no valores internos |
| Uso profesional recomendado  | ❌ No usar más              | ✅ Usar por defecto      | ✅ Usar si no se reasigna                |

---

## 🧬 SECCIÓN 3 – ¿QUÉ ES EL *SCOPE*?

### 🔍 Definición técnica

> **Scope** es el contexto léxico donde una variable vive y desde donde puede ser accedida.

Es decir: **¿dónde puedes usar esa variable sin que te dé error?**

---

### 🎯 Tipos de scope en JS

| Tipo de Scope | Descripción                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------------- |
| 🌍 Global     | Fuera de cualquier función o bloque                                                                                   |
| 🧩 De función | Dentro de una función (vale para `var`, `let`, `const`)                                                               |
| 📦 De bloque  | Dentro de `{}` como en `if`, `for`, `while` (solo para `let` y `const`)                                               |
| 🔄 Léxico     | El scope se determina por la **posición física del código en el archivo**, no por cómo se ejecuta (clave en closures) |

---

### ⚠️ `var` NO RESPETA EL BLOCK SCOPE

```js
if (true) {
  var nombre = "Gabo";
}
console.log(nombre); // ✅ "Gabo"
```

Esto es un comportamiento inesperado en código moderno.
Lo correcto sería que esa variable **no saliera del bloque `{}`**.

Con `let` o `const`, esto sí se respeta:

```js
if (true) {
  let apellido = "Pérez";
}
console.log(apellido); // ❌ ReferenceError
```

---

## 💡 SECCIÓN 4 – HOISTING: EL ASCENSO FANTASMA

### 🎓 Definición técnica

> El **hoisting** es un comportamiento por el cual **las declaraciones de variables y funciones se “elevan” internamente** al principio de su contexto antes de ejecutar el código.

⚠️ Esto no significa que la variable esté inicializada.

---

### 🧪 Ejemplo con `var`

```js
console.log(mensaje); // undefined
var mensaje = "Hola Gabo";
```

Esto NO da error, pero no imprime `"Hola Gabo"` sino `undefined`. ¿Por qué?

🔬 Internamente, el motor JS hace esto:

```js
var mensaje; // "elevado"
console.log(mensaje); // todavía no se ha asignado
mensaje = "Hola Gabo";
```

---

### ⚠️ PELIGRO CON `let` y `const`: TDZ

Con `let` y `const`, **sí hay hoisting**, pero la variable queda en una **zona muerta temporal (TDZ - Temporal Dead Zone)** hasta que se inicializa.

```js
console.log(nombre); // ❌ ReferenceError
let nombre = "Ada Lovelace";
```

No es `undefined`, es un error directo.
Esto protege el código de errores difíciles de depurar.

---

## 🧠 SECCIÓN 5 – INMUTABILIDAD RELATIVA DE `const`

### 📍 `const` impide la **reasignación del identificador**, pero no congela el contenido si es un objeto o array

```js
const usuario = { nombre: "Gabo" };
usuario.nombre = "Ada"; // ✅ Válido
usuario = { nombre: "Otro" }; // ❌ Error
```

⚠️ Para congelar completamente, se usa:

```js
Object.freeze(usuario);
```

---

## 🧰 SECCIÓN 6 – SHADOWING Y AMBIGÜEDADES

### 💥 ¿Qué pasa si declaras dos variables con el mismo nombre en scopes distintos?

```js
let nombre = "Gabo";

function saludar() {
  let nombre = "Ada";
  console.log(nombre);
}
saludar(); // Ada
console.log(nombre); // Gabo
```

Esto se llama **shadowing**: la variable interna *eclipsa* a la externa.

---

## 🔩 SECCIÓN 7 – BUENAS PRÁCTICAS REALES EN PROYECTOS

✅ Usa `let` para variables que **pueden cambiar su valor**
✅ Usa `const` como preferencia si **no necesitas reasignar**
✅ ❌ Evita `var`, excepto cuando:

* Analices código legacy
* Participes en entrevistas
* Quieras ilustrar hoisting o bugs clásicos

✅ Declara tus variables al inicio del bloque o función (no en mitad del código)
✅ Nombra claramente tus variables: sin ambigüedades ni nombres genéricos

---

## 📊 DIAGRAMA DE FLUJO – DECLARACIÓN DE VARIABLES EN JS

```.
Inicio del programa
↓
¿Se declara variable con var?
├── Sí → Hoisting a undefined → Scope de función → Puede redeclararse
└── No ↓
¿Se declara variable con let o const?
    ├── Sí → Hoisting con TDZ → Scope de bloque
    │       ├── ¿Se usa antes de declararse? → Error
    │       └── ¿Se reasigna?
    │             ├── let → permitido
    │             └── const → ❌ Error
    └── No → Error: variable no declarada
↓
Se ejecuta el resto del código
```

---

## 💼 EJEMPLOS EN LA VIDA REAL

### ✅ En un proyecto moderno (React, Vue, Node.js)

* Jamás deberías ver `var` salvo en bibliotecas antiguas.
* Toda la declaración de estado, funciones, lógica interna: **`let` y `const`**
* Mucho mejor usar `const` como valor por defecto para evitar bugs.

### ✅ En una entrevista técnica

* Te pueden poner trampas con `var`, hoisting y `for` con closures
* Saber explicar scope **te hace destacar**

---
¡Excelente, Gabo! 💪
Damos paso al **primer ejercicio** de esta clase intensa y fundamental.

---

## 🧪 EJERCICIO 1 – `01_compararVarLetConst.js`

---

### 🎯 **Objetivo del ejercicio**

Analizar y comparar el comportamiento real de `var`, `let` y `const` en diferentes contextos:

* scope global
* scope de bloque
* re-declaración
* re-asignación
* errores por mal uso

Este ejercicio **te permitirá visualizar en código real las diferencias** vistas en la teoría.
Será tu base para detectar errores y mejorar la legibilidad de tu código en el mundo profesional.

---

## 🧠 TEORÍA PUNTUAL APLICADA

1. 🔁 `var` permite redeclaración y reasignación dentro del mismo scope.
2. 🚫 `let` y `const` **no permiten redeclaración** en el mismo scope.
3. 📦 `let` y `const` **tienen scope de bloque**, `var` no.
4. ❌ `const` **no permite reasignación**.
5. 👻 El uso de `var` puede llevar a bugs por su hoisting y falta de bloque.

---

### 🧪 Ejemplo mínimo para fijar el concepto

```js
{
  var x = 1;
  let y = 2;
  const z = 3;
}
console.log(x); // ✅ 1
console.log(y); // ❌ ReferenceError
console.log(z); // ❌ ReferenceError
```

Aquí puedes observar el **scope de bloque** respetado por `let` y `const`, pero ignorado por `var`.

---

## 📊 DIAGRAMA DE FLUJO DEL EJERCICIO

```.
Inicio del script
↓
Declarar variable con var
↓
Declarar variable con let
↓
Declarar variable con const
↓
Imprimir sus valores dentro de bloque
↓
Intentar imprimir fuera del bloque
├── Si es var → Se imprime normalmente
├── Si es let o const → ReferenceError
↓
Intentar redeclarar las variables
├── var → Permitido
├── let o const → SyntaxError
↓
Intentar reasignar valores
├── var o let → Permitido
└── const → TypeError
↓
Fin del script
```

---

## 🧱 `01_compararVarLetConst.js`

// 01\_compararVarLetConst.js

```js
// Inicio del script

// Declarar variable con var
var varVariable = "Soy var";

// Declarar variable con let
let letVariable = "Soy let";

// Declarar variable con const
const constVariable = "Soy const";

// Imprimir valores dentro de un bloque
{
    console.log("Dentro del bloque:");
    console.log("varVariable:", varVariable); // Se imprime: Soy var
    console.log("letVariable:", letVariable); // Se imprime: Soy let
    console.log("constVariable:", constVariable); // Se imprime: Soy const
}

// Intentar imprimir fuera del bloque
console.log("\nFuera del bloque:");
console.log("varVariable:", varVariable); // Se imprime normalmente: Soy var
console.log("letVariable:", letVariable); // No genera error porque está en ámbito global
console.log("constVariable:", constVariable); // No genera error porque está en ámbito global

// Ejemplo con let y const dentro de un bloque para forzar ReferenceError
console.log("\nEjemplo con let y const dentro de un bloque:");
{
    let letVariableBlock = "Soy let en bloque";
    const constVariableBlock = "Soy const en bloque";
    console.log("letVariableBlock:", letVariableBlock); // Se imprime: Soy let en bloque
    console.log("constVariableBlock:", constVariableBlock); // Se imprime: Soy const en bloque
}

console.log("letVariableBlock:", typeof letVariableBlock); // ReferenceError: letVariableBlock is not defined
console.log("constVariableBlock:", typeof constVariableBlock); // ReferenceError: constVariableBlock is not defined

// Intentar redeclarar las variables (en funciones separadas para evitar SyntaxError)
console.log("\nIntentando redeclarar variables:");
function redeclareVar() {
    var varVariable = "Re-declarada var"; // Permitido
    console.log("varVariable redeclarada:", varVariable); // Se imprime: Re-declarada var
}
redeclareVar();

// Comentar las redeclaraciones de let y const para evitar SyntaxError
// let letVariable = "Re-declarada let"; // SyntaxError: Identifier 'letVariable' has already been declared
// const constVariable = "Re-declarada const"; // SyntaxError: Identifier 'constVariable' has already been declared
console.log("letVariable redeclarada: No se puede, genera SyntaxError");
console.log("constVariable redeclarada: No se puede, genera SyntaxError");

// Intentar reasignar valores
console.log("\nIntentando reasignar valores:");
varVariable = "Nuevo valor var"; // Permitido
letVariable = "Nuevo valor let"; // Permitido
console.log("varVariable reasignada:", varVariable); // Se imprime: Nuevo valor var
console.log("letVariable reasignada:", letVariable); // Se imprime: Nuevo valor let
constVariable = "Nuevo valor const"; // TypeError: Assignment to constant variable

// Resumen de lo aprendido
/*
Lo aprendido:
- `var` permite redeclaración y reasignación, con ámbito global o de función, lo que puede causar problemas si no se controla.
- `let` permite reasignación pero no redeclaración en el mismo ámbito, y su alcance es de bloque, lo que lo hace más seguro.
- `const` no permite reasignación ni redeclaración, asegurando que el valor permanezca constante, pero los objetos declarados con const pueden modificar sus propiedades.
- Intentar acceder a `let` o `const` fuera de su bloque genera ReferenceError.
- Redeclarar `let` o `const` en el mismo ámbito genera SyntaxError, deteniendo la ejecución.
- Reasignar un valor a `const` genera TypeError.
- Usar funciones separadas o comentarios evita que los errores de sintaxis rompan el script.
*/
```

---

## 🧪 EJERCICIO 2 – `02_probarHoistingConVar.js`

---

### ✍️ **Objetivo del ejercicio**

📌 Demostrar experimentalmente cómo actúa el **hoisting** con `var`, y comparar su comportamiento con `let` y `const` dentro de diferentes contextos:

* Global
* Dentro de funciones
* Dentro de bloques

Este ejercicio te permitirá **visualizar la elevación silenciosa** de las declaraciones con `var` y te preparará para evitar errores en código real.

---

## 🧠 TEORÍA

### 🔍 ¿Qué es el *hoisting*?

> El hoisting es un mecanismo por el cual **las declaraciones de variables y funciones son procesadas antes de ejecutar el código**, lo que permite **usar variables antes de que aparezcan en el código fuente** (con ciertas restricciones).

🧪 Con `var`, se hace hoisting de la **declaración, no del valor asignado**.
🔒 Con `let` y `const`, también se hace hoisting, pero quedan en la **Zona Muerta Temporal (TDZ)** hasta ser inicializadas (por eso generan errores si las accedes antes).

---

### ⚠️ Ejemplo mínimo ilustrativo

```js
console.log(x); // undefined, no error
var x = 5;
```

Internamente, esto ocurre:

```js
var x;        // hoisted
console.log(x); // undefined
x = 5;
```

---

## DIAGRAMA DE FLUJO DEL EJERCICIO

```.
Inicio del script
↓
Intentar acceder a una variable declarada con var antes de declararla
↓
¿Se lanza error?
├── No → Se imprime undefined
└── Sí → No ocurre con var
↓
Declarar e inicializar la variable var
↓
Imprimir después de declarar → Se imprime valor asignado
↓
Repetir mismo patrón con let y const
↓
¿Se lanza error?
├── Sí → ReferenceError (TDZ)
↓
Encapsular mismo patrón dentro de una función
↓
Observar si el comportamiento del hoisting cambia en contexto local
↓
Fin del script
```

---

## `02_probarHoistingConVar.js`

```js
// 02_probarHoistingConVar.js
console.clear()
// Inicio del script

// Intentar acceder a una variable declarada con var antes de declararla
console.log("Intentando acceder a var antes de declararla:");
console.log("varVariable:", varVariable); // Se imprime: undefined (no error, debido a hoisting)

// Declarar e inicializar la variable var
var varVariable = "Soy var";

// Imprimir después de declarar
console.log("varVariable después de declarar:", varVariable); // Se imprime: Soy var

// Repetir mismo patrón con let
console.log("\nIntentando acceder a let antes de declararla:");
console.log("letVariable:", letVariable); // ReferenceError: Cannot access 'letVariable' before initialization (TDZ)

// Declarar e inicializar la variable let
let letVariable = "Soy let";

// Imprimir después de declarar
console.log("letVariable después de declarar:", letVariable); // Se imprime: Soy let

// Repetir mismo patrón con const
console.log("\nIntentando acceder a const antes de declararla:");
console.log("constVariable:", constVariable); // ReferenceError: Cannot access 'constVariable' before initialization (TDZ)

// Declarar e inicializar la variable const
const constVariable = "Soy const";

// Imprimir después de declarar
console.log("constVariable después de declarar:", constVariable); // Se imprime: Soy const

// Encapsular mismo patrón dentro de una función
function testHoistingInFunction() {
    // Intentar acceder a var antes de declararla
    console.log("\nDentro de función - Intentando acceder a var antes de declararla:");
    console.log("varLocal:", varLocal); // Se imprime: undefined (hoisting en ámbito de función)

    // Declarar e inicializar var
    var varLocal = "Soy var local";
    console.log("varLocal después de declarar:", varLocal); // Se imprime: Soy var local

    // Intentar acceder a let antes de declararla
    console.log("\nDentro de función - Intentando acceder a let antes de declararla:");
    console.log("letLocal:", letLocal); // ReferenceError: Cannot access 'letLocal' before initialization (TDZ)

    // Declarar e inicializar let
    let letLocal = "Soy let local";
    console.log("letLocal después de declarar:", letLocal); // Se imprime: Soy let local

    // Intentar acceder a const antes de declararla
    console.log("\nDentro de función - Intentando acceder a const antes de declararla:");
    console.log("constLocal:", constLocal); // ReferenceError: Cannot access 'constLocal' before initialization (TDZ)

    // Declarar e inicializar const
    const constLocal = "Soy const local";
    console.log("constLocal después de declarar:", constLocal); // Se imprime: Soy const local
}

// Ejecutar la función
testHoistingInFunction();

// Resumen de lo aprendido
/*
Lo aprendido:
- `var` sufre hoisting: se eleva al inicio del ámbito (global o de función), inicializándose 
como undefined, por lo que no genera error al acceder antes de su declaración.
- `let` y `const` también tienen hoisting, pero están en la Zona Muerta Temporal (TDZ), 
lo que provoca un ReferenceError si se accede antes de su declaración.
- El comportamiento de hoisting es idéntico en el ámbito global y dentro de una función para 
`var` (undefined), y para `let` y `const` (ReferenceError por TDZ).
- La TDZ asegura que `let` y `const` no sean accesibles antes de su inicialización, promoviendo 
un código más predecible.
- Usar `var` puede llevar a errores sutiles debido a su hoisting implícito, mientras que `let` y `const` 
son más estrictos y seguros.
*/
```

---

## 🧪 EJERCICIO 3 – `03_scopeEnCondicionalesYFunciones.js`

---

### 👁️ **Objetivo del ejercicio**

Experimentar, visualizar y **comparar los distintos tipos de scope** en JavaScript:

* Scope **global**
* Scope **de bloque** (usando `if`, `for`, `{}`)
* Scope **de función**
* Diferencias reales entre `var`, `let` y `const` dentro de esos scopes

Este ejercicio **te permitirá detectar posibles bugs** en flujos de control y refinar tu entendimiento del **contexto léxico real de una variable**.

---

## ✍️ TEORÍA PUNTUAL APLICADA

### 🔍 ¿Qué es el scope?

> El *scope* es el contexto en el cual una variable está disponible (visible y accesible) durante la ejecución del código.

En JS moderno, existen:

| Tipo de Scope | ¿Quién lo crea? | ¿Qué lo activa?   | ¿Var aplica? | ¿Let/Const aplican? |
| ------------- | --------------- | ----------------- | ------------ | ------------------- |
| 🌐 Global     | Todo el archivo | Código en raíz    | ✅            | ✅                   |
| 🔧 De función | Una función     | `function() {}`   | ✅            | ✅                   |
| 📦 De bloque  | Un bloque `{}`  | `if`, `for`, etc. | ❌ (NO)       | ✅                   |

---

## 🔬 EJEMPLO MÍNIMO EXPLICATIVO

```js
if (true) {
  var a = "var";
  let b = "let";
}
console.log(a); // ✅ var
console.log(b); // ❌ ReferenceError
```

* `a` sale del bloque: `var` **ignora** el bloque
* `b` queda dentro: `let` **respeta** el bloque

---

## 👌 DIAGRAMA DE FLUJO DEL EJERCICIO

```.
Inicio del script
↓
Declarar variable global con var, let y const
↓
Crear un bloque (if o {} sin condición)
├── Declarar nuevas variables dentro del bloque (var, let, const)
├── Imprimir dentro del bloque
↓
Imprimir esas mismas variables fuera del bloque
├── ¿var? → Se imprime (sale del bloque)
├── ¿let/const? → ReferenceError
↓
Crear función con declaraciones internas
├── Declarar variables con var, let y const
├── Imprimir dentro
↓
Imprimir fuera de la función
├── Todas dan ReferenceError (el scope es cerrado)
↓
Reflexionar sobre las diferencias entre scope de bloque y scope de función
↓
Fin del script
```

---

## EJERCICIO 3 – `03_scopeEnCondicionalesYFunciones.js`

// 03\_scopeEnCondicionalesYFunciones.js

```js
// 03_scopeEnCondicionalesYFunciones.js
console.clear()
//1️⃣ Declarar tres variables globales: una con var, una con let y una con const
var varGlobal = "Soy Var Global";
let letGlobal = "Soy let Global";
const constGlobal = "Soy const Global";

// 2️⃣ Crear un bloque if (por ejemplo: if (true) { ... })
if (true){
     // 3️⃣ Dentro del if, declarar tres nuevas variables: var, let, const
    var varif = "Soy Var if";
    let letif = "Soy let if";
    const constif = "Soy const if";

    // 4️⃣ Imprimir dentro del bloque los valores de estas tres variables

    console.log("\n Imprimir dentro del bloque if");
    console.log("varif:", varif); // varif: Soy Var if
    console.log("letif:", letif); // letif: Soy let if
    console.log("constif:", constif); // constif: Soy const if
}

// 5️⃣ Imprimir fuera del bloque para ver qué variables están disponibles
console.log("\n Imprimir fuera del bloque if");
console.log("varif:", varif); // varif: Soy Var if
//console.log("letif:", letif); // ReferenceError: letif is not defined
//console.log("constif:", constif); // ReferenceError: ifConst is not defined

// 6️⃣ Comentar qué pasó con var, let y const fuera del if
/*
Qué pasó fuera del bloque if:
- `varif` (var): Se imprime normal porque `var` no respeta el scope de bloque y 
se eleva al ámbito global o de función, haciéndola accesible fuera del bloque if.

- `letif` (let): Genera un ReferenceError porque `let` tiene scope de bloque, por 
lo que no está definida fuera del bloque if.

- `constif` (const): Genera un ReferenceError porque `const` también tiene scope 
de bloque, por lo que no está definida fuera del bloque if.
*/

// 7️⃣ Crear una función y repetir lo mismo dentro de la función: declarar var, let, const
function testFunctionScope (){
    var varFunction = "Soy Var function"; 
    let letFunction = "Soy let function"; 
    const constfunction = "Soy const function"; 

    // 8️⃣ Imprimir dentro de la función los valores
    console.log("\n Imprimir dentro de la función");
    console.log("varfunction:", varfunction); // varfunction: Soy Var function
    console.log("letfunction:", letfunction); // letfunction: Soy let function
    console.log("constfunction:", constfunction); // constfunction: Soy const function
}
// Ejecutar la función
testFunctionScope();

// 9️⃣ Intentar imprimir esas variables fuera de la función (ver si generan error)
console.log("\n Imprimir fuera de la función");
//console.log("varfunction:", varfunction); // ReferenceError: varfunction is not defined
//console.log("letfunction:", letfunction); // ReferenceError: letfunction is not defined
//console.log("constfunction:", constfunction); // ReferenceError: constfunction is not defined

// 🔟 Reflexión: ¿por qué `var` sale de bloques pero no de funciones? ¿Qué implicaciones tiene esto?
/*
Reflexión:
- **Por qué `var` sale de bloques pero no de funciones**:
- `var` tiene un ámbito de función o global, no de bloque. Cuando se declara dentro de un bloque como 
`if`, se eleva (hoisting) al ámbito de la función que lo contiene o al ámbito global si no está dentro 
de una función. Por eso, `ifVar` es accesible fuera del bloque `if`.

- En cambio, dentro de una función, `var` está limitada al ámbito de esa función, ya que el scope de función 
es un límite más estricto. Esto significa que `functionVar` no es accesible fuera de `testFunctionScope`.

- **Implicaciones**:
  - **Riesgo con `var` en bloques**: Como `var` ignora el scope de bloque, puede causar comportamientos 
inesperados, como sobrescribir variables en el ámbito global o de función, lo que lleva a errores difíciles de depurar.
  - **Seguridad con `let` y `const`**: Estas respetan el scope de bloque, lo que las hace más predecibles y seguras, 
evitando colisiones de nombres fuera de su contexto.
  - **Encapsulación en funciones**: El scope de función es ideal para encapsular lógica y datos, ya que ninguna variable 
(`var`, `let`, `const`) escapa de la función, protegiendo el ámbito externo.
  - **Buenas prácticas**: Preferir `let` y `const` sobre `var` para un control más estricto del ámbito y evitar problemas 
de hoisting. Usar funciones para encapsular código sensible mejora la modularidad y reduce errores.
*/
```

---

💎 ¡Excelente decisión, Gabo!
Este ejercicio es clave para **desmitificar el uso de `const` con estructuras complejas como objetos y arrays**. Muchos creen que `const` los hace completamente inmutables... pero eso es solo media verdad. Vamos a comprobarlo con bisturí técnico. 🧪🔬

---

## 🧪 EJERCICIO 4 – `04_constInmutableConObjetos.js`

---

### ⏺️ **Objetivo del ejercicio**

Explorar cómo funciona `const` cuando se aplica a objetos y arrays en JavaScript, para comprender **qué es realmente inmutable y qué no**.

✔️ Vas a crear un objeto y un array declarados con `const`.

✔️ Probarás modificar sus propiedades o elementos.

✔️ Luego intentarás **reasignar completamente** esas variables.

✔️ Vas a reflexionar sobre qué significa **inmutabilidad por referencia vs por valor**.

---

## 😈 TEORÍA PUNTUAL APLICADA

### 🔍 ¿Qué hace `const` realmente?

> `const` **bloquea la reasignación del identificador**, pero **no congela el contenido** del valor si este es un **objeto o array**.

👉 Es decir:

* ❌ **No puedes hacer:** `miObjeto = otroObjeto`
* ✅ **Pero puedes hacer:** `miObjeto.propiedad = nuevoValor`

🔐 Para que un objeto sea verdaderamente inmutable, debes usar:

```js
Object.freeze(objeto)
```

Esto impide agregar, modificar o eliminar propiedades (aunque hay formas de romperlo también 😅).

---

## 😈 EJEMPLO MÍNIMO EXPLICATIVO

```js
const persona = { nombre: "Ada" };
persona.nombre = "Gabo"; // ✅ Permitido
persona = { nombre: "Otro" }; // ❌ TypeError
```

🔁 Igual con arrays:

```js
const numeros = [1, 2, 3];
numeros.push(4); // ✅ Permitido
numeros = [9, 8, 7]; // ❌ TypeError
```

---

## 😈 DIAGRAMA DE FLUJO DEL EJERCICIO

```>
Inicio del script
↓
Crear un objeto con const
↓
Modificar una propiedad interna del objeto
├── ¿Se permite? → Sí
↓
Intentar reasignar el objeto por completo
├── ¿Se permite? → No (TypeError)
↓
Repetir mismo patrón con un array
↓
Modificar elementos del array (push, pop, etc.)
├── ¿Se permite? → Sí
↓
Intentar reasignar el array completo
├── ¿Se permite? → No (TypeError)
↓
(Extra) Aplicar Object.freeze() y volver a probar modificación
↓
Reflexionar sobre la diferencia entre:
├── Inmutabilidad de la referencia
└── Mutabilidad del contenido
↓
Fin del script
```

---

## 😈 EJERCICIO 4 – `04_constInmutableConObjetos.js`

```js
// EJERCICIO 4 – 04_constInmutableConObjetos.js

// 1️⃣ Declarar un objeto con const, con al menos 2 propiedades
const user = {
    name: "Ernesto", 
    userId: "98072216E",
    status: "pro"
};

// 2️⃣ Imprimir el objeto original
console.log(user); // Output: { name: 'Ernesto', userId: '98072216E', status: 'pro' }

// 3️⃣ Modificar una propiedad del objeto (userId)
user.userId = "0140052279"; 

// 5️⃣ Imprimir el objeto modificado
console.log(user); // Output: { name: 'Ernesto', userId: '0140052279', status: 'pro' }

// 6️⃣ Intentar reasignar el objeto completo a otra referencia (debe dar error)
/*user = {
    name: "Juan", 
    userId: "12345678",
    status: "none"
};
console.table(user); // Output: TypeError: Assignment to constant variable. */
//===============================================================================//

// 7️⃣ Declarar un array con const y algunos elementos
const myArray = [1, "Hello", true, 3.14];

// 8️⃣ Imprimir el array original
console.log(myArray); // Output: [1, "Hello", true, 3.14]

// 9️⃣ Usar métodos como push, pop, splice para modificar el contenido

//Push
myArray.push("addPush");
console.log(myArray); // Output:  1, 'Hello', true, 3.14, 'addPush' ]

// pop
const lastItem = myArray.pop();
console.log(myArray); // Output: [ 1, 'Hello', true, 3.14 ]
console.log(lastItem); // Output: addPush

// splice
myArray.splice(1,1); // Eliminar un elemento con splice
console.log(myArray); // Output: [ 1, true, 3.14 ]

myArray.splice(1,0, 'Hello'); // En la posición 1, añade 'Hello' sin eliminar elementos.
console.log(myArray); // Output: [ 1, 'Hello', true, 3.14 ]

myArray.splice(-1,1, '2.71'); // En la posición -1 o 3 elimina 1 elemento (' 3.14') y añade '2.71'
console.log(myArray); // Output: [ 1, 'Hello', true, '2.71' ]

// 1️⃣1️⃣ Intentar reasignar el array completo (debe dar error)
/*myArray = [2, "Hi", false, 360];
console.log(myArray); Output: TypeError: Assignment to constant variable.*/

// 1️⃣2️⃣ (Opcional) Usar Object.freeze() y probar si puedes modificar el objeto
Object.freeze(myArray); // Congela el array
console.log(Object.isFrozen(myArray)); // Output: true

/* 1️⃣3️⃣ Reflexión final: ¿Qué es realmente inmutable con const?
Con `const`, la referencia a la variable es inmutable, no su contenido. En objetos y arrays, 
las propiedades o elementos pueden modificarse, pero no se puede reasignar la variable a un nuevo 
objeto o array. Esto implica que debemos usar métodos como Object.freeze() para proteger el contenido 
si se necesita inmutabilidad total, y tener cuidado al compartir referencias para evitar modificaciones 
inesperadas. */
```

---
