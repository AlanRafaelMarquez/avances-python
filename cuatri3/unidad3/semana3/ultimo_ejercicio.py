#Crea un programa en Python para gestionar información de estudiantes, aplicando listas, tuplas, diccionarios y sets.
#1. Crea una lista de estudiantes, donde cada estudiante es una tupla con:
#Nombre del estudiante.
#Grupo.
#Conjunto de materias inscritas (set).
#2. Guarda la información en un diccionario donde:
#La clave sea el nombre del estudiante.
#El valor sea otra estructura con el grupo y sus materias (set).
#3. Permite al usuario:
#a) Agregar un nuevo estudiante con sus materias.
#b) Mostrar todos los estudiantes y sus materias.
#c) Buscar un estudiante y mostrar su información.
#d) Mostrar un set de todas las materias únicas (sin duplicados).

listas_estudiantes = [("Alan",{"3A","Programacion"}),
                      ("Alejandro",{"3B","BaseDatos"}),
                      ("Carlos",{"3C","Matematicas"}),
                      ("Gael",{"4A","Ingles"}),
                      ("Oziel",{"4B","Aleman"})]

diccionario = dict(listas_estudiantes)

permitir = input("Que es lo que quieres pedir: \na) Agregar un nuevo estudiante con sus materias.\nb) Mostrar todos los estudiantes y sus materias.\nc) Buscar un estudiante y mostrar su información.\nd) Mostrar un set de todas las materias únicas (sin duplicados).\n")


def agregar(diccionario):
    nombre = input("Dime el nombre: ")
    grupo = input("Dime el grupo: ")
    materia = input("Dime la materia: ")
    diccionario[nombre]={grupo,materia}
    print(diccionario)
    return diccionario

def mostrar():
    print(diccionario)

def buscar():
    encontrar = input("Dime el nombre del estudiante que quieras saber su informacion: ")
    print(diccionario.get(encontrar,"No se encuentra"))
    return encontrar

def sin_duplicados():
    conjunto = set(diccionario)
    print(conjunto)
    return conjunto


if permitir == "a":
    agregar(diccionario)
elif permitir == "b":
    mostrar()
elif permitir == "c":
    buscar()
elif permitir == "d":
    sin_duplicados()
else:
    print("No se encuentra: ")
        







