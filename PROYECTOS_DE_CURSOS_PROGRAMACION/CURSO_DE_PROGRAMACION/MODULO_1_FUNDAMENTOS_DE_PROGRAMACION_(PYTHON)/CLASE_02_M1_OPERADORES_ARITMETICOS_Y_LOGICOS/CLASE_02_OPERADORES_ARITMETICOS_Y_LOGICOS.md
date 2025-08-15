# ➗ Clase 02 — Operadores aritméticos y lógicos

---

## 🎯 Objetivo de la clase

Comprender y aplicar los operadores aritméticos y lógicos en Python, construyendo expresiones que permiten evaluar condiciones, realizar cálculos y tomar decisiones dentro de un programa.

---

## 📚 Teoría profunda

### 🔢 Operadores aritméticos

Los operadores aritméticos permiten realizar cálculos matemáticos entre valores numéricos (`int`, `float`, etc.).

| Operador | Descripción       | Ejemplo        | Resultado |
|----------|-------------------|----------------|-----------|
| `+`      | Suma              | `4 + 2`        | `6`       |
| `-`      | Resta             | `10 - 3`       | `7`       |
| `*`      | Multiplicación    | `5 * 3`        | `15`      |
| `/`      | División flotante | `10 / 4`       | `2.5`     |
| `//`     | División entera   | `10 // 4`      | `2`       |
| `%`      | Módulo (resto)    | `10 % 4`       | `2`       |
| `**`     | Potencia          | `2 ** 3`       | `8`       |

### 🔄 Precedencia de operadores

Los operadores aritméticos tienen un orden de ejecución:

1. Paréntesis `()`
2. Potencias `**`
3. Multiplicación/División/Modulo `* / // %`
4. Suma/Resta `+ -`

### ⚖️ Operadores lógicos

Los operadores lógicos permiten evaluar expresiones booleanas:

| Operador | Nombre | Uso                          | Resultado               |
|----------|--------|------------------------------|--------------------------|
| `and`    | Y      | `True and False`             | `False`                 |
| `or`     | O      | `False or True`              | `True`                  |
| `not`    | NO     | `not True`                   | `False`                 |

### 🔍 Evaluación lógica

- `and`: solo es `True` si ambas expresiones son `True`.
- `or`: es `True` si al menos una es `True`.
- `not`: invierte el valor lógico.

---

## 💡 Aplicaciones reales

- Verificar si una persona puede acceder a un sistema (mayor de edad y con permiso).
- Determinar si una compra califica para descuento (precio > 100 o cliente VIP).
- Evaluar resultados matemáticos y condiciones combinadas.

---

## 🧪 Ejercicios prácticos

---

### ✍️ 01_operaciones_basicas.py

**🎯 Objetivo:** Realizar todas las operaciones aritméticas básicas con dos números ingresados por el usuario.

#### 🧭 Diagrama de flujo

```.
Inicio
↓
Solicitar dos números
↓
Realizar suma, resta, multiplicación, división, módulo y potencia
↓
Mostrar resultados
↓
Fin
```

#### ✅ Código realizado

```python
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potencia: {a ** b}")
```

---

### ✍️ 02_logica_acceso.py

**🎯 Objetivo:** Verificar si un usuario puede acceder a una página según edad y contraseña correcta.

#### 💥 Diagrama de flujo

```.
Inicio
↓
Pedir edad y contraseña
↓
Evaluar si edad ≥ 18 y contraseña correcta
↓
Mostrar resultado (Acceso permitido o denegado)
↓
Fin
```

#### 💥 Código realizado

```python
edad = int(input("Ingrese su edad: "))
clave = input("Ingrese su contraseña: ")

if edad >= 18 and clave == "python123":
    print("✔️ Acceso permitido")
else:
    print("❌ Acceso denegado")
```

---

### ✍️ 03_evaluar_descuento.py

**🎯 Objetivo:** Determinar si una compra califica para un descuento.

#### 🟨 Diagrama de flujo

```,
Inicio
↓
Pedir monto de compra y tipo de cliente
↓
Evaluar si compra > 100 o cliente == "VIP"
↓
Mostrar si tiene descuento o no
↓
Fin
```

#### 🟨 Código realizado

```python
monto = float(input("Monto de la compra: "))
cliente = input("Tipo de cliente (Normal/VIP): ").lower()

if monto > 100 or cliente == "vip":
    print("🎉 Descuento aplicado")
else:
    print("Sin descuento disponible")
```

---

### ✍️ 04_validar_entrada.py

**🎯 Objetivo:** Comprobar si una persona puede entrar a una sala de estudio: solo mayores de 16 y con carnet.

#### 🏁 Diagrama de flujo

```.
Inicio
↓
Pedir edad y si tiene carnet
↓
Evaluar condiciones con and
↓
Mostrar resultado
↓
Fin
```

#### 🏁 Código realizado

```python
edad = int(input("Edad del usuario: "))
carnet = input("¿Tiene carnet de estudiante? (sí/no): ").lower()

if edad >= 16 and carnet == "sí":
    print("✅ Entrada permitida")
else:
    print("🚫 Entrada denegada")
```

---

## 🧾 Cierre de la clase

Con esta clase has aprendido a dominar la lógica fundamental de Python mediante operadores aritméticos y lógicos. Estos elementos son esenciales para construir condiciones, validar entradas, realizar cálculos y dirigir el flujo de cualquier programa.

---

## 🧠 Evaluación

🔹 Ejercicios presentados: **4**  
🔹 Dominio de lógica: ✅ Correcto  
🔹 Errores detectados: **0**  
🔹 Calidad del código: **10/10**
