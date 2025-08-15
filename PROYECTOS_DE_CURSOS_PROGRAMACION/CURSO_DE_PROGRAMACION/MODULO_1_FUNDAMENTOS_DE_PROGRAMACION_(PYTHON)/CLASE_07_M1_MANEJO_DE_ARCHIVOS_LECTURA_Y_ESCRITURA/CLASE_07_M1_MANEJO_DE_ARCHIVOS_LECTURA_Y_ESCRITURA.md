# 🗂️ CLASE_07_M1_MANEJO_DE_ARCHIVOS_LECTURA_Y_ESCRITURA

## 🎯 Objetivo de la clase

Comprender el manejo básico de archivos en Python, enfocándose en la lectura y escritura de archivos de texto. Se busca dotar al estudiante de herramientas para manipular datos persistentes desde scripts Python, abriendo paso al trabajo con almacenamiento no volátil.

---

## 🧠 Teoría Profunda

### 📌 ¿Qué es un archivo?

Un archivo es una colección de datos almacenados en un medio físico (como un disco duro) bajo un nombre específico. En Python, el manejo de archivos se realiza con funciones que permiten abrir, leer, escribir, y cerrar estos archivos.

---

### 📎 Modos de apertura de archivos

```python
open(""archivo.txt"", ""modo"")
```

| Modo | Significado |
|------|-------------|
| `""r""` | Read (lectura, archivo debe existir) |
| `""w""` | Write (escritura, sobreescribe si existe) |
| `""a""` | Append (agrega al final) |
| `""x""` | Exclusive creation (falla si el archivo existe) |
| `""b""` | Binario (usar junto con otro modo) |
| `""t""` | Texto (modo por defecto) |

> 🧠 **Nota**: Siempre que se abre un archivo, es importante cerrarlo. Usar `with` garantiza que se cierre automáticamente.

---

### 🧩 Funciones principales

- `open(ruta, modo)`: Abre el archivo
- `archivo.read()`: Lee todo el contenido
- `archivo.readline()`: Lee una línea
- `archivo.readlines()`: Retorna todas las líneas como lista
- `archivo.write(cadena)`: Escribe texto
- `archivo.writelines(lista)`: Escribe una lista de líneas

---

### 🧷 Context Manager (`with`)

```python
with open(""datos.txt"", ""r"") as archivo:
    contenido = archivo.read()
```

Ventajas:

- Cierra el archivo automáticamente.
- Mejora la legibilidad del código.
- Evita errores por olvido de `.close()`.

---

## 🧪 Aplicaciones prácticas del manejo de archivos

- 📝 Automatización de informes y reportes.
- 📊 Almacenamiento de datos estructurados simples.
- 📒 Guardar logs y auditorías en scripts.
- 🗂️ Creación de sistemas de notas, inventarios, agendas.
- 📤 Exportar datos recolectados desde formularios o sensores.

---

## 🧱 Ejercicios resueltos de la clase

---

### ✅ ejercicio_01_escritura_y_lectura_basica

#### 🎯 Objetivo:

Crear un archivo, escribir contenido en él y luego leerlo.

#### 🔽 Diagrama de flujo

```,
Inicio
 ↓
Solicitar nombre y edad
 ↓
Abrir archivo en modo escritura
 ↓
Escribir nombre y edad
 ↓
Cerrar archivo
 ↓
Abrir archivo en modo lectura
 ↓
Leer contenido
 ↓
Mostrar en consola
 ↓
Fin
```

#### 💻 Código realizado

```python
nombre = input(""Ingresa tu nombre: "")
edad = input(""Ingresa tu edad: "")

with open(""datos_usuario.txt"", ""w"") as archivo:
    archivo.write(f""Nombre: {nombre}\nEdad: {edad}\n"")

with open(""datos_usuario.txt"", ""r"") as archivo:
    contenido = archivo.read()
    print(""Contenido del archivo:\n"")
    print(contenido)
```

---

### ✅ ejercicio_02_guardar_lista_de_tareas

#### 🎯 Objetivo:

Guardar una lista de tareas en un archivo `.txt` y luego mostrarla al usuario.

#### 🔽 Diagrama de flujo

```
Inicio
 ↓
Inicializar lista vacía
 ↓
Solicitar tareas hasta que sea ""fin""
 ↓
Guardar tareas en lista
 ↓
Abrir archivo en modo escritura
 ↓
Escribir tareas en archivo (una por línea)
 ↓
Cerrar archivo
 ↓
Abrir archivo en modo lectura
 ↓
Leer y mostrar contenido
 ↓
Fin
```

#### 💻 Código realizado:

```python
tareas = []
print(""Escribe tus tareas. Escribe 'fin' para terminar."")

while True:
    tarea = input(""Tarea: "")
    if tarea.lower() == ""fin"":
        break
    tareas.append(tarea + ""\n"")

with open(""lista_tareas.txt"", ""w"") as archivo:
    archivo.writelines(tareas)

print(""\nTus tareas guardadas:"")
with open(""lista_tareas.txt"", ""r"") as archivo:
    print(archivo.read())
```

---

### ✅ ejercicio_03_append_y_lectura_linea_a_linea

#### 🎯 Objetivo:
Agregar contenido a un archivo existente sin sobrescribirlo y leer línea por línea.

#### 🔽 Diagrama de flujo:

```
Inicio
 ↓
Solicitar frase al usuario
 ↓
Abrir archivo en modo append
 ↓
Escribir frase
 ↓
Cerrar archivo
 ↓
Abrir archivo en modo lectura
 ↓
Leer línea por línea
 ↓
Mostrar cada línea con numeración
 ↓
Fin
```

#### 💻 Código realizado:

```python
frase = input(""Escribe una frase para guardar: "")

with open(""diario.txt"", ""a"") as archivo:
    archivo.write(frase + ""\n"")

with open(""diario.txt"", ""r"") as archivo:
    print(""\nContenido del diario:\n"")
    for i, linea in enumerate(archivo, 1):
        print(f""{i}: {linea.strip()}"")
```

---

## 🔚 Cierre de la clase

Esta clase introduce uno de los pilares esenciales para construir programas útiles: la persistencia de datos. El manejo de archivos permite crear sistemas funcionales, como gestores de tareas, almacenamiento de formularios, historiales, logs, bitácoras o listas. Dominar estos conceptos abre la puerta a proyectos que necesitan guardar información entre ejecuciones.

➡️ **A partir de esta base podrás implementar:**

- Sistemas de notas personales.
- Aplicaciones de registro.
- Automatización con logs.
- Scripts para informes automáticos.
"
