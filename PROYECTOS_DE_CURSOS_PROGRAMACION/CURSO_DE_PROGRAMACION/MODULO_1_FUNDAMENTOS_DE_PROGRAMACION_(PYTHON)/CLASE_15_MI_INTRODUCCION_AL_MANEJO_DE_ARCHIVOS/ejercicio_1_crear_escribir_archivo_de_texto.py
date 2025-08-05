"""
?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
!🧪 EJERCICIO 1  CLASE 15
?📌 Nombre: Crear y escribir en un archivo de texto
todo: 🔑 Concepto: open(), write(), close()

!🎯 ¿Qué debe hacer el programa?

1️⃣ Crear un archivo llamado registro.txt.
2️⃣ Escribir dentro del archivo un mensaje personalizado:
---Por ejemplo: #?"Usuario Gabo registrado con éxito.\n"
---Y otra línea: #?"Archivo creado desde Python."
3️⃣ Cerrar correctamente el archivo con close() (sin usar with aún).
4️⃣ No debe imprimir nada en pantalla (solo escribir el archivo).
?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
"""
file = open("registro.txt", "w", encoding="utf-8")
file.write("👋Usuario Gabo registrado con éxito.\n")
file.write("Archivo creado desde Python.\n")
file.write("(❁´◡`❁)\n")
file.close()

