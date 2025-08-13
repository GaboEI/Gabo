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