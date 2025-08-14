// EJERCICIO 2: RASTREAR PROCESO CON GROUP

function procesarPedido() {
    console.group("🛒 Inicio del pedido");

    console.log("🔍 Validar id del producto");
    console.log("✍️ Validar stock del producto en el almacén");
    console.log("📤 Validar sistema de logística");

    console.group("📦 Preparación del producto");
    console.log("🔖 Etiquetar producto");
    console.log("📏 Verificar dimensiones y peso");
    console.log("📦 Empaquetar producto");
    console.groupEnd();

    console.log("✅ Pedido procesado con éxito");

    console.groupEnd();
}

procesarPedido();

/* 
=================================================
RESPUESTA DE CONSOLA ENBEVIDA 
=================================================
node 02_rastrearProcesoConGroup.js
🛒 Inicio del pedido
    🔍 Validar id del producto
    ✍️ Validar stock del producto en el almacén
    📤 Validar sistema de logística
📦 Preparación del producto
    🔖 Etiquetar producto
    📏 Verificar dimensiones y peso
    📦 Empaquetar producto
    ✅ Pedido procesado con éxito
=================================================  
*/