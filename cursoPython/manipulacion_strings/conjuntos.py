#Creamos dos conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

#Unimos los conjuntos con | y si hay numeros repetidos elimina el dupilcado
union = a | b

#Es una interseccion de conjuntos, el numero repetido de lo da
interseccion = a & b

#Se elimina los numeros que estan del conjunto a del conjunto b
diferencia = a - b

#Te da solo los elementos que no estan duplicados de los dos conjuntos
simetrica = a ^ b

#Comprobamos que el numero 2 esta en a
print(2 in a)
  
#Comprueba que el numero 6 esta en b
print(6 in b) 

#Creamos una lista
lista = [1, 2, 2, 3]

#La lista la convertimos a conjunto set
conjunto = set(lista)

#De nuevo el conjunto lo convertimos a una lista
nueva_lista = list(conjunto)

print(nueva_lista)  

print(simetrica) 
