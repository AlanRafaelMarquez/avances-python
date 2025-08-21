nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo: ")

if sexo.lower() == "f": 
    print(f"Tu nombre es {nombre}")
    print(f"Tu eres del grupo A")
else:
    print(f"Tu nombre es {nombre}")
    print(f"Tu eres del grupo B")