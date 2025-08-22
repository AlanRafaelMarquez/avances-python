class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
        
    def estudiar(self):
        print("Estudiando...")
        
                
nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
grado = input("Dime en que grado vas: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      El estudiante se llama: {estudiante.nombre} \n
      La edad del estudiante es: {estudiante.edad} \n
      El grado del estudiante es: {estudiante.grado}
      """)


while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()