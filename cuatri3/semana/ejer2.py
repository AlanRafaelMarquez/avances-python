lista = [1, 2, 3, 4, 5]
objetivo = 6
pares = []

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] + lista[j] == objetivo:
            pares.append((lista[i], lista[j]))

print(pares)