#Crea una lista que se puede modificar
lista = ["Alan Rafael","Soy Alan",True,1.67]

#Crea una lista que (no se puede modificar)
tupla = ("Alan Rafael","Soy Alan",True,1.67)

#Esto es valido
lista[3] = "Maquinola"

#Esto no es valido
#tupla[3] = "Maquinola"

#creando un conjunto (set) (nose acceda a los elementos por indice ,no se pueder llamar a los elementos por su indice , no almacena datos duplicados)

conjuto = {"Alan Rafael","Soy Alan",True,1.67}
#print(conjuto[3]) -> no puede acceder al elemento

#creando un diccionario (dic) (la estructura es key : value y separamos con comas)
diccioanario = {
    'nombre' : "Alan Rafael",
    'estudios' : "programacion",
    'esta_emocionado' : True,
    'altura' : 1.84
}
print(diccioanario['nombre'])