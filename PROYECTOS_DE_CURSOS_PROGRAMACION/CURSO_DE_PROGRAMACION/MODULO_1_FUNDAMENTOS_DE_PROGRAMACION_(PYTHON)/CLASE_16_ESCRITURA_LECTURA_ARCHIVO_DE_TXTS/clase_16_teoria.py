#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
!🧠 CLASE 16  Escritura y lectura de archivos de texto
?📘 Módulo 1 (Ampliado)  Clase 16 de 30

todo: 🎯 Objetivo

1️⃣ Aprender a combinar escritura y lectura de archivos .txt.
2️⃣ Usar correctamente #![write(), read(), readlines(), y with.]
3️⃣ Manipular archivos existentes y ver sus contenidos desde el código.
4️⃣ Practicar el flujo completo: #![guardar ➜ cerrar ➜ volver a abrir ➜ leer.]

?🧱 Funciones clave
!Función	        ¿Qué hace?

write(texto)	    Escribe texto dentro del archivo
read()	            Lee todo el contenido como un solo string
readlines()	        Lee línea por línea y devuelve una lista
with	            Abre el archivo y lo cierra automáticamente
"""
#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※

#!📘 Ejemplo profesional

#1️⃣ Escribimos un archivo
with open("notas.txt", "w", encoding="utf-8") as file:
    file.write("Estudiante: Gabo\n")
    file.write("Nota: 9.8\n")
    file.write("Curso: Programación intensiva\n")

#2️⃣ Leemos el contenido que escribimos
with open("notas.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

print("📄 Contenido del archivo:")
print(contenido)
#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
!💡 Aplicaciones reales
✅ Reportes de ventas, logs de actividad
✅ Registro de entradas o formularios
✅ Edición de plantillas de configuración
✅ Sistemas básicos de exportación de datos
"""
#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
