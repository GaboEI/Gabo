# Sin encoding (puede funcionar en algunos sistemas, en otros da error)
archivo = open("areas.txt", "w", encoding="utf-8")
archivo.write("Hola, ¿Como estas?\n")
archivo.write("¿Manana estudiarremos programacion?\n")
archivo.write("simbolos: €, £, ¥, №, ⁂, ※\n")
archivo.close()


archivo = open("tareas.txt", "r", encoding="utf-8")
contenido = archivo.read()
print(contenido)
archivo.close()


with open("prueba_sin_utf8.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)