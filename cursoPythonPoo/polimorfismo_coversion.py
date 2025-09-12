num = 3
num2 = 4.4

resultado = num + num2

print(resultado)

print(type(resultado))


def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
        
        
lista = [1,2,3,4]

lista2 = ["Hola","Como","Estas"]
texto = "ComoEstas"
recorrer(texto)
recorrer(lista2)