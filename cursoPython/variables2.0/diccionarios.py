#Creando diccionario con dict()
diccionario = dict(nombre="Alan", apellido="Rafael")

#Las listas no pueden ser claves y usamos frozen para meter conjuntos
diccionario = {frozenset(["Alan","Rancio"]):"jajajaj"}

#Creando diccionarios con fromkeys() con dos parametros
diccionario = dict.fromkeys(["nombre","apellido"])

#Creando diccionarios con fromkeys() cambiando el valor por defecto a nose
diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario)