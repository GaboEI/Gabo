print("Sistema de registro de notas. Ingrese 'salir' para terminar.")

def evaluar_nota(nota):
    if not (0 <= nota <= 100):
        return "❌ Nota inválida"
    elif 90 <= nota <= 100:
        return "🎓 Excelente"
    elif 75 <= nota < 90:
        return "👍 Muy bien"
    elif 60 <= nota < 75:
        return "😊 Bien"
    elif 50 <= nota < 60:
        return "🌟 Aprobado justo"
    else:
        return "❌ Reprobado"

while True:
    nombre = input("Nombre del estudiante: ").strip()
    if nombre.lower() == "salir":
        break
    if not nombre:
        print("❌ Error: El nombre no puede estar vacío.")
        continue
    if not all(c.isalpha() or c.isspace() for c in nombre):
        print("❌ Error: El nombre solo puede contener letras y espacios.")
        continue

    try:
        nota = int(input("Nota (0-100): "))
        evaluacion = evaluar_nota(nota)
        if "❌" in evaluacion:
            print(evaluacion)
            continue
    except ValueError:
        print("❌ Error: La nota debe ser un número entero.")
        continue

    with open("notas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Nombre: {nombre} – Nota: {nota} – {evaluacion}\n")
    
    print(f"✅ Nota registrada con éxito para {nombre} ({evaluacion})")

print("\n=== Notas Registradas ===")
try:
    with open("notas.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("No hay notas registradas aún.")