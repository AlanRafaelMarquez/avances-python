#Creando una funcio que nos devuelve los numeros primos
#Entre 0 y el argumentos que le pasemos

#Creamos una funcion que verifica si un numero es primo
def es_primo(num):
    #Verificamos que el numero pasado no pueda dividirse
    #Por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #Si es divisible por alguno retornamos false y terminamos el bucle
        if num%i==0: return False
        #Si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Creando una funcion que retorne una lista con todos los numeros primos
def primos_hasta(num):
    #Creamos una lista
    primos = []
    for i in range(3,num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #En caso de que sea los agregamos a una lista
        if resultado == True: primos.append(i)
    
    #Devolvemos la lista    
    return primos

#Creamos el resultado llamando a la funcion y la mostramos
resultado = primos_hasta(98)
print(resultado)
        
    