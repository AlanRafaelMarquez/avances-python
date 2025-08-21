num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

cociente = num1//num2
resto_inicial = (cociente * num2)
resto_final =   num1 - resto_inicial
print(f"El primer numero que me diste es, {num1}, el segundo numero es, {num2} da un cociente de, {cociente} y  un resto de ,{resto_final}")