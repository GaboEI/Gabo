# banderas buleanas ejercicio de entrenamiento
clientes = [
    {"nombre": "Ana", "facturas": [{"id": 1, "estado": "pagada"}, {"id": 2, "estado": "pendiente"}]},
    {"nombre": "Luis", "facturas": [{"id": 3, "estado": "pagada"}]},
]

factura_pendiente = False

for cliente in clientes:
    for factura in cliente["facturas"]:
        if factura["estado"] == "pendiente":
            # factura_pendiente = True
            cliente_endeudado = cliente["nombre"]
            break
    if factura_pendiente == True:
        print(f"⚠️ Cliente con factura pendiente: {cliente_endeudado}")
    else:
        print(f"✅ Cliente al día: {cliente['nombre']}")