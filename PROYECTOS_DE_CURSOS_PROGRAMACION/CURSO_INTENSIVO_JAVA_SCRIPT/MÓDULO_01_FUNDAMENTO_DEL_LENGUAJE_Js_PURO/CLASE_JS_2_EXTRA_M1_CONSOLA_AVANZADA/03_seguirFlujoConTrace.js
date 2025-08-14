// EJERCICIO 3: SEGUIR FLUJO CON TRACE:

function analizarProceso() {
    verificarDato();
}

function verificarDato() {
    ejecutarTarea();
}

function ejecutarTarea() {
    console.trace("📍 Trazando la ejecución del programa hasta aquí");
}

analizarProceso();

/* 
=================================================================================
RESPUESTA DE CONSOLA ENBEVIDA (las dirercciones fueron abreviadas manualmente )
=================================================================================
node 03_seguirFlujoConTrace.js
Trace: 📍 Trazando de la ejecucion del programa hasta aqui
    at ejecutarTarea (...js:12:13)
    at verrificarDatod (...js:8:5)
    at analizarProceso (...js:4:5)
    at Object.<anonymous> (...js:15:1)
    at Module._compile (node:internal/modules/cjs/loader:1688:14)
    at Object..js (node:internal/modules/cjs/loader:1820:10)
    at Module.load (node:internal/modules/cjs/loader:1423:32)
    at Function._load (node:internal/modules/cjs/loader:1246:12)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)
=================================================================================  
*/