#Le pedimos al usuario que nos diga una frase (o varias)
frase = input("Dime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#Creamos una lista con todas las palabras de la frase (se sepera cada vez que hayas hecho un espacio en blanco)
cantidad_separadas = frase.split(" ")

#Usamos el len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palbras = len(cantidad_separadas)

#En caso de que tarde un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palbras > 120:
    print("Puedes para tampoco te pedi un testamento")
    
#Calculamos cuanto tardarias en decir las palabras y de lo decimos
print(f"Dijiste {cantidad_de_palbras} palabras, y tardarias {cantidad_de_palbras/2} segundos en decirlos")
print(f"Dalto diria en {cantidad_de_palbras * 100 // 2 * 1.3 / 100 } segundos")