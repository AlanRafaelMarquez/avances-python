
#Usando open para abrir un archivo con una codificacion universal ("UTF-8") a "archivos"
archivo = open("archivos\\texto_de_alan.txt",encoding="UTF-8")
#Leer el archivo completo
archivo = archivo.read()


#Leer linea por linea
#lineas = archivo_sin_leer.readlines()

#Leer una sola linea
#linea = archivo_sin_leer.readline()

#Cerrar el archivo
archivo.close()

print(archivo)