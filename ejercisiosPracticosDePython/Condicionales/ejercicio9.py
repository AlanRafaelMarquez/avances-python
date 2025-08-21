edad = int(input("Dime tu edad para la sala de juegos: "))

if edad < 4 :
    print("La entrada es gratis")
elif edad >= 4 and edad < 18:
    print("El costo es de $5 ")
else: 
    print("El costo de de $10")