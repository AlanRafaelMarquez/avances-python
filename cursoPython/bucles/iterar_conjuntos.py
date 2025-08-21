animales = {"gato","perro","loro","cocodrilo",}
numeros = {12,3445,56,78,90,34}

#Recorriendo la conjunto animales
for animal in animales:
    print(f"Ahora la variable animal es igual a : {animal}")
    
#Recorriendo la conjunto numeros y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#Interando dos conjuntos del mismos tamaño al mismo tiempo    
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo conjunto 1 : {numero}")
    print(f"Recorriendo conjunto 2 : {animal}")
    
    
    
#Forma correcta de recorrer una conjunto con su indice       
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es : {indice} y el valor es : {valor} ")
    
    
    
#Usando el for/else     
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual : {numero} ")
else:
    print("EL bucle termino")
    
    
#Todo lo anterior funciona exactamente igual con tuplas y listas