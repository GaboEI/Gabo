# Ejercicio 03 - lectura_y_escritura_csv.py
# Objetivo: Leer y escribir archivos CSV usando el módulo csv
# aplicando banderas booleanas para el control del flujo.
# -----------------------------------------------------------
#1️⃣ Importar el módulo csv y, si se desea, datetime y os.
import csv
import datetime
import os
from tabulate import tabulate

# CONSTANTES
#2️⃣ Definir el nombre del archivo CSV a usar.
ARCHIVO_CSV = "03_lectura_y_escritura_csv.csv"

#3️⃣ Definir la lista de ENCABEZADOS (fieldnames)
ENCABEZADOS = ["Nombre", "ID", "Teléfono", "Status"]
FECHA = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")



#4️⃣ Crear una lista de diccionarios con datos de ejemplo.
clientes = [
    {"Nombre": "Eduardo", "ID": 4258, "Teléfono": "+79625875689", "Status":"VIP"},
    {"Nombre": "Ramon", "ID": 98575, "Teléfono": "+79215896514", "Status":"VIP"},
    {"Nombre": "Francisco", "ID": 56587, "Teléfono": "+79678564287", "Status":"CASUAL"},
    {"Nombre": "Juan", "ID": 89875, "Teléfono": "+79628550045", "Status":"INVITADO"},
    {"Nombre": "Pedro", "ID": 89854, "Teléfono": "+79855743337", "Status":"BLOQUEADO"},
    {"Nombre": "Ana", "ID": 70235, "Teléfono": "+79626963706", "Status":"VIP"}
]


#5️⃣ Inicializar una bandera
archivo_creado = False
lectura_exitosa = False

#6️⃣ Abrir el archivo CSV en modo escritura ("w") con 'with open'
try:   
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=ENCABEZADOS)
        escritor_csv.writeheader()
        escritor_csv.writerows(clientes)
        archivo_creado = True
except Exception as error_escritura:
    print(f"❌ ERROR: {error_escritura} al crear el archivo")

if os.path.exists(ARCHIVO_CSV):
    #7️⃣ Mostrar un mensaje de confirmación
    print(f"✅ Archivo '{ARCHIVO_CSV}' creado correctamente.\n")
    
else:
    print("⚠️ Advertencia: No se pudo crear el archivo CSV.")

#8️⃣ Abrir nuevamente el archivo CSV en modo lectura ("r")
try:
    with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        datos = list(lector_csv)
        if not datos:
            raise ValueError("❌ El archivo está vacío o sin datos válidos")
        print(f"⏱️  Fecha de creación: {FECHA}.\n")
        print(tabulate(datos, headers="keys", tablefmt="fancy_grid"))
        lectura_exitosa = True

        #print(f"{'NOMBRE':<15}{'ID':<10}{'Teléfono':<15}{'STATUS':<10}")
        #print("-" * 50)
        #for fila in lector_csv:
            #print(f"{fila['Nombre']:<15}"
                  #f"{fila['ID']:<10}"
                  #f"{fila['Teléfono']:<15}"
                  #f"{fila['Status']:<10}"
                  #)
except Exception as error_lectura:
    print(f"❌ ERROR: {error_lectura} al leer el archivo")
else:
    print("\n📑 Lectura realizada sin errores. ")
finally:
    if lectura_exitosa:
        print("\n❇️ Estado final: LECTURA EXITOSA")
    else:
        print("\n✴️ Estado final: ERROR EN LA LECTURA")

"""
RESPUESTA DE CONSOLA
------------------------------------------------------------------
✅ Archivo '03_lectura_y_escritura_csv.csv' creado correctamente.

⏱️  Fecha de creación: 16.10.2025 20:10.

╒═══════════╤═══════╤══════════════╤═══════════╕
│ Nombre    │    ID │     Teléfono │ Status    │
╞═══════════╪═══════╪══════════════╪═══════════╡
│ Eduardo   │  4258 │ +79625875689 │ VIP       │
├───────────┼───────┼──────────────┼───────────┤
│ Ramon     │ 98575 │ +79215896514 │ VIP       │
├───────────┼───────┼──────────────┼───────────┤
│ Francisco │ 56587 │ +79678564287 │ CASUAL    │
├───────────┼───────┼──────────────┼───────────┤
│ Juan      │ 89875 │ +79628550045 │ INVITADO  │
├───────────┼───────┼──────────────┼───────────┤
│ Pedro     │ 89854 │ +79855743337 │ BLOQUEADO │
├───────────┼───────┼──────────────┼───────────┤
│ Ana       │ 70235 │ +79626963706 │ VIP       │
╘═══════════╧═══════╧══════════════╧═══════════╛

📑 Lectura realizada sin errores. 

❇️ Estado final: LECTURA EXITOSA
"""