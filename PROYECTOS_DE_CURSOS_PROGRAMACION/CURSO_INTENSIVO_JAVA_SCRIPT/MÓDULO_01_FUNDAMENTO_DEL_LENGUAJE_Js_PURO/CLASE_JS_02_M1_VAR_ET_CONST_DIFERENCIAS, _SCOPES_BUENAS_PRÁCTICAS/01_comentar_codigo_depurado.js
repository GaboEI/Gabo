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