# Clase 19 Modulo 1 – Pensamiento algorítmico: análisis y resolución paso a paso

## 🧱 Estructura completa de la clase

### 🎯 Objetivos pedagógicos

* Desarrollar **pensamiento algorítmico profesional** capaz de abordar problemas complejos.
* Aprender a **estructurar soluciones paso a paso** antes de codificar.
* Mejorar la **precisión y optimización** en la resolución de problemas.
* Aplicar el razonamiento lógico en contextos reales de programación.

### 📁 Nombres de ejercicios (formato `snake_case` listos para `.py`)

1. `01_algoritmo_suma_condicional.py`
2. `02_simulador_de_descuento.py`
3. `03_validar_edad_y_categoria.py`
4. `04_calculadora_pasos_pedidos.py`
5. `05_revisar_credito_simplificado.py`

---

## 🧠 1. Introducción al pensamiento algorítmico

En programación, **pensar algorítmicamente** significa ser capaz de analizar un problema y traducirlo en una secuencia de pasos lógicos, claros y finitos que una máquina pueda ejecutar.
No se trata solo de escribir código: es **diseñar la solución antes de programar**.

**Analogía:**
Un chef no se pone a cocinar sin una receta clara. El algoritmo es esa receta: lista de ingredientes (entradas), pasos ordenados (proceso) y el plato final (salida).

---

## 📜 2. Elementos clave de un algoritmo

1. **Entradas**: Datos que recibe el programa para procesar.
   Ejemplo: número de unidades de un producto y precio por unidad.
2. **Procesos**: Instrucciones que manipulan las entradas para producir un resultado.
   Ejemplo: multiplicar unidades por precio y aplicar descuentos.
3. **Salidas**: Resultados obtenidos tras procesar las entradas.
   Ejemplo: precio final con impuestos incluidos.
4. **Condiciones**: Decisiones que alteran el flujo del algoritmo según una situación.
   Ejemplo: si la cantidad comprada supera 10, aplicar descuento.
5. **Repeticiones**: Ciclos que ejecutan una parte del algoritmo múltiples veces.
   Ejemplo: revisar una lista de pedidos uno por uno.

---

## 🛠 3. Fases para resolver un problema algorítmicamente

### 3.1 Comprensión del problema

* **Objetivo:** Saber exactamente qué se debe lograr.
* Preguntas clave:

  * ¿Qué datos necesito?
  * ¿Qué restricciones existen?
  * ¿Cuál es el formato de salida esperado?

**Error común:** empezar a programar sin entender completamente el enunciado.

---

### 3.2 Planteamiento de la solución

Aquí NO se escribe código. Se piensa:

* Pasos lógicos a seguir.
* Orden de las operaciones.
* Casos especiales que pueden romper el algoritmo.

---

### 3.3 Representación de la solución

Para esto usamos **diagramas de flujo** (en tu formato textual) o pseudocódigo.

**Ejemplo – Algoritmo para calcular el precio final de una compra con descuento:**

```.
Inicio
↓
Pedir cantidad y precio unitario
↓
Calcular subtotal = cantidad × precio_unitario
↓
SI cantidad > 10
   ├── Aplicar descuento del 10%
   └── Calcular total con descuento
SINO
   └── Total = subtotal
↓
Mostrar total al usuario
↓
Fin
```

---

### 3.4 Implementación en código

Cuando el diagrama está listo, el código se convierte en una **traducción directa** de la lógica.

---

### 3.5 Pruebas y validación

* Usar datos de prueba variados (casos normales, límites y errores).
* Validar que las salidas sean correctas en todos los casos.

---

## ⚙️ 4. Buenas prácticas al diseñar algoritmos

1. **Divide y vencerás**: divide problemas grandes en subproblemas manejables.
2. **Evita la ambigüedad**: cada paso debe ser claro y sin interpretaciones múltiples.
3. **Minimiza la complejidad**: menos pasos no siempre significa mejor, pero sí más eficiencia.
4. **Piensa en casos límite**: ¿qué pasa si el usuario mete un 0, un número negativo o un texto?
5. **Prueba mentalmente**: simula el algoritmo con lápiz y papel antes de programar.

---

## 🏗 5. Ejemplo profesional – Validación de edad para un sistema de acceso

**Objetivo:** Determinar si un usuario puede entrar a un evento según su edad.

**Entradas:** Edad del usuario.
**Proceso:**

* Si es menor de 0 o mayor de 120 → error.
* Si tiene menos de 18 años → acceso denegado.
* Si tiene entre 18 y 60 → acceso permitido.
* Si tiene más de 60 → acceso permitido con descuento.

**Diagrama textual:**

```.
Inicio
↓
Pedir edad
↓
SI edad < 0 O edad > 120
   └── Mostrar "Edad inválida"
SINO SI edad < 18
   └── Mostrar "Acceso denegado"
SINO SI edad <= 60
   └── Mostrar "Acceso permitido"
SINO
   └── Mostrar "Acceso permitido con descuento"
↓
Fin
```

---

## 📈 6. Aplicación profesional del pensamiento algorítmico

En el mundo real, este enfoque se usa en:

* **Automatización empresarial**: flujos de facturación, control de inventarios.
* **Desarrollo de videojuegos**: inteligencia artificial de NPCs.
* **Sistemas críticos**: control de tráfico aéreo, diagnósticos médicos asistidos por software.
* **Procesamiento de datos**: análisis y filtrado de grandes volúmenes de información.

Un algoritmo bien diseñado es **fácil de mantener**, **eficiente** y **escalable**.

---

Perfecto, seguimos con la **segunda parte** de la teoría de la **Clase 19 – Pensamiento algorítmico: análisis y resolución paso a paso**.

---

## 🔄 7. Algoritmos iterativos y condicionales complejos

En problemas reales, rara vez un algoritmo es lineal.
A menudo incluye **ramificaciones** (condiciones) y **bucles** (iteraciones).

### 7.1 Algoritmos con múltiples condiciones

Cuando hay que evaluar varios criterios en orden, es importante:

* Usar **estructura clara** (`if / elif / else`)
* Ordenar las condiciones desde **más restrictiva** a **menos restrictiva**
* Evitar redundancia en las verificaciones

**Ejemplo – Sistema de envío de paquetes:**

```.
Inicio
↓
Pedir peso y destino
↓
SI peso <= 0
   └── Mostrar "Peso inválido"
SINO SI destino == "internacional"
   ├── Calcular costo = peso × tarifa_internacional
   └── Mostrar costo
SINO
   ├── Calcular costo = peso × tarifa_nacional
   └── Mostrar costo
↓
Fin
```

---

### 7.2 Algoritmos iterativos

Cuando debemos **repetir** una acción hasta cumplir una condición, usamos bucles.

Ejemplo: sumar precios de productos hasta que el usuario indique "fin".

```.
Inicio
↓
total = 0
↓
REPETIR
   ├── Pedir precio
   ├── SI precio != "fin"
   │     └── total = total + precio
   └── SI precio == "fin" → salir del bucle
↓
Mostrar total
↓
Fin
```

---

## ⚡ 8. Estrategias de optimización algorítmica

### 8.1 Reducción de pasos innecesarios

Un algoritmo puede funcionar pero ser **ineficiente**.

* Evitar cálculos repetidos
* Usar variables para almacenar resultados intermedios

### 8.2 Algoritmos “perezosos” (lazy evaluation)

Procesar solo lo que es necesario, cuando es necesario.
Ejemplo: en una búsqueda, detenerse en el primer resultado encontrado.

### 8.3 Complejidad temporal y espacial

* **Tiempo**: cuántas operaciones se ejecutan
* **Espacio**: cuánta memoria se consume
  En proyectos reales, optimizar uno puede afectar al otro.

---

## 🚫 9. Errores comunes al diseñar algoritmos

1. **No considerar casos límite**: entradas vacías, negativas o muy grandes.
2. **Flujos circulares sin salida**: bucles infinitos por no definir bien la condición de salida.
3. **Duplicación de código**: repite la misma lógica varias veces en lugar de crear un bloque reutilizable.
4. **Ambigüedad** en el planteamiento: pasos que no indican claramente qué hacer.
5. **Ignorar validaciones**: confiar en que el usuario ingresará datos correctos.

---

## 📝 10. Cómo documentar un algoritmo profesionalmente

En la industria, un algoritmo bien documentado debe incluir:

* **Título y descripción breve**
* **Lista de entradas y salidas**
* **Diagrama de flujo textual** o gráfico
* **Notas sobre casos especiales**
* **Complejidad estimada** (básico en Big O si es relevante)
* **Ejemplos de uso**

Ejemplo de documentación:

```_
Título: Algoritmo de cálculo de precio final con descuento
Entradas: cantidad (int), precio_unitario (float)
Salidas: total (float)
Flujo:
Inicio → pedir datos → calcular subtotal → aplicar descuento si corresponde → mostrar total
Casos especiales: cantidad <= 0 → error; precio_unitario <= 0 → error
Complejidad: O(1)
```

---

## 🌍 11. Aplicación profesional en empresas

En un entorno real, diseñar un buen algoritmo:

* Reduce **costos de mantenimiento**
* Mejora la **velocidad de desarrollo**
* Evita errores en producción
* Facilita que otros programadores **entiendan y modifiquen** el código

Ejemplos:

* **E-commerce**: cálculo de descuentos y promociones.
* **Bancos**: validación de transacciones según reglas de negocio.
* **Logística**: optimización de rutas de entrega.
* **IA**: preprocesamiento de datos antes de entrenar un modelo.

---

## 🟥 Ejercicio 1: Algoritmo suma condicional

## 🟥 Breve teoría puntual

Este ejercicio aplica **pensamiento algorítmico con suma condicional**.
La idea central es **sumar dos o más números** y **aplicar una condición lógica** para decidir una acción adicional, por ejemplo, verificar si el resultado cumple un criterio.

**Definiciones clave:**

* **Condicional (`if / elif / else`)**: estructura que permite ejecutar bloques de código solo si se cumple una condición booleana.
* **Operador de comparación**: `>`, `<`, `==`, `!=`, `>=`, `<=`. Usado para evaluar relaciones entre valores.
* **Entrada del usuario**: datos proporcionados por el usuario (por ejemplo, mediante `input()`), que deben validarse.
* **Salida**: mensaje final que informa el resultado y, en caso necesario, la evaluación de la condición.

**Lógica general del ejercicio:**

1. Recibir dos números del usuario.
2. Sumar ambos.
3. Verificar si el resultado cumple la condición definida (ejemplo: mayor a cierto valor).
4. Mostrar el resultado y un mensaje según el caso.

---

## 🟥 Ejemplo mínimo ilustrativo

**Escenario simple**:

* Usuario ingresa `7` y `5`.
* Suma = `12`.
* Si la suma es mayor a `10`, mostrar mensaje especial; si no, mensaje estándar.

Este ejemplo es solo para ilustrar la lógica, no es la solución del ejercicio.

---

## 🟥 Diagrama de flujo textual

```.
Inicio
↓
Pedir primer número
↓
Pedir segundo número
↓
Calcular suma = primer + segundo
↓
SI suma cumple condición establecida
   └── Mostrar mensaje especial
SINO
   └── Mostrar mensaje estándar
↓
Fin
```

---

## 🟥 RESPUESTA EJERCICIO 1

```python
#=== SCRIPT ===#
numero1 = float(input("🔢 Ingrese el primer número: "))
numero2 = float(input("🔢 Ingrese el segundo número: "))

resultado = numero1 + numero2

if resultado > 10:
    print(f"La suma es {resultado}, que es mayor que 10.")
else:
    print(f"La suma es {resultado}, que es 10 o menor.")

#=== RESPUESTA DE LA CONSOLA ===#
"""
EJEMPLO 1:
🔢 Ingrese el primer número: 2
🔢 Ingrese el segundo número: 3
La suma es 5.0, que es 10 o menor.

EJEMPLO 2:
🔢 Ingrese el primer número: 10
🔢 Ingrese el segundo número: 10
La suma es 20.0, que es mayor que 10.
"""
```

## 🟧 Ejercicio 02 – Simulador de descuento

---

## 🟧 Breve teoría puntual

Este ejercicio aplica **cálculo de descuentos con condicionales**.
La lógica principal consiste en:

1. **Recibir el precio y la cantidad de un producto**.
2. **Determinar si se aplica un descuento** según una condición (por ejemplo, cantidad mínima o monto total).
3. **Calcular el precio final** considerando el descuento si aplica.
4. **Mostrar al usuario el detalle del precio**: subtotal, descuento aplicado (o no) y total a pagar.

**Definiciones clave:**

* **Descuento porcentual**: reducción expresada como porcentaje del precio original (ej. 15%).
* **Condicional (`if / else`)**: estructura que decide si aplicar el descuento.
* **Validación**: asegurarse de que la cantidad y el precio no sean negativos o cero.

---

## 🟧 Ejemplo mínimo ilustrativo

Supongamos que el descuento es del **10%** si compras más de **5 unidades**.

* **Entrada:** precio = 20, cantidad = 6
* **Subtotal:** 20 × 6 = 120
* Como cantidad > 5 → aplicar 10% de descuento: 120 × 0.10 = 12
* **Total:** 120 − 12 = 108

Este ejemplo es solo para entender la lógica, no es la solución final del ejercicio.

---

## 🟧 Diagrama de flujo textual (estándar Gabo)

```.
Inicio
↓
Pedir precio unitario
↓
Pedir cantidad
↓
Calcular subtotal = precio × cantidad
↓
SI cantidad cumple condición de descuento
   ├── Calcular monto de descuento
   └── Calcular total = subtotal − descuento
SINO
   └── Total = subtotal
↓
Mostrar subtotal, descuento (si aplica) y total
↓
Fin
```

---

## 🟧 RESPUESTA EJERCICIO 2

```python
#=== SCRIPT ===#
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

subtotal = precio_unitario * cantidad

if cantidad > 5:

    descuento = subtotal * 0.10  
else:
    descuento = 0

total_final = subtotal - descuento

print(f"Subtotal: ${subtotal:.2f}")
if descuento > 0:
    print(f"Descuento aplicado (10%): ${descuento:.2f}")
else:
    print("No se aplicó descuento.")
print(f"Total final: ${total_final:.2f}")

#=== RESPUESTA DE LA CONSOLA ===#
"""
EJEMPLO 1:
Ingrese el precio unitario del producto: 77
Ingrese la cantidad de productos: 5
Subtotal: $385.00
No se aplicó descuento.
Total final: $385.00
"""
```

---

## 🟨 Ejercicio 03 – Validar edad y categoria

## 🟨 Breve teoría puntual

Este ejercicio aplica **validación de datos** y **clasificación por rangos** usando condicionales.
La idea central es:

1. Solicitar la edad de una persona.
2. Validar que sea un número entero positivo y dentro de un rango lógico (por ejemplo, 0 a 120 años).
3. Clasificar a la persona en una **categoría** según la edad (niño, adolescente, adulto, adulto mayor, etc.).
4. Mostrar el resultado con un mensaje claro.

**Definiciones clave:**

* **Validación de entrada:** Comprobar que los datos son del tipo correcto y cumplen reglas de negocio.
* **Clasificación por rangos:** Asignar una etiqueta según un valor numérico que cae en un rango definido.
* **Condicional múltiple (`if / elif / else`):** Permite manejar más de dos posibles rutas lógicas.

---

## 🟨 Ejemplo mínimo ilustrativo

**Categorías de ejemplo:**

* Edad < 0 o > 120 → entrada inválida.
* 0 a 12 → Niño.
* 13 a 17 → Adolescente.
* 18 a 59 → Adulto.
* 60 o más → Adulto mayor.

**Ejemplo:**
Entrada: `edad = 45` → Clasificación: Adulto.

---

## 🟨 Diagrama de flujo textual

```\
Inicio
↓
Pedir edad
↓
SI edad < 0 O edad > 120
   └── Mostrar "Edad inválida"
SINO SI edad <= 12
   └── Categoría = "Niño"
SINO SI edad <= 17
   └── Categoría = "Adolescente"
SINO SI edad <= 59
   └── Categoría = "Adulto"
SINO
   └── Categoría = "Adulto mayor"
↓
Mostrar categoría al usuario
↓
Fin
```

---

## 🟨 RESPUESTA EJERCICIO 3

```python
#=== SCRIPT ===
while True:
    edad_str = input("👉 Por favor, introduce tu edad: ")
    try:
        edad = int(edad_str)
        if 0 <= edad <= 120:
            break
        else:
            print(f"⚠️ ¡Error! La edad '{edad}' no es un valor lógico. Por favor, introduce una edad entre 0 y 120.")
            
    except ValueError:
        print("❌ ¡Error! Eso no parece un número. Por favor, introduce un número entero.")

if edad < 13:
    categoria = "👶 Niño"
elif 13 <= edad < 18:
    categoria = "🧑‍🦱 Adolescente"
elif 18 <= edad < 65:
    categoria = "👨 Adulto"
else:  
    categoria = "👵 Adulto mayor"

print(f"🎉 ¡Genial! Tu categoría es: **{categoria}**.")
print("¡Gracias por usar nuestro programa! 😊")

#=== REAPUESTAS DE CONSOLA ===
"""
Ejemplo 1: Entrada válida
Salida de la consola:
👉 Por favor, introduce tu edad: 35
🎉 ¡Genial! Tu categoría es: **👨 Adulto**.
¡Gracias por usar nuestro programa! 😊

Ejemplo 2: Entrada no numérica
Salida de la consola:
👉 Por favor, introduce tu edad: hola
❌ ¡Error! Eso no parece un número. Por favor, introduce un número entero.
👉 Por favor, introduce tu edad: 25
🎉 ¡Genial! Tu categoría es: **👨 Adulto**.
¡Gracias por usar nuestro programa! 😊

Ejemplo 3: Entrada fuera de rango
Salida de la consola:
👉 Por favor, introduce tu edad: 150
⚠️ ¡Error! La edad '150' no es un valor lógico. Por favor, introduce una edad entre 0 y 120.
👉 Por favor, introduce tu edad: 17
🎉 ¡Genial! Tu categoría es: **🧑‍🦱 Adolescente**.
¡Gracias por usar nuestro programa! 😊
"""
```

## 🟩 Ejercicio 04 – Calculadora pasos pedidos

---

## 🟩 Breve teoría puntual

Este ejercicio combina **pensamiento algorítmico secuencial**, **operaciones matemáticas** y **estructura clara de entradas y salidas**.
El objetivo es **simular un cálculo basado en un proceso paso a paso**, donde el usuario ingresa datos de un pedido, y el sistema responde con el cálculo final.

Este tipo de algoritmo es común en entornos como:

* Sistemas de pedidos online
* Terminales de venta en comercios
* Aplicaciones móviles de delivery
* Automatización de procesos empresariales

---

## 🟩 Escenario de ejemplo para este ejercicio

Supón que el programa debe calcular el **total a pagar por un pedido**, aplicando además **una tarifa de envío** y **un impuesto**.
La lógica podría ser así:

1. Ingresar el precio del producto.
2. Ingresar la cantidad deseada.
3. Calcular el subtotal.
4. Aplicar un impuesto fijo (por ejemplo, 8%).
5. Sumar un cargo de envío (por ejemplo, 5 unidades monetarias).
6. Mostrar todos los valores desglosados.

---

## 🟩 Diagrama de flujo con validación y manejo de errores

```-
Inicio
↓
INICIAR bucle principal (while True)
├── Pedir precio del producto
│   ├── Intentar convertir a float (try)
│   │   ├── Si éxito → ¿precio > 0?
│   │   │   ├── Sí → continuar
│   │   │   └── No → mostrar error, repetir
│   │   └── Si falla (ValueError) → mostrar error, repetir
↓
SALIR del bucle cuando precio válido
↓
INICIAR segundo bucle (while True)
├── Pedir cantidad de productos
│   ├── Intentar convertir a int (try)
│   │   ├── Si éxito → ¿cantidad > 0?
│   │   │   ├── Sí → continuar
│   │   │   └── No → mostrar error, repetir
│   │   └── Si falla (ValueError) → mostrar error, repetir
↓
SALIR del bucle cuando cantidad válida
↓
Calcular subtotal = precio × cantidad
↓
Calcular impuesto = subtotal × 0.08
↓
Asignar tarifa de envío = 5.0
↓
Calcular total = subtotal + impuesto + envío
↓
Mostrar desglose formateado:
   ├── Subtotal
   ├── Impuesto
   ├── Envío
   └── Total
↓
Fin
```

---

## 🟩 RESPUESTA EJERCICIO 4

```python
#=== SCRIPT ===#
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio > 0:
            break  
        else:
            print("Error: El precio debe ser un número positivo. Inténtelo de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de productos: "))
        if cantidad > 0:
            break  
        else:
            print("Error: La cantidad debe ser un número entero positivo. Inténtelo de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número entero.")

subtotal = precio * cantidad
impuesto = subtotal * 0.08
envio = 5.0
total = subtotal + impuesto + envio

print("\n--- Desglose de la compra ---")
print(f"Subtotal: €{subtotal:.2f}")
print(f"Impuesto (8%): €{impuesto:.2f}")
print(f"Envío: €{envio:.2f}")
print("-----------------------------")
print(f"Total: €{total:.2f}")

#=== REAPUESTAS DE CONSOLA ===#
"""
Ejemplo 1:
Ingrese el precio del producto: 2000
Ingrese la cantidad de productos: 41

--- Desglose de la compra ---
Subtotal: €82000.00
Impuesto (8%): €6560.00
Envío: €5.00
-----------------------------
Total: €88565.00

Ejemplo 2:
Ingrese el precio del producto: redf**
Error: Entrada no válida. Por favor, ingrese un número.
Ingrese el precio del producto: 
"""
```

---

## 🏁 Ejercicio 05 – Revisar credito simplificado

---

### 🏁 Enunciado

Crea un programa que evalúe si un cliente es **apto para recibir un crédito básico**, según tres condiciones:

1. **Edad** del cliente: debe ser mayor o igual a 21 años
2. **Ingresos mensuales**: deben ser al menos 1500 unidades monetarias
3. **Historial crediticio** (respuesta del usuario): debe responder **"bueno"** o **"excelente"**

---

El programa debe:

* Pedir los tres datos al usuario, con validación de errores y bucles.
* Mostrar al final un mensaje claro:

  * Si cumple las 3 condiciones → “✅ Crédito aprobado”
  * Si no las cumple → “❌ Crédito rechazado”
  * (Opcional) Puede indicar **cuál o cuáles condiciones no cumplió**

---

### 🏁  Diagrama de flujo con validaciones robustas y bucles autocontenidos

```.
Inicio
↓
INICIAR bucle para edad
├── Pedir edad
├── Intentar convertir a entero
│   ├── Si falla → mostrar error y repetir
│   └── Si éxito →
│       ├── ¿Edad ≥ 0?
│       │   ├── Sí → continuar
│       │   └── No → mostrar error y repetir
↓
INICIAR bucle para ingresos
├── Pedir ingresos mensuales
├── Intentar convertir a float
│   ├── Si falla → mostrar error y repetir
│   └── Si éxito →
│       ├── ¿Ingreso ≥ 0?
│       │   ├── Sí → continuar
│       │   └── No → mostrar error y repetir
↓
INICIAR bucle para historial crediticio
├── Pedir historial (bueno/excelente)
├── Convertir a minúsculas
│   ├── ¿Historial válido?
│   │   ├── Sí → continuar
│   │   └── No → mostrar error y repetir
↓
Evaluar condiciones:
├── Edad ≥ 21 ?
├── Ingreso ≥ 1500 ?
├── Historial == "bueno" o "excelente" ?
↓
¿TODAS las condiciones se cumplen?
├── Sí → Mostrar “✅ Crédito aprobado”
└── No → Mostrar “❌ Crédito rechazado” (opcional: indicar cuáles fallaron)
↓
Fin

```

---

### 🏁 Esqueleto guía comentado

```python
#=== 🏁 Ejercicio 05 – Revisar crédito simplificado ===#

def revisar_credito_simplificado():
    # Constantes para valores fijos
    EDAD_MINIMA = 21
    INGRESOS_MINIMOS = 1500
    HISTORIAL_VALIDO = ["b", "e"]
    MENSAJE_REINTENTAR = "Inténtelo nuevamente."

    # Entrada y validación del nombre
    while True:
        nombre_completo = input("👤 Por favor, ingrese su nombre completo (solo letras y espacios): ")
        nombre_limpio = nombre_completo.strip()

        if not nombre_limpio:
            print(f"🚫 El nombre no puede estar vacío. {MENSAJE_REINTENTAR}")
        elif not all(palabra.isalpha() for palabra in nombre_limpio.split()):
            print(f"❌ El nombre solo puede contener letras. {MENSAJE_REINTENTAR}")
        else:
            nombre_formateado = ' '.join(palabra.capitalize() for palabra in nombre_limpio.split())
            print("✅ Nombre ingresado correctamente.")
            print(f"👋 ¡Bienvenido, {nombre_formateado}!")
            break

    # Entrada y validación de la edad
    while True:
        try:
            edad = int(input(f"🎂 {nombre_formateado}, por favor ingrese su edad: "))
            if edad <= 0:
                print(f"❌ La edad debe ser un número positivo. {MENSAJE_REINTENTAR}")
                continue
            else:
                print("✅ Edad ingresada correctamente.")
                break
        except ValueError:
            print(f"🚫 La edad debe ser un número entero. {MENSAJE_REINTENTAR}")

    # Entrada y validación de los ingresos
    while True:
        try:
            ingresos = float(input(f"💸 {nombre_formateado}, por favor ingrese sus ingresos mensuales: "))
            if ingresos <= 0:
                print(f"❌ Los ingresos deben ser un número positivo. {MENSAJE_REINTENTAR}")
                continue
            else:
                print("✅ Ingresos ingresados correctamente.")
                break
        except ValueError:
            print(f"🚫 Los ingresos deben ser un número válido. {MENSAJE_REINTENTAR}")

    # Entrada y validación del historial crediticio
    while True:
        pedir_historial = input(f"✍️ {nombre_formateado}, por favor indique si su historial crediticio es bueno o excelente [b/e]: ")
        pedir_historial_minuscula = pedir_historial.lower()

        if pedir_historial_minuscula in HISTORIAL_VALIDO:
            print(f"🎉 ¡Felicidades, {nombre_formateado}! Su historial crediticio es válido.")
            break
        else:
            print(f"🚫 Opción inválida. Por favor, escriba 'b' o 'e' para continuar. {MENSAJE_REINTENTAR}")

    # Evaluar condiciones para aprobar o rechazar el crédito
    if edad >= EDAD_MINIMA and ingresos >= INGRESOS_MINIMOS and pedir_historial_minuscula in HISTORIAL_VALIDO:
        print(f"🪙 ¡Felicidades, {nombre_formateado}! Su crédito ha sido aprobado.")
    else:
        print(f"🥹 Lo sentimos, {nombre_formateado}. Su crédito ha sido rechazado.")

    # Mensaje final
    print(f"🏦 Gracias por usar nuestro sistema de crédito, {nombre_formateado}. Vuelva pronto.")

revisar_credito_simplificado()

#=== REAPUESTAS DE CONSOLA ===#
"""
👤 Por favor, ingrese su nombre completo (solo letras y espacios): gabo123
❌ El nombre solo puede contener letras. Inténtelo nuevamente.
👤 Por favor, ingrese su nombre completo (solo letras y espacios):   Gabriel ESPINOSA
✅ Nombre ingresado correctamente.
👋 ¡Bienvenido, Gabriel Espinosa!
🎂 Gabriel Espinosa, por favor ingrese su edad: 27ANOS
🚫 La edad debe ser un número entero. Inténtelo nuevamente.
🎂 Gabriel Espinosa, por favor ingrese su edad: -8
❌ La edad debe ser un número positivo. Inténtelo nuevamente.
🎂 Gabriel Espinosa, por favor ingrese su edad: 27
✅ Edad ingresada correctamente.
💸 Gabriel Espinosa, por favor ingrese sus ingresos mensuales: MUCHOS
🚫 Los ingresos deben ser un número válido. Inténtelo nuevamente.
💸 Gabriel Espinosa, por favor ingrese sus ingresos mensuales: -9
❌ Los ingresos deben ser un número positivo. Inténtelo nuevamente.
💸 Gabriel Espinosa, por favor ingrese sus ingresos mensuales: 9000.56
✅ Ingresos ingresados correctamente.
✍️ Gabriel Espinosa, por favor indique si su historial crediticio es bueno o excelente [b/e]: BUENICIMO
🚫 Opción inválida. Por favor, escriba 'b' o 'e' para continuar. Inténtelo nuevamente.
✍️ Gabriel Espinosa, por favor indique si su historial crediticio es bueno o excelente [b/e]: e
🎉 ¡Felicidades, Gabriel Espinosa! Su historial crediticio es válido.
🪙 ¡Felicidades, Gabriel Espinosa! Su crédito ha sido aprobado.
🏦 Gracias por usar nuestro sistema de crédito, Gabriel Espinosa. Vuelva pronto.
"""
```

---
