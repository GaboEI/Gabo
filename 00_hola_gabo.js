//1️⃣ Importamos el módulo 'readline' para poder leer datos del usuario
const readline = require("readline");

//2️⃣ Creamos una interfaz de lectura desde la consola estándar
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

//3️⃣ Solicitamos al usuario que ingrese su nombre
rl.question("👤 ¿Cuál es tu nombre?: ", (nombre) => {
  //4️⃣ Mostramos un saludo personalizado con la entrada recibida
    console.log(`✨ ¡Hola, ${nombre}! Bienvenido a tu entorno JavaScript en WSL.`);

  //5️⃣ Cerramos la interfaz para evitar que el programa quede esperando
    rl.close();
});

