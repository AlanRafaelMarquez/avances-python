#Dos listas unas con nombres y otras con apellidos
nombres = ["Alan","Alejandro","Carlos","Gael","Oziel"]
apellidos = ["Marquez","Hurtado","Jimenez","Fernandez","Aleman"]

#Registrar esta informacion de un TXT de forma optima
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.write("Los datos son:\n\n ")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------------------\n")for n,a in zip(nombres,apellidos) ]