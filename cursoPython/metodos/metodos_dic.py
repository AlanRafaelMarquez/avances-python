diccionario = {
    "nombre" : 'Alan',
    "apellido" : 'Marquez',
    "edad" : 18
}

#Nos devuelve un objeto ic_item
claves = diccionario.keys()

#Obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_None = diccionario.get("nombre")

#Elimino todo del diccionario
#diccionario.clear()
 
#Eliminando un elemento del diccionario
diccionario.pop("edad")

#Obteniendo un elemento dict_items interable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)