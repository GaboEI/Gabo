# -----------------------------------------------------------
# Ejercicio 02 - busqueda_en_estructura_anidada.py
# Objetivo: Buscar un elemento que cumpla condiciones
# específicas dentro de una estructura anidada usando
# una bandera booleana para controlar el flujo lógico.
# -----------------------------------------------------------

import datetime
import json
import csv

NOW = datetime.datetime.now()
FECHA_FORMATIADA = NOW.strftime("%d/%m/%Y %H:%M") 
ARCHIVO_JSON = "resultado_busqueda.json"
ARCHIVO_CSV = "resultado_busqueda.csv"

ENCABEZADOS = ["nombre", "monto", "articulo", "cantidad", "categoria", "fecha de registro"]

#1️⃣ Crear una estructura de datos anidada
carrito_compras = [ 
    {
        "Nombre": "Eduardo",
        "compras": [
            {"monto": 300, "articulo": "pantalones", "cantidad": 1, "categoria": "ropa"},
            {"monto": 800, "articulo": "audifonos", "cantidad": 2, "categoria": "electronica"},
        ],
    },
    {
        "Nombre": "Javier",
        "compras": [
            {"monto": 900, "articulo": "platos", "cantidad": 20, "categoria": "hogar"},
            {"monto": 1800, "articulo": "faros", "cantidad": 4, "categoria": "automotriz"}, 
            {"monto": 200, "articulo": "libro", "cantidad": 1, "categoria": "papeleria"}, 
        ],
    },
    {
        "Nombre": "Virginia",
        "compras": [
            {"monto": 100, "articulo": "cepillo", "cantidad": 2, "categoria": "hogar"},
            {"monto": 750, "articulo": "destornillador", "cantidad": 4, "categoria": "herramienta"},
            {"monto": 50, "articulo": "carne", "cantidad": "2kg", "categoria": "alimentos"},
        ], 
    },

]

#2️⃣ Inicializar la bandera booleana en False.
encontrados = False
compra_de_alimentos = None

#3️⃣ Iniciar bucles.
for cliente in carrito_compras:
    
    #4️⃣ Iniciar bucle interno
    for compra in cliente["compras"]:
        if compra["categoria"] == "alimentos" and compra["articulo"] == "carne":
          
            compra_de_alimentos = {
                "nombre": cliente["Nombre"],    
                "monto": compra["monto"],
                "articulo": compra["articulo"], 
                "cantidad": compra["cantidad"],
                "categoria": compra["categoria"],
                "fecha de registro": FECHA_FORMATIADA
            }
            break 
           
    if compra_de_alimentos:
        break

if compra_de_alimentos:
    print("✅ EXITO EN LA BUSQUEDA: AL MENOS UNA DE LAS COMPRAS FUE DE ALIMENTOS\n")
    print("-" * 90)
    # ✅ CORRECCIÓN DE CONSISTENCIA: La columna "Articulo"
    print(f"{'Nombre':<15}{'Monto':<10}{'Articulo':<15}{'Cantidad':<10}{'Categoria':<15}{'Fecha':<15}")
    print("-" * 90)
    print(
            f"{compra_de_alimentos['nombre']:<15}"
            f"{compra_de_alimentos['monto']:<10}"
            f"{compra_de_alimentos['articulo']:<15}"
            f"{compra_de_alimentos['cantidad']:<10}"
            f"{compra_de_alimentos['categoria']:<15}"
            f"{compra_de_alimentos['fecha de registro']:<15}"
           )
    
    # 💾 GUARDAR EN JSON
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo_json_guardar:
        json.dump(compra_de_alimentos, archivo_json_guardar, indent=4 )
   
    # 📝 GUARDAR EN CSV
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=ENCABEZADOS)
        escritor_csv.writeheader()
        escritor_csv.writerow(compra_de_alimentos)
        
    print(f"\nResultado de la busqueda guardado en los archivos: {ARCHIVO_JSON} y {ARCHIVO_CSV}")

else:
    print("❌ FRACASO EN LA BUSQUEDA: NINGUNA COMPRA ES DE ALIMENTOS")

"""
RESPUESTA DE CONSOLA:
✅ EXITO EN LA BUSQUEDA: AL MENOS UNA DE LAS COMPRAS FUE DE ALIMENTOS

------------------------------------------------------------------------------------------
Nombre         Monto     Articulo       Cantidad  Categoria      Fecha          
------------------------------------------------------------------------------------------
Virginia       50        carne          2kg       alimentos      16/10/2025 00:27

Resultado de la busqueda guardado en los archivos: resultado_busqueda.json y resultado_busqueda.csv

contenido del archivo: resultado_busqueda.json
{
    "nombre": "Virginia",
    "monto": 50,
    "articulo": "carne",
    "cantidad": "2kg",
    "categoria": "alimentos",
    "fecha de registro": "16/10/2025 00:27"
}
contenido del archivo: resultado_busqueda.csv
nombre	monto	articulo	cantidad	categoria	fecha de registro
Virginia	50	carne	2kg	alimentos	16/10/2025 00:27

"""