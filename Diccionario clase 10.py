# Lista principal donde se guardarán los estudiantes
estudiantes = []

# Función para agregar un estudiante a la lista
def agregar_estudiante(lista):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    nota = float(input("Ingrese la nota del estudiante: "))

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }

    lista.append(estudiante)
    print(f"Estudiante {nombre} agregado correctamente.\n")

# Bucle para agregar varios estudiantes
for _ in range(3):
    agregar_estudiante(estudiantes)

# Imprimir en formato tabla
print("\nLista de Estudiantes Registrados:\n")
print("N°  | Nombre       | Edad | Nota")
print("-" * 30)

for idx, est in enumerate(estudiantes, 1):
    nombre = est['nombre'].ljust(12)
    edad = str(est['edad']).ljust(4)
    nota = f"{est['nota']:.2f}".ljust(5)
    print(f"{str(idx).ljust(3)} | {nombre} | {edad} | {nota}")