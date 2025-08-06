#==============================================================================================================
"""
!# 🟩 Etapa 3  Análisis del archivo y estadísticas
!🎯 Objetivo: Leer el archivo `notas.txt` y realizar un análisis estadístico con los datos existentes.

!🧠 Aplicación profesional
Este análisis es fundamental en:
* Sistemas escolares y boletines automatizados
* Dashboards de rendimiento académico
* Análisis estadístico de encuestas, reportes, etc.
* Backends que generan informes periódicos
"""
#==============================================================================================================

nombre_archivo = input("✍️ Escriba el nombre del archivo que desea leer: ")

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        # Contadores y acumuladores para las estadísticas
        total_estudiantes = 0
        suma_notas = 0
        
        excelente = 0
        muy_bien = 0
        bien = 0
        aprobado_justo = 0
        reprobado = 0
        
        print(f"💥 EL CONTENIDO DEL ARCHIVO '{nombre_archivo}' ES 💥\n")

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
                    
                    print(linea.strip())
            except (ValueError, IndexError):
                print(f"⚠️ Advertencia: No se pudo procesar la nota en la línea: '{linea.strip()}'")

        print("\n--- RESUMEN DE ESTADÍSTICAS ---")
        if total_estudiantes > 0:
            promedio_notas = suma_notas / total_estudiantes
            
            # --- 🎯 CÁLCULO DE PORCENTAJES 🎯 ---
            porcentaje_aprobados = ((excelente + muy_bien + bien + aprobado_justo) / total_estudiantes) * 100
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
    print(f"❌ El archivo '{nombre_archivo}' no se ha encontrado")

#==============================================================================================================
"""
#! CONTENIDO ORIJIDAL DEL ARCHIVO DE PRUEVAS: notas.txt
Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien
Nombre: Diego Betancour Espinosa  Nota: 55.89  🟧 Aprobado justo
Nombre: Roberto Mastrapa Aguilar  Nota: 25.00  🟥 Reprobado
"""
#==============================================================================================================
"""
#!respuestas de la consola
#! eje 1:
✍️ Escriba el nombre del archivo que desea leer: nota.txt
❌ El archivo 'nota.txt' no se ha encontrado
#! eje 2:
✍️ Escriba el nombre del archivo que desea leer: notas.txt
💥 EL CONTENIDO DEL ARCHIVO 'notas.txt' ES 💥

Nombre: Gabriel Espinosa Izada  Nota: 100.00  ✅ Excelente
Nombre: Cristina Espinosa Izada  Nota: 86.00  🟩 Muy bien
Nombre: Limiana Betancour Espinosa  Nota: 70.50  🟨 Bien
Nombre: Diego Betancour Espinosa  Nota: 55.89  🟧 Aprobado justo
Nombre: Roberto Mastrapa Aguilar  Nota: 25.00  🟥 Reprobado

--- RESUMEN DE ESTADÍSTICAS ---
📊 Total de estudiantes: 5
⭐ Nota promedio: 67.48
✅ Porcentaje de aprobados: 60.00%
❌ Porcentaje de reprobados: 40.00%

--- DETALLE POR EVALUACIÓN ---
🟢 Excelente (90-100): 1
🟩 Muy bien (80-89): 1
🟨 Bien (70-79): 1
🟧 Aprobado justo (60-69): 0
🟥 Reprobado (<60): 2
❯ /usr/bin/python3

"""
#==============================================================================================================

