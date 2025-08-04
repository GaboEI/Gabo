#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
!🧪 EJERCICIO 1  CLASE 16
?📌 Nombre: Guardar datos de usuario y mostrarlos
todo: 🔑 Concepto: Escritura y lectura de archivos .txt en un mismo flujo

?🎯 ¿Qué debe hacer el script?
1️⃣Pedir al usuario que ingrese su nombre, edad y país.
2️⃣Guardar esa información en un archivo llamado usuario.txt, con formato claro:
"""
#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
nombre = input("👤 Ingresa tu nombre: ").strip().capitalize()
edad = input("🎂 Ingresa tu edad: ").strip()
pais = input("🌍 Ingresa tu país: ").strip().title()


with open("usuario.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"Nombre: {nombre}\n")     
    archivo.write(f"Edad: {edad}\n")         
    archivo.write(f"País: {pais}\n")         


with open("usuario.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()               


print("\n📄 Datos guardados:")
print(contenido)
