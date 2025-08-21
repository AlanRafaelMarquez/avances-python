payasos = int(input("Cuantos payasos se vendieron : "))
muñecas = int(input("Cuantas muñecas se vendieron : "))

peso_de_p = payasos * 112
peso_de_m = muñecas * 75

peso_total = peso_de_p+peso_de_m

print(f"El peso total de los paquetes es: {peso_total}g")
