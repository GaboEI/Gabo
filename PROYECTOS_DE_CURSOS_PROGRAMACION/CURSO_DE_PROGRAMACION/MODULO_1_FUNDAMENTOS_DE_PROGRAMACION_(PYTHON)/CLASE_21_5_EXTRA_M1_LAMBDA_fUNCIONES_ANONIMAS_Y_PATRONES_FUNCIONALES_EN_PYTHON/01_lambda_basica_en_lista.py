#📝 01_lambda_basica_en_lista.py

#1️⃣ Crear una lista fija de números enteros
num = [47, 82, 13, 65, 29, 93, 56]
print(f"Lista Original: {num}")

#2️⃣ Aplicar la función map() con una función lambda para duplicar cada número
#3️⃣ Convertir el resultado de map() en una lista con list()
duplicado = list(map(lambda x: x*2, num))

#4️⃣ Imprimir la lista resultante en consola
print(f"Lista duplicada: {duplicado}")

#5️⃣ (Opcional) Mostrar la suma de la lista original y la suma de la lista resultante
sum_original = sum(num)
sum_duplicado = sum(duplicado)
print(f"""
Suma de la lista original: {sum_original}
Suma de la lista duplicada: {sum_duplicado} 
"""
)

#6️⃣ (Opcional) Mostrar la diferencia entre cada par (original → transformado)
print("Diferencia entre cada par [original -> transformado]:")
for original, duplicado in zip (num, duplicado):
    print(f"{original} -> {duplicado}, diferencia: {duplicado - original}")

"""
RESPUESTA DE TERMINAL
Lista Original: [47, 82, 13, 65, 29, 93, 56]
Lista duplicada: [94, 164, 26, 130, 58, 186, 112]

Suma de la lista original: 385
Suma de la lista duplicada: 770 

Diferencia entre cada par [original -> transformado]:
47 -> 94, diferrencia: 47
82 -> 164, diferrencia: 82
13 -> 26, diferrencia: 13
65 -> 130, diferrencia: 65
29 -> 58, diferrencia: 29l
93 -> 186, diferrencia: 93
56 -> 112, diferrencia: 56
"""

print("*"*100)
duplicado = list(map(lambda u: u*45, num))
print(f"Lista duplicada: {duplicado}")
print("*"*100)
print(f"Suma de la lista original: {sum(num)}")
print(f"Suma de la lista duplicada: {sum(duplicado)}")
print("*"*100)
print("Diferencia entre cada par [original -> transformado]:")
for original, duplicado in zip (num, duplicado):
    print(f"{original} -> {duplicado}, diferencia: {duplicado - original}")
print("*"*100)