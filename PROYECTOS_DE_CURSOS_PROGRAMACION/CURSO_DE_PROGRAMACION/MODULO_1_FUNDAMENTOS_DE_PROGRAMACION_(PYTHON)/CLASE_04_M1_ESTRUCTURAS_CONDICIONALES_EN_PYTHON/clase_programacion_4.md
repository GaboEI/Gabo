# **Clase de Programación 4: Estructuras condicionales en Python**

## **1️⃣ Objetivo de la clase**

- Aprender a usar `if`, `elif`, `else` para tomar decisiones en Python.
- Aplicar decisiones lógicas en programas reales.
- Resolver ejercicios prácticos que integren lógica y automatización.

---

## **2️⃣ Teoría clara y práctica**

### **¿Qué son las estructuras condicionales?**

Permiten a tu programa tomar decisiones según condiciones:

```python
if condicion:
    # Código si se cumple la condición
elif otra_condicion:
    # Código si la anterior no se cumplió y esta sí
else:
    # Código si ninguna condición anterior se cumplió
```

**Usos:** Validaciones de datos, flujos de decisión, generación de mensajes automáticos.

### **Símbolos importantes:**

- `:` indica que después de la condición viene un bloque indentado.
- Indentación (4 espacios o tabulación) para definir el bloque.
- `==`, `!=`, `<`, `>`, `<=`, `>=` para comparar valores.
- `and`, `or`, `not` para combinar condiciones.

---

## **3️⃣ Ejercicios prácticos (resueltos)**

### **✅ Ejercicio 1: Clasificación de calificaciones**

Pide una calificación numérica y devuelve el nivel del estudiante.

```python
calificacion = 88

if calificacion >= 95:
    print("Excelente")
elif calificacion >= 85:
    print("Bien")
elif calificacion >= 75:
    print("Regular")
elif calificacion >= 60:
    print("Mal pero aprobó")
else:
    print("Desaprobado")
```

### **✅ Ejercicio 2: Positivo, negativo o cero**

```python
numero = -3

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es igual a cero")
```

### **✅ Ejercicio 3: Determinar el mayor de tres números**

```python
num1 = 10
num2 = 25
num3 = 20

if num1 >= num2 and num1 >= num3:
    print("El número mayor es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El número mayor es:", num2)
else:
    print("El número mayor es:", num3)
```

---

## **4️⃣ Ejercicio de integración (script de 3 estudiantes)**

Se integraron los 3 ejercicios en un solo script que:

- Evalúa las notas de 3 estudiantes.
- Clasifica cada nota.
- Determina cuál obtuvo la nota más alta.

```python
# Notas de los tres estudiantes
nota_est1 = 92
nota_est2 = 67
nota_est3 = 76

# Evaluación individual
print("Evaluación Individual de Estudiantes:")

# Estudiante 1
print("\nEstudiante 1, nota:", nota_est1)
if nota_est1 >= 95:
    print("Excelente")
elif nota_est1 >= 85:
    print("Bien")
elif nota_est1 >= 75:
    print("Regular")
elif nota_est1 >= 60:
    print("Mal pero aprobó")
else:
    print("Desaprobado")

# Estudiante 2
print("\nEstudiante 2, nota:", nota_est2)
if nota_est2 >= 95:
    print("Excelente")
elif nota_est2 >= 85:
    print("Bien")
elif nota_est2 >= 75:
    print("Regular")
elif nota_est2 >= 60:
    print("Mal pero aprobó")
else:
    print("Desaprobado")

# Estudiante 3
print("\nEstudiante 3, nota:", nota_est3)
if nota_est3 >= 95:
    print("Excelente")
elif nota_est3 >= 85:
    print("Bien")
elif nota_est3 >= 75:
    print("Regular")
elif nota_est3 >= 60:
    print("Mal pero aprobó")
else:
    print("Desaprobado")

# Determinar la nota más alta
if nota_est1 >= nota_est2 and nota_est1 >= nota_est3:
    mejor_resultado = nota_est1
    estudiante = "Estudiante 1"
elif nota_est2 >= nota_est1 and nota_est2 >= nota_est3:
    mejor_resultado = nota_est2
    estudiante = "Estudiante 2"
else:
    mejor_resultado = nota_est3
    estudiante = "Estudiante 3"

print(f"\nLa nota más alta es {mejor_resultado}, obtenida por el {estudiante}.")
```

---

## **5️⃣ Aplicaciones prácticas en la vida profesional**

✅ Automatización de reportes de calificaciones. ✅ Clasificación de resultados en encuestas y formularios. ✅ Evaluación de datos de ventas y desempeño. ✅ Construcción de flujos de decisión en bots y aplicaciones.

---

## ✅ **Estado al cierre de la Clase 4:**

- Estructuras condicionales entendidas y practicadas.
- Ejercicios completados con nota alta.
- Listo para **Clase de Programación 5: Bucles (for y while).**

Cuando estés listo, avisa con: **“Clase de programación 5”** y continuamos tu avance sin perder ritmo.

¡Excelente trabajo, Gabo! Tu avance es firme y profesional.
