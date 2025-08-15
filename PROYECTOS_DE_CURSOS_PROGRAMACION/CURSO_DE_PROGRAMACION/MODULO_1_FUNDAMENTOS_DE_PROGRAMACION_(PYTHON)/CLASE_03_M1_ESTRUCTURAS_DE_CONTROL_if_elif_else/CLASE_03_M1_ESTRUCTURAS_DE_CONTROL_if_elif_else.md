# 🔁 Clase 03 — Estructuras de control: if, elif, else

---

## 🎯 Objetivo de la clase

Aprender a utilizar estructuras condicionales en Python para tomar decisiones dentro del código. Usar `if`, `elif` y `else` para ejecutar diferentes bloques de código según condiciones lógicas.

---

## 📚 Teoría profunda

### 🧱 ¿Qué es una estructura condicional?

Permite que un programa ejecute diferentes instrucciones según si una condición es verdadera o falsa.

### 🔑 Sintaxis básica

```python
if condición:
    bloque_si_verdadero
elif otra_condición:
    bloque_si_otra_condición
else:
    bloque_si_todo_lo_demás
```

- `if`: evalúa la primera condición
- `elif`: opcional, evalúa otra condición si la anterior fue falsa
- `else`: opcional, se ejecuta si ninguna condición anterior fue verdadera

### 📌 Evaluación booleana

Las condiciones son expresiones que devuelven `True` o `False`. Se pueden construir con:

- Comparaciones (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Lógica (`and`, `or`, `not`)

### 🧠 Indentación obligatoria

Python exige que el bloque de código bajo cada `if`, `elif`, `else` esté correctamente indentado (por convención: 4 espacios).

---

## 💡 Aplicaciones reales

- Verificar contraseñas
- Evaluar el resultado de un examen
- Clasificar edades
- Determinar precios con descuento

---

## 🧪 Ejercicios prácticos

---

### ✍️ 01\_evaluar\_mayoria\_de\_edad.py

**🎯 Objetivo:** Determinar si una persona es mayor o menor de edad.

#### 🧭 Diagrama de flujo

```.
Inicio
↓
Solicitar edad
↓
Si edad >= 18 → Mostrar "Mayor de edad"
↓
Si no → Mostrar "Menor de edad"
↓
Fin
```

#### ✅ Código realizado

```python
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("✅ Eres mayor de edad.")
else:
    print("⛔ Eres menor de edad.")
```

---

### ✍️ 02\_clasificar\_nota.py

**🎯 Objetivo:** Clasificar una nota entre 0 y 100 en categorías.

#### 👁️ Diagrama de flujo

```.
Inicio
↓
Pedir nota
↓
Si nota >= 90 → Excelente
├── elif nota >= 70 → Aprobado
├── elif nota >= 50 → Regular
└── else → Reprobado
↓
Fin
```

#### 💥 Código realizado

```python
nota = int(input("Ingrese su calificación (0-100): "))

if nota >= 90:
    print("🏅 Excelente")
elif nota >= 70:
    print("✅ Aprobado")
elif nota >= 50:
    print("⚠️ Regular")
else:
    print("❌ Reprobado")
```

---

### ✍️ 03\_tipo\_de\_numero.py

**🎯 Objetivo:** Determinar si un número es positivo, negativo o cero.

#### 💥 Diagrama de flujo

```,
Inicio
↓
Pedir número
↓
Si número > 0 → Positivo
├── elif número < 0 → Negativo
└── else → Cero
↓
Fin
```

#### 🟨 Código realizado

```python
numero = float(input("Ingrese un número: "))

if numero > 0:
    print("🔵 Número positivo")
elif numero < 0:
    print("🔴 Número negativo")
else:
    print("⚪ Es cero")
```

---

### ✍️ 04\_menu\_opciones.py

**🎯 Objetivo:** Crear un menú simple con 3 opciones y ejecutar la acción correspondiente.

#### 🟨 Diagrama de flujo

```.
Inicio
↓
Mostrar menú
↓
Pedir opción
↓
Si opción == 1 → Saludar
├── elif opción == 2 → Mostrar hora
├── elif opción == 3 → Salir
└── else → Opción inválida
↓
Fin
```

#### 👁️ Código realizado

```python
print("""
🔸 MENÚ 🔸
1. Saludar
2. Ver hora
3. Salir
""")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    print("👋 ¡Hola, usuario!")
elif opcion == "2":
    from datetime import datetime
    print("🕒 La hora actual es:", datetime.now().strftime("%H:%M:%S"))
elif opcion == "3":
    print("👋 Hasta luego!")
else:
    print("❌ Opción no válida")
```

---

## 🧾 Cierre de la clase

Las estructuras condicionales permiten dirigir el flujo del programa y tomar decisiones dinámicas. Saber aplicar `if`, `elif` y `else` te permitirá escribir programas interactivos, inteligentes y adaptativos. ¡Este es uno de los pilares del pensamiento computacional!

---

## 🧠 Evaluación

🔹 Ejercicios presentados: **4**\
🔹 Razonamiento aplicado: ✅ Excelente\
🔹 Errores detectados: **0**\
🔹 Calidad del código: **10/10**
