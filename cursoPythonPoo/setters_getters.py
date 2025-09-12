class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
         
    def set_nombre(self,new_nombre):
        self._nombre = new_nombre
        
        
alan = Persona("Alan",18)
         
nombre = alan.get_nombre()
print(nombre)

alan.set_nombre("Rafael")
nombre = alan.get_nombre()

print(nombre)