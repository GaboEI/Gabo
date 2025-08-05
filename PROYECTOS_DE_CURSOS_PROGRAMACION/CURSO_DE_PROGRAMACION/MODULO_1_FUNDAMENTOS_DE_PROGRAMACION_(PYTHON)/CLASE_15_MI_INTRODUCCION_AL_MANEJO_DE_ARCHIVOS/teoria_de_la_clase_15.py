"""
?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
!🧠 CLASE 15  Introducción al manejo de archivos

?📘 Módulo 1 (Ampliado)  Clase 15 de 30

todo| 🎯 Objetivo de esta clase

⏺️Aprender a leer y escribir archivos de texto con Python.
⏺️Comprender el uso de las funciones #todo: open(), read(), write() y el bloque with.
⏺️Manipular archivos .txt de forma controlada y segura.

?🧱 Conceptos clave

!Función/cláusula	¿Qué hace?
open()	            Abre un archivo para leer, escribir o ambas cosas
read()	            Lee el contenido de un archivo
write()	            Escribe texto dentro de un archivo
with	            Maneja archivos de forma segura y automática
close()	            #!Cierra el archivo manualmente (no necesario con with)
?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
"""
#!📂 Modos de apertura con open()

archivo = open("archivo.txt", "r")   # Lectura
archivo = open("archivo.txt", "w")   # Escritura (sobrescribe)
archivo = open("archivo.txt", "a")   # Escritura al final (append)

#!📘 Ejemplo básico 1: escribir un archivo

#1️⃣ Creamos y escribimos en un archivo de texto
archivo = open("saludo.txt", "w")
archivo.write("Hola Gabo, este archivo fue creado desde Python.\n")
archivo.close()  #2️⃣ Siempre se debe cerrar el archivo (si no usas with)

#!📘 Ejemplo básico 2: leer un archivo

archivo = open("saludo.txt", "r")
contenido = archivo.read()  #3️⃣ Lee todo el contenido
print(contenido)
archivo.close()

#!🧪 Ejemplo con with (forma recomendada)

#4️⃣ Con with, no necesitas cerrar manualmente
with open("saludo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

"""
?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
!💼 Aplicaciones reales en la vida profesional

✅ Leer y guardar configuraciones o preferencias de usuario
✅ Guardar logs de procesos o errores
✅ Generar reportes en .txt
✅ Automatizar edición de archivos
✅ Integrar con otros sistemas y herramientas externas

?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
"""