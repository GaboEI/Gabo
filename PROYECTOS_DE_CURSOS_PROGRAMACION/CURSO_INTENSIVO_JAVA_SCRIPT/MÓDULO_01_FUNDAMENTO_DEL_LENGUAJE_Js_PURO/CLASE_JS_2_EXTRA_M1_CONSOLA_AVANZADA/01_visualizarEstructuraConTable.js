// Ejercicio 1: VISUALIZAR ESTRUCTURA CON TABLE

const ventaLibros = [
    {nombre: "Anatomía de las expresiones faciales", precio: 1550, disponible: true},
    {nombre: "El cuerpo se cura a sí mismo", precio: 550, disponible: false},
    {nombre: "Forma de la cabeza y el cuello", precio: 1550, disponible: true},
    {nombre: "Atlas clínico de puntos gatillo",precio: 1000, disponible: false},
    {nombre: "Atlas de Tricoscopia", precio: 1800, disponible: false}
];
const ventaLibrosconIndice = ventaLibros.map((ventaLibros, index) => ({
    No: index + 1,
    nombre: ventaLibros.nombre,
    precio: ventaLibros.precio,
    disponible: ventaLibros.disponible ? "Disponible" : "No disponible"
}));
console.table(ventaLibrosconIndice)

/* RESPUESTA DE CONSOLA ENBEVIDA 
┌─────────┬────┬────────────────────────────────────────┬────────┬─────────────────┐
│ (index) │ No │ nombre                                 │ precio │ disponible      │
├─────────┼────┼────────────────────────────────────────┼────────┼─────────────────┤
│ 0       │ 1  │ 'Anatomía de las expresiones faciales' │ 1550   │ 'Disponible'    │
│ 1       │ 2  │ 'El cuerpo se cura a sí mismo'         │ 550    │ 'No disponible' │
│ 2       │ 3  │ 'Forma de la cabeza y el cuello'       │ 1550   │ 'Disponible'    │
│ 3       │ 4  │ 'Atlas clínico de puntos gatillo'      │ 1000   │ 'No disponible' │
│ 4       │ 5  │ 'Atlas de Tricoscopia'                 │ 1800   │ 'No disponible' │
└─────────┴────┴────────────────────────────────────────┴────────┴─────────────────┘
*/