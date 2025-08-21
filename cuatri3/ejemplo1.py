frutas = ["manzana", "banana", "cereza"]
print(frutas) # ['manzana', 'banana', 'cereza']
print(frutas[0]) # manzana
print(frutas[2]) # cereza
frutas.append("nuevo") # Agrega al final
frutas.insert(2, "otro") # Inserta en posición específica
frutas.remove("otro") # Elimina por valor
frutas.pop() # Elimina el último
frutas.pop(0) # Elimina por índice
frutas.index("nuevo") # Devuelve el índice
"nuevo" in frutas # True o False
frutas.count("nuevo") # Cuántas veces aparece
frutas * 2 # Repite la lista
frutas.sort() # Ordena (ascendente)
frutas.sort(reverse=True) # Ordena descendente
frutas.reverse() # Invierte la lista