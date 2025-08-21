#Abriendo el archivo con with open
with open("archivos\\texto_de_alan.txt", encoding="UTF-8") as archivo:
    
    #Leemos el archivo
    contenido = archivo.read()
    
    #Mostramos el archivo
    print(contenido)
    
#No es necesario cerrarlo al usar with open