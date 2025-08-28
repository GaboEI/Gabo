//EJERCICIO 5 – 05_buenasPracticasEnDeclaracion.js

// Carrito de Frutas

// Valores fijos (no cambian)
const maxFrutas = 2;
const nombreTienda = "Tienda de Frutas";

// Información del usuario
const nombreUsuario = "Sofia";

// Información del carrito (puede cambiar)
let frutasEnCarrito = [];
let costoTotal = 0;

// Lista de frutas
const frutas = [
    { nombre: "Manzana", precio: 2 },
    { nombre: "Plátano", precio: 3 }
];

// Función para agregar una fruta al carrito
function agregarFruta(nombreFruta) {
    if (frutasEnCarrito.length >= maxFrutas) {
        console.log("¡El carrito está lleno!");
    } else {
        // Buscar la fruta
        const fruta = frutas.find(f => f.nombre === nombreFruta);
        if (fruta) {
            frutasEnCarrito.push(fruta);
            costoTotal = costoTotal + fruta.precio;
            console.log(fruta.nombre + " añadida. Total: $" + costoTotal);
        } else {
            console.log("¡Fruta no encontrada!");
        }
    }
}

// Función para mostrar el carrito
function mostrarCarrito() {
    console.log("Carrito de " + nombreUsuario + ":");
    frutasEnCarrito.forEach(fruta => console.log("- " + fruta.nombre + ": $" + fruta.precio));
    console.log("Total: $" + costoTotal);
}

// Probar el código
agregarFruta("Manzana");
agregarFruta("Plátano");
mostrarCarrito();

// Verificar algunos valores
console.log("Usuario:", nombreUsuario);
console.log("Frutas en el carrito:", frutasEnCarrito.length);

/* 
**Reflexión Final**:
- **Mantenimiento**: Nombres claros como `costoTotal` y organización por bloques (usuario, carrito) facilitan modificar el código.
- **Debugging**: Usar `const` evita cambios accidentales, y los `console.log` ayudan a verificar qué pasa.
- **Trabajo en equipo**: Código claro y sin `var` es fácil de entender para otros, agilizando la colaboración.
*/

/*
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
❯ node 05_buenasPracticasEnDeclaracion.js
Manzana añadida. Total: $2
Plátano añadida. Total: $5
Carrito de Sofia:
- Manzana: $2
- Plátano: $3
Total: $5
Usuario: Sofia
Frutas en el carrito: 2
====================================================================
*/