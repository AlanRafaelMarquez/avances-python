#ordena la lista de  numeros aleatorios sin sort
#se tiene que usar len
#ahora tiene que ser con un numero radom
import random
ra2=[random.randint(1,100) for _ in range(10)]
for i in range(len(ra2)):
    for j in range(i+1,len(ra2)):
        if ra2[i] > ra2[j]:
            ra2[i] , ra2[j] = ra2[j] , ra2[i]
            print(ra2)