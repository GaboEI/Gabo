def obtener_desempeno(nota):
    """
    Determina el desempeño del estudiante basado en su nota.
    """
    if not (0 <= nota <= 100):
        return "Nota inválida"
    elif 90 <= nota <= 100:
        return "Excelente"
    elif 75 <= nota < 90:
        return "Muy bien"
    elif 60 <= nota < 75:
        return "Bien"
    elif 50 <= nota < 60:
        return "Aprobado justo"
    else: # Esto cubre 0 <= nota < 50
        return "Reprobado"

def registrar_nota():
    """
    Solicita el nombre y la nota de un estudiante, valida ambos,
    determina el desempeño y lo registra en el archivo 'notas.txt'.
    """
    while True: # Bucle para la entrada del estudiante completo (nombre y nota)
        # --- Bucle para la validación del nombre ---
        nombre_estudiante_valido = False
        while not nombre_estudiante_valido:
            nombre_completo = input("Ingresa el nombre del estudiante (o 'salir' para finalizar): ").strip()
            
            if nombre_completo.lower() == 'salir':
                return False # Indica que el usuario quiere salir del programa
            
            nombre_limpio = nombre_completo.strip()

            if not nombre_limpio:
                print("El nombre no puede estar vacío. Inténtalo de nuevo.")
            elif not all(word.isalpha() for word in nombre_limpio.split()):
                print("Error: El nombre solo debe contener letras y espacios. Inténtalo de nuevo.")
            else:
                nombre_estudiante = ' '.join(word.capitalize() for word in nombre_limpio.split())
                nombre_estudiante_valido = True # Nombre validado, salimos del bucle interno

        # --- Bucle para la validación de la nota ---
        while True:
            nota_str = input(f"Ingresa la nota de {nombre_estudiante} (entre 0 y 100): ").strip()
            try:
                nota = float(nota_str)
                if 0 <= nota <= 100:
                    break # Nota válida, salimos del bucle de validación de nota
                else:
                    print("Error: La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Ingresa un valor numérico válido para la nota.")
        
        # Obtener el desempeño basado en la nota
        desempeno = obtener_desempeno(nota)
        
        # Formatear la línea y guardarla en el archivo, incluyendo el desempeño
        linea = f"Nombre: {nombre_estudiante} – Nota: {nota} ({desempeno})\n"
        with open('notas.txt', 'a') as archivo:
            archivo.write(linea)
        print(f"Nota de {nombre_estudiante} registrada exitosamente como '{desempeno}'.\n")
        return True # Indica que se registró una nota y se puede pedir otra

def mostrar_registros():
    """
    Lee y muestra todas las entradas registradas en el archivo 'notas.txt'.
    """
    try:
        with open('notas.txt', 'r') as archivo:
            print("\n--- REGISTRO DE NOTAS ---")
            contenido = archivo.read()
            if not contenido:
                print("No hay registros de notas aún.")
            else:
                print(contenido.strip())
            print("-------------------------\n")
    except FileNotFoundError:
        print("\nEl archivo 'notas.txt' no existe. No hay registros para mostrar.\n")

# --- LÓGICA PRINCIPAL DEL SCRIPT (directa, sin if __name__ == "__main__":) ---
print("¡Bienvenido al sistema de registro de notas!")
print("Puedes empezar a ingresar los datos de los estudiantes.")
print("Escribe 'salir' en el nombre del estudiante para finalizar la entrada de datos.")

while registrar_nota():
    pass

mostrar_registros()
print("¡Gracias por usar el sistema de registro de notas!")

