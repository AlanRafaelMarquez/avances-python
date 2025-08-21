peso = int(input("Dame tu peso en Kg : "))
estatura = float(input("Dime tu estatura en  metros: "))

masa_corporal = peso/estatura**2
resultado = masa_corporal//1

print(f"Tu indice de masa corporal es:  {resultado}")