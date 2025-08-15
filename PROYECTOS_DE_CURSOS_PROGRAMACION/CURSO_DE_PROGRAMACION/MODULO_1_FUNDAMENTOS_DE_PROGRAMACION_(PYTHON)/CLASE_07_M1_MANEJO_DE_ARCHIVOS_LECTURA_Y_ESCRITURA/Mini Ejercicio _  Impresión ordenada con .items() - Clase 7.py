# ✅ Mini Ejercicio: Impresión legible con .items()
# 1️⃣ Crear un diccionario libro con:
libro = {
    "titulo": "Manipulacion Fascial",
    "Autor": "Stecco",
    "Anio": 2015,
    "Generro": "Medicina"
    }
# 2️⃣ Imprimir el diccionario de forma directa
print(libro)
# 3️⃣ Imprimir de forma ordenada usando .items()
print("\nInformacion del libro")
for clave, valor in libro.items():
    print(f"- {clave.capitalize()} : {valor}")
    