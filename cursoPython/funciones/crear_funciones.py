#Creando una funcion simple
#def saludar():
#    print("Hola alan, ¿Como estas?")
    
#Ejecutando una funcion simple
#saludar()

#Creando una funcion  que tenga parametros

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "niña"
    elif (sexo == "hombre"):
        adjetivo = "maquina"
    else:
        adjetivo = "amor"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿Como estas?")

saludar("Camila","Mujer")
saludar("Alan","Hombre")
saludar("Rafael","hetero")


#Creando una funcion que retorne dos valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#Desempaquetando los resultados obtenidos y los datos utilizados para obternerlo
passwor,primer_numero = crear_contraseña_random(981)
print(f"Tu contraseña nueva es: {passwor}")
print(f"El numero utilizado para crearla fue : {primer_numero}")
