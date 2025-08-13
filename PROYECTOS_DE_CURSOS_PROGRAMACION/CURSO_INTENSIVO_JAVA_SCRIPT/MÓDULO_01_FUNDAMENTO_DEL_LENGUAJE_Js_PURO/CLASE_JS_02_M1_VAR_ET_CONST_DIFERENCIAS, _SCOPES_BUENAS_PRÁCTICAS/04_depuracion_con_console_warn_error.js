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
