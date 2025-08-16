# 🧪 Clase 09 — Proyecto Mini: Calculadoras, organizadores de texto, etc. (versión extendida y profesional)

---

## 🎯 Objetivo de la clase

Aplicar de forma integrada los conocimientos adquiridos en las clases anteriores para construir proyectos funcionales: una calculadora aritmética, una calculadora lógica y un organizador de texto básico. Este mini-proyecto refuerza el pensamiento algorítmico, la modularización del código, el manejo de errores y la interacción con el usuario.

---

## 📚 Enfoque teórico

Esta clase está diseñada como una práctica aplicada. Aquí consolidamos habilidades clave:

- Uso de funciones personalizadas y parámetros
- Control de flujo con `if`, `elif`, `else`
- Entrada y salida de datos del usuario
- Manejo de errores con `try/except`
- Operadores aritméticos y lógicos
- Manipulación básica de strings y estructuras de datos

### 🧩 ¿Por qué crear mini proyectos?

- Permiten integrar múltiples habilidades en una sola solución.
- Favorecen el razonamiento estructurado y el diseño de soluciones modulares.
- Simulan tareas reales del entorno profesional.

---

## 🧪 Ejercicio 01 — `01_calculadora_aritmetica.py`

**🎯 Objetivo:** Desarrollar una calculadora básica de operaciones: suma, resta, multiplicación y división.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar número 1
↓
Solicitar número 2
↓
Solicitar operación (+, -, *, /)
↓
Validar operación
├── No válida → mostrar error y salir
↓
Realizar operación
↓
Mostrar resultado
↓
Fin
```

### ✅ Código realizado

```python
def calculadora():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        op = input("Ingrese la operación (+, -, *, /): ")

        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        elif op == "*":
            resultado = a * b
        elif op == "/":
            if b == 0:
                print("❌ Error: División por cero no permitida.")
                return
            resultado = a / b
        else:
            print("❌ Operación no válida.")
            return

        print(f"✅ Resultado: {resultado}")

    except ValueError:
        print("❌ Entrada inválida. Por favor, use solo números.")

calculadora()
```

---

## 🧪 Ejercicio 02 — `02_calculadora_logica.py`

**🎯 Objetivo:** Simular operaciones lógicas: AND, OR y NOT usando inputs booleanos.

### 🧭 Diagrama de flujo

```
Inicio
↓
Pedir operación lógica (AND, OR, NOT)
↓
Pedir booleanos según el caso
↓
Evaluar expresión
↓
Mostrar resultado
↓
Fin
```

### ✅ Código realizado

```python
def calculadora_logica():
    operacion = input("Ingrese la operación lógica (AND, OR, NOT): ").lower()

    if operacion == "not":
        a = input("Valor (True/False): ").lower() == "true"
        print("Resultado:", not a)

    elif operacion in ["and", "or"]:
        a = input("Valor A (True/False): ").lower() == "true"
        b = input("Valor B (True/False): ").lower() == "true"

        if operacion == "and":
            print("Resultado:", a and b)
        else:
            print("Resultado:", a or b)

    else:
        print("❌ Operación no válida.")

calculadora_logica()
```

---

## 🧪 Ejercicio 03 — `03_organizador_de_texto.py`

**🎯 Objetivo:** Tomar un texto y mostrarlo organizado: número de palabras, palabras únicas, y versión capitalizada.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar texto al usuario
↓
Separar palabras
↓
Contar cantidad total
↓
Eliminar duplicados con set
↓
Capitalizar texto
↓
Mostrar resumen
↓
Fin
```

### ✅ Código realizado

```python
def organizador_de_texto():
    texto = input("Ingrese un texto: ")
    palabras = texto.split()
    unicas = set(palabras)
    capitalizado = texto.title()

    print("\n📊 Resumen del texto:")
    print("- Total de palabras:", len(palabras))
    print("- Palabras únicas:", len(unicas))
    print("- Texto capitalizado:", capitalizado)

organizador_de_texto()
```

---

## 🧾 Cierre de la clase

🎓 Este mini-proyecto demuestra la capacidad de combinar múltiples herramientas del lenguaje Python en problemas concretos. Nos prepara para construir aplicaciones más complejas al consolidar habilidades como:

- Entrada y validación del usuario
- Modularización
- Control de flujo
- Manejo de errores
- Salida formateada y presentación profesional

---

## 🧠 Evaluación simbólica

🔹 Aplicación de operadores: ✅ Aritméticos y lógicos\
🔹 Estructuras vistas: ✅ Funciones, listas, sets, strings, condicionales\
🔹 Validación y errores: ✅ Incluidos\
🔹 Presentación: ✅ Clara, profesional y didáctica\
🔹 Nota simbólica: **10.5/10**

📘 **Clase completa, extensa y lista para ser subida a GitHub. ¡Buen trabajo integrando conceptos, Gabo! 💻🚀**

