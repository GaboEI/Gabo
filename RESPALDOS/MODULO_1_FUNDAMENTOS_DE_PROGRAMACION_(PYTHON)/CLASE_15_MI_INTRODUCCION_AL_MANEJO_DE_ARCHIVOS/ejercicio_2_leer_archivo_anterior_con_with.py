"""
?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
!🧪 EJERCICIO 2  CLASE 15
?📌 Nombre: Leer el archivo anterior usando with
todo: 🔑 Concepto: lectura segura con #![open(), read(), with]

?🎯 ¿Qué debe hacer el script?
1️⃣Abrir el archivo registro.txt que creaste en el ejercicio anterior.
2️⃣Leer todo su contenido.
3️⃣Mostrarlo en pantalla con print().
4️⃣Usar la estructura with open(...) as archivo: para que el archivo se cierre automáticamente.
?⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
"""
with open("registro.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("📚 Contenido del archivo:")
print(content)