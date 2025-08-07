from colorama import init, Fore, Style, Back
init(autoreset=True)
#!=========================================================================
"""
🟩 Etapa 4 (Versión simplificada)  Menú sin funciones**

📄 Archivo sugerido: `sistema_registro_basico.py
🎯 Objetivo: Crear un menú interactivo con while e if, sin usar funciones ni 
estructuras que aún no has visto oficialmente.

!🧠 ¿Qué aprendes con esta versión?

* Control de flujo con `while` y `if`
* Diseño de menú de consola
* Reutilización de lo aprendido, sin adelantar temas
* Base sólida para cuando llegues a funciones

DIAGRAMA DE FLUJO 
INICIO
↓
Mostrar mensaje de bienvenida
↓
BUCLE: while True
↓
    Mostrar menú de opciones
    ↓
    Leer opción del usuario
    ↓
    DECISIÓN: ¿opción ingresada?
    ├── "1" → REGISTRAR ESTUDIANTE
    │   ↓
    │   Pedir nombre
    │   ↓
    │   BUCLE: Validar nota ingresada
    │       ↓
    │       ¿Es número válido entre 0 y 100?
    │       ├── Sí → continuar
    │       └── No → volver a pedir nota
    │   ↓
    │   Clasificar nota según rango:
    │       ├── 90-100 → Excelente
    │       ├── 80-89 → Muy bien
    │       ├── 70-79 → Bien
    │       ├── 60-69 → Aprobado justo
    │       └── <60 → Reprobado
    │   ↓
    │   Guardar en archivo (append)
    │   ↓
    │   Mostrar mensaje de éxito
    │   ↓
    │   VOLVER AL MENÚ
    │
    ├── "2" → VER TODAS LAS NOTAS
    │   ↓
    │   ¿Existe el archivo?
    │       ├── Sí → Leer y mostrar contenido
    │       └── No → Mostrar error
    │   ↓
    │   VOLVER AL MENÚ
    │
    ├── "3" → VER ESTADÍSTICAS
    │   ↓
    │   ¿Existe el archivo?
    │       ├── No → Mostrar error
    │       └── Sí →
    │           Leer línea por línea
    │           ↓
    │           Extraer nota
    │           Clasificar según evaluación
    │           Sumar estadísticas:
    │               - Total estudiantes
    │               - Suma de notas
    │               - Contadores por categoría
    │           ↓
    │           Calcular:
    │               - Promedio
    │               - % aprobados y reprobados
    │           ↓
    │           Mostrar estadísticas
    │   ↓
    │   VOLVER AL MENÚ
    │
    ├── "4" → SALIR
    │   ↓
    │   Mostrar mensaje de despedida
    │   ↓
    │   FIN DEL PROGRAMA
    │
    └── Cualquier otra opción
        ↓
        Mostrar error de opción inválida
        ↓
        VOLVER AL MENÚ

"""
#!==============================================================================================================
# --- 1️⃣ MENSAJE DE BIENVENIDA ---
NOMBRE_ARCHIVO = "notas.txt"

print("👋 ¡Bienvenido al Sistema de Gestión de Notas! 👋")

# --- 2️⃣ BUCLE PRINCIPAL DEL MENÚ ---
while True:
    print(Fore.CYAN +"\n--- MENÚ DE OPCIONES ---")
    print(Fore.CYAN +"1. Registrar estudiante")
    print(Fore.CYAN +"2. Ver todas las notas")
    print(Fore.YELLOW +"3. Ver estadísticas")
    print(Fore.CYAN +"4. Salir")
    print(Fore.CYAN +"------------------------")
    
    opcion = input("👉 Seleccione una opción (1-4): ")

    # --- 3️⃣ OPCIÓN 1: REGISTRAR ESTUDIANTE ---
    if opcion == "1":
        nombre = input(Fore.CYAN + Back.BLACK + Style.BRIGHT +"✍️ Ingrese el nombre del estudiante: ").title().strip()
        
        while True:
            try:
                nota = float(input(f"✍️ Ingrese la nota de {nombre}: "))
                if 0 <= nota <= 100:
                    break
                else:
                    print("⚠️ La nota debe estar entre 0 y 100.")
            except ValueError:
                print("❌ Entrada no válida. Por favor, ingrese un número.")
        
        # Determinar la evaluación en base a la nota
        if nota >= 90:
            evaluacion = "✅ Excelente"
        elif nota >= 80:
            evaluacion = "🟩 Muy bien"
        elif nota >= 70:
            evaluacion = "🟨 Bien"
        elif nota >= 60:
            evaluacion = "🟧 Aprobado justo"
        else:
            evaluacion = "🟥 Reprobado"
        
        # Guardar la línea en modo de añadir (append)
        linea = f"Nombre: {nombre} Nota: {nota:.2f} {evaluacion}\n"
        with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(linea)
        
        print(f"\n✅ Estudiante {nombre} registrado exitosamente.")

    # --- 4️⃣ OPCIÓN 2: VER TODAS LAS NOTAS ---
    elif opcion == "2":
        try:
            with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
                print(f"\n💥 CONTENIDO DEL ARCHIVO '{NOMBRE_ARCHIVO}' 💥\n")
                contenido = archivo.read()
                if contenido:
                    print(contenido.strip())
                else:
                    print("El archivo está vacío.")
        except FileNotFoundError:
            print(f"\n❌ El archivo '{NOMBRE_ARCHIVO}' no se ha encontrado. Registre un estudiante primero.")

    # --- 5️⃣ OPCIÓN 3: VER ESTADÍSTICAS ---
    elif opcion == "3":
        try:
            with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
                total_estudiantes, suma_notas = 0, 0
                excelente, muy_bien, bien, aprobado_justo, reprobado = 0, 0, 0, 0, 0

                for linea in archivo:
                    try:
                        posicion_nota = linea.find("Nota:")
                        if posicion_nota != -1:
                            texto_nota = linea[posicion_nota + len("Nota:"):].strip()
                            nota_str = texto_nota.split()[0]
                            nota = float(nota_str)

                            total_estudiantes += 1
                            suma_notas += nota

                            if nota >= 90:
                                excelente += 1
                            elif nota >= 80:
                                muy_bien += 1
                            elif nota >= 70:
                                bien += 1
                            elif nota >= 60:
                                aprobado_justo += 1
                            else:
                                reprobado += 1
                    except (ValueError, IndexError):
                        pass # Ignorar líneas con formato incorrecto para el cálculo

                print("\n--- RESUMEN DE ESTADÍSTICAS ---")
                if total_estudiantes > 0:
                    promedio_notas = suma_notas / total_estudiantes
                    aprobados = excelente + muy_bien + bien + aprobado_justo
                    porcentaje_aprobados = (aprobados / total_estudiantes) * 100
                    porcentaje_reprobados = (reprobado / total_estudiantes) * 100

                    print(f"📊 Total de estudiantes: {total_estudiantes}")
                    print(f"⭐ Nota promedio: {promedio_notas:.2f}")
                    print(f"✅ Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")
                    print(f"❌ Porcentaje de reprobados: {porcentaje_reprobados:.2f}%")
                    
                    print("\n--- DETALLE POR EVALUACIÓN ---")
                    print(f"🟢 Excelente (90-100): {excelente}")
                    print(f"🟩 Muy bien (80-89): {muy_bien}")
                    print(f"🟨 Bien (70-79): {bien}")
                    print(f"🟧 Aprobado justo (60-69): {aprobado_justo}")
                    print(f"🟥 Reprobado (<60): {reprobado}")
                else:
                    print("No se encontraron datos de estudiantes para analizar.")
        except FileNotFoundError:
            print(f"\n❌ El archivo '{NOMBRE_ARCHIVO}' no se ha encontrado. Registre un estudiante primero.")

    # --- 6️⃣ OPCIÓN 4: SALIR ---
    elif opcion == "4":
        print("👋 Saliendo del programa. ¡Hasta pronto!")
        break
    
    # --- 6️⃣ OPCIÓN NO VÁLIDA ---
    else:
        print("⚠️ Opción no válida. Por favor, elija un número del 1 al 4.")
#!==============================================================================================================
"""
#!respuestas de la consola
👋 ¡Bienvenido al Sistema de Gestión de Notas! 👋

--- MENÚ DE OPCIONES ---
1. Registrar estudiante
2. Ver todas las notas
3. Ver estadísticas
4. Salir
------------------------
👉 Seleccione una opción (1-4): 1
✍️ Ingrese el nombre del estudiante: Gabriel espinosa izada
✍️ Ingrese la nota de Gabriel Espinosa Izada: 99.9999

✅ Estudiante Gabriel Espinosa Izada registrado exitosamente.

--- MENÚ DE OPCIONES ---
1. Registrar estudiante
2. Ver todas las notas
3. Ver estadísticas
4. Salir
------------------------
👉 Seleccione una opción (1-4): 2

💥 CONTENIDO DEL ARCHIVO 'notas.txt' 💥

Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien
Nombre: Diego Betancour Espinosa  Nota: 55.89  🟧 Aprobado justo
Nombre: Roberto Mastrapa Aguilar  Nota: 25.00  🟥 Reprobado
Nombre: Gabrreil espinosa izada Nota: 100.00 ✅ Excelente
Nombre: Gabriel Espinosa Izada Nota: 100.00 ✅ Excelente

--- MENÚ DE OPCIONES ---
1. Registrar estudiante
2. Ver todas las notas
3. Ver estadísticas
4. Salir
------------------------
👉 Seleccione una opción (1-4): 3

--- RESUMEN DE ESTADÍSTICAS ---
📊 Total de estudiantes: 7
⭐ Nota promedio: 76.77
✅ Porcentaje de aprobados: 71.43%
❌ Porcentaje de reprobados: 28.57%

--- DETALLE POR EVALUACIÓN ---
🟢 Excelente (90-100): 3
🟩 Muy bien (80-89): 1
🟨 Bien (70-79): 1
🟧 Aprobado justo (60-69): 0
🟥 Reprobado (<60): 2

--- MENÚ DE OPCIONES ---
1. Registrar estudiante
2. Ver todas las notas
3. Ver estadísticas
4. Salir
------------------------
👉 Seleccione una opción (1-4): 4
👋 Saliendo del programa. ¡Hasta pronto!
"""
#!==============================================================================================================
"""
###! cONTENIDO DEL ARCHIVO notas.tx AL REALIZAR LA PRUEVA DE TERMINAL
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien
Nombre: Diego Betancour Espinosa  Nota: 55.89  🟧 Aprobado justo
Nombre: Roberto Mastrapa Aguilar  Nota: 25.00  🟥 Reprobado
Nombre: Gabrreil espinosa izada Nota: 100.00 ✅ Excelente
Nombre: Gabriel Espinosa Izada Nota: 100.00 ✅ Excelente
"""
#!==============================================================================================================