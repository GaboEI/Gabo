# **Clase de Programación 6: Funciones en Python**

## **1️⃣ Objetivos de la clase**

- Comprender qué es una función y para qué sirve.
- Aprender a definir funciones con `def`.
- Usar parámetros, argumentos y `return` en funciones.
- Aplicar funciones en cálculos reales (suma, factorial, tablas de multiplicar).
- Preparar estructuras para automatización profesional y proyectos.

---

## **2️⃣ Teoría clara y completa**

### **🔹 ¿Qué es una función?**

Es un bloque de código reutilizable que realiza una tarea específica, evitando repetir código y organizando proyectos de forma profesional.

**Sintaxis:**

```python
def nombre_funcion(parametros):
    # bloque de código indentado
    return valor_opcional
```

✅ `def`: palabra clave para definir funciones. ✅ `nombre_funcion`: nombre de la función. ✅ `parametros`: valores que la función recibe. ✅ `return`: devuelve un resultado para su uso posterior.

---

### **🔹 Ejemplo básico de función:**

```python
def saludar():
    print("¡Hola!")

saludar()
```

### **🔹 Ejemplo con parámetros:**

```python
def saludar_usuario(nombre):
    print(f"¡Hola {nombre}! Bienvenido a programación.")

saludar_usuario("Gabo")
```

### **🔹 Ejemplo con ****\`\`****:**

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)
```

---

## **3️⃣ Ejercicios realizados en clase**

### ✅ **Ejercicio 1: Función de saludo personalizado**

```python
def saludar_usuario(nombre):
    print(f"¡Hola {nombre}! Bienvenido a programación.")

saludar_usuario("Gabo")
```

### ✅ **Ejercicio 2: Función que sume dos números**

```python
def sumar(a, b):
    resultado = a + b
    return resultado

suma1 = sumar(867, 23)
suma2 = sumar(400, 50)
suma3 = sumar(1, 8)
total = suma1 + suma2 + suma3

print(f"suma 1: {suma1}\nsuma 2: {suma2}\nsuma 3: {suma3}\n\nEl resultado de la suma de las tres operaciones es: {total}")
```

### ✅ **Ejercicio 3: Función de tabla de multiplicar**

```python
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(9)
```

### ✅ **Ejercicio 4: Función de factorial**

```python
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

n = int(input("Ingresa un número para calcular su factorial: "))
resultado = calcular_factorial(n)
print(f"\nEl factorial de {n} es: {resultado}")
```

### ✅ **Ejercicio Final Integrador de Clase 6**

```python
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def calcular_suma(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    return suma

n = int(input("Ingresa un número para generar el reporte: "))
print(f"\nTabla de multiplicar del {n}:")
tabla_multiplicar(n)

factorial = calcular_factorial(n)
print(f"\nEl factorial de {n} es: {factorial}")

suma = calcular_suma(n)
print(f"\nLa suma de los números del 1 a {n} es: {suma}")

print("\n✅ Gracias por usar el Generador de Reportes con Funciones.")
```

---

## **4️⃣ Aplicaciones profesionales de lo aprendido**

- Automatizar cálculos y reportes de negocio.
- Estructurar scripts de automatización de ventas o inventario.
- Preparación para usar funciones en proyectos con APIs y bases de datos.
- Uso de funciones para limpieza de datos y procesos de OCR.

---

## **5️⃣ Resumen de preguntas y respuestas de la clase**

✅ **¿Por qué usar funciones?** Para reutilizar código, mantener orden y facilitar automatización. ✅ **¿Qué es ****\`\`****?** Python lo requiere para entender el bloque de la función. ✅ **¿Puedo llamar una función varias veces?** Sí, las funciones pueden reutilizarse con diferentes valores. ✅ **¿Qué sucede si no coloco ****\`\`****?** La función no devuelve un valor, solo ejecuta las instrucciones internas.

---

## ✅ **Cierre de la Clase 6**

- Comprendes la creación y uso de funciones.
- Realizaste ejercicios aplicando funciones en casos prácticos.
- Estás preparado para avanzar a **Clase 7: Estructuras de Datos (listas, tuplas, diccionarios, sets).**

---
