#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
!🧪 EJERCICIO 2  CLASE 16
?📌 Nombre: Leer línea por línea con readlines()
🔑 Concepto: lectura de archivo como lista + recorrido con bucle
"""
#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
with open("usuario.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


f = f"{"№":<4} |{"📜 Contenido del Archivo linea por linea":<45}"
print("=" * 55)
print(f)
print("=" * 55)
for i, line in enumerate(lines, start=1):
    print(f"{i:<4} |{line.strip():<45}")

#※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※

"""
respuesta consola:
=======================================================
№    |📜 Contenido del Archivo linea por linea
=======================================================
1    |Nombre: Gabo
2    |Edad: 27
3    |País: Rusia
"""
