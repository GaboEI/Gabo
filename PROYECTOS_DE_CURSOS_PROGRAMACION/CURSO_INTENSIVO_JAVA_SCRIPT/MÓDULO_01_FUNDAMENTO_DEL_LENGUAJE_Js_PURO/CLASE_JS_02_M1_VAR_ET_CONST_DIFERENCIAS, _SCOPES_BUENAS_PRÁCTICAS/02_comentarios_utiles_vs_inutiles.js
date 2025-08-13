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
El primer bloque incluye comentarios redundantes que repiten lo que el código ya hace evidente, lo que lo hace menos claro. 
El segundo bloque utiliza comentarios concisos y útiles, explicando el propósito de las variables y operaciones, logrando mayor limpieza y claridad.
*/

/*RESPUESTA DE CONSOLA ENBEVIDA
4000
El precio final a pagar es: 147.5
*/