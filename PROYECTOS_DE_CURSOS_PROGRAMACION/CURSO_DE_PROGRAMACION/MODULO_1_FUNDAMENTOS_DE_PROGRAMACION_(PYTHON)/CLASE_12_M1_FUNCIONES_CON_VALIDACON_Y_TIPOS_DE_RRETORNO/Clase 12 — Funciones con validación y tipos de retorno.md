# 🧠 Clase 12 — Funciones con validación y tipos de retorno

---

## 🎯 Objetivo de la clase

Aprender a construir **funciones robustas** que incluyan validación de entradas, uso de condiciones internas y múltiples tipos de retorno (booleanos, cadenas, listas, etc.). Esta clase consolida las bases para crear funciones profesionales con control interno de errores y lógica adaptable.

---

## 📚 Fundamentos teóricos

Una función bien diseñada no solo ejecuta una tarea, sino que **verifica y controla** el tipo y la validez de los datos que recibe. Además, puede retornar distintos tipos de datos según la lógica aplicada.

### 🔹 Validación dentro de funciones

Consiste en comprobar que los argumentos recibidos cumplen ciertas condiciones antes de continuar el procesamiento.

#### Ejemplo:

```python
def dividir(a, b):
    if b == 0:
        return "❌ Error: división por cero"
    return a / b
```

### 🔹 Tipos de retorno válidos en Python

- `int`, `float`, `str`, `bool`
- `list`, `tuple`, `dict`, `set`
- `None` (sin retorno explícito)
- Combinaciones (`tuple` con múltiples valores, por ejemplo)

### 🔹 Patrón profesional: retorno múltiple

```python
def analizar_texto(texto):
    palabras = texto.split()
    cantidad = len(palabras)
    contiene_python = "python" in texto.lower()
    return cantidad, contiene_python
```

---

## 🧪 Ejercicio 01 — `01_validar_division.py`

**🎯 Objetivo:** Crear una función que divida dos números, validando que el divisor no sea cero.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar numerador y denominador
↓
Enviar a función dividir
↓
Si divisor == 0 → Retornar error
└── Si no → Retornar resultado
↓
Mostrar mensaje al usuario
↓
Fin
```

### ✅ Código realizado

```python
def dividir(numerador, denominador):
    if denominador == 0:
        return "Error: no se puede dividir entre 0"
    return numerador / denominador

n1 = float(input("Numerador: "))
n2 = float(input("Denominador: "))
resultado = dividir(n1, n2)
print("Resultado:", resultado)
```

---

## 🧪 Ejercicio 02 — `02_analizar_palabras.py`

**🎯 Objetivo:** Crear una función que analice un texto y retorne:

1. Número de palabras
2. Si contiene la palabra "python"

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar texto
↓
Enviar a función analizar
↓
Dividir texto en palabras
↓
Contar palabras
↓
Verificar presencia de "python"
↓
Retornar ambos resultados
↓
Mostrar resultados al usuario
↓
Fin
```

### ✅ Código realizado

```python
def analizar_texto(texto):
    palabras = texto.split()
    cantidad = len(palabras)
    contiene = "python" in texto.lower()
    return cantidad, contiene

entrada = input("Escribe una frase: ")
num_palabras, tiene_python = analizar_texto(entrada)
print("Cantidad de palabras:", num_palabras)
print("¿Contiene 'python'?:", "Sí" if tiene_python else "No")
```

---

## 🧪 Ejercicio 03 — `03_formato_y_validacion_nombre.py`

**🎯 Objetivo:** Validar si el nombre ingresado es válido (no vacío y sin números), y devolverlo formateado.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre
↓
Enviar a función validar_nombre
↓
Si nombre está vacío o contiene dígitos → Error
└── Si válido → strip() y title()
↓
Retornar nombre o error
↓
Mostrar mensaje
↓
Fin
```

### ✅ Código realizado

```python
def validar_nombre(nombre):
    if not nombre.strip() or any(char.isdigit() for char in nombre):
        return "❌ Nombre inválido."
    return nombre.strip().title()

nombre = input("Introduce tu nombre: ")
resultado = validar_nombre(nombre)
print("Resultado:", resultado)
```

---

## 🧾 Cierre de la clase

Has aprendido a construir funciones que validan internamente las entradas y retornan información de forma más profesional. Esta capacidad es clave en proyectos reales donde se necesita garantizar la robustez del software.

---

## 🧠 Evaluación simbólica

🔹 Validación de entradas: ✅ Sólida y bien aplicada 🔹 Uso de condiciones internas: ✅ Dominado 🔹 Tipos de retorno: ✅ Variados y correctos 🔹 Presentación de resultados: ✅ Clara y formateada 🔹 Nota simbólica: **10.5/10** 🏆

📘 Esta clase te sitúa en un nivel superior de control sobre funciones. ¡Excelente trabajo, Gabo!

