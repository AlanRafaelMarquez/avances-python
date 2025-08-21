productos = {
    "bana" : 5,
    "leche" : 78,
    "arrox" : 4,
    "pcgamer" : 600,
    "pañales" : 55
}


precio = input("Dime un producto y te digo el precio: ")

print(productos.get(precio,"No se encuentra"))

