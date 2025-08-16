# 🧠 Clase 13 — Parámetros opcionales, funciones limpias

---

## 🎯 Objetivo de la clase

Comprender y aplicar el uso de **parámetros opcionales**, valores por defecto y cómo escribir **funciones limpias**, es decir, funciones legibles, concisas, bien documentadas y con una única responsabilidad clara. Esta clase representa un paso hacia la profesionalización del código y la adopción de buenas prácticas.

---

## 📚 Fundamentos teóricos

### 🔹 ¿Qué son los parámetros opcionales?

Son parámetros que tienen un valor por defecto asignado. Esto permite que la función sea invocada sin necesidad de proporcionar todos los argumentos.

#### Ejemplo básico:

```python
def saludar(nombre, idioma="es"):
    if idioma == "es":
        print(f"Hola, {nombre}!")
    elif idioma == "en":
        print(f"Hello, {nombre}!")
```

### 🔹 Ventajas de los parámetros opcionales

- Mayor flexibilidad
- Código más limpio y reutilizable
- Ideal para funciones con comportamiento por defecto que puede personalizarse

### 🔹 Funciones limpias (Clean Code)

Una función limpia cumple con estos principios:

- Tiene **una sola responsabilidad**
- Es **corta** y **clara**
- Usa **nombres descriptivos** para sus variables y argumentos
- Tiene **comentarios útiles** o docstrings explicativos
- Evita efectos colaterales y validaciones fuera de su alcance

---

## 🧪 Ejercicio 01 — `01_saludo_idioma.py`

**🎯 Objetivo:** Crear una función de saludo con idioma opcional (por defecto español).

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre
↓
Enviar a función saludar(nombre, idioma="es")
↓
Si idioma == "es" → Mostrar "Hola"
├── Si idioma == "en" → Mostrar "Hello"
└── Otro → Mensaje de idioma no soportado
↓
Fin
```

### ✅ Código realizado

```python
def saludar(nombre, idioma="es"):
    if idioma == "es":
        print(f"Hola, {nombre}!")
    elif idioma == "en":
        print(f"Hello, {nombre}!")
    else:
        print("Idioma no soportado.")

saludar("Gabo")
saludar("Gabo", idioma="en")
saludar("Gabo", idioma="fr")
```

---

## 🧪 Ejercicio 02 — `02_generar_linea.py`

**🎯 Objetivo:** Generar una línea de caracteres personalizada con longitud e ícono opcional.

### 🧭 Diagrama de flujo

```
Inicio
↓
Función generar_linea(longitud=10, simbolo="*")
↓
Repetir símbolo "longitud" veces
↓
Retornar cadena generada
↓
Mostrar al usuario
↓
Fin
```

### ✅ Código realizado

```python
def generar_linea(longitud=10, simbolo="*"):
    return simbolo * longitud

print(generar_linea())
print(generar_linea(5))
print(generar_linea(7, "#"))
```

---

## 🧪 Ejercicio 03 — `03_registro_usuario.py`

**🎯 Objetivo:** Crear una función para registrar usuarios con nombre obligatorio y país opcional (por defecto "Desconocido").

### 🧭 Diagrama de flujo

```
Inicio
↓
Solicitar nombre (obligatorio)
↓
Solicitar país (opcional)
↓
Función registrar(nombre, pais="Desconocido")
↓
Devolver cadena formateada
↓
Mostrar en consola
↓
Fin
```

### ✅ Código realizado

```python
def registrar(nombre, pais="Desconocido"):
    return f"Usuario: {nombre} | País: {pais}"

print(registrar("Ana"))
print(registrar("Luis", "Cuba"))
```

---

## 🧾 Cierre de la clase

Has aprendido a usar **parámetros opcionales**, mejorar la flexibilidad de tus funciones y adoptar buenas prácticas de **código limpio**. Este enfoque mejora no solo la funcionalidad, sino también el mantenimiento del código.

---

## 🧠 Evaluación simbólica

🔹 Uso de valores por defecto: ✅ Correcto y práctico\
🔹 Funciones limpias y legibles: ✅ Excelentes prácticas\
🔹 Ejercicios con claridad y utilidad: ✅ Completos y bien presentados\
🔹 Modularidad y organización: ✅ Avanzada

📌 **Nota simbólica: 10.5/10** 🌟 ¡Dominio absoluto!

---

¿Listo para avanzar a la siguiente clase?

