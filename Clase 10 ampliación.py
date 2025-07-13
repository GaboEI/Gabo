# Lista principal donde se guardarán los estudiantes
estudiantes = []

# Función para agregar un estudiante a la lista
def agregar_estudiante(lista):
    # Solicitar el nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    # Solicitar la edad del estudiante
    edad = int(input("Ingrese la edad del estudiante: "))
    # Solicitar la nota del estudiante
    nota = float(input("Ingrese la nota del estudiante: "))
    
    # Crear el diccionario con los datos
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }
    
    # Agregar el diccionario a la lista
    lista.append(estudiante)
    
    # Mensaje de confirmación
    print(f"Estudiante {nombre} agregado correctamente.")

# Programa principal
# Bucle para agregar varios estudiantes (3 en este caso)
for _ in range(3):
    agregar_estudiante(estudiantes)

# Imprimir la lista para verificar de manera ordenada
print("\nLista de estudiantes:")
print("-" * 40)  # Separador visual
if estudiantes:
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"Estudiante {i}:")
        print(f"  Nombre: {estudiante['nombre']}")
        print(f"  Edad: {estudiante['edad']} años")
        print(f"  Nota: {estudiante['nota']}")
        print("-" * 40)  # Separador entre estudiantes
else:
    print("No se agregaron estudiantes.")