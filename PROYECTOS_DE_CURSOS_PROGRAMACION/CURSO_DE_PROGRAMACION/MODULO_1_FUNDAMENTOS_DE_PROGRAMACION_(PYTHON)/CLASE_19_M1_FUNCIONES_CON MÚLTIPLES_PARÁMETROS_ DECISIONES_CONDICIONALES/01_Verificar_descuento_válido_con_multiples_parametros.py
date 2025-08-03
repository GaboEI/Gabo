"""
#=====================================================================================
!🧪 EJERCICIO 1  CLASE 19
?📌 Nombre: Verificar si se aplica un descuento según tipo de cliente y monto
?🔑 Enfoque: múltiples parámetros + condicionales + retorno lógico

!🎯 ¿Qué debe hacer el script?
1️⃣ Crear una función llamada calcular_descuento()
2️⃣ Recibir dos parámetros:
----monto (obligatorio)
----tipo_cliente (opcional, valor por defecto: "regular")
3️⃣ Aplicar estas reglas:
----Si el cliente es "premium" y el monto es mayor a 100, aplicar 20% de descuento
----Si es "regular" y el monto es mayor a 200, aplicar 10% de descuento
----En los demás casos, no aplicar descuento
4️⃣ Retornar el monto final
5️⃣ Mostrar dos o tres ejemplos en consola
#=====================================================================================
"""
def pedir_monto(mensaje: str) -> float:
    """
    Pide al usuario que ingrese un número flotante con validación.
    Repite hasta que el usuario ingrese un valor válido.
    """
    while True:
        try:
            monto = float(input(mensaje))
            return monto
        except ValueError:
            print("❌ Error: Ingrese un monto numérico válido.\n")


def calcular_descuento(monto: float, tipo_cliente: str = "regular") -> float:
    """
    Calcula el monto final aplicando descuento según el tipo de cliente.

    Parámetros:
    - monto (float): monto total de la compra.
    - tipo_cliente (str, opcional): "premium" o "regular". Por defecto "regular".

    Retorna:
    - float: monto final con o sin descuento.
    """
    tipo_cliente = tipo_cliente.lower()
    
    if tipo_cliente == "premium" and monto > 100:
        monto_final = monto * 0.8
    elif tipo_cliente == "regular" and monto > 200:
        monto_final = monto * 0.9
    else:
        monto_final = monto

    return round(monto_final, 2)


# 🔽 Uso práctico
print("\n📦 Cliente PREMIUM")
monto1 = pedir_monto("Ingresa el monto para cliente premium: ")
final1 = calcular_descuento(monto1, "premium")
print(f"Monto final: ${final1}\n")

print("📦 Cliente REGULAR")
monto2 = pedir_monto("Ingresa el monto para cliente regular: ")
final2 = calcular_descuento(monto2, "regular")
print(f"Monto final: ${final2}")
