renta = int(input("Cual es tu renta anual: "))

if renta <= 10000:
    print("Tipo impositivo que le corresponde es de 5%")
elif renta > 10000 and renta < 20000:
    print("Tipo impositivo que le corresponde es de 15%")
elif renta > 20000 and renta < 30500:
    print("Tipo impositivo que le corresponde es de 20%")
elif renta > 30500 and renta < 60000:
    print("Tipo impositivo que le corresponde es de 30%")
else:
    print("Tipo impositivo que le corresponde es de 45%")
    
    
    