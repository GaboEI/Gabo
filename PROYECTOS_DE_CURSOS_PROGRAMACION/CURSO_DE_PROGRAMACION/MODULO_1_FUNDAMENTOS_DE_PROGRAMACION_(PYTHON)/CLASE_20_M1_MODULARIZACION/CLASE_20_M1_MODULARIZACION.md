# 📘 Clase 20 — Modularización: separar código en funciones prácticas

## 🔢 Número de ejercicios

📌 **Total: 5 ejercicios obligatorios + 1 opcional**

---

## 📁 Nombres de los ejercicios (listos para `.py`)

1. `01_saludo_modular.py`
2. `02_validar_correo_modular.py`
3. `03_calculadora_modular.py`
4. `04_registro_usuarios_modular.py`
5. `05_menu_modular_con_funciones.py`
6. *(Opcional)* `06_modulo_utilidades_personalizadas.py`

---

¡Perfecto, Gabo! 🎯
Arrancamos oficialmente la **Clase 20 — Modularización: separar código en funciones prácticas** 🧠💻
Prepárate para sumergirte en uno de los pilares del desarrollo profesional de software.

---

## 🧠 TEORÍA PROFUNDA — MODULARIZACIÓN EN PYTHON

## 📌 ¿Qué es la modularización?

> **Modularizar** significa **dividir un programa en bloques funcionales llamados *módulos*** o *funciones*, cada uno con una tarea específica.
> En Python, esto se logra con funciones (`def`) que encapsulan lógica y pueden reutilizarse.
> Es el primer paso hacia el desarrollo **profesional**, **escalable** y **mantenible**.

---

## 🧱 ¿Por qué es tan importante?

| Ventaja                            | Explicación                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| ✅ **Reutilización**                | Puedes usar una función varias veces sin reescribir código.                        |
| 🔄 **DRY (Don’t Repeat Yourself)** | Evita repetir bloques similares en diferentes partes del programa.                 |
| 🧼 **Legibilidad**                 | El código modular es más limpio, más fácil de entender y documentar.               |
| 🔧 **Mantenimiento**               | Si algo cambia, solo modificas el módulo correspondiente.                          |
| 📦 **Organización**                | Puedes separar lógicas en archivos distintos (lo verás más adelante).              |
| 🤝 **Colaboración**                | Facilita el trabajo en equipo: cada persona puede trabajar en un módulo diferente. |

---

## 🧬 ¿Qué es una función modular?

Una **función modular**:

* Tiene **un solo propósito**
* Recibe datos a través de **parámetros**
* Devuelve resultados con **`return`**
* No se mezcla con lógica de entrada/salida (idealmente)

---

## 🧠 Pensamiento modular vs código plano

### 🔴 Código plano (malo para escalar)

```python
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")
```

### 🟢 Código modular

```python
def pedir_nombre():
    return input("¿Cuál es tu nombre? ")

def saludar(nombre):
    print(f"Hola {nombre}!")

nombre_usuario = pedir_nombre()
saludar(nombre_usuario)
```

👉 *Aunque parezca más largo, el código modular es mucho más limpio y profesional.*

---

## 💎 Principios que rigen la modularización

| Principio                                      | Explicación                                                     |
| ---------------------------------------------- | --------------------------------------------------------------- |
| 🎯 **SRP (Responsabilidad única)**             | Cada función hace UNA cosa bien.                                |
| 🪞 **Transparencia**                           | El nombre de la función debe describir exactamente lo que hace. |
| 🔁 **Reutilizable**                            | Que se pueda usar en múltiples partes del código.               |
| 📤 **No efectos secundarios ocultos**          | No debe alterar otras partes del programa sin que se note.      |
| 🛡️ **Control de errores dentro de funciones** | Manejo robusto de errores con `try/except` interno.             |

---

## 🧪 Buenas prácticas profesionales

| ✅ Recomendado                              | ❌ Evitar                                       |
| ------------------------------------------ | ---------------------------------------------- |
| Usar nombres claros: `validar_email()`     | Nombres genéricos como `funcion1()`            |
| Pasar argumentos bien definidos            | Usar variables globales                        |
| Documentar con docstrings                  | Poner lógica compleja sin comentarios          |
| Retornar valores, no imprimir directamente | Mezclar lógica, input y output sin modularizar |

---

## ⚙️ Aplicación profesional

### 🏢 En empresas reales

* Los proyectos grandes se dividen en **módulos** → paquetes → librerías → servicios.
* Modularizar es el primer paso para **convertir tu código en una API o microservicio**.
* Permite que múltiples desarrolladores trabajen sobre diferentes partes sin conflictos.

### 🧑‍💻 Como programador freelance

* Tus scripts se verán **pro**, organizados, confiables.
* Puedes empaquetar tus funciones en librerías personales (`utils.py`, `email_tools.py`, `cleaning.py`, etc.)
* Te abre la puerta a automatizar procesos de forma robusta.

---

## 🔁 Flujo lógico para modularizar un script

```.
Inicio
↓
Identificar partes del código que se repiten
↓
Detectar bloques lógicos con una única responsabilidad
↓
Extraer cada bloque en una función bien nombrada
↓
Probar cada función individualmente (unit testing)
↓
Armar el flujo principal llamando a las funciones
↓
Documentar el código
↓
Fin
```

---

## 🔧 Tipos de funciones más comunes al modularizar

| Tipo                     | Ejemplo                                      |
| ------------------------ | -------------------------------------------- |
| 🔣 Validación            | `validar_email()`, `es_numero_positivo()`    |
| 🎛️ Lógica de cálculo    | `calcular_descuento()`, `obtener_promedio()` |
| 📥 Entrada/Salida        | `pedir_datos_usuario()`, `mostrar_menu()`    |
| 📁 Lectura/archivo       | `guardar_en_archivo()`, `leer_archivo_csv()` |
| 🔄 Reutilización general | `formatear_texto()`, `limpiar_entrada()`     |

---

## 📦 Avance futuro: modularización real con archivos

Muy pronto verás que puedes guardar funciones en **otros archivos `.py`**, y luego importarlas con:

```python
from utilidades import validar_email
```

Ese será tu paso hacia la **programación escalable y profesional real**.

---

## 📚 Documentación oficial

📖 [Función `def` en Python — documentación oficial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

---

¡Excelente, Gabo! 🧠💪
Comenzamos con el primer ejercicio práctico de esta clase fundamental:

---

## 🧪 **Ejercicio 01 — saludo\_modular.py**

🎯 **Objetivo:** Aprender a separar la lógica de entrada, procesamiento y salida en funciones simples y reutilizables.

---

### 🧭 Diagrama de flujo (estilo Gabo)

```>>>
Inicio
↓
Llamar a pedir_nombre()
    ↓
    ├── Mostrar mensaje "¿Cuál es tu nombre?"
    ↓
    ├── 🟥 Limpiar entrada con .strip()
    ↓
    ├── 🟥 Validar que no esté vacío
    │   └── Si está vacío → Mostrar error y repetir
    ↓
    ├── 🟥 Validar que contenga letras (no solo números)
    │   └── Si no es válido → Mostrar error y repetir
    ↓
    └── 🟥 Formatear nombre con .title()
    ↓
    Retornar nombre validado
↓
Llamar a saludar_usuario(nombre)
    └── Mostrar saludo: "¡Hola, [Nombre]! Bienvenido al sistema."
↓
Fin

```

---

### 🧩 `01_saludo_modular.py`

```python
# 🐍 EJERCICIO 1 saludo_modular.py
"""🎯 Objetivo: Aprender a separar la lógica de entrada, 
procesamiento y salida en funciones simples y reutilizables."""

def pedir_nombre():
    while True:
        nombre_completo = input("👤Ingrese su nombre y apellido: ").strip()
        palabras = nombre_completo.split()

        if not palabras:
            print("❌ No puede estar vacío")
            continue
        elif all(palabra.isalpha() for palabra in palabras):
            nombre_formateado = " ".join(p.capitalize() for p in palabras)
            print(f"✅ Nombre válido: {nombre_formateado}")
            
        else:
            print("❌ Solo se permiten letras en el nombre y apellido")
            continue
        return nombre_formateado

def saludar_usuario(nombre_formateado):
    print(f"¡Bienvenido, {nombre_formateado}! Es un placer saludarlo.")

nombre_usuario = pedir_nombre()
saludar_usuario(nombre_usuario)
```

```python
"""
=============================================================
=== RESPUESTA DE CONSOLA ===
=============================================================

👤Ingrese su nombre y apellido: Gabriel123
❌ Solo se permiten letras en el nombre y apellido
👤Ingrese su nombre y apellido: 
❌ No puede estar vacío
👤Ingrese su nombre y apellido: GabRRIEL ESPINOSA IZADA
✅ Nombre válido: Gabrriel Espinosa Izada
¡Bienvenido, Gabrriel Espinosa Izada! Es un placer saludarlo.
=============================================================
"""
```

---

## 🧪 **Ejercicio 02 — validar\_correo\_modular.py**

🎯 **Objetivo:** Separar la lógica de validación de correos en funciones limpias y reutilizables, aplicando condiciones básicas y pensamiento lógico estructurado.

---

## 🧭 Diagrama de flujo (formato Gabo)

```>>>
Inicio
↓
Llamar a pedir_correo()
    ↓
    ├── Mostrar mensaje "📧 Ingrese su correo:"
    ↓
    ├── Limpiar entrada con .strip()
    ↓
    ├── Validar que no esté vacío
    │   └── Si vacío → Mostrar error y repetir
    ↓
    ├── Validar que contenga "@"
    │   └── Si no → Mostrar error y repetir
    ↓
    ├── Validar que contenga "."
    │   └── Si no → Mostrar error y repetir
    ↓
    🟥 Validar que no empiece ni termine con "@" o "."
    │   └── Mostrar error y repetir si no cumple
    ↓
    🟥 Validar que solo haya un "@" → .count("@") == 1
    │   └── Mostrar error y repetir si hay más
    ↓
    🟥 Validar que @ esté antes que el último punto
    │   └── .find("@") < .rfind(".")
    ↓
    🟥 Validar que no tenga espacios (" " not in correo)
    │   └── Mostrar error y repetir
    ↓
    🟥 Convertir correo a minúsculas con .lower()
    ↓
    Retornar correo válido
↓
Llamar a saludar_con_correo(correo)
    └── Mostrar: "Gracias, hemos registrado el correo: [correo]"
↓
Fin

```

---

## 🧩 `02_validar_correo_modular.py`

```python
# 🐍 validar_correo_modular.py
"""Debe pedir el correo al usuario, validarlo 
y retornarlo si es correcto"""

def pedir_correo():
    while True:
        correo = input("📧 Ingrese su correo: ").strip()

        if not correo:
            print("❌ El Campo correo no puede estar vacio")
            continue
        elif "@" not in correo:
            print("❌ Error: El correo debe contener '@'.")
            continue
        elif "." not in correo:
            print("❌ Error: El correo debe contener (.).")
            continue
        elif correo.startswith(("@", ".")) or correo.endswith(("@", ".")):
            print("Error: El correo no puede empezar ni terminar con '@' o '.'.")
            continue
        elif correo.count("@") != 1:
            print("Error: El correo debe contener exactamente un '@'.")
            continue
        elif correo.find("@") >= correo.rfind("."):
            print("Error: El '@' debe estar antes del último punto.")
            continue
        elif " " in correo:
            print("Error: El correo no puede contener espacios.")
            continue
        else:
            correo = correo.lower()
            print("🟩 Correo registrado con exito")
            return correo


def saludar_con_correo(correo):
    print(f"Gracias, hemos registrado el correo: {correo}")

correo_valido = pedir_correo()
saludar_con_correo(correo_valido)
```

```.
"""
================================================================
=== RESPUESTA DE CONSOLA ===
================================================================
📧 Ingrese su correo: 123
❌ Error: El correo debe contener '@'.

📧 Ingrese su correo: @gabo123
❌ Error: El correo debe contener (.).

📧 Ingrese su correo: ..gabo
❌ Error: El correo debe contener '@'.

📧 Ingrese su correo: gespinosaizada03gmail.com
❌ Error: El correo debe contener '@'.

📧 Ingrese su correo: GESPINOSAIZADA03@GMAIL.COM
🟩 Correo registrado con exito
Gracias, hemos registrado el correo: gespinosaizada03@gmail.com
================================================================
"""
```

## 🧪 **Ejercicio 03 — calculadora\_modular.py**

🎯 **Objetivo:** Aplicar la modularización para construir una calculadora básica, que pueda sumar, restar, multiplicar y dividir dos números, controlando errores de entrada.

---

## 🧭 Diagrama de flujo

```..
Inicio
↓
Llamar a pedir_operacion()
    └── Mostrar menú de operaciones
    └── Pedir opción al usuario (1 a 4)
    └── Validar opción válida → retornar tipo
↓
Llamar a pedir_numeros()
    └── Pedir dos números con input()
    └── Validar que sean números (try/except)
    └── Retornar como floats
↓
Llamar a calcular_resultado(op, num1, num2)
    ├── Si suma → retornar num1 + num2
    ├── Si resta → retornar num1 - num2
    ├── Si multiplicación → retornar num1 * num2
    ├── Si división
    │   └── Validar que num2 ≠ 0
    │   └── Retornar num1 / num2
↓
Llamar a mostrar_resultado(resultado)
    └── Mostrar: "El resultado es: ..."
↓
Fin
```

---

## 🧩 `03_calculadora_modular.py`

```python
# 🐍 calculadora_modular.py
# Calculadora que realiza operaciones básicas según el diagrama de flujo

def pedir_operacion():
    """Muestra un menú de operaciones, pide una opción y valida que sea válida."""
    
    while True:
        print("""
--------------------------
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------      
""")
        try:
            opcion = int(input("📧 Seleccione una operación (1-4): "))
            
            if opcion in [1, 2, 3, 4]:
                if opcion == 1:
                    return "suma"
                elif opcion == 2:
                    return "resta"
                elif opcion == 3:
                    return "multiplicación"
                else:
                    return "división"
            else:
                print("❌ Error: Debe ingresar un número entre 1 y 4.")
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")


def pedir_numeros():
    while True:
        try:
            num1 = float(input("🔢 Ingrese el primer número: "))
            num2 = float(input("🔢 Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("❌ Error: Debe ingresar números válidos.")


def calcular_resultado(op, num1, num2):
    """Calcula el resultado según la operación. Valida división por cero."""
    if op == "suma":
        return num1 + num2
    elif op == "resta":
        return num1 - num2
    elif op == "multiplicación":
        return num1 * num2
    elif op == "división":
        if num2 == 0:
            print("❌ Error: no se puede dividir por cero")
            return None
        return num1 / num2

def mostrar_resultado(resultado):
    if resultado is not None:
        print(f"🟩 El resultado es: {resultado:.2f}")


# Flujo principal
operacion = pedir_operacion()
numero1, numero2 = pedir_numeros()
resultado = calcular_resultado(operacion, numero1, numero2)
mostrar_resultado(resultado)
```

```.
"""
=============================================
=== RESPUESTA DE CONSOLA ===
=============================================
OPCION INVALIDA:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 1
🔢 Ingrese el primer número: qq
❌ Error: Debe ingresar números válidos.

OPCION 1 SUMA :
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 1
🔢 Ingrese el primer número: 22
🔢 Ingrese el segundo número: 44.999
🟩 El resultado es: 67.00

OPCION 2 RESTA:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 2
🔢 Ingrese el primer número: 3
🔢 Ingrese el segundo número: 22.8905765
🟩 El resultado es: -19.89

OPCION 3 MULTIPLICACION:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 3
🔢 Ingrese el primer número: 78587
🔢 Ingrese el segundo número: 22.99999999999
🟩 El resultado es: 1807501.00

OPCION 4 DIVISION ENTRE CERO:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 4
🔢 Ingrese el primer número: 1
🔢 Ingrese el segundo número: 0
❌ Error: no se puede dividir por cero

OPCION 4 DIVISION:
|📋 Menú de operaciones: |
--------------------------
|1. Suma                 |          
|2. Resta                |
|3. Multiplicación       |
|4. División             |
--------------------------

📧 Seleccione una operación (1-4): 4
🔢 Ingrese el primer número: 2
🔢 Ingrese el segundo número: 454543645.4654             
🟩 El resultado es: 0.00
=============================================
"""
```

---

## 🧪 **Ejercicio 04 — registro\_usuarios\_modular.py**

🎯 **Objetivo:** Aplicar modularización para registrar información básica de usuarios: nombre, edad y correo, con validaciones y salida formateada.

---

## 🧱 Elementos obligatorios según la Clase 20

* Modularización: cada parte del flujo en su función
* Validaciones básicas:

  * Nombre: solo letras
  * Edad: número entero positivo
  * Correo: validación básica (reutilizable)
* Mostrar resumen del usuario registrado

---

## 🔴 Mejoras opcionales (válidas solo hasta Clase 20) para nota extra

| Mejora opcional 🟥                                          | Concepto ya estudiado           |
| ----------------------------------------------------------- | ------------------------------- |
| 🟥 Validar nombre con `.title()`, `.strip()` y `.isalpha()` | Clase de strings y validaciones |
| 🟥 Validar edad dentro de rango lógico (ej. 0 < edad < 120) | Condiciones                     |
| 🟥 Convertir correo a minúsculas                            | `.lower()`                      |
| 🟥 Reutilizar función `validar_correo()` de clase anterior  | Modularización                  |
| 🟥 Limpiar entrada de espacios dobles                       | `.split()` + `" ".join()`       |
| 🟥 Preguntar al final si desea registrar otro usuario       | `while True:` con confirmación  |

---

## 🧭 Diagrama de flujo con mejoras opcionales en rojo 🟥

```.
Inicio
↓
Llamar a pedir_nombre()
    ├── Pedir nombre
    ├── Limpiar con .strip() 🟥
    ├── Validar que no esté vacío
    ├── Validar que sean letras con .isalpha()
    ├── Formatear con .title() 🟥
    ├── Corregir espacios dobles con split+join 🟥
    └── Retornar nombre válido
↓
Llamar a pedir_edad()
    ├── Pedir edad
    ├── Validar que sea número entero positivo
    ├── Validar que esté en rango lógico (0 < edad < 120) 🟥
    └── Retornar edad válida
↓
Llamar a pedir_correo()
    ├── Pedir correo
    ├── Validar: contiene @ y .
    ├── Validar que no tenga espacios 🟥
    ├── Validar que @ vaya antes del último punto 🟥
    ├── Convertir a minúsculas 🟥
    └── Retornar correo válido
↓
Llamar a mostrar_usuario(nombre, edad, correo)
    └── Mostrar resumen del usuario formateado
↓
🟥 Preguntar si desea registrar otro usuario (s/n)
├── Si sí → repetir flujo
└── Si no → Fin
```

---

## `04_registro_usuarios_modular.py`

```python
#🧪 Ejercicio 04 — registro_usuarios_modular.py

"""🎯 Objetivo: Aplicar modularización para registrar información básica 
de usuarios: nombre, edad y correo, con validaciones y salida formateada."""

def pedir_nombre():
    
    while True:
        try:
            nombre_completo = input("Ingrese su nombre y apellido: ").strip()
            palabras = nombre_completo.split()
            if not palabras:
                print("❌ No puede estar vacío")
                continue
            if len(palabras) < 2:
                print("❌ Debe ingresar al menos un nombre y un apellido")
                continue
            elif all(palabra.isalpha() for palabra in palabras):
                nombre_formateado = " ".join(p.capitalize() for p in palabras)
                print(f"✅ Nombre válido: {nombre_formateado}")
                return nombre_formateado
            else:
                print("❌ Solo se permiten letras en el nombre y apellido")
        except KeyboardInterrupt:
            print("\n❌ Entrada cancelada por el usuario")
            return None

def pedir_edad(nombre_formateado):
    while True:
        try:
            entrada = input(f"{nombre_formateado}, ingrese su edad: ").strip()
            if not entrada:
                print(f"❌ {nombre_formateado}, el campo de la edad no puede estar vacío")
                continue
            edad = int(entrada)
            if edad <= 0 or edad > 120:
                print("❌ Error: esa edad parece falsa 🤔")
                continue
            print(f"🟩 {nombre_formateado}, su edad ha sido registrada con éxito")
            return edad
        except ValueError:
            print("❌ Error: ingrese un número válido para la edad")
        except KeyboardInterrupt:
            print("\n❌ Entrada cancelada por el usuario")
            return None
            

def pedir_correo(nombre_formateado):
    while True:
        correo = input(f"📧 {nombre_formateado}, Ingrese su correo: ").strip()

        if not correo:
            print("❌ El Campo correo no puede estar vacio")
            continue
        elif "@" not in correo:
            print("❌ Error: El correo debe contener '@'.")
            continue
        elif "." not in correo:
            print("❌ Error: El correo debe contener (.).")
            continue
        elif correo.startswith(("@", ".")) or correo.endswith(("@", ".")):
            print("Error: El correo no puede empezar ni terminar con '@' o '.'.")
            continue
        elif correo.count("@") != 1:
            print("Error: El correo debe contener exactamente un '@'.")
            continue
        elif correo.find("@") >= correo.rfind("."):
            print("Error: El '@' debe estar antes del último punto.")
            continue
        elif " " in correo:
            print("Error: El correo no puede contener espacios.")
            continue
        else:
            correo = correo.lower()
            print(f"🟩 {nombre_formateado} su correo fue registrado con exito")
            return correo

def mostrar_usuario(nombre_formateado, edad, correo):
    print("\nDatos registrados:")
    print(f"Nombre: {nombre_formateado}")
    print(f"Edad: {edad}")
    print(f"Correo: {correo}")


if __name__ == "__main__":
    nombre = pedir_nombre()
    if nombre:
        edad = pedir_edad(nombre)
        if edad is not None:
            correo = pedir_correo(nombre)
            if correo:
                mostrar_usuario(nombre, edad, correo)
```

```python
"""
===========================================================================
===                  RESPUESTA DE CONSOLA                               ===
===========================================================================
Ingrese su nombre y apellido: gabo123                                      
❌ Debe ingresar al menos un nombre y un apellido
Ingrese su nombre y apellido:     GABRRIEL 
❌ Debe ingresar al menos un nombre y un apellido
Ingrese su nombre y apellido:      GABRIEL ESPINOSA izada
✅ Nombre válido: Gabriel Espinosa Izada
Gabriel Espinosa Izada, ingrese su edad: wwew
❌ Error: ingrese un número válido para la edad
Gabriel Espinosa Izada, ingrese su edad: 0
❌ Error: esa edad parece falsa 🤔
Gabriel Espinosa Izada, ingrese su edad: 152
❌ Error: esa edad parece falsa 🤔
Gabriel Espinosa Izada, ingrese su edad: 27
🟩 Gabriel Espinosa Izada, su edad ha sido registrada con éxito
📧 Gabriel Espinosa Izada, Ingrese su correo: @
❌ Error: El correo debe contener (.).
📧 Gabriel Espinosa Izada, Ingrese su correo: .
❌ Error: El correo debe contener '@'.
📧 Gabriel Espinosa Izada, Ingrese su correo: GESPINOSAIZADA03@GMAIL.COM
🟩 Gabriel Espinosa Izada su correo fue registrado con exito

Datos registrados:
Nombre: Gabriel Espinosa Izada
Edad: 27
Correo: gespinosaizada03@gmail.com
===========================================================================
"""
```

## 🧩 `05_menu_modular_con_funciones.py`

---

### 🎯 1. Objetivo del ejercicio

Construir un **menú interactivo en consola** con múltiples opciones, donde cada opción ejecuta una función modular distinta, y el flujo esté correctamente controlado con validaciones, bucles y salidas limpias. Este ejercicio consolidará tu dominio de:

* Funciones con responsabilidades claras
* Menús textuales interactivos
* Bucles controlados (`while True`)
* Validación de entrada del usuario
* Salida profesional

---

### 📘 2. Breve teoría del concepto aplicado

#### 🧠 ¿Qué es un menú modular?

Un menú es una **interfaz de navegación textual** que le permite al usuario elegir una acción. Cuando lo hacemos de forma modular, cada opción del menú:

* Llama a una función específica
* No mezcla lógicas
* Es extensible y fácil de mantener

#### 🔄 Estructura típica de un menú en consola

1. Se muestra el menú (normalmente con `print`)
2. Se pide una opción (`input`)
3. Se valida la entrada
4. Se ejecuta la acción correspondiente (una función)
5. Se repite mientras no se elija "Salir"

---

### 📌 3. Ejemplo mínimo (para visualizar la lógica)

```plaintext
Menú Principal
1. Saludar
2. Mostrar Fecha
3. Salir
Seleccione una opción:
```

Si el usuario escribe `1`, se ejecuta la función `saludar()`
Si escribe `2`, se ejecuta `mostrar_fecha()`
Si escribe `3`, termina el programa.

---

### 🔧 4. Diagrama de flujo (con mejoras opcionales 🟥)

```.
Inicio
↓
while True:
    ↓
    Mostrar menú principal
    ↓
    Pedir opción al usuario
    ↓
    Validar que sea un número
    ├── Si no lo es → Mostrar error y repetir 🟥
    ↓
    Validar que esté entre opciones válidas
    ├── Si no está → Mostrar error y repetir 🟥
    ↓
    Ejecutar opción:
        ├── Si 1 → Llamar a funcion_opcion_1()
        ├── Si 2 → Llamar a funcion_opcion_2()
        ├── ...
        └── Si N → Llamar a salir() y romper bucle
↓
Fin
```

---

### `05_menu_modular_con_funciones.py`

```python
# 🐍 05_menu_modular_con_funciones.py

def mostrar_menu():
    print("\n=== 🌟 MENÚ PRINCIPAL 🌟 ===")
    print("1. 👋 Saludar")
    print("2. 💪 Mostrar mensaje motivacional")
    print("3. 🚪 Salir")
    print("======================")


def pedir_opcion():
    while True:
        try:
            opcion = int(input("➡️ Ingrese una opción (1-3): "))
            if 1 <= opcion <= 3:
                return opcion
            else:
                print("❌ Error: La opción debe estar entre 1 y 3.")
        except ValueError:
            print("❌ Error: Por favor, ingrese un número válido.")


def funcion_opcion_1():
    nombre = input("✍️ Ingrese su nombre: ")
    print(f"👋 ¡Hola, {nombre}! Bienvenido al programa 🎉")


def funcion_opcion_2():
    print("💪 ¡Tú puedes con todo! Sigue adelante y alcanza tus metas 🌟")


def salir():
    print("\n🙏 ¡Gracias por usar el programa! Hasta pronto 😊")


def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 1:
            funcion_opcion_1()
        elif opcion == 2:
            funcion_opcion_2()
        elif opcion == 3:
            salir()
            break


if __name__ == "__main__":
    main()
```

```python
"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
=== 🌟 MENÚ PRINCIPAL 🌟 ===
1. 👋 Saludar
2. 💪 Mostrar mensaje motivacional
3. 🚪 Salir
======================
➡️ Ingrese una opción (1-3): 1
✍️ Ingrese su nombre: Grabiel Espinosa Izada
👋 ¡Hola, Grabiel Espinosa Izada! Bienvenido al programa 🎉

=== 🌟 MENÚ PRINCIPAL 🌟 ===
1. 👋 Saludar
2. 💪 Mostrar mensaje motivacional
3. 🚪 Salir
======================
➡️ Ingrese una opción (1-3): 2
💪 ¡Tú puedes con todo! Sigue adelante y alcanza tus metas 🌟

=== 🌟 MENÚ PRINCIPAL 🌟 ===
1. 👋 Saludar
2. 💪 Mostrar mensaje motivacional
3. 🚪 Salir
======================
➡️ Ingrese una opción (1-3): 3

🙏 ¡Gracias por usar el programa! Hasta pronto 😊
====================================================================
"""
```

---

### 🧠 Mejoras opcionales válidas hasta la Clase 20 (🟥)

| Mejora 🟥                           | Tema relacionado                |
| ----------------------------------- | ------------------------------- |
| Validar que la opción sea numérica  | `try/except` de entradas        |
| Validar que esté dentro del menú    | Condicionales y listas          |
| Agregar separación visual elegante  | UX con `print("="*30)`          |
| Confirmar salida con pregunta (s/n) | Bucle `while`, control booleano |
| Colocar íconos en el menú (🎯, ✅)   | Presentación profesional        |

---

## 🧩 `06_calculadora_menu_funcional.py`

---

### ✍️ 1. Objetivo del ejercicio

Construir una **calculadora de operaciones básicas** (suma, resta, multiplicación, división) que funcione mediante un **menú interactivo modular**:

* Cada opción ejecuta una función matemática diferente
* Entrada validada para los números
* Control de división por cero
* Ciclo hasta que el usuario decida salir

Este ejercicio es **la unión natural entre**:

* `03_calculadora_modular.py`
* `05_menu_modular_con_funciones.py`

---

### 📘 2. Teoría puntual: Menú + funciones matemáticas

#### 🔄 Estructura general esperada

1. Mostrar menú con operaciones
2. Pedir opción válida
3. Pedir dos números
4. Ejecutar operación correspondiente
5. Mostrar resultado
6. Repetir hasta que se elija "Salir"

#### 🧠 Conceptos aplicados

* **Funciones**: separar cada operación (`sumar()`, `restar()`, etc.)
* **Menú**: diseño profesional y controlado
* **Entrada de datos**: validada con `try/except`
* **Estructura modular**: cada parte en su función
* **UX profesional**: mensajes claros y consistentes

---

### 🔁 3. Diagrama de flujo (con mejoras opcionales 🟥)

```m
Inicio
↓
while True:
    ↓
    Mostrar menú con opciones (1 a 5)
    ↓
    Pedir opción del usuario
    ├── 🟥 Validar que sea número
    ├── 🟥 Validar que esté en rango 1–5
    ↓
    Si opción == 5 → salir() y break
    ↓
    Pedir dos números
    ├── 🟥 Validar que sean float (try/except)
    ├── 🟥 Si división y num2 == 0 → error
    ↓
    Ejecutar operación correspondiente:
        ├── Si 1 → sumar(num1, num2)
        ├── Si 2 → restar(num1, num2)
        ├── Si 3 → multiplicar(num1, num2)
        └── Si 4 → dividir(num1, num2)
    ↓
    Mostrar resultado
    ↓
Fin
```

---

### 🧱 `06_calculadora_menu_funcional.py`

```python
# 🐍 06_calculadora_menu_funcional.py

def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")
    print("==================")

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("❌ Error: Opción debe estar entre 1 y 5")
        except ValueError:
            print("❌ Error: Ingrese un número válido")

def pedir_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("❌ Error: Ingrese números válidos")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def mostrar_resultado(resultado):
    print("\n==================")
    print(f"Resultado: {resultado}")
    print("==================\n")

def salir():
    print("\n¡Gracias por usar la calculadora!")
    print("👋 Programa finalizado")

def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 5:
            salir()
            break
            
        num1, num2 = pedir_numeros()
        
        try:
            if opcion == 1:
                resultado = sumar(num1, num2)
            elif opcion == 2:
                resultado = restar(num1, num2)
            elif opcion == 3:
                resultado = multiplicar(num1, num2)
            elif opcion == 4:
                resultado = dividir(num1, num2)
                
            mostrar_resultado(resultado)
            
        except ValueError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
```

```consola
"""
====================================================================
=== RESPUESTA DE CONSOLA ===
====================================================================
=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 1
Ingrese el primer número: 5
Ingrese el segundo número: 3

==================
Resultado: 8.0
==================

=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 4
Ingrese el primer número: 10
Ingrese el segundo número: 0
❌ Error: No se puede dividir por cero

=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 3
Ingrese el primer número: 4
Ingrese el segundo número: 5

==================
Resultado: 20.0
==================

=== CALCULADORA ===
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
==================
Seleccione una opción (1-5): 5

¡Gracias por usar la calculadora!
👋 Programa finalizado
====================================================================
"""
```

---

### 🟥 Mejoras opcionales válidas hasta Clase 20

| Mejora extra 🟥                         | Tema ya estudiado |
| --------------------------------------- | ----------------- |
| Validar si la opción es un número       | `try/except`      |
| Validar rango 1 a 5                     | Condicionales     |
| Validar entrada de números flotantes    | `try/except`      |
| Validar división por cero               | Condiciones       |
| Decoración visual del menú (`"=" * 30`) | UX                |
| Repetición hasta salir con opción       | `while True`      |

---
