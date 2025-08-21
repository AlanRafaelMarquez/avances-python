#Creando las listas
frutas = ["banana","Manzana","Ciruelas","Pera","Naranja","Granada","Durazno"]
cadena = "Hola Alan"
numeros = [1,5,8,10,18]

#Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "Manzana":
        continue
    print(f"Me voy a comer una : {fruta}")
    
#Evitando que se siga ejecutando(El else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una : {fruta}")
    if fruta == "Pera":
        break
else:
    print("Bucle terminado")
    
#Recorrer una cade de texto
for letra in cadena:
    print(letra)
    
    
#For en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
