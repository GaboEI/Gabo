# 🧠 Clase 14 — Manejo de errores: try, except, else, finally

---

## 🎯 Objetivo de la clase

Comprender cómo manejar errores de manera controlada utilizando las estructuras `try`, `except`, `else` y `finally`, con el fin de desarrollar programas **robustos**, **seguros** y **profesionales**, capaces de continuar su ejecución incluso cuando se presentan situaciones inesperadas.

---

## 📚 Fundamentos teóricos

### 🔹 ¿Qué es el manejo de errores?

En programación, los errores pueden ser de **sintaxis** o **lógicos**. Sin embargo, incluso el código sin errores de sintaxis puede fallar en tiempo de ejecución por factores como:

- División por cero (`ZeroDivisionError`)
- Archivos no encontrados (`FileNotFoundError`)
- Conversión inválida de tipo (`ValueError`)

Para evitar que un programa se detenga abruptamente, se emplea el **manejo de excepciones**.

### 🔸 Sintaxis básica

```python
ttry:
    # bloque de código que puede causar error
except TipoDeError:
    # qué hacer si ocurre ese error
else:
    # qué hacer si NO ocurre ningún error
finally:
    # este bloque se ejecuta siempre, haya error o no
```

### 🔹 ¿Por qué es fundamental el manejo de errores?

- Protege al usuario de caídas inesperadas
- Mejora la experiencia y la confianza en el software
- Permite registrar errores para depuración
- Esencial en desarrollo profesional, backend, APIs, archivos, etc.

---

## 🧪 Ejercicio 01 — `01_division_segura.py`

**🎯 Objetivo:** Dividir dos números con control de errores y mensajes personalizados.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar número 1
↓
Solicitar número 2
↓
Intentar dividir
├── Error → mostrar mensaje de error (ZeroDivisionError o ValueError)
↓
Si éxito → mostrar resultado
↓
Mostrar mensaje de finalización (finally)
↓
Fin
```

### ✅ Código realizado

```python
def dividir_seguro():
    try:
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador: "))
        resultado = a / b
    except ZeroDivisionError:
        print("❌ Error: No se puede dividir entre cero.")
    except ValueError:
        print("❌ Error: Entrada inválida. Debe ingresar números.")
    else:
        print(f"✅ Resultado: {resultado}")
    finally:
        print("🔚 Operación finalizada.")

# dividir_seguro()  ← descomenta para probar
```

---

## 🧪 Ejercicio 02 — `02_acceso_archivo.py`

**🎯 Objetivo:** Intentar abrir un archivo y manejar errores si no existe.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre del archivo
↓
Intentar abrir archivo en modo lectura
├── FileNotFoundError → mostrar mensaje de error
↓
Si éxito → mostrar contenido del archivo
↓
Mensaje final (finally)
↓
Fin
```

### ✅ Código realizado

```python
def leer_archivo():
    try:
        ruta = input("🔍 Ingrese el nombre del archivo: ")
        with open(ruta, "r", encoding="utf-8") as archivo:
            print("📄 Contenido:")
            print(archivo.read())
    except FileNotFoundError:
        print("❌ Error: El archivo no fue encontrado.")
    else:
        print("✅ Lectura exitosa.")
    finally:
        print("📌 Proceso concluido.")

# leer_archivo()  ← descomenta para probar
```

---

## 🧪 Ejercicio 03 — `03_conversion_segura.py`

**🎯 Objetivo:** Convertir texto a entero de forma segura y controlada.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar texto
↓
Intentar convertir a entero con int()
├── ValueError → mostrar mensaje de error
↓
Si éxito → mostrar número entero
↓
Mensaje final (finally)
↓
Fin
```

### ✅ Código realizado

```python
def convertir_a_entero():
    try:
        valor = input("Ingrese un número: ")
        numero = int(valor)
    except ValueError:
        print("❌ Error: No se pudo convertir a número entero.")
    else:
        print(f"✅ Conversión exitosa: {numero}")
    finally:
        print("📌 Conversión finalizada.")

# convertir_a_entero()  ← descomenta para probar
```

---

## 🧾 Cierre de la clase

Dominar `try`, `except`, `else` y `finally` te permite diseñar software más profesional, preparado para fallos y con experiencia de usuario sólida. Aplicar estas estructuras es una señal de madurez como desarrollador.

---

## 🧠 Evaluación simbólica

🔸 Identificación y uso de bloques `try-except`: ✅ Perfecto\
🔸 Manejo de errores específicos: ✅ Correcto\
🔸 Flujo profesional con `else` y `finally`: ✅ Aplicado\
🔸 UX, claridad y robustez: ✅ Nivel avanzado

📌 **Nota simbólica: 10.5/10** 🎯 ¡Dominio profesional!

¿Avanzamos con la Clase 15 o deseas reforzar esta antes? 🧑‍🏫✨

