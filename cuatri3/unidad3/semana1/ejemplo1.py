#listas
mi_lista = [1, 2, 3, "hola", True]



# 1. .append(x) Agrega un elemento al final.

frutas = ["manzana", "platano"]
frutas.append("uva")
print(frutas)  # ['manzana', 'platano', 'uva']

# 2. .extend(iterable) Agrega múltiples elementos al final

numeros = [1, 2]
numeros.extend([3, 4, 5])
print(numeros)  # [1, 2, 3, 4, 5]

#3  3. .insert(i, x) Inserta un elemento en una posición específica

letras = ['a', 'c', 'd']
letras.insert(1, 'b')
print(letras)  # ['a', 'b', 'c', 'd']


# 4. .remove(x) Elimina la primera aparición de un valor

colores = ['rojo', 'verde', 'azul', 'rojo']
colores.remove('rojo')
print(colores)  # ['verde', 'azul', 'rojo']

#  5. .pop([i]) Elimina y retorna el último elemento (o el indicado)

nombres = ['Ana', 'Luis', 'Juan']
ultimo = nombres.pop()
print(ultimo)     # Juan
print(nombres)    # ['Ana', 'Luis']

# 6.  Devuelve el índice de la primera aparición de x.


nombres = ['Ana', 'Luis', 'Juan']
print(nombres.index('Luis'))  # 1

#7. .count(x) Cuenta cuántas veces aparece un valor
numeros = [1, 2, 3, 1, 1]
print(numeros.count(1))  # 3

#8. .sort() Ordena la lista (modifica la lista original).

edades = [23, 12, 44, 5]
edades.sort()
print(edades)  # [5, 12, 23, 44]