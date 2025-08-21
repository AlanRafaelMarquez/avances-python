#ordena la lista de  numeros aleatorios sin sort
#se tiene que usar len
lista = [8,45,32,19,10]
for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:
            lista[i] , lista[j] = lista[j] , lista[i]
            print(lista)
                        