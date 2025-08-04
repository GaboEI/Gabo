#===================================================================================================================
"""
!🧠 CLASE 19  FUNCIONES CON MÚLTIPLES PARÁMETROS Y DECISIONES CONDICIONALES
?📘 Objetivo de la clase:
Aprender a construir funciones más inteligentes, que reciban varios parámetros,
validen condiciones, y tomen decisiones distintas según cada caso.

*📌 CONTENIDO DE LA CLASE
?1. Teoría:
⏺️ Múltiples parámetros en funciones #!(def ejemplo(a, b, c=0))
⏺️ Uso de #![if, elif, else] para control de flujo
⏺️ Parámetros opcionales vs. obligatorios
⏺️ Buenas prácticas: funciones con lógica clara y mensajes consistentes

?2. Ejercicios:
todo: Tendrás 3 ejercicios:
| Nº   Nombre                                                   Concepto clave                           
| ---  -------------------------------------------------------  -----------------------------------------
| 1️⃣ | Verificar descuento válido con múltiple parámetro       | Parámetro obligatorio + opcional + lógica
| 2️⃣ | Validar acceso a una app con edad y contraseña opcional | `if / elif / else` + lógica compuesta     
| 3️⃣ | Clasificar notas con función y mensajes dinámicos       | Múltiples condiciones y retorno limpio 
"""
#===================================================================================================================
#!TEORIA EJERCICIO 1

#?🧠 TEORÍA  Funciones con múltiples parámetros y decisiones condicionales
#📌 ¿Qué son funciones con múltiples parámetros?
#Son funciones que reciben más de un dato de entrada, permitiendo operaciones más complejas y personalizadas.
#todo|| Ejemplo:
def registrar(nombre, edad, ciudad):
    ...

"""Puedes tener:
✅ Parámetros obligatorios (se deben pasar siempre)
✅ Parámetros opcionales (con valores por defecto)"""
def registrar(nombre, edad=18):
    ...
"""📌 ¿Qué es el control de flujo condicional?
Son estructuras como if, elif, y else que permiten ejecutar diferentes bloques de código según condiciones lógicas.
"""
#!🔹 Estructura:
#if condición_1:
    #hacer_algo()
#elif condición_2:
    #hacer_algo_distinto()
#else:
    #hacer_algo_por_defecto()

#!🔹 ¿Cuándo usar cada uno?
"""
| Palabra clave | ¿Cuándo se usa?                        |
| ------------- | -------------------------------------- |
| `if`          | Primera condición                      |
| `elif`        | Condiciones alternativas               |
| `else`        | Si ninguna de las anteriores se cumple |

#!📌 ¿Por qué es importante?
Porque la vida real no es lineal: las decisiones en sistemas reales (ventas, accesos, notas, descuentos, etc.)
se basan en condiciones:
“Si el usuario es cliente premium y su compra es mayor a 100€, entonces...”
Aprender a estructurar decisiones con múltiples parámetros te permite crear funciones profesionales,
inteligentes y reutilizables.

"""
#!📚 Ejemplo completo:
def aplicar_descuento(precio, cliente_premium=False):
    if cliente_premium:
        return precio * 0.8  # 20% de descuento
    else:
        return precio
#===================================================================================================================
#!TEORIA EJERCICIO 2

#!🧠 EJERCICIO 2 – CLASE 19
#*📌 Nombre: Validar acceso a una app con edad mínima y contraseña opcional

#?🧠 TEORÍA PROFUNDA
"""
#!1️⃣ ¿Qué es la lógica condicional compuesta?
Es cuando usas combinaciones de condiciones para tomar decisiones más específicas.

#*Ejemplo:
if edad >= 18 and clave == "1234":
    ...
Aquí estás diciendo:
"Solo pasa si se cumplen ambas condiciones a la vez"

#?🔹 Palabras clave importantes:
| Palabra | Función                           |
| ------- | --------------------------------- |
| `if`    | Evalúa una condición inicial      |
| `elif`  | Evalúa una alternativa            |
| `else`  | Ejecuta si no se cumple ninguna   |
| `and`   | Ambas condiciones deben cumplirse |
| `or`    | Basta con que una se cumpla       |

#!2️⃣ ¿Qué es una contraseña opcional?
Una contraseña opcional es un parámetro con valor por defecto.
#todo|| def acceso_usuario(edad, clave="0000"):
Esto significa que si el usuario no proporciona contraseña, el sistema usará #!"0000".

#!3️⃣ ¿Qué es una validación de acceso?
Es cuando decides si permitir o denegar algo a un usuario según reglas lógicas #!(edad, clave, permisos, etc.).

#!4️⃣ ¿Qué es el control de flujo?
Es el orden en que se ejecutan los bloques de código según las condiciones que se cumplan.

#!5️⃣ ¿Qué es una función con retorno booleano o textual?
Puedes hacer que la función retorne:
✅ True o False → si es solo validación
✅ "Acceso permitido" o "Acceso denegado" → si quieres un mensaje claro
"""
#===================================================================================================================
"""
#! 🧠 CLASE 19 EJERCICIO 3

#?📌 Nombre: Clasificar notas académicas con mensajes dinámicos
🔑 Tema central: múltiples condiciones `if / elif / else`, uso de rangos, funciones con retorno textual

#! 🎯 OBJETIVO DEL EJERCICIO
Crear una función que reciba una nota numérica (de 0 a 100)
y devuelva un mensaje de texto que clasifique esa nota** según un sistema de evaluación.

#! 🧠 TEORÍA PROFUNDA

#*1️⃣ ¿Qué son los rangos de valores?
Son intervalos numéricos que usamos para **tomar decisiones diferentes según el valor recibido**.

Ejemplo:

if nota >= 90:
    return "Excelente"
elif nota >= 80:
    return "Muy bien"

👉 Cada bloque `elif` evalúa un rango.

#*2️⃣ ¿Qué es la validación de rango?
Es asegurarte de que el dato **está dentro de un límite aceptable**, por ejemplo entre 0 y 100.

if nota < 0 or nota > 100:
    return "❌ Nota inválida"

#*3️⃣ ¿Por qué usar `elif` en vez de múltiples `if`?
Porque `elif` solo se evalúa si los anteriores **no se cumplen**, por lo que ahorra trabajo al programa
y mejora la lógica.

#* 4️⃣ Buenas prácticas en funciones de clasificación

| Práctica                         | ¿Por qué es buena?                                            |
| -------------------------------- | ------------------------------------------------------------- |
| Retorno textual                  | Hace la función más útil para interfaces, reportes o sistemas |
| Validación previa                | Previene errores silenciosos o lógicos                        |
| Rango de 0 a 100                 | Estándar académico en muchos países                           |
| `elif` ordenado de mayor a menor | Más eficiente, lógica descendente                             |

#* 📝 Sistema de evaluación propuesto:

| Rango de nota         Clasificación   
| --------------------  --------------- 
| 90 – 100              Excelente       
| 80 – 89               Muy bien        
| 70 – 079              Bien            
| 60 – 69               Aprobado justo  
| 00 – 59               Reprobado ❌     
| Cualquier otro valor  Nota inválida ❌ 
"""
#===================================================================================================================