class celular:
    def __init__(self, marca, modelo, camara):
        self.marc = marca
        self.modelo = modelo
        self.camara = camara
    
celular1 = celular("Samsung","S23","48MP")
celular2 = celular("Apple","Iphon 15 Pro","96MP")

print(celular1.marc)
