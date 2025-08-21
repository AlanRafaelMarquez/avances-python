#creando un conjuto con set
conjunto = set(["Dato1","Dato2"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({"dato1","dato2"})
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verifica si es un subjconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificamos si es un superconjuto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)