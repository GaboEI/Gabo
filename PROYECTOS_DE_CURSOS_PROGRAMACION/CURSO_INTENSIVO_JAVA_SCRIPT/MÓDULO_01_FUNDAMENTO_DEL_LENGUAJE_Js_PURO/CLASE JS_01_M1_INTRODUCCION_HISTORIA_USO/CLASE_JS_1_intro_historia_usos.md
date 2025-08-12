# 📘 CLASE JS 1 – Introducción a JavaScript, historia y usos

## 🧠 Objetivo de la clase
Comprender qué es JavaScript, cómo surgió, dónde se usa y cómo comenzar a trabajar con él desde el navegador y archivos locales.

---

## 🧾 Contenido cubierto

- Qué es JavaScript y por qué es importante
- Historia resumida del lenguaje
- Ámbitos de uso profesional de JS
- Consola del navegador como herramienta de desarrollo
- Estructura básica HTML + JS
- Vinculación de archivos externos `.js`
- Exploración de DevTools en Chrome
- Primeros comandos en consola

---

## 📚 Teoría impartida

### ¿Qué es JavaScript?

JavaScript es un **lenguaje de programación de alto nivel**, interpretado, ligero, dinámico, orientado a objetos y multiparadigma, que se utiliza principalmente para crear interactividad en páginas web.

**Frase clave:** *"HTML estructura, CSS embellece, JavaScript da vida."*

### Características clave

- Ejecutado por los navegadores
- Interpretado (no requiere compilación)
- Permite programación funcional y orientada a objetos
- Trabaja con el DOM y eventos
- Se puede usar en frontend y backend (Node.js)

---

### Breve historia de JavaScript

| Año | Evento |
|-----|--------|
| 1995 | Brendan Eich crea JS en 10 días para Netscape |
| 1996 | Microsoft lanza JScript |
| 1997 | Se establece el estándar ECMAScript |
| 2009 | Nace Node.js |
| 2015 | Llega ES6 con mejoras modernas |
| 2020+ | JS domina frontend, backend y apps móviles |

---

### ¿Dónde se usa JS?

- Frontend web (interactividad, validaciones, eventos)
- Backend (Node.js)
- Apps móviles (React Native, Ionic)
- Automatización, testing, herramientas CLI
- Manipulación del DOM
- Consumo de APIs

---

## 🧪 Ejercicios realizados

### ✅ Ejercicio 1 – Comandos en consola

```js
// 1️⃣ Imprime un mensaje en pantalla
console.log("¡Hola, Gabo desde la consola de JavaScript!");

// 2️⃣ Realiza una suma
console.log(10 + 5);

// 3️⃣ Declara una variable y úsala
let nombre = "Gabo";
console.log("Tu nombre es: " + nombre);

// 4️⃣ Prueba una condición
console.log(10 > 3);

// 5️⃣ Usa typeof
console.log(typeof nombre);
```

🧠 Observaciones:
- `console.log()` es usado para imprimir resultados.
- `typeof` permite saber el tipo de dato.

---

### ✅ Ejercicio 2 – Archivo `.js` vinculado a HTML

**Estructura de archivos:**

```
ejercicio_2/
├── index.html
└── script.js
```

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi primer JavaScript externo</title>
</head>
<body>
  <h1>Hola Gabo desde HTML</h1>
  <script src="script.js"></script>
</body>
</html>
```

**script.js**
```js
console.log("🎉 ¡Hola, Gabo! Este mensaje viene desde un archivo JS externo.");

let saludo = "¡Bienvenido al mundo JavaScript profesional!";
console.log(saludo);

let resultado = 2025 - 1998;
console.log("Tu edad aproximada es: " + resultado);
```

🧠 Observaciones:
- `script.js` se ejecuta automáticamente al ser cargado.
- Los `console.log()` aparecen en DevTools (no en la pantalla HTML).
- La consola muestra:
```
🎉 ¡Hola, Gabo! Este mensaje viene desde un archivo JS externo.
¡Bienvenido al mundo JavaScript profesional!
Tu edad aproximada es: 27
```

---

### ✅ Ejercicio 3 – Exploración de DevTools

✅ Accediste correctamente a:
- Pestaña **Elementos** (DOM)
- Pestaña **Fuentes** (`Sources`) → Abriste `script.js`
- Añadiste **breakpoint** en `console.log(saludo)`
- Ejecutaste con depuración detenida
- Observaste el valor de la variable `saludo` paso a paso

💬 Resultado esperado:
- `console.log()` ejecutado parcialmente
- Código detenido en el breakpoint
- Variables visibles en el panel de seguimiento

---

## ✅ Calificación final: **10.5 / 10**

💬 Comentario del mentor:
> Clase ejecutada con excelencia técnica, disciplina en el flujo de trabajo, y alto compromiso por entender los conceptos. Gabo inicia el curso de JavaScript como un programador real: cuestionando, observando y construyendo con lógica.

---

## 🧩 Aplicación profesional

Todo lo aprendido en esta clase representa lo que hacen los frontend developers diariamente:

- Prueban código en consola
- Vinculan JS correctamente a HTML
- Usan DevTools para inspección, pruebas y debugging

---

## 📁 Estructura de carpetas recomendada para GitHub

```
MÓDULO_01_FUNDAMENTOS_DEL_LENGUAJE_JS_PURO/
└── CLASE_JS_1_intro_historia_usos/
    ├── index.html
    ├── script.js
    └── README.md (este archivo)
```

---

## 📌 Clase oficialmente cerrada

> 🎓 **Clase JS 1 – Concluida y aprobada con mención de excelencia**

---
