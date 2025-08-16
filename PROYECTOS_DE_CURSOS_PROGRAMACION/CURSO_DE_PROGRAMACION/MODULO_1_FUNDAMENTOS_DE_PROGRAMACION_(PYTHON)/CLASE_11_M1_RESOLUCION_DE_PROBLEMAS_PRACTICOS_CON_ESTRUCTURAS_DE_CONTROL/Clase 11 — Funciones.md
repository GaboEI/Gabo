# 🧠 Clase 11 — Funciones: def, argumentos, retorno de valores

---

## 🎯 Objetivo de la clase

Dominar el uso de **funciones definidas por el usuario** en Python, aprendiendo a diseñarlas con argumentos, retorno de valores y estructuras internas claras. Esta clase marca el inicio formal de la programación modular y profesional.

---

## 📚 Fundamentos teóricos

Una **función** es un bloque de código reutilizable que realiza una tarea específica. En Python se define con la palabra clave `def`.

### 🔹 ¿Por qué usar funciones?

- Organizan el código en bloques lógicos
- Aumentan la reutilización y claridad
- Facilitan la depuración y el mantenimiento
- Permiten crear bibliotecas de utilidades

### 🔹 Componentes de una función:

- `def` ➜ palabra clave para definir
- Nombre ➜ identificador de la función
- Paréntesis ➜ donde van los argumentos
- Dos puntos `:` ➜ indica inicio del bloque
- Cuerpo ➜ el bloque de instrucciones indentadas
- `return` ➜ valor devuelto (opcional)

### 🔹 Ejemplo básico

```python
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Gabo")
print(mensaje)  # Hola, Gabo!
```

---

## 📌 Aplicaciones en la vida real

- Calcular precios con impuestos
- Validar datos de entrada
- Operaciones matemáticas personalizadas
- Automatizar tareas repetitivas

---

## 🧪 Ejercicio 01 — `01_funcion_suma_personalizada.py`

**🎯 Objetivo:** Crear una función que reciba dos números, los sume y retorne el resultado.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar dos números
↓
Enviar a función suma
↓
Retornar resultado
↓
Mostrar resultado
↓
Fin
```

### ✅ Código realizado

```python
def sumar(a, b):
    return a + b

x = int(input("Primer número: "))
y = int(input("Segundo número: "))
resultado = sumar(x, y)
print("Resultado:", resultado)
```

---

## 🧪 Ejercicio 02 — `02_funcion_validar_edad.py`

**🎯 Objetivo:** Validar si una edad ingresada permite votar.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar edad
↓
Enviar a función validar
↓
Si edad >= 18 → Puede votar
└── Si no → No puede votar
↓
Mostrar resultado
↓
Fin
```

### ✅ Código realizado

```python
def puede_votar(edad):
    return edad >= 18

edad = int(input("Introduce tu edad: "))
if puede_votar(edad):
    print("✅ Puedes votar.")
else:
    print("❌ No puedes votar.")
```

---

## 🧪 Ejercicio 03 — `03_funcion_formato_nombre.py`

**🎯 Objetivo:** Formatear un nombre completo: eliminar espacios y poner en mayúscula.

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre
↓
Enviar a función formatear
↓
Aplicar strip() y title()
↓
Retornar nombre limpio
↓
Mostrar nombre
↓
Fin
```

### ✅ Código realizado

```python
def formatear(nombre):
    return nombre.strip().title()

nombre = input("Escribe tu nombre completo: ")
print("Bienvenido,", formatear(nombre))
```

---

## 🧾 Cierre de la clase

En esta clase aprendiste a construir funciones útiles, legibles y reutilizables, lo que te da herramientas para estructurar mejor tus proyectos futuros. Las funciones son la piedra angular de todo código profesional.

---

## 🧠 Evaluación simbólica

🔹 Claridad en argumentos: ✅ Excelente 🔹 Uso de `return`: ✅ Correcto 🔹 Diseño de lógica propia: ✅ Implementado con éxito 🔹 Formato y presentación: ✅ Cumplido 🔹 Nota simbólica: **10/10**

📦 **Clase documentada profesionalmente y lista para GitHub. ¡Sigues avanzando como un verdadero desarrollador!** 🚀🧑‍💻

