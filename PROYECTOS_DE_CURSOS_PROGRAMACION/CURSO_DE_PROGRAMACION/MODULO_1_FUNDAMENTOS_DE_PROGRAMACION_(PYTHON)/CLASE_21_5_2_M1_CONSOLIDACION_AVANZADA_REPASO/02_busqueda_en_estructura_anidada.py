import csv

# Escribir en un archivo CSV
with open('datos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Nombre', 'Edad'])
    escritor_csv.writerow(['Juan', '30'])
    escritor_csv.writerow(['María', '25'])
    escritor_csv.writerow(['Pedro', '40'])
    escritor_csv.writerow(['Ana', '22'])
    escritor_csv.writerow(['Luis', '28'])
    escritor_csv.writerow(['Sofía', '35'])
    escritor_csv.writerow(['Carlos', '33'])
    
    # hacer una nueva coolumna que sume la edad de todos
    escritor_csv.writerow(['Total Edad', sum([30, 25, 40, 22, 28, 35, 33])])
    escritor_csv.writerow(['Promedio Edad', sum([30, 25, 40, 22, 28, 35, 33]) / 7])     
    escritor_csv.writerow(['Máxima Edad', max([30, 25, 40, 22, 28, 35, 33])])
    escritor_csv.writerow(['Mínima Edad', min([30, 25, 40, 22, 28, 35, 33])])
    escritor_csv.writerow(['Rango Edad', max([30, 25, 40, 22, 28, 35, 33]) - min([30, 25, 40, 22, 28, 35, 33])])
    escritor_csv.writerow(['Varianza Edad', sum((x - (sum([30, 25, 40, 22, 28, 35, 33]) / 7)) ** 2 for x in [30, 25, 40, 22, 28, 35, 33]) / 7])
    escritor_csv.writerow(['Desviación Estándar Edad', (sum((x - ( sum([30, 25, 40, 22, 28, 35, 33]) / 7)) ** 2 for x in [30, 25, 40, 22, 28, 35, 33]) / 7) ** 0.5])
    escritor_csv.writerow(['Mediana Edad', sorted([30, 25, 40, 22, 28, 35, 33])[len([30, 25, 40, 22, 28, 35, 33]) // 2]])       