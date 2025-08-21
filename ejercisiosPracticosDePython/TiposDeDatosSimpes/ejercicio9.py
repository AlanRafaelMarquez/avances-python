invertir = int(input("Dime la cantidad a invertir : "))
intereses = int(input("Dime el interes anual : "))
años = int(input("Dime los años que vas a  invertir : "))

capital = invertir*(intereses/100+1)**años 

print(f"La capital es:  {capital}")