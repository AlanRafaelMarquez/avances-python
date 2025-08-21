#Forma no optima de sumar valores
#def suma(lista):
    #numeros_sumados = 0
    #for numero in lista:
        #numeros_sumados = numeros_sumados + numero
        #return numeros_sumados

#resultado = sum([5,3,8])

#Forma optima de sumar valores
def suma_total(numeros):
    
        return sum([*numeros])

resultado2 = suma_total([5,3,8])
print(resultado2)

#Lo mismo que arriba pero utilizando el parametro args * con argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Alan",1,2,3,5)
