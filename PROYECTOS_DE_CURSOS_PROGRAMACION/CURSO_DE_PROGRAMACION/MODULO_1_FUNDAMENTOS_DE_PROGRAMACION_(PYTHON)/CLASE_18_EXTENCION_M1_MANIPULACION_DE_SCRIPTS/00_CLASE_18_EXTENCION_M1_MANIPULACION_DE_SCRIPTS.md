# 🟪 **CLASE 18 EXTENSIÓN – Métodos útiles de strings**

---
📘 *Ampliación natural posterior a la Clase 18 oficial – Aprobada por Gabo*
🎯 Tema: Métodos avanzados de string para transformación, consulta y validación textual.

## 📚 TEORÍA PROFUNDA – MÉTODOS ÚTILES DE STRINGS

Los strings (`str`) en Python no son simples textos:
Son **objetos que tienen métodos internos incorporados**, que puedes aplicar directamente para manipular, transformar y consultar datos de forma profesional.

Vamos uno por uno con definiciones, ejemplos y casos reales.

---

## 🧠 1. `.upper()` y `.lower()`

### 🔹 `.upper()`

Convierte **todo el texto** a **mayúsculas**.

```python
texto = "hola mundo"
print(texto.upper())  # 'HOLA MUNDO'
```

### 🔹 `.lower()`

Convierte **todo el texto** a **minúsculas**.

```python
texto = "Python ES Genial"
print(texto.lower())  # 'python es genial'
```

🔧 **Casos reales:**

* Comparar textos sin importar mayúsculas/minúsculas
* Preparar datos para sistemas que requieren formato uniforme
* Transformar campos para búsqueda

---

## 🧠 2. `.replace()`

### 🔹 ¿Qué hace?

Reemplaza **una subcadena por otra**.

```python
frase = "Hola Gabo"
print(frase.replace("Gabo", "Mundo"))  # 'Hola Mundo'
```

### 🔹 Sintaxis

```python
texto.replace("antiguo", "nuevo")
```

📌 También sirve para eliminar:

```python
texto.replace(" ", "")  # elimina todos los espacios
```

🔧 **Casos reales:**

* Corregir errores comunes de escritura
* Preparar texto para exportar (quitar símbolos)
* Censurar palabras

---

## 🧠 3. `.startswith()` y `.endswith()`

### 🔹 `.startswith(substring)`

Devuelve `True` si el texto **comienza con** esa subcadena.

```python
codigo = "ABC123"
print(codigo.startswith("ABC"))  # True
```

### 🔹 `.endswith(substring)`

Devuelve `True` si el texto **termina con** esa subcadena.

```python
archivo = "informe.pdf"
print(archivo.endswith(".pdf"))  # True
```

🔧 **Casos reales:**

* Verificar extensiones de archivo
* Validar prefijos de código o identificadores
* Control de formatos

---

## 🧠 4. `.title()` y `.capitalize()`

### 🔹 `.title()`

Convierte la primera letra de **cada palabra** a mayúscula.

```python
nombre = "gabo espinosa"
print(nombre.title())  # 'Gabo Espinosa'
```

### 🔹 `.capitalize()`

Convierte solo la **primera letra del string** a mayúscula, el resto en minúscula.

```python
titulo = "hOLa mUnDo"
print(titulo.capitalize())  # 'Hola mundo'
```

🔧 **Casos reales:**

* Estilizar nombres, títulos, encabezados
* Mostrar campos correctamente formateados en formularios

---

## 🧠 5. `.find()` y `.index()`

### 🔹 `.find("texto")`

Devuelve la **posición (índice)** donde aparece la subcadena.
Si no la encuentra, devuelve `-1`.

```python
frase = "Python es poderoso"
print(frase.find("es"))  # 7
```

### 🔹 `.index("texto")`

Hace lo mismo que `.find()`, pero **lanza error** si no encuentra.

```python
frase.index("no-existe")  # ❌ ValueError
```

🔧 **Casos reales:**

* Buscar palabras clave en descripciones
* Extraer partes desde una posición específica
* Validar contenido

---

## 🧠 6. `.count()`

### ⏺️ ¿Qué hace?

Cuenta cuántas veces aparece una subcadena.

```python
texto = "gabo gabo gabo"
print(texto.count("gabo"))  # 3
```

🔧 **Casos reales:**

* Contar ocurrencias de palabras, símbolos, etc.
* Verificar repeticiones en texto plano

---

## 🧠 7. `.isdigit()`, `.isalpha()`, `.isalnum()`

| Método       | ¿Qué valida?                                |
| ------------ | ------------------------------------------- |
| `.isdigit()` | Solo números                                |
| `.isalpha()` | Solo letras (sin espacios)                  |
| `.isalnum()` | Letras y números (sin espacios ni símbolos) |

```python
"123".isdigit()   # True
"abc".isalpha()   # True
"abc123".isalnum()  # True
"abc 123".isalnum() # False
```

🔧 **Casos reales:**

* Validar inputs antes de guardar o procesar
* Evitar errores en conversiones
* Seguridad de datos

---

## 🧠 8. `.strip()`, `.lstrip()`, `.rstrip()` (repaso rápido)

Ya visto antes, pero aquí va de nuevo por contexto:

| Método      | Elimina...             |
| ----------- | ---------------------- |
| `.strip()`  | Espacios a ambos lados |
| `.lstrip()` | Solo al inicio         |
| `.rstrip()` | Solo al final          |

---

## 🧠 9. `.split()` (combinado con otros métodos)

```python
frase = "  hola mundo  "
palabras = frase.strip().lower().split()
print(palabras)  # ['hola', 'mundo']
```

🔧 Así puedes combinar `.strip()`, `.lower()` y `.split()` para hacer **preprocesamiento de texto real**, como se hace en proyectos de scraping, IA o limpieza de datos.

---

## 📊 TABLA RESUMEN DE MÉTODOS ÚTILES

| Método          | ¿Para qué sirve?                    |
| --------------- | ----------------------------------- |
| `.upper()`      | Convertir todo en mayúsculas        |
| `.lower()`      | Convertir todo en minúsculas        |
| `.replace()`    | Reemplazar texto                    |
| `.startswith()` | Verificar inicio de texto           |
| `.endswith()`   | Verificar final de texto            |
| `.title()`      | Capitalizar cada palabra            |
| `.capitalize()` | Capitalizar solo la primera palabra |
| `.find()`       | Buscar posición de una subcadena    |
| `.count()`      | Contar cuántas veces aparece algo   |
| `.isdigit()`    | ¿Solo números?                      |
| `.isalpha()`    | ¿Solo letras?                       |
| `.isalnum()`    | ¿Letras y números (sin símbolos)?   |

---

## 📂 LISTADO DE EJERCICIOS (Clase 18 Extensión)

| Nº  | Archivo sugerido                     | Nombre del ejercicio                                | Métodos enfocados                           |
| --- | ------------------------------------ | --------------------------------------------------- | ------------------------------------------- |
| 1️⃣ | `01_validar_archivo_pdf.py`          | Verificar si un archivo es `.pdf`                   | `.endswith()`                               |
| 2️⃣ | `02_formatear_nombre_completo.py`    | Formatear nombre y apellido correctamente           | `.strip()`, `.title()`                      |
| 3️⃣ | `03_reemplazar_palabra.py`           | Reemplazar palabras prohibidas por asteriscos       | `.replace()`                                |
| 4️⃣ | `04_buscar_y_contar_palabra.py`      | Buscar palabra clave y contar cuántas veces aparece | `.find()`, `.count()`                       |
| 5️⃣ | `05_validar_codigo_identificador.py` | Validar estructura de un código alfanumérico        | `.startswith()`, `.isalnum()`, `.isdigit()` |

---

## 🆎 **Ejercicio 1 – Verificar si un archivo es `.pdf`**

📄 Archivo sugerido: `01_validar_archivo_pdf.py`
🎯 **Objetivo:** Validar si el nombre de archivo ingresado por el usuario termina en `.pdf`, con limpieza y robustez.

---

## 🔽 DIAGRAMA DE FLUJO (estilo textual profesional)

```/
Inicio
↓
Solicitar al usuario que escriba el nombre de un archivo
↓
Limpiar espacios con .strip()
↓
Convertir a minúsculas con .lower()
↓
Verificar si el texto termina en ".pdf"
├── Sí → Mostrar mensaje: "✅ Archivo válido (PDF)"
└── No → Mostrar mensaje: "❌ Archivo no es PDF"
↓
Finalizar
```

---

## 💻 ESQUELETO GUÍA CON PISTAS

```python
#1️⃣ Solicitar al usuario que escriba un nombre de archivo
#   💡 Usa input() para capturar, y guarda en una variable llamada archivo

#2️⃣ Aplicar .strip() y .lower() para limpiar y normalizar
#   💡 Guarda el resultado en una variable nueva como archivo_limpio

#3️⃣ Usar .endswith(".pdf") para verificar si termina con esa extensión
#   💡 Usa una estructura if...else

#4️⃣ Mostrar resultado al usuario
#   💡 Mensaje profesional y claro según corresponda

#5️⃣ (Opcional) Mostrar el nombre limpio del archivo para confirmar
#   💡 Útil para visualizar errores de escritura o espacios accidentales
```

---

## 💻 EJERCICIO 1 RESUELTO

```python
#! === 🟪 Ejercicio 1 – Verificar si un archivo es .pdf === #!
#?📄 Archivo sugerido: 01_validar_archivo_pdf.py
#*🎯 Objetivo: Validar si el nombre de archivo ingresado por el 
#* usuario termina en .pdf, con limpieza y robustez.

#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
archivo = input(Fore.MAGENTA + "📜 Por favor escriba el nombre del archivo: ")
archivo_limpio = archivo.strip().lower()

if archivo_limpio.endswith(".pdf"):
    print(Fore.GREEN + "✅ Archivo válido (PDF)")
    print(Fore.CYAN + f"Nombre procesado: {archivo_limpio}")
else:
    print(Fore.RED +"🚫 Archivo no es (PDF)")

#! === RESPUESTA DE CONSOLA === #!
"""
📜 Por favor escriba el nombre del archivo: notas.pdf
✅ Archivo válido (PDF)
Nombre procesado: notas.pdf

📜 Por favor escriba el nombre del archivo: NOTAS.pd
🚫 Archivo no es (PDF)
"""
```

---

## 🟪 **Ejercicio 2 – Formatear nombre completo correctamente**

📄 Archivo sugerido: `02_formatear_nombre_completo.py`
🎯 **Objetivo:** Limpiar espacios innecesarios y capitalizar correctamente el nombre y apellido de una persona usando `.strip()` y `.title()`.

---

## 📘 TEORÍA PUNTUAL

### 🔹 `.strip()`

* Elimina espacios al **inicio y final** de un string.
* También puede eliminar caracteres específicos si se pasan como argumento.

Ejemplo:

```python
"   gabo espinosa   ".strip()  
# 'gabo espinosa'
```

---

### 💥 `.title()`

* Convierte la **primera letra de cada palabra** a mayúscula y las demás a minúscula.

Ejemplo:

```python
"gabo espinosa".title()
# 'Gabo Espinosa'
```

---

### 🔧 Uso combinado `.strip()` + `.title()`

Al aplicar juntos:

```python
nombre = "   gaBo ESPINOSA   "
print(nombre.strip().title())
# 'Gabo Espinosa'
```

* `.strip()` limpia la entrada.
* `.title()` corrige el formato.

---

### 🧠 Casos profesionales

* Formularios de registro.
* Limpieza de datos en bases de datos.
* Formatear listas de clientes para reportes.

---

## 🔽 DIAGRAMA DE FLUJO

```_
Inicio
↓
Solicitar al usuario que ingrese su nombre completo
↓
Eliminar espacios al inicio y final con .strip()
↓
Convertir a formato título con .title()
↓
Mostrar el nombre limpio y formateado al usuario
↓
Finalizar
```

---

## 🧩 ESQUELETO GUÍA CON PISTAS

```python
#1️⃣ Solicitar al usuario que escriba su nombre completo
#   💡 Usa input() y guarda en variable nombre

#2️⃣ Limpiar espacios al inicio y final
#   💡 Usa .strip()

#3️⃣ Convertir a formato título (Primera letra de cada palabra en mayúscula)
#   💡 Usa .title()

#4️⃣ Mostrar el nombre limpio y formateado
#   💡 Mensaje profesional con confirmación
```

---

## 💻 EJERCICIO 2 RESUELTO

```python
#! === 🟪 Ejercicio 2 – Formatear nombre completo correctamente === #!
#? 🎯 Objetivo: Limpiar espacios innecesarios y capitalizar correctamente el 
#? nombre y apellido de una persona usando .strip() y .title()

#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
while True:
    nombre_completo = input(Style.BRIGHT + Fore.CYAN +"👤 Por favor ingrese su nombre completo (solo letras y espacios): ")
    nombre_limpio = nombre_completo.strip()

    if not nombre_limpio:
        print(Fore.RED +"🚫 El nombre no puede estar vacío. inténtelo nuevamente")
    elif not all(palabra.isalpha() for palabra in nombre_limpio.split()):
        print(Fore.YELLOW +"❌ Solo se permiten letras. No uses números ni símbolos.")
    else:
        nombre_formateado = ' '.join(palabra.title() for palabra in nombre_limpio.split())
        print(Fore.MAGENTA + "Nombre ingresado correctamente")
        print(Fore.CYAN + f"👋 {nombre_formateado} sea usted Bienvenido")
        break

#! === RESPUESTA DE CONSOLA === #!
"""
👤 Por favor ingrese su nombre completo (solo letras y espacios): gABO134
❌ El nombre solo puede contener letras. inténtelo nuevamente
👤 Por favor ingrese su nombre completo (solo letras y espacios):          gabriel ESPINOSA IZADA
Nombre ingresado correctamente
👋 Gabriel Espinosa Izada sea usted Bienvenido
"""
```

---

## 🟥 **Ejercicio 3 – Reemplazar palabras prohibidas por asteriscos**

📄 Archivo sugerido: `03_reemplazar_palabra.py`
🎯 **Objetivo:** Detectar si una frase contiene una palabra "prohibida" (por ejemplo, groserías, spam, etc.) y reemplazarla por asteriscos `*****`, sin alterar el resto del texto.

---

## 📘 TEORÍA PUNTUAL – `.replace()`

### 💥 ¿Qué hace?

`.replace()` busca todas las apariciones de una subcadena dentro de un string y las **reemplaza por otra**.

---

### 💥 Sintaxis

```python
texto.replace("viejo", "nuevo")
```

🔁 Reemplaza **todas** las ocurrencias de `"viejo"` por `"nuevo"`.

---

### 💥 Ejemplo simple

```python
frase = "Este producto es malo, muy malo."
nueva = frase.replace("malo", "*****")
print(nueva)  # Este producto es *****, muy *****.
```

---

### 🔧 Casos reales

* Moderar lenguaje ofensivo en comentarios o foros.
* Censurar información sensible.
* Limpiar datos para reportes.

---

### 🧠 Consejo profesional

Antes de reemplazar, puedes usar `.lower()` para comparar sin importar mayúsculas:

```python
"Basura".lower() == "basura"  # True
```

---

## 💥 DIAGRAMA DE FLUJO

```_
Inicio
↓
Solicitar al usuario que escriba una frase
↓
Solicitar palabra prohibida
↓
Limpiar ambas entradas con .strip()
↓
Verificar si la palabra prohibida aparece en la frase (sin importar mayúsculas)
├── Sí →
│     Reemplazar todas las ocurrencias por asteriscos
│     Mostrar la frase modificada
└── No →
      Informar que la palabra no fue encontrada
↓
Finalizar
```

---

## 💥 ESQUELETO GUÍA CON PISTAS

```python
#1️⃣ Solicitar al usuario una frase de entrada
#   💡 Usa input(), guárdala en frase_original

#2️⃣ Solicitar la palabra prohibida
#   💡 Usa input(), guárdala en palabra_prohibida

#3️⃣ Limpiar ambas entradas con .strip()
#   💡 Para eliminar espacios antes o después

#4️⃣ Comprobar si la palabra prohibida está en la frase (sin importar mayúsculas)
#   💡 Usa .lower() para comparar de forma segura

#5️⃣ Si está presente, reemplazar con asteriscos del mismo largo
#   💡 Usa .replace(palabra_prohibida, "*" * len(palabra_prohibida))

#6️⃣ Mostrar la frase resultante con la palabra censurada
#   💡 Mensaje claro al usuario, usando colorama si deseas

#7️⃣ Si la palabra no aparece, muestra aviso de que no se encontró
```

---

## 🟥 EJERCICIO 3 RESUELTO

```python
#! === 🟪 Ejercicio 3 – Reemplazar palabras prohibidas por asteriscos === #!
"""
🎯 Objetivo: Detectar si una frase contiene una palabra "prohibida" (por ejemplo, groserías, 
spam, etc.) y reemplazarla por asteriscos *****, sin alterar el resto del texto.
"""
#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
frase = input(Fore.CYAN + "Ingrese una frase: ")
palabra_prohibida = input(Fore.CYAN + "😎 Ingrese la palabra prohibida: ")

# Limpiar entradas
frase_limpia = frase.strip()
palabra_limpia = palabra_prohibida.strip()

# Verificar y reemplazar
if palabra_limpia.lower() in frase_limpia.lower():
    # Reemplazar palabra (ignorando mayúsculas/minúsculas)
    frase_modificada = frase_limpia
    for palabra in frase_limpia.split():
        if palabra.lower() == palabra_limpia.lower():
            frase_modificada = frase_modificada.replace(palabra, "*" * len(palabra))
    print(Fore.GREEN + f"Frase modificada: {frase_modificada}")
else:
    print(Fore.YELLOW + "La palabra prohibida no fue encontrada en la frase.")

#! === RESPUESTA DE CONSOLA === #!
"""
Ingrese una frase: No hay caminos para la paz; la paz es el camino 
😎 Ingrese la palabra prohibida: caminos
Frase modificada: No hay ******* para la paz; la paz es el camino
"""
```

---

## 🟩 **Ejercicio 4 – Buscar y contar palabra clave**

📄 Archivo sugerido: `04_buscar_y_contar_palabra.py`
🎯 **Objetivo:** Localizar la posición de la primera aparición de una palabra clave en un texto y contar cuántas veces aparece, usando `.find()` y `.count()`.

---

## 💥 TEORÍA PUNTUAL

### 🔹 `.find()`

* **Función:** Devuelve el índice (posición) de la **primera aparición** de una subcadena.
* Si no la encuentra → devuelve `-1`.

Ejemplo:

```python
texto = "Python es poderoso"
print(texto.find("es"))  # 7
print(texto.find("Java"))  # -1
```

---

### 🔹 `.count()`

* **Función:** Cuenta cuántas veces aparece una subcadena en un string.
* No distingue mayúsculas/minúsculas a menos que lo prepares con `.lower()`.

Ejemplo:

```python
texto = "gabo gabo GABO"
print(texto.lower().count("gabo"))  # 3
```

---

### 🧠 Uso combinado

```python
texto_limpio = texto.lower()
posicion = texto_limpio.find("gabo")
cantidad = texto_limpio.count("gabo")
```

Así evitas errores por mayúsculas/minúsculas.

---

## 🏁 DIAGRAMA DE FLUJO

```/
Inicio
↓
Solicitar al usuario un texto
↓
Solicitar palabra clave a buscar
↓
Limpiar y convertir ambos a minúsculas
↓
Usar .find() para obtener la posición de la primera aparición
↓
Si posición == -1 → Mostrar mensaje de que no se encontró
↓
Si posición != -1 →
     Usar .count() para contar cuántas veces aparece
     Mostrar posición y cantidad
↓
Finalizar
```

---

## ✍️ ESQUELETO GUÍA CON PISTAS

```python
#1️⃣ Solicitar texto al usuario
#   💡 Usa input(), guárdalo en variable texto_original

#2️⃣ Solicitar palabra clave
#   💡 Usa input(), guárdalo en palabra_clave

#3️⃣ Limpiar y convertir a minúsculas
#   💡 Usa .strip() y .lower()

#4️⃣ Buscar posición de la primera aparición con .find()
#   💡 Guarda el índice en variable posicion

#5️⃣ Si posicion == -1 → mostrar "No se encontró"
#   💡 Mensaje en rojo

#6️⃣ Si posicion != -1 → usar .count() para contar repeticiones
#   💡 Mostrar ambas informaciones con formato profesional
```

---

## 🟥 **Ejercicio 5 – Validar código identificador**

📄 Archivo sugerido: `05_validar_codigo_identificador.py`
🎯 **Objetivo:** Verificar que un código ingresado por el usuario cumpla con una estructura específica (por ejemplo, empieza con una letra y sigue con números, o un formato de tipo `ABC123`).

---

## 🟥 TEORÍA PUNTUAL

### 🔹 `.startswith()`

* **Función:** Comprueba si un string comienza con un prefijo específico.
* **Sintaxis:**

  ```python
  texto.startswith("ABC")
  ```

  Devuelve `True` si el texto empieza por `"ABC"`, `False` en caso contrario.

---

### 🔹 `.isalnum()`

* **Función:** Comprueba si todos los caracteres del string son alfanuméricos (letras y/o números).
* **Importante:** No permite espacios ni símbolos.
* **Ejemplo:**

  ```python
  "ABC123".isalnum()  # True
  "ABC 123".isalnum() # False
  ```

---

### 🔹 `.isdigit()`

* **Función:** Comprueba si todos los caracteres son dígitos (0-9).
* **Ejemplo:**

  ```python
  "123".isdigit()  # True
  "12a".isdigit()  # False
  ```

---

### 📌 Validación típica para este ejercicio

1. Que empiece con **3 letras** (`.isalpha()` en el primer tramo).
2. Que después haya **3 dígitos** (`.isdigit()` en el segundo tramo).
3. Que en total tenga **6 caracteres**.
4. Sin espacios ni símbolos.

Ejemplo válido: `ABC123`
Ejemplos inválidos: `AB123`, `ABC12A`, `A1C123`, `ABC 123`.

---

## 🟥 DIAGRAMA DE FLUJO

```.
Inicio
↓
Solicitar al usuario el código identificador
↓
Limpiar entrada con .strip()
↓
Verificar longitud total == 6
├── No → Mostrar error y pedir de nuevo
↓
Separar primeros 3 y últimos 3 caracteres
↓
Verificar que primeros 3 sean letras con .isalpha()
├── No → Mostrar error y pedir de nuevo
↓
Verificar que últimos 3 sean dígitos con .isdigit()
├── No → Mostrar error y pedir de nuevo
↓
Si todo es correcto → Mostrar mensaje de validación exitosa
↓
Fin
```

---

## 🟥 ESQUELETO GUÍA CON PISTAS

```python
#1️⃣ Solicitar al usuario el código identificador
#   💡 Usa input() y guárdalo en variable codigo

#2️⃣ Limpiar espacios con .strip()

#3️⃣ Verificar que la longitud sea exactamente 6 caracteres
#   💡 Usa len(codigo) == 6

#4️⃣ Extraer primeros 3 caracteres y verificar que sean letras
#   💡 Usa .isalpha()

#5️⃣ Extraer últimos 3 caracteres y verificar que sean dígitos
#   💡 Usa .isdigit()

#6️⃣ Si todas las validaciones pasan → mostrar mensaje de éxito
#   💡 Usa colorama para colores

#7️⃣ Si alguna validación falla → mostrar mensaje de error y explicar el motivo
```

---

## 🟥 EJERCICIO 4 RESUELTO

```python
#=== 🟥 Ejercicio 5 – Validar código identificador #===
#📄 Archivo sugerido: 05_validar_codigo_identificador.py 
#!🎯 Objetivo: Verificar que un código ingresado por el usuario cumpla con una estructura específica 
#! (por ejemplo, empieza con una letra y sigue con números, o un formato de tipo ABC123).

#! === ESTILOS === #!
from colorama import init, Fore, Style
init(autoreset=True)

#! === SCRIPT === #!
while True:
    codigo = input("Por favor, ingresa tu código de identificación (o 'salir' para terminar): ")
    if codigo.lower() == 'salir':
        print(Fore.YELLOW + "Programa terminado.")
        break

    codigo = codigo.strip()
    error_messages = []

    # Check length
    if len(codigo) != 6:
        error_messages.append("❌ El código debe tener exactamente 6 caracteres.")
    
    # Check for spaces
    if " " in codigo:
        error_messages.append("❌ El código no debe contener espacios.")
    
    # Check first three characters (letters)
    if len(codigo) >= 3:
        primeros_tres = codigo[:3]
        if not primeros_tres.isalpha():
            error_messages.append("❌ Los primeros tres caracteres deben ser letras.")
        elif primeros_tres != primeros_tres.upper():
            error_messages.append("❌ Los primeros tres caracteres deben ser letras mayúsculas.")
    
    # Check last three characters (digits)
    if len(codigo) >= 6:
        ultimos_tres = codigo[3:]
        if not ultimos_tres.isdigit():
            error_messages.append("❌ Los últimos tres caracteres deben ser dígitos.")

    # Output results
    if not error_messages:
        print(Fore.GREEN + "✅ ¡El código de identificación es válido!")
    else:
        for message in error_messages:
            print(Fore.RED + message)
        print(Fore.YELLOW + "Por favor, intenta de nuevo.")

#! === RESPUESTA DE CONSOLA === #!
"""
Por favor, ingresa tu código de identificación (o 'salir' para terminar): AAA22045
❌ El código debe tener exactamente 6 caracteres.
Por favor, intenta de nuevo.
Por favor, ingresa tu código de identificación (o 'salir' para terminar): GAI980
✅ ¡El código de identificación es válido!
Por favor, ingresa tu código de identificación (o 'salir' para terminar): salir
Programa terminado.
"""
```
