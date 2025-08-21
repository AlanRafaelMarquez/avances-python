contraseñe = "lol"

pedir_contraseña = input("Dime la contraseña para acceder: ")

if contraseñe == pedir_contraseña.lower():
    print("Acceso concedido")
else:
    print("Contraseña incorrecta")