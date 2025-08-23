// EJERCICIO 1 – 01_compararVarLetConst.js
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