class celular:
    def __init__(self, marca, modelo, camara):
        self.marc = marca
        self.modelo = modelo
        self.camara = camara
    def llamar (self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")
    def cortar (self):
        print(f"Cortaste la llamada desde de un {self.modelo}")
    
celular1 = celular("Samsung","S23","48MP")
celular2 = celular("Apple","Iphon 15 Pro","96MP")

celular1.llamar()
celular2.cortar()
