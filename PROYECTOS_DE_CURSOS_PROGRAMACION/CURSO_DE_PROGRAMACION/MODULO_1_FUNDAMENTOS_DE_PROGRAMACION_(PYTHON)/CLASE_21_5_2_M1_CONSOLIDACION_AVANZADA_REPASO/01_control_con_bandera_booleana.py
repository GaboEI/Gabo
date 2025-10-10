lientes = [
    {"nombre": "Ana", "facturas": [{"id": 1, "estado": "pagada"}, {"id": 2, "estado": "pendiente"}]},
    {"nombre": "Luis", "facturas": [{"id": 3, "estado": "pagada"}]},
]

factura_pendiente = False

for cliente in clientes:
    for factura in cliente["facturas"]: 
        if factura["estado"] == "pendiente":
            factura_pendiente = True
            cliente_con_deuda = cliente["nombre"]
            break  # Rompe el segundo bucle
    if factura_pendiente:
        break  # Rompe el primero también
    print(f"El cliente {cliente['nombre']} no tiene facturas pendientes.")
if factura_pendiente:
    print(f"El cliente {cliente_con_deuda} tiene facturas pendientes.")# Ejemplo de control de flujo con bandera booleana