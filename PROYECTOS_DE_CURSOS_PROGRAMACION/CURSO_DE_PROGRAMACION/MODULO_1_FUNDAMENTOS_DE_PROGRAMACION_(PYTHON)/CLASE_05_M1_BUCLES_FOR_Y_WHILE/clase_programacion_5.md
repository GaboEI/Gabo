# **Clase de Programación 5: Bucles (**`** y **`**) en Python**

## **1️⃣ Objetivos de la clase**

- Comprender qué son los bucles `for` y `while`.
- Automatizar tareas repetitivas de forma ordenada.
- Utilizar `range()` con pasos.
- Usar `+=` para sumas acumulativas y `*=` para productos acumulativos.
- Aplicar `input()` para interacción.
- Mostrar resultados claros usando `f-string`.

---

## **2️⃣ Teoría clara y práctica**

### **🔹 ¿Qué es un bucle?**

Un bucle permite **ejecutar instrucciones de forma repetida** según una condición o un rango.

---

### \*\*🔹 Bucle \*\*\`\`

Ejecuta mientras la condición sea verdadera.

```python
contador = 1
while contador <= 5:
    print("Contador:", contador)
    contador += 1
```

---

### \*\* 🔹 Bucle \*\*\`\`

Permite recorrer rangos o listas de forma ordenada.

```python
for i in range(1, 6):
    print("Número:", i)
```

---

### \*\*🔹 Uso de \*\*`** y **`

- `+=` ➔ Suma acumulativa: `total += valor` (equivale a `total = total + valor`).
- `*=` ➔ Producto acumulativo: `factorial *= valor` (equivale a `factorial = factorial * valor`).

---

## **3️⃣ Ejercicios prácticos (completos y ejecutados)**

### ✅ \*\*Ejercicio 1: Imprimir números del 1 al 10 usando \*\*\`\`

```python
contador = 1
while contador <= 10:
    print("contador:", contador)
    contador += 1
```

---

### ✅ \*\*Ejercicio 2: Sumar del 1 al 100 usando \*\*\`\`

```python
suma = 0
for i in range(1, 101):
    suma += i
print(f"La suma de los números del 1 al 100 es: {suma}")
```

---

### ✅ \*\*Ejercicio 3: Tabla de multiplicar usando \*\*`** y **`

```python
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```

---

### ✅ \*\*Mini ejercicio de factorial usando \*\*\`\`

```python
numero = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")
```

---

### ✅ **Ejercicio Final Integrador Clase 5**

```python
n = int(input("Ingresa el número para generar el reporte: "))

# Tabla de multiplicar
tprint(f"\nTabla de multiplicar del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"\nEl factorial de {n} es: {factorial}")

# Suma del 1 al n
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"\nLa suma de los números del 1 a {n} es: {suma}")

# Mensaje de cierre
print("\nGracias por usar el Generador de Reportes.")
```

---

## **4️⃣ Aplicaciones prácticas en la vida profesional**

- Automatización de cálculos repetitivos.
- Validación y procesamiento de datos.
- Creación de reportes automatizados.
- Construcción de scripts que interactúan con usuarios y generan resultados.

---

## **5️⃣ Resumen de preguntas y respuestas durante la clase:**

✅ **¿Qué significa **``**?** ➔ Es la variable de control, se incrementa automáticamente y puedes cambiar su nombre. ✅ **¿Qué es **``**?** ➔ Cuando ejecutas el programa, aparece el mensaje en consola y debes escribir el número allí y presionar Enter. ✅ **¿Por qué usamos ****\`\`****?** ➔ Porque `range()` no incluye el último número, por lo que sumamos 1 para incluir `n` en el cálculo.

---

## ✅ **Estado de cierre de la Clase 5:**

- Bucles `for` y `while` comprendidos y practicados.
- Uso de `+=` y `*=` dominado.
- Uso de `input()` y `f-string` consolidado.
- Ejercicios resueltos de forma profesional.
- Listo para avanzar a **Clase de Programación 6: Funciones en Python.**

---
