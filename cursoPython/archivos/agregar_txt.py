with open("archivos\\texto_de_alan.txt", "a", encoding="UTF-8") as archivo:
    #Usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        #Agregando lineas
        archivo.write(f"Linea agregada{i+1}\n")
    
