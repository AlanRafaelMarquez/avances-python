#Creando una funcion e 3 parametros
#def frase(nombre,apellido,adjetivo):
    #return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#Utilizando keyword arguments
#frase_resultante = frase(adjetivo="rico",nombre="Alan",apellido="Marquez")
#print(frase_resultante)

#Creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo="tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase("Alan","Marquez","Inteligente")
print(frase_resultante)
