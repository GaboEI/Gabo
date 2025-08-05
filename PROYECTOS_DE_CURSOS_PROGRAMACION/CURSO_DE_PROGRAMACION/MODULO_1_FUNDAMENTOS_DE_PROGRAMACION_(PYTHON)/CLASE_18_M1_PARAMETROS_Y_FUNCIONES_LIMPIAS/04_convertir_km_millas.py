def km_a_millas(kimetros: float) -> float:
    if kimetros <=  0:
        return "❌ Error: los kilometrods no pueden ser negativos 0."
    millas = kimetros * 0.621371
    return round(millas, 3)

print(f"20 km = {km_a_millas(20)} mi")  
print(f"1 km = {km_a_millas(1)} mi") 