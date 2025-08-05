# ====== Sistema de Registro de Notas de Estudiantes ======
# Prueba de Pase de Nivel: Modulo 1
archivo_estudiantes = "Estudiantes_Notas.txt"
# === Funciones ===
def agregar_estudiante():
    # Solisitar Nombre de los estudiantes.
    nombre = input("Nombre del estudiante: ").strip().capitalize()
    # Solisitar la edad del estudiante
    while True:
        try:
            entrada = int(input("Edad del estudiante: ").strip())
            edad = int(entrada)
            if edad >=0:
                break
            else:
                print("La edad no puede ser negativa") 
        except ValueError:
            print("Porfavor ingrese un numero entero")
    # Validar nota entre 0 a 10:
    while True:
        try:
            nota = float(input("Nota del estudiante de [0-10]: "))
            nota_formateada = "{:.2f}".format(nota)
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entr [0-10]") 
        except ValueError:
            print("Ingrese un numero valido para la nota")
    # Validar estatus del estudiante:
    estado = "APROBADO" if nota >= 6 else "DESAPROBADO"
    # Guardar en Archivo:
    try:
        with open("Estudiantes_Notas.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre.ljust(10)}|{str(edad).ljust(3)}|{str(nota_formateada).ljust(4)}|{estado.ljust(4)}\n")
        print(f"Estudiante, {nombre} agregado corectamente")
    except Exception as e:
        print(f"ERROR AL GUARDA'{e}'")
def ver_estudiantes():
    try:
        with open("Estudiantes_Notas.txt", "r", encoding="utf-8") as archivo:
            estudiantes = archivo.readlines()
        if estudiantes:
            print("\n=== Lista de los Estudiantes ===")
            for idx, linea in enumerate(estudiantes, 1):
                partes = linea.strip().split("|")
                if len(partes) != 4:
                    continue
                nombre, edad, nota, estado = partes
                nota = float(nota)
                estado = "APROBADO" if nota >= 6 else "DESAPROBADO"
                print(f"{idx}. Nombre: {nombre.ljust(10)}|Edad: {edad.ljust(3)}|Nota: {str(nota).ljust(10)}|Estado: {estado}")
        else:
            print("No hay estudiantes reguistrados.")
    except FileNotFoundError:
        print("Archivo no encontrado, Se creara al agregar el primer estudiante")
# Eliminar Estudiante
def eliminar_estudiante():
    try:
        with open("Estudiantes_Notas.txt", "r", encoding="utf-8") as archivo:
            estudiantes = archivo.readlines()
        if estudiantes:
            print("=== Estudiantes registrados ===")
            for idx, linea in enumerate(estudiantes, 1):
                partes = linea.strip().split("|")
                if len(partes) != 4:
                    continue
                nombre, edad, nota, estado = partes
                print(f"{idx}. Nombre: {nombre} | Edad: {edad} | Nota: {nota} | Estado: {estado}")
            try:
                numero = int(input("seleccione una opcion para eliminar "))
                if 1 <= numero <= len(estudiantes):
                    estudiante_eliminar = estudiantes.pop(numero - 1)
                    with open("Estudiantes_Notas.txt", "w", encoding="utf-8") as archivo:
                        archivo.writelines(estudiantes)
                    print(f"Estudiante eliminado: {estudiante_eliminar.strip()}")
                else:
                    print("seleccion de numero invalido")
            except ValueError:
                print("Ingrese un numero valido")          
        else:
            print("No hay estudiantes a eliminar")             
    except FileNotFoundError:
        print("El estudiante seleccionado no se encuentra en la lista ")
# Ver Estadisticas
def ver_estadisticas():
    try:
        with open("Estudiantes_Notas.txt", "r", encoding="utf-8") as archivo:
            estudiantes = archivo.readlines()
            if estudiantes:
                total = len(estudiantes)
                notas = []
                nombres = []
                aprobados = 0
                desaprobados = 0
                for linea in estudiantes:
                    partes = linea.strip().split("|")
                    if len(partes) != 4:
                        continue
                    nombre, edad, nota, estado = partes
                    notas.append(float(nota))
                    nombres.append(nombre)
                    if estado.lower() == "APROBADO":
                        aprobados += 1
                    else:
                        desaprobados += 1
                promedio = sum(notas) / total
                nota_max = max(notas)
                nota_min = min(notas)
                idx_max = notas.index(nota_max)
                idx_min = notas.index(nota_min)
                print("\n=== Estadisticas del Grupo ===")
                print(f"Total de estudiantes: {total}")
                print(f"Promedio General: {promedio:.2f}")
                print(f"Nota mas Alta: {nota_max:.2f} de {nombres[idx_max]}")
                print(f"Nota mas Baja: {nota_min:.2f} de {nombres[idx_min]}")
                print(f"Aprobados: {aprobados}")
                print(f"Desaprobados: {desaprobados}")
    except FileNotFoundError:
        print("El archivo no existe ")
# === Menu central ===
while True:
    print("""
=== Sistema de registro de las notas de los estudiantes ===
[1] Agregar estudiante
[2] Ver estudiantes
[3] Eliminar estudiante
[4] Ver estadisticas
[0] Salir
""")
    opcion = input("Seleccione una Opcion: ").strip()
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        ver_estudiantes()
    elif opcion == "3":
        eliminar_estudiante()
    elif opcion == "4":
        ver_estadisticas()
    elif opcion == "0":      
        print("Saliendo del sistema de Reguistro")
        break
    else:
        print("Opcion invalida. Intente nuevamente")
print("Gracias por usar el sistema de registro")