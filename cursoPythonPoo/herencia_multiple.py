class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
        
    def hablar(self):
        print("Hola, estoy hablando")
        
        
class Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas, universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad


class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print( f"Hola soy : {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
        
    
roberto = EmpleadoArtista("Roberto",34,"Mexicano","cantar",100000,"oxford")

herencia = issubclass(EmpleadoArtista,Persona)
istancia = isinstance(roberto,Persona)
roberto.presentarse()

print(istancia)