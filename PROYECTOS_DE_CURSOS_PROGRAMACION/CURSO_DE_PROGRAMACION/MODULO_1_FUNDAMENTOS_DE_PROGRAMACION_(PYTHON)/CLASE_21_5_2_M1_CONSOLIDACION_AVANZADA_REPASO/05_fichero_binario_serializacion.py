import json
import os
from datetime import datetime
from tabulate import tabulate

# 1️⃣ Definir archivos y variables principales
ARCHIVO_JSON = "04_guardar_y_cargar_json.json"
BACKUP_JSON = "usuarios_backup.json"
FECHA = datetime.now().strftime("📆 %d.%m.%Y ⏱️ %H:%M")

\
guardado_exitoso = False
carga_exitosa = False

# 4️⃣ Crear copia de seguridad antes de sobrescribir el archivo principal
if os.path.exists(ARCHIVO_JSON):
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo_original:
            contenido = archivo_original.read()
        with open(BACKUP_JSON, "w", encoding="utf-8") as respaldo:
            respaldo.write(contenido)
        print(f"🗂️ Copia de respaldo creada correctamente → {BACKUP_JSON}")
    except Exception as e:
        print(f"⚠️ No se pudo crear la copia de respaldo: {e}")

# 5️⃣ Guardar los datos actualizados
try:
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo_json:
        json.dump(carrito_de_compras, archivo_json, indent=4, ensure_ascii=False)
        guardado_exitoso = True
except Exception as error_escritura:
    print(f"❌ ERROR al guardar el archivo: {error_escritura}")
else:
    print(f"\n✅ Archivo '{ARCHIVO_JSON}' creado correctamente ({FECHA})")

# 6️⃣ Leer y validar el contenido del archivo
if guardado_exitoso:
    print(f"\n🗃️ LEYENDO ARCHIVO → {ARCHIVO_JSON}\n")
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo_json:
            datos_json = json.load(archivo_json)
            carga_exitosa = True
    except json.JSONDecodeError as e:
        print(f"❌ Error de decodificación JSON: {e}")
    except Exception as e:
        print(f"❌ Error general al leer el archivo: {e}")
    else:
        total_registros = len(datos_json)
        print(f"📑 Lectura exitosa. Total de registros principales: {total_registros}")
    finally:
        estado = "LECTURA EXITOSA" if carga_exitosa else "ERROR EN LA LECTURA"
        print(f"\n🧭 Estado final: {estado}")
else:
    print("🛑 Error al crear o acceder al archivo JSON.")
