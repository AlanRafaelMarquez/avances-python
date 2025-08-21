barras = int(input("Cuantas barras has vendido este dia : "))

precio = barras * 3.49 // 1
descuento = precio * 0.6

precio_descuento = precio - descuento // 1

print(f"El precio de las barras comunes es {precio}, y si fueran del siguiente dia sera {precio_descuento}")