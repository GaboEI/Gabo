# Ruta del archivo donde se guardarán las ventas
archivo_ventas = "ventas.txt"

# Función para registrar una nueva venta
def registrar_venta():
    producto = input("Ingrese el nombre del producto: ").strip()
    while not producto:
        print("⚠️ El nombre del producto no puede estar vacío.")
        producto = input("Ingrese el nombre del producto: ").strip()
    
    try:
        unidades = int(input("Ingrese la cantidad de unidades vendidas: "))
        if unidades <= 0:
            raise ValueError("Las unidades deben ser mayores a 0.")
        precio = float(input("Ingrese el precio unitario: "))
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
    except ValueError as e:
        if str(e).startswith("Las unidades") or str(e).startswith("El precio"):
            print(f"⚠️ Error: {e}")
        else:
            print("⚠️ Error: Ingrese valores numéricos válidos.")
        return
    
    venta = {
        "producto": producto,
        "unidades": unidades,
        "precio": precio,
        "total": unidades * precio
    }
    
    try:
        with open(archivo_ventas, "a", encoding="utf-8") as archivo:
            archivo.write(f"{producto},{unidades},{precio},{unidades * precio}\n")
        print(f"✅ Venta de {unidades} {producto}(s) registrada correctamente.")
    except Exception as e:
        print(f"⚠️ Error al guardar la venta: {e}")

# Función para mostrar todas las ventas registradas
def mostrar_ventas():
    try:
        with open(archivo_ventas, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("⚠️ No hay ventas registradas.")
                return
            
            # Imprimir encabezado de la tabla
            print("\n{:<20} | {:<10} | {:<10} | {:<10}".format("Producto", "Unidades", "Precio", "Total"))
            print("-" * 55)
            
            # Mostrar cada venta
            for linea in lineas:
                try:
                    producto, unidades, precio, total = linea.strip().split(",")
                    producto = producto[:20] if len(producto) > 20 else producto
                    unidades = int(unidades)
                    precio = float(precio)
                    total = float(total)
                    print("{:<20} | {:<10} | {:<10.2f} | {:<10.2f}".format(
                        producto, unidades, precio, total))
                except ValueError:
                    print(f"⚠️ Línea inválida en el archivo: {linea.strip()}")
                    continue
    except FileNotFoundError:
        print("⚠️ No hay ventas registradas (archivo no encontrado).")
    except Exception as e:
        print(f"⚠️ Error al leer el archivo: {e}")

# Función para calcular estadísticas
def calcular_estadisticas():
    try:
        with open(archivo_ventas, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("⚠️ No hay ventas registradas.")
                return
            
            total_unidades = 0
            ingreso_total = 0.0
            productos = {}
            
            for linea in lineas:
                try:
                    producto, unidades, precio, total = linea.strip().split(",")
                    unidades = int(unidades)
                    precio = float(precio)
                    total = float(total)
                    
                    total_unidades += unidades
                    ingreso_total += total
                    
                    if producto in productos:
                        productos[producto]["unidades"] += unidades
                        productos[producto]["total"] += total
                    else:
                        productos[producto] = {"unidades": unidades, "total": total}
                except ValueError:
                    print(f"⚠️ Línea inválida en el archivo: {linea.strip()}")
                    continue
            
            mas_vendido = max(productos.items(), key=lambda x: x[1]["unidades"], default=("Ninguno", {"unidades": 0}))
            mayor_ingreso = max(productos.items(), key=lambda x: x[1]["total"], default=("Ninguno", {"total": 0.0}))
            
            precio_promedio = ingreso_total / total_unidades if total_unidades > 0 else 0
            
            print("\n=== Estadísticas de Ventas ===")
            print(f"Total de productos vendidos: {total_unidades}")
            print(f"Ingreso total generado: ${ingreso_total:.2f}")
            print(f"Producto más vendido: {mas_vendido[0]} ({mas_vendido[1]['unidades']} unidades)")
            print(f"Producto con mayores ingresos: {mayor_ingreso[0]} (${mayor_ingreso[1]['total']:.2f})")
            print(f"Precio promedio por unidad: ${precio_promedio:.2f}")
            
            guardar_estadisticas_txt(total_unidades, ingreso_total, mas_vendido, mayor_ingreso, precio_promedio)
            
    except FileNotFoundError:
        print("⚠️ No hay ventas registradas (archivo no encontrado).")
    except Exception as e:
        print(f"⚠️ Error al procesar estadísticas: {e}")

# Función para guardar las estadísticas en otro archivo txt
def guardar_estadisticas_txt(total_unidades, ingreso_total, mas_vendido, mayor_ingreso, precio_promedio):
    try:
        with open("estadisticas_ventas.txt", "w", encoding="utf-8") as archivo:
            archivo.write("=== Estadísticas de Ventas ===\n")
            archivo.write(f"Total de productos vendidos: {total_unidades}\n")
            archivo.write(f"Ingreso total generado: ${ingreso_total:.2f}\n")
            archivo.write(f"Producto más vendido: {mas_vendido[0]} ({mas_vendido[1]['unidades']} unidades)\n")
            archivo.write(f"Producto con mayores ingresos: {mayor_ingreso[0]} (${mayor_ingreso[1]['total']:.2f})\n")
            archivo.write(f"Precio promedio por unidad: ${precio_promedio:.2f}\n")
        print("✅ Estadísticas guardadas en 'estadisticas_ventas.txt'.")
    except Exception as e:
        print(f"⚠️ Error al guardar estadísticas: {e}")

# Menú principal
def menu():
    while True:
        print("""
=== Registro de Ventas ===
1. Registrar nueva venta
2. Mostrar ventas registradas
3. Calcular estadísticas
0. Salir
""")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()