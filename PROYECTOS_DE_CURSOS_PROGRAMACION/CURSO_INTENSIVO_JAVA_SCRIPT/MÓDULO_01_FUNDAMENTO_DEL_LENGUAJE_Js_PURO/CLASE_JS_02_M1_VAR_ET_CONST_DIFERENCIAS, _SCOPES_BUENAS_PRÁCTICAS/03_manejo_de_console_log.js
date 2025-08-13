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