# === Class 10 Extension - Sales Registration

#*** == File path where sales will be saved == ***#
import os
sales_file = "sales.txt"

#* == Function to Register a Sale ==
def record_sales():
    print("\n=== Register a New Sale ===")
    product_sold = input("Enter the product name: ").strip().title()
    try:
        units_sold = int(input("Enter the number of units sold: "))
        price = float(input("Enter the unit price: "))
    except ValueError:
        print("Invalid number try again")
        return
    total_sales = units_sold * price
    with open(sales_file, "a", encoding="utf-8") as file:
        if os.stat(sales_file).st_size == 0:
            file.write("-" * 66 + "|" + "\n")
            file.write(f"{'Product':<30}| {'Quantity':<10}| {'Price':<10}| {'Total':<10}\n")
            file.write("-" * 66 + "|" + "\n")
        line = (f"{product_sold:<30}| {units_sold:<10}| {price:<9.2f}| {total_sales:<9.2f}\n")
        file.write(line)
    print("Successful registered sale. \n")

#* == Function to display all registered sales  ==
def show_sales():
    try:
        with open(sales_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
        if len(lines) <= 1:
            print("No Sales Recorded Yet")
            return
        print("Registered Sale")
        print(lines[0].strip())
        for line in lines[1:]:
            print(line.strip())
    except FileNotFoundError:
        print("There is no sales file to display.")

#* == Delete sale function ==
def remove_sale():
    try:
        with open("sales.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        if len(lines) <= 1:
            print("No sales registered for disposal")
            return
        print("registered sale")
        print(lines[0].strip())
        for idx, line in enumerate(lines[1:], 1):
            print(f"{idx}. {line.strip()}")
        num = int(input("\nEnter the number corresponding to the sale you want to delete: "))
        if 1 <= num <= len(lines) - 1:
            sale_eliminated = lines.pop(num)
            with open(sales_file, "w", encoding="utf-8") as file:
                file.writelines(lines)
            print(f"Venta eliminada: {sale_eliminated.strip()}")
        else:
            print("Number out of range")
    except FileNotFoundError:
        print("The sales file does not exist yet")
    except FileNotFoundError:
        print("Invalid entry, please enter a valid character")

#TODO == Function to calculate statistics ==
def calculate_statistics():
    try:
        with open("sales.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        if len(lines) <= 1:
            print("There is not enough data to calculate the statistics.")
            return
        total_amount = 0
        total_money = 0
        products = {}
        for line in lines[1:]:
            parts = line.strip().split("|")
            if len(parts) != 4:
                continue
            product = parts[0].strip()
            quantity = parts[1].strip()
            price = parts[2].strip()
            total = parts[3].strip()
            try:
                quantity = int(quantity)
                price = float(price)
            except ValueError:
                continue  
            total_amount += quantity
            total_money += price * quantity
            if product in products:
                products[product] += quantity
            else:
                products[product] = quantity
        if not products:
            print("No valid sales data to process statistics.")
            return
        best_selling_product = max(products, key=products.get)
        print("\nSTATISTICS")
        print(f"Total products sold: {total_amount}")
        print(f"Total revenue collected: {total_money:.2f}")
        print(f"Best-selling product: {best_selling_product}")
    except FileNotFoundError:
        print("Sales archive not found.")

#* == Function for saving statistics to another file ==
def save_statistics_txt():
    try:
        with open("sales.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        if len(lines) <= 1:
            print("No sales registered for deletion")
            return
        total_amount = 0
        total_money = 0
        products = {}
        for line in lines[1:]:
            parts = line.strip().split("|")
            if len(parts) != 4:
                continue
            product = parts[0].strip()
            quantity = parts[1].strip()
            price = parts[2].strip()
            total = parts[3].strip()
            try:
                quantity = int(quantity)
                price = float(price)
            except ValueError:
                continue  
            total_amount += quantity
            total_money += price * quantity
            if product in products:
                products[product] += quantity
            else:
                products[product] = quantity
        if not products:
            print("No valid sales data to process statistics.")
            return
        best_selling_product = max(products, key=products.get)
        with open("statistics_of_sales.txt", "w", encoding="utf-8") as file:
            file.write("STATISTICS OF SALES\n")
            file.write(f"Total products sold: {total_amount}\n")
            file.write(f"Total collected: ${total_money:.2f}")
            file.write(f"Best-selling product: {best_selling_product}\n")
        print("Archive 'statistics_of_sales.txt' correctly generated")
    except FileNotFoundError:
        print("Sales archive not found.")

#todo === Function to search for a product by name === #!!! NO FUNCIONA 
def search_product(product_name, file_name="sales.txt"):
    import os

    try:
        # Verifica si el archivo realmente existe antes de intentar abrirlo
        if not os.path.exists(file_name):
            print(f"⚠️ El archivo '{file_name}' no se encontró en la ruta: {os.path.abspath(file_name)}")
            return

        with open(file_name, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if len(lineas) <= 1:
            print("⚠️ El archivo está vacío o sin registros.")
            return

        encabezado = lineas[0].strip()
        encontrados = []

        for linea in lineas[1:]:
            producto = linea.strip().split("|")[0]
            if producto.lower() == product_name.lower():
                encontrados.append(linea.strip())

        if encontrados:
            print("🔍 Producto encontrado:")
            print(encabezado)
            for linea in encontrados:
                print(linea)
        else:
            print(f"⚠️ No se encontraron ventas con el nombre '{product_name}'.")

    except Exception as e:
        print(f"❌ Error inesperado: {e}")







# == System Main Menu == 
def menu():
    while True:
        print("""
=== Sales records ===
[1] → Register new sale
[2] → Show Registered Sales
[3] → Eliminate sale              
[4] → Calculate statistics
[5] → Save statistics to file
[6] → Search product by name
[0] → Exit
""")
        option = input("Select an option: ")                          
        if option == "1":
            record_sales()
        elif option == "2":
            show_sales()
        elif option == "3":
            remove_sale()
        elif option == "4":
            calculate_statistics()
        elif option == "5":
            save_statistics_txt()
        elif option == "6":
            name = input("Ingrese el nombre del producto a buscar: ")
            search_product(name)  # ⬅️ No pases el archivo manualmente

        elif option == "0":
            print("See you later")
            break
        else:
            print("Invalid option, try again")
        
# == Program execution ==
menu()