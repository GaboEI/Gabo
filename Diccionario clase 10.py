# Lista principal donde se guardarán los estudiantes
estudiantes = []

# Función para agregar un estudiante a la lista
def agregar_estudiante(lista):
    # Solicitar el nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    
    # Solicitar la edad del estudiante y convertir a entero
    edad = int(input("Ingrese la edad del estudiante: "))
    
    # Solicitar la nota del estudiante y convertir a float
    nota = float(input("Ingrese la nota del estudiante: "))
    
    # Crear un diccionario con los datos del estudiante
    estudiante = {
        'nombre': nombre,
        'edad': edad,
        'nota': nota
    }
    
    # Agregar el diccionario a la lista de estudiantes
    lista.append(estudiante)
    
    # Mensaje de confirmación
    print(f"Estudiante {nombre} agregado correctamente.\n")

# Función para mostrar los estudiantes en formato de tabla
def mostrar_estudiantes(lista):
    print("\nLista de Estudiantes Registrados:\n")
    print("{:<4} | {:<12} | {:<5} | {:<6}".format("N°", "Nombre", "Edad", "Nota"))
    print("-" * 40)
    
    for i, estudiante in enumerate(lista, start=1):
        print("{:<4} | {:<12} | {:<5} | {:<6.2f}".format(
            i,
            estudiante['nombre'],
            estudiante['edad'],
            estudiante['nota']
        ))

# Programa principal
# Bucle para agregar varios estudiantes (3 en este caso)
for _ in range(3):
    agregar_estudiante(estudiantes)

# Mostrar la lista de estudiantes en formato de tabla
mostrar_estudiantes(estudiantes)