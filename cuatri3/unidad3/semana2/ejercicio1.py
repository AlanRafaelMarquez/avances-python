
semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
pedir_dia = int(input("Dime un numero del 1 al 7 : "))

valor1 = semana[0]
valor2 = semana[1]
valor3 = semana[2]
valor4 = semana[3]
valor5 = semana[4]
valor6 = semana[5]
valor7 = semana[6]
if pedir_dia == 1:
    print(valor1)
elif pedir_dia == 2:
    print(valor2)
elif pedir_dia == 3:
    print(valor3)
elif pedir_dia == 4:
    print(valor4)
elif pedir_dia == 5:
    print(valor5)
elif pedir_dia == 6:
    print(valor6)
elif pedir_dia == 7:
    print(valor7)
else:
    print("No se encuentra el dia de la semana")




