"""
===================================================================================================
!🧪 EJERCICIO 2  CLASE 17
?📌 Nombre: Guardar múltiples registros en archivo con append
todo::🔑 Enfoque: escritura segura en modo “a” (append) para acumular datos

?🎯 ¿Qué debe hacer el programa?
1️⃣ Abrir el archivo notas.txt (creado en el ejercicio anterior).
2️⃣ Leer su contenido línea por línea.
3️⃣ Mostrar cada línea con un formato ordenado, limpio y numerado.
4️⃣ Evitar errores si el archivo está vacío o no existe (opcional, si lo quieres hacer más pro).
5️⃣ Cerrar con un mensaje final de cierre elegante.
===================================================================================================
"""
#1️⃣ Abrir el archivo 'notas.txt' en modo lectura usando 'with'
with open("notas.txt", "r", encoding="utf-8") as archivo:
    #2️⃣ Usa .readlines() para leer todas las líneas como una lista
    lineas = archivo.readlines()

#3️⃣ Mostrar encabezado visual
print("📋 Lista de estudiantes registrados:\n")
print("="*50)

#4️⃣ Contador manual para líneas no vacías
contador = 1
for linea in lineas:
    #5️⃣ Filtrar líneas vacías y mostrar con número y formato: “Nº X ➜ contenido”
    if linea.strip():  # Solo muestra la línea si no está vacía
        print(f"Nº {contador} ➜ {linea.strip()}")
        contador += 1

# Si no hay líneas no vacías, mostrar mensaje
if contador == 1:
    print("⚠️ No hay registros de estudiantes en el archivo.")