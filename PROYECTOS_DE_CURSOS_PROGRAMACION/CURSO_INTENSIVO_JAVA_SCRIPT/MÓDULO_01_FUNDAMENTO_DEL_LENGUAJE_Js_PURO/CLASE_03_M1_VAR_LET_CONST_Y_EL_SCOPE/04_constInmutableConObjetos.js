// EJERCICIO 4 – 04_constInmutableConObjetos.js

// 1️⃣ Declarar un objeto con const, con al menos 2 propiedades
const user = {
    name: "Ernesto", 
    userId: "98072216E",
    status: "pro"
};

// 2️⃣ Imprimir el objeto original
console.log(user); // Output: { name: 'Ernesto', userId: '98072216E', status: 'pro' }

// 3️⃣ Modificar una propiedad del objeto (userId)
user.userId = "0140052279"; 

// 5️⃣ Imprimir el objeto modificado
console.log(user); // Output: { name: 'Ernesto', userId: '0140052279', status: 'pro' }

// 6️⃣ Intentar reasignar el objeto completo a otra referencia (debe dar error)
/*user = {
    name: "Juan", 
    userId: "12345678",
    status: "none"
};
console.table(user); // Output: TypeError: Assignment to constant variable. */
//===============================================================================//

// 7️⃣ Declarar un array con const y algunos elementos
const myArray = [1, "Hello", true, 3.14];

// 8️⃣ Imprimir el array original
console.log(myArray); // Output: [1, "Hello", true, 3.14]

// 9️⃣ Usar métodos como push, pop, splice para modificar el contenido

//Push
myArray.push("addPush");
console.log(myArray); // Output:  1, 'Hello', true, 3.14, 'addPush' ]

// pop
const lastItem = myArray.pop();
console.log(myArray); // Output: [ 1, 'Hello', true, 3.14 ]
console.log(lastItem); // Output: addPush

// splice
myArray.splice(1,1); // Eliminar un elemento con splice
console.log(myArray); // Output: [ 1, true, 3.14 ]

myArray.splice(1,0, 'Hello'); // En la posición 1, añade 'Hello' sin eliminar elementos.
console.log(myArray); // Output: [ 1, 'Hello', true, 3.14 ]

myArray.splice(-1,1, '2.71'); // En la posición -1 o 3 elimina 1 elemento (' 3.14') y añade '2.71'
console.log(myArray); // Output: [ 1, 'Hello', true, '2.71' ]

// 1️⃣1️⃣ Intentar reasignar el array completo (debe dar error)
/*myArray = [2, "Hi", false, 360];
console.log(myArray); Output: TypeError: Assignment to constant variable.*/

// 1️⃣2️⃣ (Opcional) Usar Object.freeze() y probar si puedes modificar el objeto
Object.freeze(myArray); // Congela el array
console.log(Object.isFrozen(myArray)); // Output: true

/* 1️⃣3️⃣ Reflexión final: ¿Qué es realmente inmutable con const?
Con `const`, la referencia a la variable es inmutable, no su contenido. En objetos y arrays, 
las propiedades o elementos pueden modificarse, pero no se puede reasignar la variable a un nuevo 
objeto o array. Esto implica que debemos usar métodos como Object.freeze() para proteger el contenido 
si se necesita inmutabilidad total, y tener cuidado al compartir referencias para evitar modificaciones 
inesperadas. */
