edad = int(input("Dime tu edad: "))
ingresos = int(input("Dime tus ingresos: "))

if edad >= 16 and ingresos >= 1000:
    print("Tienes tributar")
else:
    print("no tienes tributar")