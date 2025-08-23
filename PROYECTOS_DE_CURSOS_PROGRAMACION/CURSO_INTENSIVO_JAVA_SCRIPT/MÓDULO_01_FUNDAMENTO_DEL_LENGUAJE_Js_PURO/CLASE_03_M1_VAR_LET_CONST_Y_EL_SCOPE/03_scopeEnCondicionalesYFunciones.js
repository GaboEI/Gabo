
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