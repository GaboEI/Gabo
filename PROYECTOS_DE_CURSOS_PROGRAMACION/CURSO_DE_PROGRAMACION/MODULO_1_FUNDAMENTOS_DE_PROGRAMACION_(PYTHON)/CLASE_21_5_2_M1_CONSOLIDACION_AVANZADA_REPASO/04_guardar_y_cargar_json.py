# ---------------------------------------------------------------------
# Ejercicio 04 - guardar_y_cargar_json.py
# Objetivo: Guardar y cargar datos estructurados en formato JSON
# usando el módulo json y controlando el flujo con banderas booleanas.
# ---------------------------------------------------------------------
#1️⃣ Importar el módulo json y opcionalmente datetime y os.
import json
import os
from datetime import datetime
#from tabulate import tabulate # -> No supe como usarlo 

#2️⃣ Definir el nombre del archivo JSON a usar.
ARCHIVO_JSON = "04_guardar_y_cargar_json.json"
FECHA = datetime.now().strftime("📆 %d.%m.%Y ⏱️  %H:%M")
#print(FECHA)

#3️⃣ Crear una estructura de datos Python (lista o diccionario)
carrito_de_compras = {
    "usuario": {
        "id_usuario": 20391, "nombre": "Gabriel Espinosa", "correo": "gabo@example.com",
        "pais": "Rusia", "moneda": "RUB", "miembro_vip": True
    },
    "carrito": {
        "fecha_creacion": "2025-10-16",
        "productos": [
            {
                "id_producto": 101, "nombre": "Teclado Mecánico RGB", "categoria": "Periféricos",
                "marca": "KeyChron", "precio_unitario": 8490.99, "cantidad": 1, "en_stock": True,
                "descuento": {"tipo": "porcentaje", "valor": 10},
                "envio": {"metodo": "Estándar", "costo": 300.0, "tiempo_estimado": "3-5 días"},
                "valoraciones": [5, 4, 5, 4, 5]
            },
            {
                "id_producto": 204, "nombre": "Mouse Logitech MX Master 3S", "categoria": "Periféricos",
                "marca": "Logitech", "precio_unitario": 11290.00, "cantidad": 2, "en_stock": True,
                "descuento": {"tipo": "fijo", "valor": 500},
                "envio": {"metodo": "Express", "costo": 450.0, "tiempo_estimado": "1-2 días"},
                "valoraciones": [5, 5, 5, 4, 5]
            },
            {
                "id_producto": 509, "nombre": "SSD NVMe 1TB Kingston Fury Renegade", "categoria": "Almacenamiento",
                "marca": "Kingston", "precio_unitario": 12500.75, "cantidad": 1, "en_stock": False,
                "descuento": {"tipo": None, "valor": 0},
                "envio": {"metodo": "No disponible", "costo": 0.0, "tiempo_estimado": None},
                "valoraciones": [5, 4, 5, 5, 5, 4]
            }
        ],
        "totales": {
            "subtotal": 0.0, "descuentos_totales": 0.0, "envio_total": 0.0,
            "iva": 0.0, "total_final": 0.0
        }
    },
    "historial": [
        {"id_pedido": 9001, "fecha": "2025-07-15", "total_pagado": 18990.50,
         "metodo_pago": "Tarjeta Visa", "estado": "Entregado",
         "productos": ["Monitor LG UltraWide 29”", "Soporte VESA"]},
        {"id_pedido": 9002, "fecha": "2025-09-10", "total_pagado": 5990.00,
         "metodo_pago": "YooMoney", "estado": "Enviado",
         "productos": ["Auriculares Sony WH-1000XM5"]}
    ],
    "preferencias": {
        "direccion_envio": {
            "pais": "Rusia", "ciudad": "San Petersburgo", "codigo_postal": "190000",
            "direccion": "Nevsky Prospekt 28, Apt. 4", "telefono_contacto": "+7 911 234-5678"
        },
        "idioma": "es", "modo_oscuro": True,
        "notificaciones": {"ofertas": True, "envios": True, "recomendaciones": False}
    }
}

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
   
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo_json:
            datos_json = json.load(archivo_json)
            carga_exitosa = True
            print(f"\n🗃️ CONTENIDO DEL ARCHIVO → {ARCHIVO_JSON}\n")
            print(datos_json)
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

"""
RESPUSTA DE CONSOLA
🗂️ Copia de respaldo creada correctamente → usuarios_backup.json

✅ Archivo '04_guardar_y_cargar_json.json' creado correctamente (📆 16.10.2025 ⏱️ 23:55)

🗃️ CONTENIDO DEL ARCHIVO → 04_guardar_y_cargar_json.json

{'usuario': {'id_usuario': 20391, (...) True, 'recomendaciones': False}}}
📑 Lectura exitosa. Total de registros principales: 4

🧭 Estado final: LECTURA EXITOSA

"""

