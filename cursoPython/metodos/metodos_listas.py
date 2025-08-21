#Creando una lista con list
lista = list(["hola","Alan",18])

#Devuelve la cantidad de elementos de una lista
resultado = len(lista)

#Agregando un elemento a la lista
agregando_con_append = lista.append("Holaaaaaa")

#Agrega un elemento a una lista en un indece especifico
lista.insert(2,"Como estas?")

#Agregando varios elementos a la lista
lista.extend([False,2006])

#Eimina un elemento de la lista (por indice)
lista.pop(-1)#-1 para eliminar el ultimo elemento de la lista, -2 para eliminar el antenultimo, y asi sucesibamente

#Removiendo un elemento por su valor
lista.remove("Alan")

#Elimina todos los elementos de la lista
#lista.clear()

#Orednando la lista de forama acendente,(Si usamos el parametro reverse=True la ordena en reversa)
#ista.sort

#Invirtiendo los elementos de una lista
lista.reverse()

#Verifica si un elemento se encuentra en la lista
elemento_encotrado = lista.index(18)

print(elemento_encotrado)