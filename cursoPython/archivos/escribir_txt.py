with open("archivos\\texto_de_alan.txt", "w", encoding="UTF-8") as archivo:
    #Sobre escribiendo el archivo
    #archivo.write("Hola como estas mi amor???")
    
    #Agregando dos lineas con writelineas 
    archivo.writelines(["Hola bb como estas\n","Hola chiquito como estas\n"])
    
    #Agregando otras dos lineas
    archivo.writelines(["Hola bb donde estas?\n","Hola chiquito que tal te va??"])

