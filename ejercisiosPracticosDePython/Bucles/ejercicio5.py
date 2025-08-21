invertir = int(input("Dime la cantidad de dinero que quieres invertir: "))
interes = int(input("Dime el interes anual: "))
años = int(input("Dime el numero de años: "))

for i in range(1,años+1):
    invertir *= interes/100+1
    print(f"La capital del año {i} es:  {invertir}")

