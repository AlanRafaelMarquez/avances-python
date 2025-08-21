#Falto el profesor de clases y el los alumnos van a dar las clases
#Pedir el nombre y la edad de los compañeros que vinieron a clase

#Funcion para obtener al asistente y el profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #Creando la lista con los compañeros
    compañeros = []
    
    #Ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Dime el nombre del alumno que vino: ")
        edad = int(input("Dime tu la edad del alumno: "))
        compañero = (nombre,edad)
        
        #Agregando la informacion a la lista
        compañeros.append(compañero)
        
        #Ordenarlos de menor a mayor segun su edad
    compañeros.sort(key=lambda x : x[1])
    
    #Compañeros[x] devuelve una tupla con {nombre,edad} y despues accedemos al nombre
    #Para definir el asistente y el profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #Retornamos una tupla
    return asistente,profesor

#Desempaquetando lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#Mostramos los resultados
print(f"El asistente es : {asistente}, y el profesor es: {profesor}")