nombre = input("Dame el primer nombre : ")
nombre1 = input("Dame el segundo nombre : ")
nombre2 = input("Dame el tercer nombre : ")
nombre3 = input("Dame el cuarto nombre : ")
nombre4 = input("Dame el quinto nombre : ")

mi_lista = []
mi_lista.extend([nombre,nombre1,nombre2,nombre3,nombre4])
mi_lista.reverse()
print(mi_lista.count(nombre))  

print(mi_lista)