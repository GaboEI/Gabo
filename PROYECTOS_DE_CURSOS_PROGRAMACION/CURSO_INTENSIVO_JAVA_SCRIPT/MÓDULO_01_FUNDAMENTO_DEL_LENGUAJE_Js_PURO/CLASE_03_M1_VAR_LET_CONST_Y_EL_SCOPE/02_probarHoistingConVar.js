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
- `var` sufre hoisting: se eleva al inicio del ámbito (global o de función), inicializándose como undefined, por lo que no genera error al acceder antes de su declaración.
- `let` y `const` también tienen hoisting, pero están en la Zona Muerta Temporal (TDZ), lo que provoca un ReferenceError si se accede antes de su declaración.
- El comportamiento de hoisting es idéntico en el ámbito global y dentro de una función para `var` (undefined), y para `let` y `const` (ReferenceError por TDZ).
- La TDZ asegura que `let` y `const` no sean accesibles antes de su inicialización, promoviendo un código más predecible.
- Usar `var` puede llevar a errores sutiles debido a su hoisting implícito, mientras que `let` y `const` son más estrictos y seguros.
*/