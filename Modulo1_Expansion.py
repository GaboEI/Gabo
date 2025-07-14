"""
# Expansión del Módulo 1: Fundamentos de Programación - 10 Clases Adicionales

**Objetivo**: Reforzar los fundamentos del Módulo 1 (tipos de datos, estructuras de control, funciones, manejo de errores, archivos, listas, diccionarios, tuplas, sets) y preparar para el Módulo 2 (Programación Orientada a Objetos) con 10 clases adicionales. Cada clase (~5-6 horas) está diseñada para tus **8 horas diarias** de estudio, dejando tiempo para descansos y revisión. Los proyectos se conectan con tus ejercicios actuales (**estudiantes** y **Gestor de Tareas**) y tu programa de estudio.

**Duración estimada**: 10 días (~50-60 horas).

**Estructura por clase**:
- **Teoría (1.5-2 horas)**: Explicación del tema con conceptos clave.
- **Ejercicios cortos (1-1.5 horas)**: Prácticas simples para aplicar la teoría.
- **Mini-proyecto (2-3 horas)**: Proyecto práctico que integra el tema.
- **Tiempo restante**: Revisión, subir a GitHub, descansos (Pomodoro: 25 min estudio, 5 min descanso).

**Consejos para estudiar**:
- Divide las 8 horas: 3h teoría/ejercicios, 3h mini-proyecto, 2h revisión/descansos.
- Usa la IA (como yo) para resolver dudas, revisar código, o pedir más ejercicios.
- Sube cada proyecto a GitHub para practicar para el Módulo 4.
- Recursos: "Automate the Boring Stuff with Python" (gratis online), videos de Corey Schafer o Tech With Tim.
- Autoevalúate al final con un examen de 10 ejercicios (nota mínima 7/10).

---

## Clase 11: Sets y operaciones avanzadas

### Teoría: Conjuntos (sets)
- **Qué son**: Estructuras de datos que almacenan elementos únicos, sin orden ni duplicados.
- **Creación**: `set([1, 2, 3])` o `{1, 2, 3}`.
- **Métodos**:
  - `add(x)`: Añade un elemento.
  - `remove(x)`: Elimina un elemento (lanza error si no existe).
  - `discard(x)`: Elimina un elemento (no lanza error).
- **Operaciones**:
  - Unión (`|`): Combina elementos de dos sets.
  - Intersección (`&`): Elementos comunes.
  - Diferencia (`-`): Elementos en un set pero no en otro.
  - Diferencia simétrica (`^`): Elementos en uno u otro, pero no en ambos.
- **Uso**: Evitar duplicados, comparar colecciones, validaciones.

### Ejemplo teórico
```python
nombres = {"Ana", "Juan", "María"}
nombres.add("Pedro")  # Añade Pedro
nombres.discard("Ana")  # Elimina Ana
print(nombres)  # {'Juan', 'María', 'Pedro'}

set_a = {"Ana", "Juan"}
set_b = {"Ana", "Pedro"}
print(set_a & set_b)  # {'Ana'} (intersección)
print(set_a - set_b)  # {'Juan'} (diferencia)
```

### Ejercicio corto
Compara dos listas de estudiantes para encontrar nombres comunes y únicos.
```python
estudiantes_a = [{"nombre": "Ana"}, {"nombre": "Juan"}, {"nombre": "María"}]
estudiantes_b = [{"nombre": "Ana"}, {"nombre": "Pedro"}, {"nombre": "María"}]
nombres_a = set(est["nombre"] for est in estudiantes_a)
nombres_b = set(est["nombre"] for est in estudiantes_b)
print(f"Estudiantes en ambos grupos: {nombres_a & nombres_b}")  # {'Ana', 'María'}
print(f"Solo en grupo A: {nombres_a - nombres_b}")  # {'Juan'}
print(f"Solo en grupo B: {nombres_b - nombres_a}")  # {'Pedro'}
```

### Mini-proyecto: Evitar tareas duplicadas en el Gestor de Tareas
Modifica el **Gestor de Tareas** para usar un set y evitar agregar tareas duplicadas.
```python
archivo_tareas = "tareas_gabo.txt"

def cargar_tareas():
    try:
        with open(archivo_tareas, "r", encoding="utf-8") as archivo:
            return set(linea.strip().split("|", 1)[1] for linea in archivo)
    except FileNotFoundError:
        return set()

def agregar_tarea():
    tarea = input("Tarea: ").strip()
    if not tarea:
        print("⚠️ La tarea no puede estar vacía.")
        return
    tareas = cargar_tareas()
    if tarea in tareas:
        print(f"⚠️ La tarea '{tarea}' ya existe.")
        return
    with open(archivo_tareas, "a", encoding="utf-8") as archivo:
        archivo.write(f"P|{tarea}\n")
    print(f"✅ Tarea '{tarea}' agregada.")

def main():
    while True:
        print("\n[1] Agregar tarea\n[2] Ver tareas\n[3] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            try:
                with open(archivo_tareas, "r", encoding="utf-8") as archivo:
                    for i, linea in enumerate(archivo, 1):
                        print(f"{i}. {linea.strip()}")
            except FileNotFoundError:
                print("⚠️ No hay tareas.")
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: El set `tareas` almacena descripciones únicas, verificando duplicados antes de agregar una tarea al archivo. Esto refuerza el uso de sets y manejo de archivos.

### Tiempo sugerido
- Teoría: 1.5h (lee sobre sets, prueba ejemplos).
- Ejercicio corto: 1.5h (implementa y prueba el código).
- Mini-proyecto: 3h (modifica el Gestor de Tareas, prueba casos).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 12: Tuplas y datos inmutables

### Teoría: Tuplas
- **Qué son**: Estructuras de datos inmutables (no se pueden modificar tras crearlas).
- **Creación**: `(1, 2, 3)` o `tuple([1, 2, 3])`.
- **Usos**: Almacenar datos fijos (fechas, coordenadas), claves en diccionarios.
- **Características**: Inmutables, rápidas, permiten desempaquetado (`x, y = (1, 2)`).
- **Métodos**: Solo `count` y `index` (por inmutabilidad).

### Ejemplo teórico
```python
fecha = (15, 7, 2025)  # Día, mes, año
print(fecha[0])  # 15
dia, mes, ano = fecha  # Desempaquetado
print(f"{dia}/{mes}/{ano}")  # 15/7/2025

notas = (8.5, 9.0, 7.5)
notas += (8.0,)  # Crea una nueva tupla
print(notas)  # (8.5, 9.0, 7.5, 8.0)
```

### Ejercicio corto
Modifica el ejercicio de **estudiantes** para almacenar notas como una tupla.
```python
estudiantes = []

def agregar_nota_extra(nombre, nueva_nota):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            try:
                nueva_nota = float(nueva_nota)
                if not 0 <= nueva_nota <= 10:
                    raise ValueError("Nota debe estar entre 0 y 10.")
                estudiante["notas"] += (nueva_nota,)
                print(f"✅ Nota {nueva_nota} agregada a {nombre}.")
                return
            except ValueError as e:
                print(f"⚠️ Error: {e}")
                return
    print(f"⚠️ Estudiante {nombre} no encontrado.")

estudiantes.append({"nombre": "Ana", "edad": 20, "notas": (8.5,)})
agregar_nota_extra("Ana", 9.0)
print(estudiantes[0]["notas"])  # (8.5, 9.0)
```

### Mini-proyecto: Fechas en el Gestor de Tareas
Añade una fecha de creación (como tupla: día, mes, año) a cada tarea.
```python
from datetime import date

archivo_tareas = "tareas_gabo.txt"

def agregar_tarea():
    tarea = input("Tarea: ").strip()
    if not tarea:
        print("⚠️ La tarea no puede estar vacía.")
        return
    hoy = date.today()
    fecha = (hoy.day, hoy.month, hoy.year)
    with open(archivo_tareas, "a", encoding="utf-8") as archivo:
        archivo.write(f"P|{tarea}|{fecha}\n")
    print(f"✅ Tarea '{tarea}' agregada con fecha {fecha}.")

def main():
    while True:
        print("\n[1] Agregar tarea\n[2] Ver tareas\n[3] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            try:
                with open(archivo_tareas, "r", encoding="utf-8") as archivo:
                    for i, linea in enumerate(archivo, 1):
                        estado, tarea, fecha = linea.strip().split("|")
                        print(f"{i}. [{estado}] {tarea} (Fecha: {fecha})")
            except FileNotFoundError:
                print("⚠️ No hay tareas.")
            except ValueError:
                print("⚠️ Error en el formato del archivo.")
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: La tupla `fecha` guarda la fecha de creación, que se escribe en el archivo. Esto refuerza tuplas y manejo de archivos, conectando con el **Gestor de Tareas**.

### Tiempo sugerido
- Teoría: 1.5h (lee sobre tuplas, prueba ejemplos).
- Ejercicio corto: 1.5h (modifica estudiantes).
- Mini-proyecto: 3h (añade fechas al Gestor de Tareas).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 13: Manejo de errores avanzado

### Teoría: Excepciones avanzadas
- **Qué son**: Mecanismos para manejar errores en tiempo de ejecución.
- **Tipos comunes**: `ValueError` (entrada inválida), `IndexError` (índice fuera de rango), `TypeError` (tipo incorrecto), `FileNotFoundError` (archivo no encontrado).
- **Estructura**: `try`, `except`, `else`, `finally`, `raise` para errores personalizados.
- **Buenas prácticas**: Maneja excepciones específicas, usa mensajes claros.

### Ejemplo teórico
```python
try:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        raise ValueError("El número no puede ser negativo.")
    print(f"Resultado: {numero * 2}")
except ValueError as e:
    print(f"⚠️ Error: {e}")
else:
    print("Operación exitosa.")
finally:
    print("Finalizando...")
```

### Ejercicio corto
Valida entradas en el ejercicio de **estudiantes** para evitar datos inválidos.
```python
def agregar_estudiante(lista):
    try:
        nombre = input("Nombre: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        edad = int(input("Edad: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        nota = float(input("Nota: "))
        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10.")
        lista.append({"nombre": nombre, "edad": edad, "nota": nota})
        print(f"✅ Estudiante {nombre} agregado.")
    except ValueError as e:
        print(f"⚠️ Error: {e}")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

estudiantes = []
agregar_estudiante(estudiantes)
```

### Mini-proyecto: Robustez en el Gestor de Tareas
Mejora el **Gestor de Tareas** para validar el formato del archivo y manejar errores específicos.
```python
archivo_tareas = "tareas_gabo.txt"

def cargar_tareas():
    try:
        with open(archivo_tareas, "r", encoding="utf-8") as archivo:
            tareas = []
            for linea in archivo:
                try:
                    estado, tarea = linea.strip().split("|", 1)
                    if estado not in ["P", "C"]:
                        raise ValueError(f"Estado inválido en: {linea.strip()}")
                    tareas.append((estado, tarea))
                except ValueError as e:
                    print(f"⚠️ Error en línea: {e}")
            return tareas
    except FileNotFoundError:
        print("⚠️ No hay tareas registradas.")
        return []
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")
        return []

def main():
    while True:
        print("\n[1] Ver tareas\n[2] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            tareas = cargar_tareas()
            for i, (estado, tarea) in enumerate(tareas, 1):
                estado_legible = "Pendiente" if estado == "P" else "Completada"
                print(f"{i}. [{estado_legible}] {tarea}")
        elif opcion == "2":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: El código valida cada línea del archivo, asegurando que el estado sea "P" o "C". Maneja errores específicos y generales, mejorando la robustez del **Gestor de Tareas**.

### Tiempo sugerido
- Teoría: 1.5h (lee sobre excepciones, prueba ejemplos).
- Ejercicio corto: 1.5h (valida estudiantes).
- Mini-proyecto: 3h (mejora el Gestor de Tareas).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 14: Módulos estándar de Python

### Teoría: Módulos estándar
- **Qué son**: Bibliotecas incluidas en Python para tareas comunes.
- **Módulos clave**:
  - `math`: Operaciones matemáticas (raíz cuadrada, potencia).
  - `random`: Generar datos aleatorios.
  - `datetime`: Manejo de fechas y horas.
  - `os`: Interacción con el sistema de archivos.
- **Uso**: Importar con `import`, acceder a funciones con `modulo.funcion()`.

### Ejemplo teórico
```python
import random
import math
import datetime

print(random.randint(1, 10))  # Número aleatorio entre 1 y 10
print(math.sqrt(16))  # 4.0
print(datetime.date.today())  # Fecha actual
```

### Ejercicio corto
Genera matrículas aleatorias para el ejercicio de **estudiantes**.
```python
import random
import string

def generar_matricula():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

estudiantes = []
estudiante = {"nombre": "Ana", "edad": 20, "nota": 8.5, "matricula": generar_matricula()}
estudiantes.append(estudiante)
print(f"Matrícula generada: {estudiante['matricula']}")
```

### Mini-proyecto: Organizador de archivos
Crea un programa que organice archivos por extensión usando `os`.
```python
import os

def organizar_archivos(directorio):
    try:
        for archivo in os.listdir(directorio):
            if os.path.isfile(archivo):
                extension = archivo.split(".")[-1].lower()
                carpeta = f"Archivos_{extension}"
                os.makedirs(carpeta, exist_ok=True)
                os.rename(archivo, os.path.join(carpeta, archivo))
        print("✅ Archivos organizados.")
    except OSError as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    organizar_archivos(".")
```
- **Explicación**: El programa crea carpetas por extensión (por ejemplo, `Archivos_txt`) y mueve archivos, usando `os` para interactuar con el sistema de archivos.

### Tiempo sugerido
- Teoría: 1.5h (lee sobre módulos, prueba ejemplos).
- Ejercicio corto: 1.5h (genera matrículas).
- Mini-proyecto: 3h (implementa el organizador).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 15: Introducción a clases y objetos

### Teoría: Clases y objetos
- **Qué son**: Clases son plantillas para crear objetos, que agrupan datos (atributos) y funciones (métodos).
- **Componentes**:
  - `__init__`: Constructor para inicializar atributos.
  - `__str__`: Método para representar el objeto como cadena.
  - Atributos: Variables asociadas al objeto.
- **Uso**: Organizar código de forma modular, preparar para POO (Módulo 2).

### Ejemplo teórico
```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

est = Estudiante("Ana", 20)
print(est)  # Ana, 20 años
```

### Ejercicio corto
Refactoriza el ejercicio de **estudiantes** usando una clase `Estudiante`.
```python
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}"

estudiantes = []
try:
    nombre = input("Nombre: ").strip()
    edad = int(input("Edad: "))
    nota = float(input("Nota: "))
    estudiantes.append(Estudiante(nombre, edad, nota))
    print(estudiantes[0])
except ValueError:
    print("⚠️ Ingrese datos válidos.")
```

### Mini-proyecto: Gestor de Tareas con clases
Refactoriza el **Gestor de Tareas** usando una clase `Tarea`.
```python
archivo_tareas = "tareas_gabo.txt"

class Tarea:
    def __init__(self, descripcion, estado="P"):
        self.descripcion = descripcion
        self.estado = estado
    
    def __str__(self):
        estado_legible = "Pendiente" if self.estado == "P" else "Completada"
        return f"[{estado_legible}] {self.descripcion}"

    def to_file_format(self):
        return f"{self.estado}|{self.descripcion}\n"

def cargar_tareas():
    try:
        with open(archivo_tareas, "r", encoding="utf-8") as archivo:
            return [Tarea(linea.split("|", 1)[1], linea[0]) for linea in archivo]
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(archivo_tareas, "w", encoding="utf-8") as archivo:
        archivo.writelines(tarea.to_file_format() for tarea in tareas)

def main():
    while True:
        print("\n[1] Agregar tarea\n[2] Ver tareas\n[3] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            descripcion = input("Tarea: ").strip()
            if descripcion:
                tareas = cargar_tareas()
                if not any(t.descripcion == descripcion for t in tareas):
                    tareas.append(Tarea(descripcion))
                    guardar_tareas(tareas)
                    print(f"✅ Tarea '{descripcion}' agregada.")
                else:
                    print("⚠️ Tarea ya existe.")
            else:
                print("⚠️ La tarea no puede estar vacía.")
        elif opcion == "2":
            tareas = cargar_tareas()
            if tareas:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
            else:
                print("⚠️ No hay tareas.")
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: La clase `Tarea` organiza los datos, preparando para el Módulo 2. El código usa manejo de archivos y validaciones, conectando con el **Gestor de Tareas**.

### Tiempo sugerido
- Teoría: 1.5h (lee sobre clases, prueba ejemplos).
- Ejercicio corto: 1.5h (refactoriza estudiantes).
- Mini-proyecto: 3h (refactoriza Gestor de Tareas).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 16: Módulos y organización de código

### Teoría: Módulos
- **Qué son**: Archivos `.py` que contienen funciones, clases, o variables reutilizables.
- **Uso**: Importar con `import modulo` o `from modulo import funcion`.
- **Ventajas**: Organiza código, permite reutilización, prepara para proyectos grandes.

### Ejemplo teórico
```python
# utilidades.py
def validar_nombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    return nombre.strip()

# main.py
from utilidades import validar_nombre

try:
    nombre = validar_nombre(input("Nombre: "))
    print(f"Nombre válido: {nombre}")
except ValueError as e:
    print(f"⚠️ Error: {e}")
```

### Ejercicio corto
Crea un módulo con funciones utilitarias para validar entradas.
```python
# utils.py
def validar_nombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    return nombre.strip()

# main.py
from utils import validar_nombre

try:
    nombre = validar_nombre(input("Nombre: "))
    print(f"Nombre válido: {nombre}")
except ValueError as e:
    print(f"⚠️ Error: {e}")
```

### Mini-proyecto: Gestor de Tareas modular
Separa el **Gestor de Tareas** en dos archivos: `tareas.py` y `main.py`.
```python
# tareas.py
archivo_tareas = "tareas_gabo.txt"

class Tarea:
    def __init__(self, descripcion, estado="P"):
        self.descripcion = descripcion
        self.estado = estado
    
    def __str__(self):
        estado_legible = "Pendiente" if self.estado == "P" else "Completada"
        return f"[{estado_legible}] {self.descripcion}"

    def to_file_format(self):
        return f"{self.estado}|{self.descripcion}\n"

def cargar_tareas():
    try:
        with open(archivo_tareas, "r", encoding="utf-8") as archivo:
            return [Tarea(linea.split("|", 1)[1], linea[0]) for linea in archivo]
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(archivo_tareas, "w", encoding="utf-8") as archivo:
        archivo.writelines(tarea.to_file_format() for tarea in tareas)
```
```python
# main.py
import tareas

def main():
    while True:
        print("\n[1] Agregar tarea\n[2] Ver tareas\n[3] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            descripcion = input("Tarea: ").strip()
            if descripcion:
                tareas_lista = tareas.cargar_tareas()
                if not any(t.descripcion == descripcion for t in tareas_lista):
                    tareas_lista.append(tareas.Tarea(descripcion))
                    tareas.guardar_tareas(tareas_lista)
                    print(f"✅ Tarea '{descripcion}' agregada.")
                else:
                    print("⚠️ Tarea ya existe.")
            else:
                print("⚠️ La tarea no puede estar vacía.")
        elif opcion == "2":
            tareas_lista = tareas.cargar_tareas()
            if tareas_lista:
                for i, tarea in enumerate(tareas_lista, 1):
                    print(f"{i}. {tarea}")
            else:
                print("⚠️ No hay tareas.")
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: Separa la lógica (clase `Tarea`, funciones de archivo) del menú principal, mejorando la organización y preparando para el Módulo 4 (Git).

### Tiempo sugerido
- Teoría: 1.5h (lee sobre módulos, prueba ejemplos).
- Ejercicio corto: 1.5h (crea módulo utilitario).
- Mini-proyecto: 3h (separa Gestor de Tareas).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 17: Bibliotecas externas

### Teoría: Bibliotecas externas
- **Qué son**: Módulos creados por terceros, instalados con `pip`.
- **Ejemplo**: `tabulate` para mostrar datos en tablas.
- **Instalación**: `pip install tabulate` en la terminal.
- **Uso**: Importar y aplicar para mejorar la presentación.

### Ejemplo teórico
```python
from tabulate import tabulate

datos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Juan", "nota": 7.0}
]
print(tabulate(datos, headers="keys", tablefmt="grid"))
```

### Ejercicio corto
Muestra los estudiantes en una tabla con `tabulate`.
```python
from tabulate import tabulate

estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Juan", "edad": 22, "nota": 7.0}
]
print(tabulate(estudiantes, headers="keys", tablefmt="grid"))
```

### Mini-proyecto: Gestor de Tareas con tablas
Usa `tabulate` para mostrar tareas en formato de tabla.
```python
from tabulate import tabulate
archivo_tareas = "tareas_gabo.txt"

def ver_tareas():
    try:
        with open(archivo_tareas, "r", encoding="utf-8") as archivo:
            tareas = []
            for linea in archivo:
                estado, descripcion = linea.strip().split("|", 1)
                estado_legible = "Pendiente" if estado == "P" else "Completada"
                tareas.append({"Estado": estado_legible, "Descripción": descripcion})
            if tareas:
                print(tabulate(tareas, headers="keys", tablefmt="grid"))
            else:
                print("⚠️ No hay tareas.")
    except FileNotFoundError:
        print("⚠️ No hay tareas registradas.")

def main():
    while True:
        print("\n[1] Ver tareas\n[2] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            ver_tareas()
        elif opcion == "2":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: La biblioteca `tabulate` mejora la visualización, mostrando tareas en una tabla clara. Instala con `pip install tabulate`.

### Tiempo sugerido
- Teoría: 1.5h (instala tabulate, prueba ejemplos).
- Ejercicio corto: 1.5h (tabla de estudiantes).
- Mini-proyecto: 3h (tabla en Gestor de Tareas).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 18: Proyecto integrador - Sistema de gestión de contactos

### Teoría: Proyectos integradores
- **Qué son**: Programas que combinan múltiples conceptos (listas, diccionarios, archivos, errores).
- **Objetivo**: Aplicar todo lo aprendido en un sistema completo.
- **Estructura**: Menú interactivo, manejo de datos persistentes, validaciones.

### Ejemplo teórico
```python
contactos = []

def agregar_contacto(nombre, telefono):
    contactos.append({"nombre": nombre, "telefono": telefono})
    print(f"Contacto {nombre} agregado.")
```

### Ejercicio corto
Filtra estudiantes por nota mayor a un umbral.
```python
estudiantes = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Juan", "nota": 7.0}
]
umbral = float(input("Nota mínima: "))
aprobados = [est for est in estudiantes if est["nota"] >= umbral]
print(aprobados)
```

### Mini-proyecto: Sistema de gestión de contactos
Crea un sistema para gestionar contactos (nombre, teléfono, correo).
```python
archivo_contactos = "contactos_gabo.txt"

def agregar_contacto():
    try:
        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        correo = input("Correo: ").strip()
        if not (nombre and telefono and correo):
            raise ValueError("Todos los campos son obligatorios.")
        with open(archivo_contactos, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre}|{telefono}|{correo}\n")
        print(f"✅ Contacto {nombre} agregado.")
    except ValueError as e:
        print(f"⚠️ Error: {e}")

def buscar_contacto():
    busqueda = input("Nombre a buscar: ").strip().lower()
    try:
        with open(archivo_contactos, "r", encoding="utf-8") as archivo:
            contactos = [c for c in archivo if busqueda in c.lower().split("|")[0]]
            if contactos:
                for i, contacto in enumerate(contactos, 1):
                    nombre, telefono, correo = contacto.strip().split("|")
                    print(f"{i}. Nombre: {nombre}, Teléfono: {telefono}, Correo: {correo}")
            else:
                print(f"⚠️ No se encontraron contactos con '{busqueda}'.")
    except FileNotFoundError:
        print("⚠️ No hay contactos registrados.")

def main():
    while True:
        print("\n[1] Agregar contacto\n[2] Buscar contacto\n[3] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: Este sistema usa manejo de archivos, listas, y validaciones, similar al **Gestor de Tareas**, pero enfocado en contactos.

### Tiempo sugerido
- Teoría: 1.5h (revisa conceptos de proyectos).
- Ejercicio corto: 1.5h (filtra estudiantes).
- Mini-proyecto: 3h (implementa sistema de contactos).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 19: Proyecto integrador - Calculadora científica

### Teoría: Proyectos modulares
- **Qué son**: Programas con funciones modulares y uso de bibliotecas estándar.
- **Objetivo**: Crear aplicaciones prácticas con lógica clara.
- **Ejemplo**: Calculadoras que combinan entrada/salida, funciones, y módulos.

### Ejercicio corto
Calcula la raíz cuadrada con validación.
```python
from math import sqrt

def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo.")
    return sqrt(numero)

try:
    numero = float(input("Número: "))
    print(f"Raíz: {raiz_cuadrada(numero)}")
except ValueError as e:
    print(f"⚠️ Error: {e}")
```

### Mini-proyecto: Calculadora científica
Crea una calculadora con operaciones avanzadas.
```python
from math import sqrt, pow

def calculadora():
    while True:
        print("\n[1] Suma\n[2] Raíz cuadrada\n[3] Potencia\n[4] Salir")
        opcion = input("Opción: ")
        try:
            if opcion == "1":
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {a + b}")
            elif opcion == "2":
                a = float(input("Número: "))
                print(f"Resultado: {sqrt(a)}")
            elif opcion == "3":
                a = float(input("Base: "))
                b = float(input("Exponente: "))
                print(f"Resultado: {pow(a, b)}")
            elif opcion == "4":
                break
            else:
                print("⚠️ Opción inválida.")
        except ValueError as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    calculadora()
```
- **Explicación**: La calculadora usa el módulo `math` y manejo de errores, cumpliendo con los mini-proyectos del Módulo 1.

### Tiempo sugerido
- Teoría: 1.5h (revisa módulos y proyectos).
- Ejercicio corto: 1.5h (raíz cuadrada).
- Mini-proyecto: 3h (calculadora).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Clase 20: Proyecto final - Sistema de gestión de biblioteca

### Teoría: Proyectos integradores con clases
- **Qué son**: Sistemas completos que combinan todos los conceptos del Módulo 1 y usan clases para preparar el Módulo 2.
- **Objetivo**: Crear un sistema robusto con persistencia, validaciones, y estructura orientada a objetos.

### Ejercicio corto
Crea una clase `Libro` para almacenar datos.
```python
class Libro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.estado = "D"
    
    def __str__(self):
        estado_legible = "Disponible" if self.estado == "D" else "Prestado"
        return f"{self.titulo} por {self.autor} ({self.ano}) [{estado_legible}]"

libro = Libro("Cien años de soledad", "García Márquez", 1967)
print(libro)
```

### Mini-proyecto: Sistema de gestión de biblioteca
Crea un sistema para gestionar libros con clases y persistencia.
```python
archivo_biblioteca = "biblioteca_gabo.txt"

class Libro:
    def __init__(self, titulo, autor, ano, estado="D"):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.estado = estado
    
    def __str__(self):
        estado_legible = "Disponible" if self.estado == "D" else "Prestado"
        return f"{self.titulo} por {self.autor} ({self.ano}) [{estado_legible}]"

    def to_file_format(self):
        return f"{self.estado}|{self.titulo}|{self.autor}|{self.ano}\n"

def cargar_libros():
    try:
        with open(archivo_biblioteca, "r", encoding="utf-8") as archivo:
            return [Libro(*linea.strip().split("|", 3)[1:], linea[0]) for linea in archivo]
    except FileNotFoundError:
        return []

def guardar_libros(libros):
    with open(archivo_biblioteca, "w", encoding="utf-8") as archivo:
        archivo.writelines(libro.to_file_format() for libro in libros)

def main():
    titulos = set(libro.titulo for libro in cargar_libros())
    while True:
        print("\n[1] Agregar libro\n[2] Ver libros\n[3] Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            try:
                titulo = input("Título: ").strip()
                if titulo in titulos:
                    raise ValueError("El libro ya existe.")
                autor = input("Autor: ").strip()
                ano = int(input("Año: "))
                if not (titulo and autor) or ano < 0:
                    raise ValueError("Datos inválidos.")
                libros = cargar_libros()
                libros.append(Libro(titulo, autor, ano))
                titulos.add(titulo)
                guardar_libros(libros)
                print(f"✅ Libro '{titulo}' agregado.")
            except ValueError as e:
                print(f"⚠️ Error: {e}")
        elif opcion == "2":
            libros = cargar_libros()
            if libros:
                for i, libro in enumerate(libros, 1):
                    print(f"{i}. {libro}")
            else:
                print("⚠️ No hay libros.")
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
```
- **Explicación**: Este sistema usa clases, sets para evitar duplicados, y manejo de archivos, integrando todos los conceptos del Módulo 1 y preparando para POO.

### Tiempo sugerido
- Teoría: 1.5h (revisa clases y proyectos).
- Ejercicio corto: 1.5h (clase Libro).
- Mini-proyecto: 3h (sistema de biblioteca).
- Restante: 2h (revisa, sube a GitHub, descansa).

---

## Autoevaluación del Módulo 1 Expandido

Para cumplir con la **evaluación de pase de módulo (nota mínima 7/10)**:
- **Crea un examen** con 10 ejercicios, uno por cada tema del Módulo 1:
  1. **Tipos de datos**: Convierte una cadena a entero y calcula su doble.
  2. **Variables**: Crea una constante para el máximo de estudiantes (por ejemplo, 100).
  3. **Operadores**: Verifica si un número es par usando `%`.
  4. **Estructuras de control**: Usa `if-elif` para clasificar una nota (aprobado, desaprobado).
  5. **Bucles**: Lista números del 1 al 10 con un bucle `for`.
  6. **Funciones**: Escribe una función que calcule el promedio de una lista de notas.
  7. **Manejo de errores**: Valida una entrada numérica con `try-except`.
  8. **Manejo de archivos**: Guarda una lista de nombres en un archivo.
  9. **Listas/Diccionarios/Sets/Tuplas**: Usa un set para eliminar nombres duplicados de una lista.
  10. **Clases**: Crea una clase simple para un estudiante.
- **Corrige con la IA**: Pídeme que evalúe tus soluciones y te dé una nota.
- **Proyecto final**: El sistema de biblioteca (Clase 20) puede servir como evaluación final.

---

## Cronograma para 10 días (8 horas/día)
- **Día 1 (Clase 11)**: Sets y operaciones avanzadas.
- **Día 2 (Clase 12)**: Tuplas y datos inmutables.
- **Día 3 (Clase 13)**: Manejo de errores avanzado.
- **Día 4 (Clase 14)**: Módulos estándar de Python.
- **Día 5 (Clase 15)**: Introducción a clases y objetos.
- **Día 6 (Clase 16)**: Módulos y organización de código.
- **Día 7 (Clase 17)**: Bibliotecas externas.
- **Día 8 (Clase 18)**: Sistema de gestión de contactos.
- **Día 9 (Clase 19)**: Calculadora científica.
- **Día 10 (Clase 20)**: Sistema de gestión de biblioteca.

---

## Cómo generar el PDF
1. **Copia el contenido**: Copia todo el texto anterior (desde el título hasta el cronograma).
2. **Pega en una herramienta**:
   - **Microsoft Word/Google Docs**: Pega el texto, ajusta el formato (títulos, subtítulos, código en `Courier New` o similar), y exporta como PDF.
   - **Typora/Obsidian**: Pega en un archivo `.md`, usa Markdown para formatear, y exporta como PDF.
   - **Online Markdown to PDF**: Usa un conversor como `markdown2pdf.com` o `pandoc`.
3. **Imprime o guarda**: Imprime el PDF o guárdalo en tu dispositivo para acceso rápido.

---

## Consejos para aplicar en tus estudios
- **8 horas diarias**:
  - 3h: Teoría y ejercicios cortos (lee, prueba ejemplos).
  - 3h: Mini-proyecto (implementa, prueba casos extremos).
  - 2h: Revisa el código, sube a GitHub, descansa (Pomodoro: 25 min estudio, 5 min descanso).
- **Usa la IA**:
  - Pregúntame: "Dame más ejercicios sobre sets", "Revisa mi sistema de biblioteca", o "Explícame clases de nuevo".
  - Pídeme un examen final: "Crea 10 ejercicios para evaluar el Módulo 1".
- **GitHub**:
  - Crea un repositorio por clase (por ejemplo, `gabo-clase-11-sets`).
  - Comandos básicos:
    ```bash
    git add .
    git commit -m "Clase 11: Sistema de etiquetas con sets"
    git push origin main
    ```
- **Recursos**:
  - "Automate the Boring Stuff with Python" (gratis online).
  - Videos de Corey Schafer o Tech With Tim en YouTube.
- **Motivación**:
  - Celebra cada clase completada.
  - Visualiza tus metas (freelance, apps) para mantenerte enfocado.

---

### Siguientes pasos
Si quieres, Gabo, puedo:
- Crear un examen de 10 ejercicios para la autoevaluación.
- Detallar más algún mini-proyecto (por ejemplo, añadir búsqueda al sistema de biblioteca).
- Generar un cronograma horario más específico (por ejemplo, 8:00-9:30 teoría, etc.).
- Ayudarte a configurar GitHub para subir tus proyectos.

¡Estás haciendo un progreso increíble! 🚀

"""
